import { createServer, type IncomingHttpHeaders, type Server } from 'node:http'
import { afterAll, afterEach, beforeAll, describe, expect, it } from 'vitest'
import { createConjoinClient } from '../../../src/core/client'
import { ConjoinConfigurationError } from '../../../src/core/errors'
import { createAuthClients, createAuthSelves, createAuthSSOPortals, createCloudSDKs } from '../../../src/frontend/index'

const SECRET_API_KEY = 'cak_live_harbourledgerserverside'
const PUBLISHABLE_KEY = 'cpk_live_harbourledgerbrowser'
const SESSION_TOKEN = 'sess_harbourledger_signedin_owner'
const PORTAL_TICKET = 'ptk_harbourledger_portal_ticket'
const PORTAL_TICKET_WITH_A_SPACE = 'ptk_harbourledger portal_ticket'
const PORTAL_TICKET_HEADER = 'x-portal-ticket'
const SUCCESS_BODY = JSON.stringify({ response: { type: 'SUCCESS', code: 200, message: 'Success' }, data: {} })

type ReceivedRequest = {
  url: string | undefined
  headers: IncomingHttpHeaders
}

describe('frontend operations send only the credential their document declares', () => {
  const received: ReceivedRequest[] = []
  let server: Server | undefined
  let baseUrl = ''

  beforeAll(async () => {
    server = createServer((request, response) => {
      received.push({ url: request.url, headers: request.headers })
      request.resume()
      response.writeHead(200, { 'content-type': 'application/json' })
      response.end(SUCCESS_BODY)
    })

    await new Promise<void>(resolve => server?.listen(0, '127.0.0.1', resolve))

    const address = server.address()

    if (address === null || typeof address === 'string') throw new Error('The receiver has no TCP port')

    baseUrl = `http://127.0.0.1:${address.port}`
  })

  afterEach(() => {
    received.length = 0
  })

  afterAll(async () => {
    await new Promise<void>(resolve => server?.close(() => resolve()))
  })

  const createBrowserClient = () =>
    createConjoinClient({ publishableKey: PUBLISHABLE_KEY, baseUrl, retry: { maxRetries: 0 } })

  it('keeps the secret key off a public, a session, and a publishable-key call from a server-side client', async () => {
    const client = createConjoinClient({ apiKey: SECRET_API_KEY, baseUrl, retry: { maxRetries: 0 } })

    await createAuthClients(client).getJwks()
    await createAuthSelves(client).readProfile(SESSION_TOKEN)
    await expect(createCloudSDKs(client).readSdkSettings()).rejects.toThrow(
      new ConjoinConfigurationError('This call needs publishableKey in the client settings'),
    )

    expect(received).toHaveLength(2)
    expect(received[0]?.headers.authorization).toBeUndefined()
    expect(received[1]?.headers.authorization).toBe(`Bearer ${SESSION_TOKEN}`)
    expect(JSON.stringify(received)).not.toContain(SECRET_API_KEY)
  })

  it('sends a portal ticket only in its header and never in the query string', async () => {
    await createAuthSSOPortals(createBrowserClient()).readSsoPortalContext({ portalTicket: PORTAL_TICKET })

    expect(received).toHaveLength(1)
    expect(received[0]?.headers[PORTAL_TICKET_HEADER]).toBe(PORTAL_TICKET)
    expect(received[0]?.headers.authorization).toBeUndefined()
    expect(received[0]?.url).not.toContain(PORTAL_TICKET)
  })

  it('refuses a malformed portal ticket without repeating it in the error', async () => {
    const failure = await createAuthSSOPortals(createBrowserClient())
      .readSsoPortalContext({ portalTicket: PORTAL_TICKET_WITH_A_SPACE })
      .then(
        () => undefined,
        (error: unknown) => error,
      )

    expect(failure).toBeInstanceOf(ConjoinConfigurationError)
    expect(String(failure)).not.toContain(PORTAL_TICKET_WITH_A_SPACE)
    expect(JSON.stringify(failure)).not.toContain(PORTAL_TICKET_WITH_A_SPACE)
    expect(received).toEqual([])
  })
})
