import type { AuthClientHandle } from '../provider/types'

export const AUTH_STATE_HEADER = 'X-Auth-State'
export const AUTH_CODE_VERIFIER_HEADER = 'X-Auth-Code-Verifier'
export const AUTH_CODE_CHALLENGE_HEADER = 'X-Auth-Code-Challenge'
export const CLIENT_HANDLE_HEADER = 'X-Conjoin-Client-Handle'
export const CSRF_TOKEN_HEADER = 'X-CSRF-Token'

export const encodeClientHandle = (handle: AuthClientHandle): string =>
  encodeURIComponent(JSON.stringify({ client_id: handle.client_id, reference_id: handle.reference_id }))
