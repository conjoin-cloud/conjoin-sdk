import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

vi.mock('react', () => ({
  cache: (fn: (...args: never[]) => unknown) => fn,
}))

vi.mock('next/headers', () => ({
  cookies: vi.fn(),
  headers: vi.fn(),
}))

vi.mock('../../server/tokens', async importOriginal => ({
  ...(await importOriginal<typeof import('../../server/tokens')>()),
  verifyToken: vi.fn(),
}))

import { cookies, headers } from 'next/headers'
import { verifyToken } from '../../server/tokens'
import { auth } from '../auth'

const mockCookies = vi.mocked(cookies)
const mockHeaders = vi.mocked(headers)
const mockVerifyToken = vi.mocked(verifyToken)

describe('auth', () => {
  beforeEach(() => {
    vi.clearAllMocks()

    process.env.CONJOIN_AUTH_DOMAIN = 'auth.conjoin.cloud'

    mockHeaders.mockResolvedValue({
      get: vi.fn().mockReturnValue(null),
    } as never)

    mockCookies.mockResolvedValue({
      get: vi.fn().mockReturnValue(undefined),
    } as never)
  })

  afterEach(() => {
    vi.restoreAllMocks()
    delete process.env.CONJOIN_AUTH_DOMAIN
  })

  it('reads token from cookie and verifies', async () => {
    const cookieGet = vi.fn().mockImplementation((name: string) => {
      if (name === '__conjoin_auth_sess') return { value: 'jwt-from-cookie' }
      return undefined
    })
    mockCookies.mockResolvedValue({ get: cookieGet } as never)

    mockVerifyToken.mockResolvedValueOnce({
      payload: { sub: 'acc_123', session_id: 'ses_456' },
      accountId: 'acc_123',
      sessionId: 'ses_456',
      organizationId: null,
      organizationRoles: [],
    })

    const result = await auth()

    expect(result).not.toBeNull()
    expect(result?.accountId).toBe('acc_123')
    expect(result?.sessionId).toBe('ses_456')
    expect(result?.getToken()).toBe('jwt-from-cookie')
    expect(mockVerifyToken).toHaveBeenCalledWith('jwt-from-cookie', {
      jwksUrl: 'https://auth.conjoin.cloud/v1/auth/client/.well-known/jwks.json',
      issuer: 'https://auth.conjoin.cloud/v1/auth/client',
    })
  })

  it('reads Bearer token from Authorization header', async () => {
    const headerGet = vi.fn().mockImplementation((name: string) => {
      if (name === 'authorization') return 'Bearer jwt-from-header'
      return null
    })
    mockHeaders.mockResolvedValue({ get: headerGet } as never)

    mockVerifyToken.mockResolvedValueOnce({
      payload: { sub: 'acc_456' },
      accountId: 'acc_456',
      sessionId: 'ses_789',
      organizationId: 'org_100',
      organizationRoles: ['member'],
    })

    const result = await auth()

    expect(result).not.toBeNull()
    expect(result?.accountId).toBe('acc_456')
    expect(result?.organizationId).toBe('org_100')
    expect(result?.getToken()).toBe('jwt-from-header')
  })

  it('prefers Bearer header over cookie', async () => {
    const headerGet = vi.fn().mockImplementation((name: string) => {
      if (name === 'authorization') return 'Bearer header-token'
      return null
    })
    mockHeaders.mockResolvedValue({ get: headerGet } as never)

    const cookieGet = vi.fn().mockImplementation((name: string) => {
      if (name === '__conjoin_auth_sess') return { value: 'cookie-token' }
      return undefined
    })
    mockCookies.mockResolvedValue({ get: cookieGet } as never)

    mockVerifyToken.mockResolvedValueOnce({
      payload: { sub: 'acc_123' },
      accountId: 'acc_123',
      sessionId: 'ses_456',
      organizationId: null,
      organizationRoles: [],
    })

    await auth()

    expect(mockVerifyToken).toHaveBeenCalledWith('header-token', expect.anything())
  })

  it('returns null when no token is present', async () => {
    const result = await auth()
    expect(result).toBeNull()
    expect(mockVerifyToken).not.toHaveBeenCalled()
  })

  it('returns null when token verification fails', async () => {
    const cookieGet = vi.fn().mockImplementation((name: string) => {
      if (name === '__conjoin_auth_sess') return { value: 'bad-token' }
      return undefined
    })
    mockCookies.mockResolvedValue({ get: cookieGet } as never)

    mockVerifyToken.mockRejectedValueOnce(new Error('invalid token'))

    const result = await auth()
    expect(result).toBeNull()
  })

  it('ignores non-Bearer authorization headers', async () => {
    const headerGet = vi.fn().mockImplementation((name: string) => {
      if (name === 'authorization') return 'Basic dXNlcjpwYXNz'
      return null
    })
    mockHeaders.mockResolvedValue({ get: headerGet } as never)

    const result = await auth()
    expect(result).toBeNull()
    expect(mockVerifyToken).not.toHaveBeenCalled()
  })
})
