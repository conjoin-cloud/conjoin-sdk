import { createServer } from 'node:http'
import { afterEach, expect, it } from 'vitest'
import { createConjoinAuthApi } from '../src/auth/auth-api'
import { type AuthManager, createAuthManager } from '../src/provider/auth-manager'
import { createWebTransport } from '../src/transport/web'

const managers: AuthManager[] = []
const servers: ReturnType<typeof createServer>[] = []

afterEach(async () => {
  for (const manager of managers.splice(0)) manager.destroy()
  for (const server of servers.splice(0)) {
    server.closeAllConnections()
    await new Promise<void>(resolve => server.close(() => resolve()))
  }
})

async function authServer() {
  const requests: string[] = []
  let handshakes = 0
  let release: (() => void) | undefined
  const server = createServer((request, response) => {
    const path = request.url ?? ''
    requests.push(path)
    const answer = (data: unknown) => response.end(JSON.stringify({ data }))
    if (path.endsWith('/handshakes')) {
      handshakes++
      const reply = () => answer({ account_id: 'account_1', session_id: 'session_1', access_token_ttl_seconds: 1 })
      if (handshakes === 1) release = reply
      else reply()
    } else if (path.endsWith('/active-organization')) {
      answer({ active_organization_id: null, active_organization_roles: [] })
    } else answer({})
  })
  servers.push(server)
  await new Promise<void>(resolve => server.listen(0, '127.0.0.1', resolve))
  const address = server.address()
  if (address === null || typeof address === 'string') throw new Error('No server address')
  return {
    api: createConjoinAuthApi('cpk_test_auth', `http://127.0.0.1:${address.port}`),
    requests,
    release: () => release?.(),
  }
}

async function waitFor(check: () => boolean) {
  const deadline = Date.now() + 2000
  while (!check()) {
    if (Date.now() >= deadline) throw new Error('The auth request did not arrive')
    await new Promise(resolve => setTimeout(resolve, 5))
  }
}

it('serialises logout after an in-flight refresh and suppresses stale account reads', async () => {
  const server = await authServer()
  const manager = createAuthManager({
    api: server.api,
    transport: createWebTransport(),
    onStateChange: () => undefined,
  })
  managers.push(manager)
  const refreshing = manager.refresh()
  await waitFor(() => server.requests.length === 1)
  const signingOut = manager.signOut()
  await new Promise(resolve => setTimeout(resolve, 30))
  expect(server.requests).toEqual(['/v1/auth/client/handshakes'])
  server.release()
  await Promise.all([refreshing, signingOut])
  expect(server.requests).toEqual(['/v1/auth/client/handshakes', '/v1/auth/client/logout'])
  expect(manager.getState()).toEqual({ isLoaded: true, isSignedIn: false })
})

it('does not schedule a refresh after a state callback signs out', async () => {
  const server = await authServer()
  let signingOut: Promise<void> | undefined
  const manager = createAuthManager({
    api: server.api,
    transport: createWebTransport(),
    onStateChange: state => {
      if (state.isLoaded && state.isSignedIn) signingOut = manager.signOut()
    },
  })
  managers.push(manager)
  const refreshing = manager.refresh()
  await waitFor(() => server.requests.length === 1)
  server.release()
  await refreshing
  await signingOut
  await new Promise(resolve => setTimeout(resolve, 5200))
  expect(server.requests.filter(path => path.endsWith('/handshakes'))).toHaveLength(1)
  expect(manager.getState()).toEqual({ isLoaded: true, isSignedIn: false })
}, 10000)
