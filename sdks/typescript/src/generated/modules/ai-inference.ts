import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateChatCompletionBody = NonNullable<operations['createAiChatCompletion']['requestBody']>['content']['application/json']
type CreateChatCompletionData = NonNullable<operations['createAiChatCompletion']['responses']['200']['content']['application/json']['data']>
type CreateAiMultiModelBody = NonNullable<operations['createAiMultiModelInference']['requestBody']>['content']['application/json']
type CreateAiMultiModelData = NonNullable<operations['createAiMultiModelInference']['responses']['200']['content']['application/json']['data']>
type CreateAiBestOfNBody = NonNullable<operations['createAiBestOfNInference']['requestBody']>['content']['application/json']
type CreateAiBestOfNData = NonNullable<operations['createAiBestOfNInference']['responses']['200']['content']['application/json']['data']>
type ListRequestsData = NonNullable<operations['listAiInferenceRequests']['responses']['200']['content']['application/json']['data']>[number]
type ListRequestsQuery = NonNullable<operations['listAiInferenceRequests']['parameters']['query']>
type ReadRequestData = NonNullable<operations['readAiInferenceRequest']['responses']['200']['content']['application/json']['data']>

export function createAiInferences(client: ConjoinClient) {
  return {
    createChatCompletion: (data: CreateChatCompletionBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateChatCompletionData>('ai/inference/chat/completions', { ...options, method: 'POST', body: data }),

    createAiMultiModel: (data: CreateAiMultiModelBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateAiMultiModelData>('ai/inference/multi-model', { ...options, method: 'POST', body: data }),

    createAiBestOfN: (data: CreateAiBestOfNBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateAiBestOfNData>('ai/inference/best-of-n', { ...options, method: 'POST', body: data }),

    listRequests: (query?: ListRequestsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListRequestsData>('ai/inference/requests', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readRequest: (requestId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadRequestData>(`ai/inference/requests/${encodePathParam(requestId)}`, { ...options, method: 'GET' }),
  }
}
