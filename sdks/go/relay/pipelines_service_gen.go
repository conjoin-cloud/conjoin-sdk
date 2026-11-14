package relay

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type PipelinesService struct {
	client *conjoin.Client
}

func (s *PipelinesService) ReadPipelineDefinitions(ctx context.Context, query *ReadPipelineDefinitionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadPipelineDefinitionsItem], error) {
	return conjoin.List[ReadPipelineDefinitionsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "relay/pipelines/",
		Query:  query,
	}, opts...)
}

func (s *PipelinesService) CreatePipelineDefinition(ctx context.Context, body *CreatePipelineDefinitionRequest, opts ...conjoin.CallOption) (*CreatePipelineDefinitionResponse, error) {
	var out CreatePipelineDefinitionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "relay/pipelines/",
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PipelinesService) ReadPipelineDefinitionsCount(ctx context.Context, query *ReadPipelineDefinitionsCountQuery, opts ...conjoin.CallOption) (*ReadPipelineDefinitionsCountResponse, error) {
	var out ReadPipelineDefinitionsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "relay/pipelines/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PipelinesService) UpdatePipelineDefinition(ctx context.Context, pipelineID string, body *UpdatePipelineDefinitionRequest, opts ...conjoin.CallOption) (*UpdatePipelineDefinitionResponse, error) {
	var out UpdatePipelineDefinitionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "relay/pipelines/{pipeline_id}",
		PathParams:   []string{pipelineID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PipelinesService) DeletePipelineDefinition(ctx context.Context, pipelineID string, opts ...conjoin.CallOption) (*DeletePipelineDefinitionResponse, error) {
	var out DeletePipelineDefinitionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "relay/pipelines/{pipeline_id}",
		PathParams: []string{pipelineID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PipelinesService) TriggerPipelineRun(ctx context.Context, pipelineID string, body *TriggerPipelineRunRequest, opts ...conjoin.CallOption) (*TriggerPipelineRunResponse, error) {
	var out TriggerPipelineRunResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "relay/pipelines/{pipeline_id}/trigger",
		PathParams:   []string{pipelineID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PipelinesService) ReadPipelineRuns(ctx context.Context, query *ReadPipelineRunsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadPipelineRunsItem], error) {
	return conjoin.List[ReadPipelineRunsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "relay/pipeline-runs/",
		Query:  query,
	}, opts...)
}

func (s *PipelinesService) ReadPipelineRunsCount(ctx context.Context, query *ReadPipelineRunsCountQuery, opts ...conjoin.CallOption) (*ReadPipelineRunsCountResponse, error) {
	var out ReadPipelineRunsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "relay/pipeline-runs/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PipelinesService) ReadPipelineRun(ctx context.Context, pipelineRunID string, opts ...conjoin.CallOption) (*ReadPipelineRunResponse, error) {
	var out ReadPipelineRunResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/pipeline-runs/{pipeline_run_id}",
		PathParams: []string{pipelineRunID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PipelinesService) CancelPipelineRun(ctx context.Context, pipelineRunID string, opts ...conjoin.CallOption) (*CancelPipelineRunResponse, error) {
	var out CancelPipelineRunResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "relay/pipeline-runs/{pipeline_run_id}/cancel",
		PathParams: []string{pipelineRunID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PipelinesService) ApprovePipelineGate(ctx context.Context, pipelineRunID string, stepID string, body *ApprovePipelineGateRequest, opts ...conjoin.CallOption) (*ApprovePipelineGateResponse, error) {
	var out ApprovePipelineGateResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "relay/pipeline-runs/{pipeline_run_id}/steps/{step_id}/approve",
		PathParams:   []string{pipelineRunID, stepID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PipelinesService) RejectPipelineGate(ctx context.Context, pipelineRunID string, stepID string, body *RejectPipelineGateRequest, opts ...conjoin.CallOption) (*RejectPipelineGateResponse, error) {
	var out RejectPipelineGateResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "relay/pipeline-runs/{pipeline_run_id}/steps/{step_id}/reject",
		PathParams:   []string{pipelineRunID, stepID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
