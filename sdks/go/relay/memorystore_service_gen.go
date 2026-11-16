package relay

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type MemorystoresService struct {
	client *conjoin.Client
}

func (s *MemorystoresService) ReadClusters(ctx context.Context, query *ReadMemorystoreClustersQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadMemorystoreClustersItem], error) {
	return conjoin.List[ReadMemorystoreClustersItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "relay/memorystore-clusters/",
		Query:  query,
	}, opts...)
}

func (s *MemorystoresService) CreateCluster(ctx context.Context, body *CreateMemorystoreClusterRequest, opts ...conjoin.CallOption) (*CreateMemorystoreClusterResponse, error) {
	var out CreateMemorystoreClusterResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/memorystore-clusters/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *MemorystoresService) ReadClustersCount(ctx context.Context, query *ReadMemorystoreClustersCountQuery, opts ...conjoin.CallOption) (*ReadMemorystoreClustersCountResponse, error) {
	var out ReadMemorystoreClustersCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "relay/memorystore-clusters/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *MemorystoresService) ReadCluster(ctx context.Context, memorystoreClusterID string, opts ...conjoin.CallOption) (*ReadMemorystoreClusterResponse, error) {
	var out ReadMemorystoreClusterResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/memorystore-clusters/{memorystore_cluster_id}",
		PathParams: []string{memorystoreClusterID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *MemorystoresService) UpdateCluster(ctx context.Context, memorystoreClusterID string, body *UpdateMemorystoreClusterRequest, opts ...conjoin.CallOption) (*UpdateMemorystoreClusterResponse, error) {
	var out UpdateMemorystoreClusterResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "relay/memorystore-clusters/{memorystore_cluster_id}",
		PathParams:   []string{memorystoreClusterID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *MemorystoresService) DeleteCluster(ctx context.Context, memorystoreClusterID string, opts ...conjoin.CallOption) (*DeleteMemorystoreClusterResponse, error) {
	var out DeleteMemorystoreClusterResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "relay/memorystore-clusters/{memorystore_cluster_id}",
		PathParams: []string{memorystoreClusterID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *MemorystoresService) SuspendCluster(ctx context.Context, memorystoreClusterID string, opts ...conjoin.CallOption) (*SuspendMemorystoreClusterResponse, error) {
	var out SuspendMemorystoreClusterResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/memorystore-clusters/{memorystore_cluster_id}/suspend",
		PathParams:            []string{memorystoreClusterID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *MemorystoresService) ExecuteCommand(ctx context.Context, memorystoreClusterID string, body *ExecuteMemorystoreCommandRequest, opts ...conjoin.CallOption) (*ExecuteMemorystoreCommandResponse, error) {
	var out ExecuteMemorystoreCommandResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/memorystore-clusters/{memorystore_cluster_id}/execute",
		PathParams:            []string{memorystoreClusterID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
