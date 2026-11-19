import { type VerifiedToken, verifyToken } from '../server/tokens'
import { resolveTokenVerificationTarget } from './config'
import type { AuthObject, NextAdapterConfig } from './types'

type VerifyAuthObjectOptions = {
  token: string
  config: NextAdapterConfig
  isTokenAccepted?: (verified: VerifiedToken) => boolean
}

export async function verifyAuthObject({
  token,
  config,
  isTokenAccepted,
}: VerifyAuthObjectOptions): Promise<AuthObject | null> {
  const { jwksUrl, issuer } = await resolveTokenVerificationTarget(config)

  try {
    const verified = await verifyToken(token, { jwksUrl, issuer })
    if (isTokenAccepted && !isTokenAccepted(verified)) return null

    return {
      accountId: verified.accountId,
      sessionId: verified.sessionId,
      organizationId: verified.organizationId,
      organizationRoles: verified.organizationRoles,
      getToken: () => token,
    }
  } catch {
    return null
  }
}
