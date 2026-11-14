import { type ChildProcess, spawn } from 'node:child_process'
import { existsSync, mkdirSync, mkdtempSync, openSync, readFileSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { dirname, join, resolve } from 'node:path'
import { setTimeout as sleep } from 'node:timers/promises'
import { fileURLToPath } from 'node:url'

export type RealtimeAppTokens = {
  storefrontConnection: string
  storefrontTestModeConnection: string
  otherTenantConnection: string
  orderPublisher: string
  orderReader: string
  otherTenantOrderReader: string
}

export type RealtimeApp = {
  port: number
  channel: string
  tokens: RealtimeAppTokens
  stop: () => Promise<void>
}

const SDK_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '../../..')
const START_TIMEOUT_MS = 10 * 60 * 1000
const STOP_TIMEOUT_MS = 60 * 1000
const POLL_MS = 250
const LOG_TAIL_CHARACTERS = 4_000

const waitForExit = async (child: ChildProcess, timeoutMs: number): Promise<boolean> => {
  if (child.exitCode !== null || child.signalCode !== null) return true

  const exited = new Promise<boolean>(resolveExit => child.once('exit', () => resolveExit(true)))

  return Promise.race([exited, sleep(timeoutMs).then(() => false)])
}

const readLogTail = (logFile: string): string =>
  existsSync(logFile) ? readFileSync(logFile, 'utf8').slice(-LOG_TAIL_CHARACTERS) : ''

export const startRealtimeApp = async (monorepoDirectory: string): Promise<RealtimeApp> => {
  const workDirectory = mkdtempSync(join(tmpdir(), 'conjoin-sdk-realtime-'))
  const childTmpDirectory = join(workDirectory, 'tmp')
  const infoFile = join(workDirectory, 'realtime.json')
  const stopFile = join(workDirectory, 'stop')
  const logFile = join(workDirectory, 'realtime.log')
  const realtimeDirectory = join(monorepoDirectory, 'apps/conjoin-realtime')
  mkdirSync(childTmpDirectory)

  const logDescriptor = openSync(logFile, 'w')
  const child = spawn(
    join(realtimeDirectory, 'node_modules/.bin/vitest'),
    ['run', '--config', 'vitest.e2e.config.ts', '--globals', '--retry', '0', '--dir', SDK_ROOT, 'realtime-app.e2e'],
    {
      cwd: realtimeDirectory,
      env: {
        ...process.env,
        TMPDIR: childTmpDirectory,
        CONJOIN_MONOREPO_DIR: monorepoDirectory,
        CONJOIN_REALTIME_INFO_FILE: infoFile,
        CONJOIN_REALTIME_STOP_FILE: stopFile,
      },
      stdio: ['ignore', logDescriptor, logDescriptor],
    },
  )

  const stop = async (): Promise<void> => {
    try {
      writeFileSync(stopFile, '')
      if (!(await waitForExit(child, STOP_TIMEOUT_MS))) {
        child.kill('SIGKILL')
        await waitForExit(child, STOP_TIMEOUT_MS)
      }
    } finally {
      rmSync(workDirectory, { recursive: true, force: true })
    }
  }

  const startedAt = Date.now()

  while (!existsSync(infoFile)) {
    if (child.exitCode !== null || Date.now() - startedAt > START_TIMEOUT_MS) {
      const tail = readLogTail(logFile)
      await stop()
      throw new Error(`The realtime app did not start:\n${tail}`)
    }

    await sleep(POLL_MS)
  }

  const info = JSON.parse(readFileSync(infoFile, 'utf8')) as Omit<RealtimeApp, 'stop'>

  return { ...info, stop }
}
