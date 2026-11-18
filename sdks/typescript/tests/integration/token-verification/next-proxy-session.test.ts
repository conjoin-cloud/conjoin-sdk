import { NextRequest } from 'next/server'
import { afterAll, beforeAll, describe, expect, it } from 'vitest'
import { conjoinProxy } from '../../../src/next/proxy'
import type { AuthObject } from '../../../src/next/types'
import {
  AUTH_CLIENT_ISSUER_PATH,
  CARDIOLOGY_ORGANIZATION_ID,
  PATIENT_ACCOUNT_ID,
  PATIENT_PORTAL_APP_ID,
  PATIENT_SESSION_ID,
  SESSION_TOKEN_AUDIENCE,
  type SigningKeyServer,
  startSigningKeyServer,
} from './signing-key-server'

const PATIENT_CLIENT_ID = 'cli_harbourpatientbrowser'
const PATIENT_REFERENCE_ID = 'ref_harbourpatientbrowser'
const PATIENT_DASHBOARD_URL = 'https://portal.harbour-clinic.example/dashboard'

const buildAuthCookieHeader = (sessionToken: string): string => {
  const clientHandle = encodeURIComponent(
    JSON.stringify({ client_id: PATIENT_CLIENT_ID, reference_id: PATIENT_REFERENCE_ID }),
  )

  return `__conjoin_auth_cl=${clientHandle}; __conjoin_auth_sess=${sessionToken}`
}

describe('conjoinProxy with the cookies that Conjoin Auth sets', () => {
  let signingKeys: SigningKeyServer

  beforeAll(async () => {
    signingKeys = await startSigningKeyServer()
  })

  afterAll(async () => {
    await signingKeys.stop()
  })

  it('sees the signed-in patient from the client handle and the session token', async () => {
    const sessionToken = await signingKeys.signToken({
      claims: {
        session_id: PATIENT_SESSION_ID,
        client_id: PATIENT_CLIENT_ID,
        app_id: PATIENT_PORTAL_APP_ID,
        live_mode: false,
        organization_id: CARDIOLOGY_ORGANIZATION_ID,
        organization_roles: ['org:viewer'],
      },
      audience: SESSION_TOKEN_AUDIENCE,
      issuer: `https://${signingKeys.authDomain}${AUTH_CLIENT_ISSUER_PATH}`,
    })
    const request = new NextRequest(PATIENT_DASHBOARD_URL, {
      headers: { cookie: buildAuthCookieHeader(sessionToken) },
    })
    const seenAuth: (AuthObject | null)[] = []
    const proxy = conjoinProxy(
      auth => {
        seenAuth.push(auth)
        return undefined
      },
      { authDomain: signingKeys.authDomain, jwksUrl: signingKeys.jwksUrl },
    )

    await proxy(request)

    expect(seenAuth).toHaveLength(1)
    expect(seenAuth[0]).toMatchObject({
      accountId: PATIENT_ACCOUNT_ID,
      sessionId: PATIENT_SESSION_ID,
      organizationId: CARDIOLOGY_ORGANIZATION_ID,
      organizationRoles: ['org:viewer'],
    })
    expect(seenAuth[0]?.getToken()).toBe(sessionToken)
  })
})
