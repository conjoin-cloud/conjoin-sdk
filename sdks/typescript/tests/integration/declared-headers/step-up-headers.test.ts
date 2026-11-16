import { createServer, type IncomingHttpHeaders, type Server } from 'node:http'
import { afterAll, afterEach, beforeAll, describe, expect, it } from 'vitest'
import { createAuthAccounts } from '../../../src/auth/index'
import { createConjoinClient } from '../../../src/core/client'
import { ConjoinConfigurationError } from '../../../src/core/errors'

const API_KEY = 'cak_test_harbourledgerstepup'
const AUTH_APP_ID = 'app_harbourledger'
const ACCOUNT_ID = 'acc_harbourledger_owner'
const STEP_UP_SESSION_ID = 'sus_harbourledger_0198f0f7'
const STEP_UP_TOKEN = '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
const DELETED_ACCOUNT = { account_id: ACCOUNT_ID, deleted: true }
const PINNED_API_VERSION = '2026-06-01'
const CALLER_VERSION = '9.9.9'

type ReceivedRequest = {
  method: string | undefined
  url: string | undefined
  headers: IncomingHttpHeaders
}

describe('deleteAuthAccount sends the step-up headers it declares', () => {
  const received: ReceivedRequest[] = []
  let server: Server | undefined
  let baseUrl = ''

  beforeAll(async () => {
    server = createServer((request, response) => {
      received.push({ method: request.method, url: request.url, headers: request.headers })
      request.resume()
      response.writeHead(200, { 'content-type': 'application/json' })
      response.end(
        JSON.stringify({ response: { type: 'SUCCESS', code: 200, message: 'Success' }, data: DELETED_ACCOUNT }),
      )
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

  const createAccounts = () =>
    createAuthAccounts(
      createConjoinClient({ apiKey: API_KEY, baseUrl, authAppId: AUTH_APP_ID, retry: { maxRetries: 0 } }),
    )

  it('puts both step-up values on the wire beside the app scope', async () => {
    const result = await createAccounts().delete(ACCOUNT_ID, undefined, {
      stepUpSessionId: STEP_UP_SESSION_ID,
      stepUpToken: STEP_UP_TOKEN,
    })

    expect(result).toEqual(DELETED_ACCOUNT)
    expect(received).toHaveLength(1)
    expect(received[0]?.method).toBe('DELETE')
    expect(received[0]?.url).toBe(`/v1/auth/accounts/${ACCOUNT_ID}`)
    expect(received[0]?.headers['step-up-session-id']).toBe(STEP_UP_SESSION_ID)
    expect(received[0]?.headers['step-up-token']).toBe(STEP_UP_TOKEN)
    expect(received[0]?.headers['auth-app-id']).toBe(AUTH_APP_ID)
  })

  it('sends the typed token when a free-form header tries to replace it', async () => {
    await createAccounts().delete(
      ACCOUNT_ID,
      undefined,
      { stepUpSessionId: STEP_UP_SESSION_ID, stepUpToken: STEP_UP_TOKEN },
      { headers: { 'step-up-token': 'ffff', 'STEP-UP-SESSION-ID': 'sus_other' } },
    )

    expect(received[0]?.headers['step-up-token']).toBe(STEP_UP_TOKEN)
    expect(received[0]?.headers['step-up-session-id']).toBe(STEP_UP_SESSION_ID)
  })

  it('sends one value of each version header when free-form headers repeat them in another case', async () => {
    const accounts = createAuthAccounts(
      createConjoinClient({
        apiKey: API_KEY,
        baseUrl,
        authAppId: AUTH_APP_ID,
        apiVersion: PINNED_API_VERSION,
        retry: { maxRetries: 0 },
      }),
    )

    await accounts.delete(ACCOUNT_ID, undefined, undefined, {
      headers: { 'x-conjoin-api-version': CALLER_VERSION, 'X-CONJOIN-SDK-VERSION': CALLER_VERSION },
    })

    const sdkVersion = received[0]?.headers['x-conjoin-sdk-version']

    expect(received[0]?.headers['x-conjoin-api-version']).toBe(PINNED_API_VERSION)
    expect(sdkVersion).toMatch(/^\d+\.\d+\.\d+$/)
    expect(sdkVersion).not.toBe(CALLER_VERSION)
  })

  it('leaves both headers off the wire when the caller supplies neither', async () => {
    await createAccounts().delete(ACCOUNT_ID)

    expect(received).toHaveLength(1)
    expect(received[0]?.headers).not.toHaveProperty('step-up-session-id')
    expect(received[0]?.headers).not.toHaveProperty('step-up-token')
  })

  it.each([
    { label: 'an uppercase token', token: STEP_UP_TOKEN.toUpperCase() },
    { label: 'a token of 257 characters', token: 'a'.repeat(257) },
    { label: 'an empty token', token: '' },
    { label: 'a token with a line break', token: `${STEP_UP_TOKEN}\r\nX-Injected: yes` },
  ])('refuses $label before any request and keeps it out of the message', async ({ token }) => {
    const call = createAccounts().delete(ACCOUNT_ID, undefined, {
      stepUpSessionId: STEP_UP_SESSION_ID,
      stepUpToken: token,
    })

    await expect(call).rejects.toBeInstanceOf(ConjoinConfigurationError)
    await call.catch((error: unknown) => {
      const message = error instanceof Error ? error.message : ''

      expect(message).toContain('stepUpToken')
      if (token.length > 0) expect(message).not.toContain(token)
    })
    expect(received).toHaveLength(0)
  })

  it('refuses a session id longer than the documented 48 characters before any request', async () => {
    const call = createAccounts().delete(ACCOUNT_ID, undefined, { stepUpSessionId: 's'.repeat(49) })

    await expect(call).rejects.toBeInstanceOf(ConjoinConfigurationError)
    expect(received).toHaveLength(0)
  })
})
