import { buildApiError } from '../core/error-response'
import { ConjoinApiError, ConjoinResponseError } from '../core/errors'
import { getConjoinRequestIdFromHeaders } from '../core/request-tracing'
import type { ConjoinCallOptions, ConjoinClient } from '../core/types'
import { createAiInferences } from '../generated/modules/ai-inference'
import { iterSSEMessages } from './sse'
import type { ChatCompletionChunk, ChatCompletionParams, ChatCompletionResponse } from './types'

const CHAT_COMPLETIONS_PATH = 'ai/inference/chat/completions'
const MAX_REPORTED_CHUNK_CHARACTERS = 200

export type ChatStreamOptions = Pick<ConjoinCallOptions, 'signal' | 'idempotencyKey' | 'conjoinRequestId'>

export type ChatStream = AsyncIterable<ChatCompletionChunk> & {
  controller: AbortController
}

type GeneratedChatCompletionBody = Parameters<ReturnType<typeof createAiInferences>['createChatCompletion']>[0]

export function createAiChat(client: ConjoinClient) {
  const inferences = createAiInferences(client)

  return {
    async complete(
      params: Omit<ChatCompletionParams, 'stream'>,
      options?: ChatStreamOptions,
    ): Promise<ChatCompletionResponse> {
      const body = { ...params, stream: false } as unknown as GeneratedChatCompletionBody
      const completion = await inferences.createChatCompletion(body, options)

      return completion as unknown as ChatCompletionResponse
    },

    stream(params: Omit<ChatCompletionParams, 'stream'>, options?: ChatStreamOptions): ChatStream {
      const controller = new AbortController()
      const signals = options?.signal ? [controller.signal, options.signal] : [controller.signal]
      const iterator = createStreamIterator(client, params, { ...options, signal: AbortSignal.any(signals) })

      return {
        controller,
        [Symbol.asyncIterator]() {
          let consumed = false
          return {
            async next() {
              const result = await iterator.next()
              if (result.done) consumed = true
              return result
            },
            async return(value) {
              if (!consumed) controller.abort()
              return iterator.return(value)
            },
            async throw(error) {
              controller.abort()
              return iterator.throw(error)
            },
          }
        },
      }
    },
  }
}

async function* createStreamIterator(
  client: ConjoinClient,
  params: Omit<ChatCompletionParams, 'stream'>,
  options: ChatStreamOptions,
): AsyncGenerator<ChatCompletionChunk> {
  const response = await client.fetchRaw(CHAT_COMPLETIONS_PATH, {
    ...options,
    method: 'POST',
    body: { ...params, stream: true },
    acceptsIdempotencyKey: true,
  })
  const requestId = getConjoinRequestIdFromHeaders(response.headers)

  if (!response.ok) {
    throw await buildApiError(response, requestId)
  }

  if (!response.body) {
    throw new ConjoinResponseError('The stream response has no body', { status: response.status, requestId })
  }

  for await (const event of iterSSEMessages(response.body)) {
    if (event.data === '[DONE]') return

    let chunk: ChatCompletionChunk | { error?: { message?: unknown; code?: unknown } }

    try {
      chunk = JSON.parse(event.data) as typeof chunk
    } catch {
      throw new ConjoinResponseError(
        `The stream sent a chunk that is not JSON: ${event.data.slice(0, MAX_REPORTED_CHUNK_CHARACTERS)}`,
        { status: response.status, requestId },
      )
    }

    if ('error' in chunk && chunk.error) {
      const message = typeof chunk.error.message === 'string' ? chunk.error.message : 'The stream reported an error'
      const code = typeof chunk.error.code === 'string' ? chunk.error.code : 'stream_error'
      throw new ConjoinApiError(message, { status: response.status, code, requestId })
    }

    yield chunk as ChatCompletionChunk
  }
}
