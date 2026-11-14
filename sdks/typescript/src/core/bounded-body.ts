import { ConjoinResponseError } from './errors'

export async function readBoundedText(response: Response, maxBytes: number, requestId?: string): Promise<string> {
  if (response.body === null) {
    return ''
  }

  const reader = response.body.getReader()
  const chunks: Uint8Array[] = []
  let total = 0

  try {
    while (true) {
      const { done, value } = await reader.read()

      if (done) {
        break
      }

      const room = maxBytes - total
      if (requestId !== undefined && value.byteLength > room) {
        throw new ConjoinResponseError('The response body exceeded the size limit', {
          status: response.status,
          requestId,
        })
      }
      const chunk = value.byteLength > room ? value.subarray(0, room) : value
      chunks.push(chunk)
      total += chunk.byteLength
      if (requestId === undefined && total >= maxBytes) break
    }
  } finally {
    await reader.cancel().catch(() => undefined)
  }

  const bytes = new Uint8Array(total)
  let offset = 0

  for (const chunk of chunks) {
    bytes.set(chunk, offset)
    offset += chunk.byteLength
  }

  return new TextDecoder().decode(bytes)
}
