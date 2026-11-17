import type { operations } from '../generated/api-types'

type ChatCompletionOperation = operations['createAiChatCompletion']

export type ChatRole = 'system' | 'user' | 'assistant' | 'tool'

export type ChatCompletionParams = Omit<
  NonNullable<ChatCompletionOperation['requestBody']>['content']['application/json'],
  'stream'
>

export type ChatMessage = ChatCompletionParams['messages'][number]

export type ChatCompletionResponse = ChatCompletionOperation['responses']['200']['content']['application/json']

export type ChatCompletionUsage = {
  prompt_tokens: number
  completion_tokens: number
  total_tokens: number
}

export type ChatCompletionChunkDelta = {
  role?: ChatRole
  content?: string | null
  tool_calls?: Array<{
    index: number
    id?: string
    type?: 'function'
    function?: {
      name?: string
      arguments?: string
    }
  }>
}

export type ChatCompletionChunk = {
  id: string
  object: 'chat.completion.chunk'
  created: number
  model: string
  choices: Array<{
    index: number
    delta: ChatCompletionChunkDelta
    finish_reason: 'stop' | 'length' | 'tool_calls' | 'content_filter' | null
  }>
  usage?: ChatCompletionUsage
}
