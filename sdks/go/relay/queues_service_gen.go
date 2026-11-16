package relay

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type QueuesService struct {
	client *conjoin.Client
}

func (s *QueuesService) ReadQueueDefinitions(ctx context.Context, query *ReadQueueDefinitionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadQueueDefinitionsItem], error) {
	return conjoin.List[ReadQueueDefinitionsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "relay/queues/",
		Query:  query,
	}, opts...)
}

func (s *QueuesService) CreateQueueDefinition(ctx context.Context, body *CreateQueueDefinitionRequest, opts ...conjoin.CallOption) (*CreateQueueDefinitionResponse, error) {
	var out CreateQueueDefinitionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/queues/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *QueuesService) ReadQueueTasks(ctx context.Context, queueID string, query *ReadQueueTasksQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadQueueTasksItem], error) {
	return conjoin.List[ReadQueueTasksItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/queues/{queue_id}/tasks",
		PathParams: []string{queueID},
		Query:      query,
	}, opts...)
}

func (s *QueuesService) EnqueueTask(ctx context.Context, queueID string, body *EnqueueTaskRequest, opts ...conjoin.CallOption) (*EnqueueTaskResponse, error) {
	var out EnqueueTaskResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/queues/{queue_id}/tasks",
		PathParams:            []string{queueID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *QueuesService) ReadDeadLetterTasks(ctx context.Context, queueID string, query *ReadDeadLetterTasksQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadDeadLetterTasksItem], error) {
	return conjoin.List[ReadDeadLetterTasksItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/queues/{queue_id}/dead-letters",
		PathParams: []string{queueID},
		Query:      query,
	}, opts...)
}

func (s *QueuesService) ReadQueueDefinitionsCount(ctx context.Context, query *ReadQueueDefinitionsCountQuery, opts ...conjoin.CallOption) (*ReadQueueDefinitionsCountResponse, error) {
	var out ReadQueueDefinitionsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "relay/queues/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *QueuesService) UpdateQueueDefinition(ctx context.Context, queueID string, body *UpdateQueueDefinitionRequest, opts ...conjoin.CallOption) (*UpdateQueueDefinitionResponse, error) {
	var out UpdateQueueDefinitionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "relay/queues/{queue_id}",
		PathParams:   []string{queueID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *QueuesService) DeleteQueueDefinition(ctx context.Context, queueID string, opts ...conjoin.CallOption) (*DeleteQueueDefinitionResponse, error) {
	var out DeleteQueueDefinitionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "relay/queues/{queue_id}",
		PathParams: []string{queueID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *QueuesService) PauseQueue(ctx context.Context, queueID string, opts ...conjoin.CallOption) (*PauseQueueResponse, error) {
	var out PauseQueueResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/queues/{queue_id}/pause",
		PathParams:            []string{queueID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *QueuesService) ResumeQueue(ctx context.Context, queueID string, opts ...conjoin.CallOption) (*ResumeQueueResponse, error) {
	var out ResumeQueueResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/queues/{queue_id}/resume",
		PathParams:            []string{queueID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *QueuesService) BatchEnqueueTasks(ctx context.Context, queueID string, body *BatchEnqueueTasksRequest, opts ...conjoin.CallOption) (*BatchEnqueueTasksResponse, error) {
	var out BatchEnqueueTasksResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/queues/{queue_id}/enqueue-batch",
		PathParams:            []string{queueID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *QueuesService) ReadQueueTasksCount(ctx context.Context, queueID string, query *ReadQueueTasksCountQuery, opts ...conjoin.CallOption) (*ReadQueueTasksCountResponse, error) {
	var out ReadQueueTasksCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/queues/{queue_id}/tasks/count",
		PathParams: []string{queueID},
		Query:      query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *QueuesService) ReadDeadLetterTasksCount(ctx context.Context, queueID string, query *ReadDeadLetterTasksCountQuery, opts ...conjoin.CallOption) (*ReadDeadLetterTasksCountResponse, error) {
	var out ReadDeadLetterTasksCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/queues/{queue_id}/dead-letters/count",
		PathParams: []string{queueID},
		Query:      query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *QueuesService) ReplayDeadLetterTask(ctx context.Context, queueID string, deadLetterID string, opts ...conjoin.CallOption) (*ReplayDeadLetterTaskResponse, error) {
	var out ReplayDeadLetterTaskResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/queues/{queue_id}/dead-letters/{dead_letter_id}/replay",
		PathParams:            []string{queueID, deadLetterID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *QueuesService) PurgeQueueTasks(ctx context.Context, queueID string, body *PurgeQueueTasksRequest, opts ...conjoin.CallOption) (*PurgeQueueTasksResponse, error) {
	var out PurgeQueueTasksResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/queues/{queue_id}/purge",
		PathParams:            []string{queueID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
