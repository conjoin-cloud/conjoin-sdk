import { createServer, type Server } from 'node:http'
import type { AddressInfo } from 'node:net'
import { exportJWK, generateKeyPair, type JWK, SignJWT } from 'jose'

export const AUTH_CLIENT_ISSUER_PATH = '/v1/auth/client'
export const SESSION_TOKEN_AUDIENCE = 'conjoin-auth-session'
export const PATIENT_PORTAL_APP_ID = 'app_harbourpatientportal'
export const PATIENT_ACCOUNT_ID = 'acc_harbourpatient'
export const PATIENT_SESSION_ID = 'ses_harbourpatient'
export const CARDIOLOGY_ORGANIZATION_ID = 'org_harbourcardiology'

const JWKS_PATH = `${AUTH_CLIENT_ISSUER_PATH}/.well-known/jwks.json`
const SIGNING_KEY_ID = 'harbour-signing-key'
const TOKEN_LIFETIME = '5m'

type SignTokenOptions = {
  claims: Record<string, unknown>
  audience: string
  issuer: string
}

export type SigningKeyServer = {
  authDomain: string
  jwksUrl: string
  signToken: (options: SignTokenOptions) => Promise<string>
  stop: () => Promise<void>
}

export const startSigningKeyServer = async (): Promise<SigningKeyServer> => {
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
    signToken: ({ claims, audience, issuer }) =>
      new SignJWT(claims)
        .setProtectedHeader({ alg: 'RS256', kid: SIGNING_KEY_ID, typ: 'JWT' })
        .setIssuer(issuer)
        .setSubject(PATIENT_ACCOUNT_ID)
        .setAudience(audience)
        .setIssuedAt()
        .setExpirationTime(TOKEN_LIFETIME)
        .sign(privateKey),
    stop: () => new Promise<void>(resolve => server.close(() => resolve())),
  }
}
