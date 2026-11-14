import type { ConjoinClient } from '@conjoin-cloud/sdk'
import { createConjoinPublicApi } from '../auth/auth-api'
import type { ConjoinBranding, ConjoinSdkConfig } from './types'

const cachedConfigs = new Map<string, ConjoinSdkConfig>()
const inflightConfigs = new Map<string, Promise<ConjoinSdkConfig>>()

const configCacheKey = (client: ConjoinClient): string =>
  `${client.config.baseUrl} ${client.config.publishableKey ?? client.config.apiKey ?? ''}`

async function readSdkConfig(client: ConjoinClient): Promise<ConjoinSdkConfig> {
  const settings = await createConjoinPublicApi(client).sdk.readSdkSettings({ auth: { type: 'default' } })

  return {
    project_id: settings.project_id,
    environment: settings.environment,
    api_url: settings.api_url,
    branding: settings.branding as ConjoinBranding | null,
    auth: settings.auth,
    relay: { url: settings.relay.url },
  }
}

export function fetchSdkConfig(client: ConjoinClient): Promise<ConjoinSdkConfig> {
  const key = configCacheKey(client)
  const cached = cachedConfigs.get(key)
  if (cached) return Promise.resolve(cached)

  const inflight = inflightConfigs.get(key)
  if (inflight) return inflight

  const request = readSdkConfig(client)
    .then(config => {
      cachedConfigs.set(key, config)
      return config
    })
    .finally(() => {
      inflightConfigs.delete(key)
    })

  inflightConfigs.set(key, request)

  return request
}
