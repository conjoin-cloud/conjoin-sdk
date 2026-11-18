export const CLIENT_HANDLE_IDENTIFIER_PATTERN = /^[\w.:-]+$/
export const CLIENT_HANDLE_IDENTIFIER_MAX_LENGTH = 256

export type ConjoinClientHandle = {
  client_id: string
  reference_id: string
}

export function isClientHandleIdentifier(value: unknown): value is string {
  return (
    typeof value === 'string' &&
    value.length > 0 &&
    value.length <= CLIENT_HANDLE_IDENTIFIER_MAX_LENGTH &&
    CLIENT_HANDLE_IDENTIFIER_PATTERN.test(value)
  )
}

export function parseClientHandle(value: unknown): ConjoinClientHandle | null {
  if (typeof value !== 'object' || value === null || Array.isArray(value)) return null

  const { client_id: clientId, reference_id: referenceId } = value as Record<string, unknown>
  if (!isClientHandleIdentifier(clientId) || !isClientHandleIdentifier(referenceId)) return null

  return { client_id: clientId, reference_id: referenceId }
}

export function encodeClientHandle({ client_id, reference_id }: ConjoinClientHandle): string {
  return encodeURIComponent(JSON.stringify({ client_id, reference_id }))
}
