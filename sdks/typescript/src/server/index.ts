import { createConjoinClient } from '../core/client'
import { getConjoinRequestIdFromHeaders, type HeaderMapLike } from '../core/request-tracing'
import type { ConjoinClient } from '../core/types'
import { createCloudSDKs } from '../generated/frontend/cloud-sdk'

export type ServerOptions = {
  apiKey: string
  baseUrl?: string
  conjoinRequestId?: string
  request?: {
    headers?: HeaderMapLike
  }
}

export function createConjoinServer(options: ServerOptions): ConjoinClient {
  const conjoinRequestId = options.conjoinRequestId ?? getConjoinRequestIdFromHeaders(options.request?.headers)

  return createConjoinClient({
    apiKey: options.apiKey,
    baseUrl: options.baseUrl,
    ...(conjoinRequestId ? { conjoinRequestId } : {}),
  })
}

export type BrandingOptions = {
  baseUrl?: string
}

export async function fetchConjoinBranding(
  publishableKey: string,
  options?: BrandingOptions,
): Promise<Record<string, unknown> | null> {
  const client = createConjoinClient({
    publishableKey,
    baseUrl: options?.baseUrl,
  })

  const settings = await createCloudSDKs(client).readSdkSettings()
  return settings.branding
}

export type {
  VerifiedToken,
  VerifyTokenOptions,
} from './tokens'
export { buildConjoinAuthIssuer, buildConjoinAuthJwksUrl, verifyToken } from './tokens'
export { verifyWebhook } from './webhooks'
