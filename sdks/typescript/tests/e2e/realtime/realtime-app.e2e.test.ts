import { existsSync, renameSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'
import { setTimeout as sleep } from 'node:timers/promises'
import { getCloudDatabase } from '@databases/conjoin-cloud'
import { getRelayBroadcastChannelModel } from '@databases/conjoin-relay/models/relay-broadcast-channel-model'

const STOREFRONT_ACCOUNT_ID = 'clacc_storefront_owner'
const STOREFRONT_PROJECT_ID = 'clproj_storefront'
const OTHER_TENANT_ACCOUNT_ID = 'clacc_other_tenant'
const OTHER_TENANT_PROJECT_ID = 'clproj_other_tenant'
const ORDER_CHANNEL_ID = 'order-updates'
const SERVE_UNTIL_STOPPED_MS = 30 * 60 * 1000
const STOP_POLL_MS = 200

const readRequiredEnv = (name: string): string => {
  const value = process.env[name]

  if (value === undefined || value.length === 0) throw new Error(`Set ${name} to serve the realtime app`)

  return value
}

const monorepoDirectory = readRequiredEnv('CONJOIN_MONOREPO_DIR')
const infoFile = readRequiredEnv('CONJOIN_REALTIME_INFO_FILE')
const stopFile = readRequiredEnv('CONJOIN_REALTIME_STOP_FILE')

it(
  'serves the realtime app until the SDK test asks it to stop',
  async () => {
    const realtimeDirectory = join(monorepoDirectory, 'apps/conjoin-realtime')
    const { startRealtimeServer } = await import(join(realtimeDirectory, 'src/realtime-server.ts'))
    const { signBroadcastToken } = await import(join(realtimeDirectory, 'tests/e2e/realtime-client.ts'))
    const server = await startRealtimeServer({ port: 0, readDatabaseReadyState: () => getCloudDatabase().readyState })

    try {
      await getRelayBroadcastChannelModel().create({
        conjoin_account_id: STOREFRONT_ACCOUNT_ID,
        conjoin_project_id: STOREFRONT_PROJECT_ID,
        live_mode: true,
        channel_id: ORDER_CHANNEL_ID,
        name: 'Order updates',
        channel_type: 'private',
        authorization_mode: 'token',
        status: 'active',
      })

      const storefront = { accountId: STOREFRONT_ACCOUNT_ID, projectId: STOREFRONT_PROJECT_ID }
      const otherTenant = { accountId: OTHER_TENANT_ACCOUNT_ID, projectId: OTHER_TENANT_PROJECT_ID }

      const partialInfoFile = `${infoFile}.partial`

      writeFileSync(
        partialInfoFile,
        JSON.stringify({
          port: server.port,
          channel: ORDER_CHANNEL_ID,
          tokens: {
            storefrontConnection: signBroadcastToken({ tokenType: 'connection', ...storefront }),
            storefrontTestModeConnection: signBroadcastToken({
              tokenType: 'connection',
              ...storefront,
              isLiveMode: false,
            }),
            otherTenantConnection: signBroadcastToken({ tokenType: 'connection', ...otherTenant }),
            orderPublisher: signBroadcastToken({
              tokenType: 'channel',
              ...storefront,
              channelId: ORDER_CHANNEL_ID,
              permissions: ['subscribe', 'publish'],
            }),
            orderReader: signBroadcastToken({
              tokenType: 'channel',
              ...storefront,
              channelId: ORDER_CHANNEL_ID,
              permissions: ['subscribe'],
            }),
            otherTenantOrderReader: signBroadcastToken({
              tokenType: 'channel',
              ...otherTenant,
              channelId: ORDER_CHANNEL_ID,
              permissions: ['subscribe'],
            }),
          },
        }),
      )
      renameSync(partialInfoFile, infoFile)

      while (!existsSync(stopFile)) await sleep(STOP_POLL_MS)
    } finally {
      await server.stop()
    }
  },
  SERVE_UNTIL_STOPPED_MS,
)
