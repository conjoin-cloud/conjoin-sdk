package relay

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SchedulersService struct {
	client *conjoin.Client
}

func (s *SchedulersService) ReadDefinitions(ctx context.Context, query *ReadSchedulerDefinitionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadSchedulerDefinitionsItem], error) {
	return conjoin.List[ReadSchedulerDefinitionsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "relay/schedules/",
		Query:  query,
	}, opts...)
}

func (s *SchedulersService) CreateDefinition(ctx context.Context, body *CreateSchedulerDefinitionRequest, opts ...conjoin.CallOption) (*CreateSchedulerDefinitionResponse, error) {
	var out CreateSchedulerDefinitionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/schedules/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SchedulersService) ReadExecutions(ctx context.Context, scheduleID string, query *ReadSchedulerExecutionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadSchedulerExecutionsItem], error) {
	return conjoin.List[ReadSchedulerExecutionsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/schedules/{schedule_id}/executions",
		PathParams: []string{scheduleID},
		Query:      query,
	}, opts...)
}

func (s *SchedulersService) ReadDeadLetterEntries(ctx context.Context, scheduleID string, query *ReadSchedulerDeadLetterEntriesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadSchedulerDeadLetterEntriesItem], error) {
	return conjoin.List[ReadSchedulerDeadLetterEntriesItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/schedules/{schedule_id}/dead-letters",
		PathParams: []string{scheduleID},
		Query:      query,
	}, opts...)
}

func (s *SchedulersService) ReadDefinitionsCount(ctx context.Context, query *ReadSchedulerDefinitionsCountQuery, opts ...conjoin.CallOption) (*ReadSchedulerDefinitionsCountResponse, error) {
	var out ReadSchedulerDefinitionsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "relay/schedules/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SchedulersService) UpdateDefinition(ctx context.Context, scheduleID string, body *UpdateSchedulerDefinitionRequest, opts ...conjoin.CallOption) (*UpdateSchedulerDefinitionResponse, error) {
	var out UpdateSchedulerDefinitionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "relay/schedules/{schedule_id}",
		PathParams:   []string{scheduleID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SchedulersService) Pause(ctx context.Context, scheduleID string, opts ...conjoin.CallOption) (*PauseSchedulerResponse, error) {
	var out PauseSchedulerResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/schedules/{schedule_id}/pause",
		PathParams:            []string{scheduleID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SchedulersService) Resume(ctx context.Context, scheduleID string, opts ...conjoin.CallOption) (*ResumeSchedulerResponse, error) {
	var out ResumeSchedulerResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/schedules/{schedule_id}/resume",
		PathParams:            []string{scheduleID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SchedulersService) Cancel(ctx context.Context, scheduleID string, opts ...conjoin.CallOption) (*CancelSchedulerResponse, error) {
	var out CancelSchedulerResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/schedules/{schedule_id}/cancel",
		PathParams:            []string{scheduleID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SchedulersService) TriggerExecution(ctx context.Context, scheduleID string, opts ...conjoin.CallOption) (*TriggerSchedulerExecutionResponse, error) {
	var out TriggerSchedulerExecutionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/schedules/{schedule_id}/trigger",
		PathParams:            []string{scheduleID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SchedulersService) ReadExecutionsCount(ctx context.Context, scheduleID string, query *ReadSchedulerExecutionsCountQuery, opts ...conjoin.CallOption) (*ReadSchedulerExecutionsCountResponse, error) {
	var out ReadSchedulerExecutionsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/schedules/{schedule_id}/executions/count",
		PathParams: []string{scheduleID},
		Query:      query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SchedulersService) ReadDeadLetterEntriesCount(ctx context.Context, scheduleID string, query *ReadSchedulerDeadLetterEntriesCountQuery, opts ...conjoin.CallOption) (*ReadSchedulerDeadLetterEntriesCountResponse, error) {
	var out ReadSchedulerDeadLetterEntriesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/schedules/{schedule_id}/dead-letters/count",
		PathParams: []string{scheduleID},
		Query:      query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SchedulersService) ReplayDeadLetterEntry(ctx context.Context, scheduleID string, deadLetterID string, opts ...conjoin.CallOption) (*ReplaySchedulerDeadLetterEntryResponse, error) {
	var out ReplaySchedulerDeadLetterEntryResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/schedules/{schedule_id}/dead-letters/{dead_letter_id}/replay",
		PathParams:            []string{scheduleID, deadLetterID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
