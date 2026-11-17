import { ConjoinResponseError } from '../core/errors'

const MAX_PENDING_EVENT_CHARACTERS = 4_194_304

export type ServerSentEvent = {
  event?: string
  data: string
}

export async function* iterSSEMessages(body: ReadableStream<Uint8Array>): AsyncGenerator<ServerSentEvent> {
  const decoder = new TextDecoder()
  const reader = body.getReader()
  let buffer = ''

  try {
    for (;;) {
      const { done, value } = await reader.read()
      if (done) break

      buffer += decoder.decode(value, { stream: true }).replace(/\r\n/g, '\n')

      const chunks = buffer.split('\n\n')
      buffer = chunks.splice(-1)[0]

      if (buffer.length > MAX_PENDING_EVENT_CHARACTERS) {
        throw new ConjoinResponseError('The stream sent an event larger than the SDK accepts', { status: 200 })
      }

      for (const chunk of chunks) {
        const event = parseSSEChunk(chunk)
        if (event) yield event
      }
    }

    if (buffer.trim()) {
      const event = parseSSEChunk(buffer)
      if (event) yield event
    }
  } finally {
    reader.releaseLock()
  }
}

function parseSSEChunk(chunk: string): ServerSentEvent | null {
  let event: string | undefined
  const dataLines: string[] = []

  for (const line of chunk.split('\n')) {
    const trimmed = line.replace(/\r$/, '')

    if (trimmed.startsWith(':')) continue
    if (trimmed === '') continue

    const colonIdx = trimmed.indexOf(':')
    if (colonIdx === -1) continue

    const field = trimmed.slice(0, colonIdx)
    const value = trimmed.slice(colonIdx + 1).replace(/^ /, '')

    if (field === 'event') {
      event = value
    } else if (field === 'data') {
      dataLines.push(value)
    }
  }

  if (dataLines.length === 0) return null

  return { event, data: dataLines.join('\n') }
}
