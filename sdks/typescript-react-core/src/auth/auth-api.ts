import { type ConjoinClient, ConjoinConfigurationError, createConjoinClient } from '@conjoin-cloud/sdk'
import {
  createAuthAccounts,
  createAuthClients,
  createAuthFlows,
  createAuthNatives,
  createAuthSelves,
  createBillingSelves,
  createCloudSDKs,
} from '@conjoin-cloud/sdk/frontend'

export type BillingSelfCalls = ReturnType<typeof createBillingSelves>

const AUTH_DOMAIN_PATTERN = /^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)*(:[0-9]{1,5})?$/i

export type AuthDomainCalls = {
  selves: ReturnType<typeof createAuthSelves>
  clients: ReturnType<typeof createAuthClients>
  webFlows: ReturnType<typeof createAuthFlows>
  nativeFlows: ReturnType<typeof createAuthNatives>
}

export type ConjoinAuthApi = AuthDomainCalls & {
  authBaseUrl: string
  billingSelves: (billingEntityId: string) => BillingSelfCalls
}

export type ConjoinPublicApi = {
  sdk: ReturnType<typeof createCloudSDKs>
  accounts: ReturnType<typeof createAuthAccounts>
}

export function resolveAuthBaseUrl(authDomain: string): string {
  const trimmed = authDomain.trim()

  if (/^https?:\/\//i.test(trimmed)) {
    const url = new URL(trimmed)

    if (url.pathname !== '/' || url.search !== '' || url.hash !== '' || url.username !== '' || url.password !== '') {
      throw new ConjoinConfigurationError(`The auth domain must be a bare origin: ${authDomain}`)
    }

    return url.origin
  }

  if (!AUTH_DOMAIN_PATTERN.test(trimmed)) {
    throw new ConjoinConfigurationError(`The auth domain is not a valid host name: ${authDomain}`)
  }

  return `https://${trimmed}`
}

export function createConjoinAuthApi(publishableKey: string, authDomain: string): ConjoinAuthApi {
  const authBaseUrl = resolveAuthBaseUrl(authDomain)
  const client = createConjoinClient({ publishableKey, baseUrl: authBaseUrl, credentials: 'include' })

  return {
    authBaseUrl,
    selves: createAuthSelves(client),
    clients: createAuthClients(client),
    webFlows: createAuthFlows(client),
    nativeFlows: createAuthNatives(client),
    billingSelves: billingEntityId => createBillingSelves(client.withScope({ billingEntityId })),
  }
}

export function createConjoinPublicApi(client: ConjoinClient): ConjoinPublicApi {
  return {
    sdk: createCloudSDKs(client),
    accounts: createAuthAccounts(client),
  }
}
