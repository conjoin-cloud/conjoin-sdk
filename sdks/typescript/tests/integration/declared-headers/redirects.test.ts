import { createServer, type IncomingHttpHeaders, type Server } from 'node:http'
import { afterAll, afterEach, beforeAll, describe, expect, it } from 'vitest'
import { createAuthAccounts } from '../../../src/auth/index'
import { createConjoinClient } from '../../../src/core/client'
import { createAuthSSOPortals } from '../../../src/frontend/index'

const API_KEY = 'cak_test_harbourledgerredirect'
const PUBLISHABLE_KEY = 'cpk_test_harbourledgerredirect'
const AUTH_APP_ID = 'app_harbourledger'
const ACCOUNT_ID = 'acc_harbourledger_owner'
const STEP_UP_SESSION_ID = 'sus_harbourledger_0198f0f7'
const STEP_UP_TOKEN = '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
const PORTAL_TICKET = 'ptk_harbourledger_portal'
const TEMPORARY_REDIRECT_STATUS = 307

type ReceivedRequest = { method: string | undefined; url: string | undefined; headers: IncomingHttpHeaders }

type Receiver = { server: Server; baseUrl: string; received: ReceivedRequest[] }

const startReceiver = async (reply: (url: string) => { status: number; headers: Record<string, string> }) => {
  const received: ReceivedRequest[] = []
  const server = createServer((request, response) => {
    received.push({ method: request.method, url: request.url, headers: request.headers })
    request.resume()
    const { status, headers } = reply(request.url ?? '/')
    response.writeHead(status, { 'content-type': 'application/json', ...headers })
    response.end('{}')
  })

  await new Promise<void>(resolve => server.listen(0, '127.0.0.1', resolve))

  const address = server.address()
  if (address === null || typeof address === 'string') throw new Error('The receiver has no TCP port')

  return { server, baseUrl: `http://127.0.0.1:${address.port}`, received } satisfies Receiver
}

describe('a redirect never carries a credential to another host', () => {
  let otherHost: Receiver | undefined
  let apiHost: Receiver | undefined

  beforeAll(async () => {
    const target = await startReceiver(() => ({ status: 200, headers: {} }))
    otherHost = target
    apiHost = await startReceiver(url => ({
      status: TEMPORARY_REDIRECT_STATUS,
      headers: { location: `${target.baseUrl}${url}` },
    }))
  })

  afterEach(() => {
    if (otherHost) otherHost.received.length = 0
    if (apiHost) apiHost.received.length = 0
  })

  afterAll(async () => {
    for (const receiver of [apiHost, otherHost]) {
      await new Promise<void>(resolve => receiver?.server.close(() => resolve()))
    }
  })

  const receivers = (): { api: Receiver; other: Receiver } => {
    if (apiHost === undefined || otherHost === undefined) throw new Error('The receivers did not start')

    return { api: apiHost, other: otherHost }
  }

  it('refuses the 307 that answers a step-up delete', async () => {
    const { api, other } = receivers()
    const accounts = createAuthAccounts(
      createConjoinClient({ apiKey: API_KEY, baseUrl: api.baseUrl, authAppId: AUTH_APP_ID, retry: { maxRetries: 0 } }),
    )

    await expect(
      accounts.delete(ACCOUNT_ID, undefined, { stepUpSessionId: STEP_UP_SESSION_ID, stepUpToken: STEP_UP_TOKEN }),
    ).rejects.toThrow()

    expect(api.received).toHaveLength(1)
    expect(api.received[0]?.headers['step-up-token']).toBe(STEP_UP_TOKEN)
    expect(other.received).toEqual([])
  })

  it('refuses the 307 that answers a portal call', async () => {
    const { api, other } = receivers()
    const portals = createAuthSSOPortals(
      createConjoinClient({ publishableKey: PUBLISHABLE_KEY, baseUrl: api.baseUrl, retry: { maxRetries: 0 } }),
    )

    await expect(portals.readSsoPortalContext({ portalTicket: PORTAL_TICKET })).rejects.toThrow()

    expect(api.received).toHaveLength(1)
    expect(other.received).toEqual([])
  })
})
