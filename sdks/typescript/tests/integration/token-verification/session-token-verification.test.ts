import { createServer, type Server } from 'node:http'
import type { AddressInfo } from 'node:net'
import { exportJWK, generateKeyPair, type JWK, SignJWT } from 'jose'
import { afterAll, beforeAll, describe, expect, it } from 'vitest'
import { verifyToken } from '../../../src/server/tokens'

const AUTH_CLIENT_ISSUER_PATH = '/v1/auth/client'
const JWKS_PATH = `${AUTH_CLIENT_ISSUER_PATH}/.well-known/jwks.json`
const SESSION_TOKEN_AUDIENCE = 'conjoin-auth-session'
const PATIENT_PORTAL_APP_ID = 'app_harbourpatientportal'
const SIGNING_KEY_ID = 'harbour-signing-key'
const PATIENT_ACCOUNT_ID = 'acc_harbourpatient'
const PATIENT_SESSION_ID = 'ses_harbourpatient'
const CARDIOLOGY_ORGANIZATION_ID = 'org_harbourcardiology'

type SigningKeyServer = {
  issuer: string
  jwksUrl: string
  signToken: (claims: Record<string, unknown>, audience: string) => Promise<string>
  stop: () => Promise<void>
}

const startSigningKeyServer = async (): Promise<SigningKeyServer> => {
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
  const issuer = `http://127.0.0.1:${port}${AUTH_CLIENT_ISSUER_PATH}`

  return {
    issuer,
    jwksUrl: `http://127.0.0.1:${port}${JWKS_PATH}`,
    signToken: (claims, audience) =>
      new SignJWT(claims)
        .setProtectedHeader({ alg: 'RS256', kid: SIGNING_KEY_ID, typ: 'JWT' })
        .setIssuer(issuer)
        .setSubject(PATIENT_ACCOUNT_ID)
        .setAudience(audience)
        .setIssuedAt()
        .setExpirationTime('5m')
        .sign(privateKey),
    stop: () => new Promise<void>(resolve => server.close(() => resolve())),
  }
}

describe('verifyToken against the keys that Conjoin Auth publishes under its issuer', () => {
  let signingKeys: SigningKeyServer

  beforeAll(async () => {
    signingKeys = await startSigningKeyServer()
  })

  afterAll(async () => {
    await signingKeys.stop()
  })

  it('reads the account, session, and active organisation from a session token', async () => {
    const sessionToken = await signingKeys.signToken(
      {
        session_id: PATIENT_SESSION_ID,
        app_id: PATIENT_PORTAL_APP_ID,
        live_mode: false,
        organization_id: CARDIOLOGY_ORGANIZATION_ID,
        organization_roles: ['org:viewer', 'org:manager'],
      },
      SESSION_TOKEN_AUDIENCE,
    )

    const verified = await verifyToken(sessionToken, { jwksUrl: signingKeys.jwksUrl, issuer: signingKeys.issuer })

    expect(verified).toMatchObject({
      accountId: PATIENT_ACCOUNT_ID,
      sessionId: PATIENT_SESSION_ID,
      organizationId: CARDIOLOGY_ORGANIZATION_ID,
      organizationRoles: ['org:viewer', 'org:manager'],
    })
  })

  it('refuses an OpenID Connect ID token that the same app signed for its client', async () => {
    const idToken = await signingKeys.signToken({ sid: PATIENT_SESSION_ID }, PATIENT_PORTAL_APP_ID)

    await expect(verifyToken(idToken, { jwksUrl: signingKeys.jwksUrl, issuer: signingKeys.issuer })).rejects.toThrow()
  })
})
