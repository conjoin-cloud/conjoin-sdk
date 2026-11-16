package storage

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ContainersService struct {
	client *conjoin.Client
}

func (s *ContainersService) Create(ctx context.Context, body *CreateContainerRequest, opts ...conjoin.CallOption) (*CreateContainerResponse, error) {
	var out CreateContainerResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "storage/storage-container/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContainersService) List(ctx context.Context, query *ListContainersQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListContainersItem], error) {
	return conjoin.List[ListContainersItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "storage/storage-container/",
		Query:  query,
	}, opts...)
}

func (s *ContainersService) Read(ctx context.Context, containerNameOrID string, opts ...conjoin.CallOption) (*ReadContainerResponse, error) {
	var out ReadContainerResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "storage/storage-container/{container_name_or_id}",
		PathParams: []string{containerNameOrID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContainersService) RequestDeletion(ctx context.Context, containerNameOrID string, query *RequestContainerDeletionQuery, opts ...conjoin.CallOption) (*RequestContainerDeletionResponse, error) {
	var out RequestContainerDeletionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "storage/storage-container/{container_name_or_id}",
		PathParams: []string{containerNameOrID},
		Query:      query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContainersService) Archive(ctx context.Context, containerNameOrID string, opts ...conjoin.CallOption) (*ArchiveContainerResponse, error) {
	var out ArchiveContainerResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "storage/storage-container/archive/{container_name_or_id}",
		PathParams: []string{containerNameOrID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContainersService) Restore(ctx context.Context, containerNameOrID string, opts ...conjoin.CallOption) (*RestoreContainerResponse, error) {
	var out RestoreContainerResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "storage/storage-container/restore/{container_name_or_id}",
		PathParams: []string{containerNameOrID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContainersService) UpdateLifecyclePolicy(ctx context.Context, containerNameOrID string, body *UpdateContainerLifecyclePolicyRequest, opts ...conjoin.CallOption) (*UpdateContainerLifecyclePolicyResponse, error) {
	var out UpdateContainerLifecyclePolicyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "storage/storage-container/lifecycle-policy/{container_name_or_id}",
		PathParams:   []string{containerNameOrID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContainersService) UpdateSettings(ctx context.Context, containerNameOrID string, body *UpdateContainerSettingsRequest, opts ...conjoin.CallOption) (*UpdateContainerSettingsResponse, error) {
	var out UpdateContainerSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "storage/storage-container/settings/{container_name_or_id}",
		PathParams:   []string{containerNameOrID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContainersService) CancelDeletion(ctx context.Context, containerNameOrID string, opts ...conjoin.CallOption) (*CancelContainerDeletionResponse, error) {
	var out CancelContainerDeletionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "storage/storage-container/cancel-deletion/{container_name_or_id}",
		PathParams: []string{containerNameOrID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContainersService) ChangeClass(ctx context.Context, containerNameOrID string, body *ChangeContainerClassRequest, opts ...conjoin.CallOption) (*ChangeContainerClassResponse, error) {
	var out ChangeContainerClassResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "storage/storage-container/storage-class/{container_name_or_id}",
		PathParams:   []string{containerNameOrID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContainersService) UpdateTransitionPolicy(ctx context.Context, containerNameOrID string, body *UpdateContainerTransitionPolicyRequest, opts ...conjoin.CallOption) (*UpdateContainerTransitionPolicyResponse, error) {
	var out UpdateContainerTransitionPolicyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "storage/storage-container/transition-policy/{container_name_or_id}",
		PathParams:   []string{containerNameOrID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
