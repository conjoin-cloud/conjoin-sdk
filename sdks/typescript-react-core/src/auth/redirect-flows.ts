import * as v from 'valibot'
import type { AuthFlowState } from '../provider/types'
import { ClientHandleSchema } from './client-handle-schema'

const REDIRECT_FLOW_KEY_PREFIX = 'conjoin_auth_redirect_flow:'
const REDIRECT_FLOW_MAX_AGE_MS = 10 * 60 * 1000
const MAX_PENDING_REDIRECT_FLOWS = 8

const StoredRedirectFlowSchema = v.object({
  savedAt: v.number(),
  flow: v.object({
    kind: v.picklist(['signin', 'signup']),
    proof: v.object({
      state: v.pipe(v.string(), v.minLength(1), v.maxLength(256)),
      codeVerifier: v.pipe(v.string(), v.minLength(43), v.maxLength(128)),
      codeChallenge: v.pipe(v.string(), v.length(43)),
    }),
    clientHandle: v.nullable(ClientHandleSchema),
  }),
})

export type RedirectFlowStore = Pick<Storage, 'getItem' | 'setItem' | 'removeItem'>

const isFresh = (savedAt: number, now: number): boolean =>
  now - savedAt >= 0 && now - savedAt <= REDIRECT_FLOW_MAX_AGE_MS

export function createRedirectFlowRegistry(readStore: () => RedirectFlowStore | null) {
  const pending = new Map<string, { savedAt: number; flow: AuthFlowState }>()

  function prune(now: number) {
    for (const [state, entry] of pending) {
      if (!isFresh(entry.savedAt, now)) pending.delete(state)
    }

    while (pending.size >= MAX_PENDING_REDIRECT_FLOWS) {
      const oldest = pending.keys().next()
      if (oldest.done) break
      pending.delete(oldest.value)
    }
  }

  function save(flow: AuthFlowState) {
    const now = Date.now()
    const entry = { savedAt: now, flow }

    prune(now)
    pending.set(flow.proof.state, entry)

    try {
      readStore()?.setItem(`${REDIRECT_FLOW_KEY_PREFIX}${flow.proof.state}`, JSON.stringify(entry))
    } catch {
      return
    }
  }

  function readStored(state: string): { savedAt: number; flow: AuthFlowState } | null {
    try {
      const store = readStore()
      const key = `${REDIRECT_FLOW_KEY_PREFIX}${state}`
      const raw = store?.getItem(key) ?? null
      store?.removeItem(key)
      if (raw === null) return null

      const parsed = v.safeParse(StoredRedirectFlowSchema, JSON.parse(raw))

      return parsed.success ? parsed.output : null
    } catch {
      return null
    }
  }

  function take(state: string): AuthFlowState | null {
    const inMemory = pending.get(state) ?? null
    pending.delete(state)
    const stored = readStored(state)
    const entry = inMemory ?? stored

    if (entry === null || entry.flow.proof.state !== state || !isFresh(entry.savedAt, Date.now())) return null

    return entry.flow
  }

  return { save, take }
}
