package storage

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ObjectACLsService struct {
	client *conjoin.Client
}

func (s *ObjectACLsService) GrantObjectAcl(ctx context.Context, containerNameOrID string, objectNameOrID string, body *GrantObjectAclRequest, opts ...conjoin.CallOption) (*GrantObjectAclResponse, error) {
	var out GrantObjectAclResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "storage/storage-object/{container_name_or_id}/{object_name_or_id}/acl/grant",
		PathParams:            []string{containerNameOrID, objectNameOrID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ObjectACLsService) RevokeObjectAcl(ctx context.Context, containerNameOrID string, objectNameOrID string, body *RevokeObjectAclRequest, opts ...conjoin.CallOption) (*RevokeObjectAclResponse, error) {
	var out RevokeObjectAclResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "storage/storage-object/{container_name_or_id}/{object_name_or_id}/acl/revoke",
		PathParams:            []string{containerNameOrID, objectNameOrID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ObjectACLsService) SetObjectPublic(ctx context.Context, containerNameOrID string, objectNameOrID string, body *SetObjectPublicRequest, opts ...conjoin.CallOption) (*SetObjectPublicResponse, error) {
	var out SetObjectPublicResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "storage/storage-object/{container_name_or_id}/{object_name_or_id}/acl/public",
		PathParams:   []string{containerNameOrID, objectNameOrID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
