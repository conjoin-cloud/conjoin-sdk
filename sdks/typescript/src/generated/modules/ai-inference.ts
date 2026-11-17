import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateChatCompletionBody = NonNullable<operations['createAiChatCompletion']['requestBody']>['content']['application/json']
type CreateChatCompletionResponse = operations['createAiChatCompletion']['responses']['200']['content']['application/json']
type CreateAiMultiModelBody = NonNullable<operations['createAiMultiModelInference']['requestBody']>['content']['application/json']
type CreateAiMultiModelData = NonNullable<operations['createAiMultiModelInference']['responses']['201']['content']['application/json']['data']>
type CreateAiBestOfNBody = NonNullable<operations['createAiBestOfNInference']['requestBody']>['content']['application/json']
type CreateAiBestOfNData = NonNullable<operations['createAiBestOfNInference']['responses']['201']['content']['application/json']['data']>
type ListRequestsData = NonNullable<operations['listAiInferenceRequests']['responses']['200']['content']['application/json']['data']>[number]
type ListRequestsQuery = NonNullable<operations['listAiInferenceRequests']['parameters']['query']>
type ListRequestsCountData = NonNullable<operations['listAiInferenceRequestsCount']['responses']['200']['content']['application/json']['data']>
type ListRequestsCountQuery = NonNullable<operations['listAiInferenceRequestsCount']['parameters']['query']>
type ReadRequestData = NonNullable<operations['readAiInferenceRequest']['responses']['200']['content']['application/json']['data']>

export function createAiInferences(client: ConjoinClient) {
  return {
    createChatCompletion: (data: CreateChatCompletionBody, options?: ConjoinCallOptions) =>
      client.fetchJson<CreateChatCompletionResponse>('ai/inference/chat/completions', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    createAiMultiModel: (data: CreateAiMultiModelBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateAiMultiModelData>('ai/multi-model-inferences/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    createAiBestOfN: (data: CreateAiBestOfNBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateAiBestOfNData>('ai/best-of-n-inferences/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    listRequests: (query?: ListRequestsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListRequestsData>('ai/inference-requests/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    listRequestsCount: (query?: ListRequestsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListRequestsCountData>('ai/inference-requests/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readRequest: (inferenceRequestId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadRequestData>(`ai/inference-requests/${encodePathParam(inferenceRequestId)}`, { ...options, method: 'GET' }),
  }
}
