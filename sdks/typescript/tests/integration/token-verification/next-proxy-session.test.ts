import { createServer, type Server } from 'node:http'
import type { AddressInfo } from 'node:net'
import { exportJWK, generateKeyPair, type JWK, SignJWT } from 'jose'
import { NextRequest } from 'next/server'
import { afterAll, beforeAll, describe, expect, it } from 'vitest'
import { conjoinProxy } from '../../../src/next/proxy'
import type { AuthObject } from '../../../src/next/types'

const AUTH_CLIENT_ISSUER_PATH = '/v1/auth/client'
const JWKS_PATH = `${AUTH_CLIENT_ISSUER_PATH}/.well-known/jwks.json`
const SESSION_TOKEN_AUDIENCE = 'conjoin-auth-session'
const SIGNING_KEY_ID = 'harbour-signing-key'
const PATIENT_PORTAL_APP_ID = 'app_harbourpatientportal'
const PATIENT_ACCOUNT_ID = 'acc_harbourpatient'
const PATIENT_SESSION_ID = 'ses_harbourpatient'
const PATIENT_CLIENT_ID = 'cli_harbourpatientbrowser'
const PATIENT_REFERENCE_ID = 'ref_harbourpatientbrowser'
const CARDIOLOGY_ORGANIZATION_ID = 'org_harbourcardiology'
const PATIENT_DASHBOARD_URL = 'https://portal.harbour-clinic.example/dashboard'

type AuthDomainServer = {
  authDomain: string
  jwksUrl: string
  signSessionToken: (clientId: string) => Promise<string>
  stop: () => Promise<void>
}

const startAuthDomainServer = async (): Promise<AuthDomainServer> => {
  const { privateKey, publicKey } = await generateKeyPair('RS256')
  const publicJwk: JWK = { ...(await exportJWK(publicKey)), kid: SIGNING_KEY_ID, alg: 'RS256', use: 'sig' }
  const server: Server = createServer((request, response) => {
    if (request.url !== JWKS_PATH) {
      response.writeHead(404).end()
      return
    }

    response.writeHead(200, { 'content-type': 'application/json' }).end(JSON.stringify({ keys: [publicJwk] }))
  })

  await new Promise<void>(resolve => server.listen(0, '127.0.0.1', resolve))

  const { port } = server.address() as AddressInfo
  const authDomain = `127.0.0.1:${port}`

  return {
    authDomain,
    jwksUrl: `http://${authDomain}${JWKS_PATH}`,
    signSessionToken: clientId =>
      new SignJWT({
        session_id: PATIENT_SESSION_ID,
        client_id: clientId,
        app_id: PATIENT_PORTAL_APP_ID,
        live_mode: false,
        organization_id: CARDIOLOGY_ORGANIZATION_ID,
        organization_roles: ['org:viewer'],
      })
        .setProtectedHeader({ alg: 'RS256', kid: SIGNING_KEY_ID, typ: 'JWT' })
        .setIssuer(`https://${authDomain}${AUTH_CLIENT_ISSUER_PATH}`)
        .setSubject(PATIENT_ACCOUNT_ID)
        .setAudience(SESSION_TOKEN_AUDIENCE)
        .setIssuedAt()
        .setExpirationTime('60s')
        .sign(privateKey),
    stop: () => new Promise<void>(resolve => server.close(() => resolve())),
  }
}

const buildAuthCookieHeader = (sessionToken: string): string => {
  const clientHandle = encodeURIComponent(
    JSON.stringify({ client_id: PATIENT_CLIENT_ID, reference_id: PATIENT_REFERENCE_ID }),
  )

  return `__conjoin_auth_cl=${clientHandle}; __conjoin_auth_sess=${sessionToken}`
}

describe('conjoinProxy with the cookies that Conjoin Auth sets', () => {
  let authDomainServer: AuthDomainServer

  beforeAll(async () => {
    authDomainServer = await startAuthDomainServer()
  })

  afterAll(async () => {
    await authDomainServer.stop()
  })

  it('sees the signed-in patient from the client handle and the session token', async () => {
    const sessionToken = await authDomainServer.signSessionToken(PATIENT_CLIENT_ID)
    const request = new NextRequest(PATIENT_DASHBOARD_URL, {
      headers: { cookie: buildAuthCookieHeader(sessionToken) },
    })
    const seenAuth: (AuthObject | null)[] = []
    const proxy = conjoinProxy(
      auth => {
        seenAuth.push(auth)
        return undefined
      },
      { authDomain: authDomainServer.authDomain, jwksUrl: authDomainServer.jwksUrl },
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
