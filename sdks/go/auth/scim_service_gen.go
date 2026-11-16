package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SCIMsService struct {
	client *conjoin.Client
}

func (s *SCIMsService) ScimBulkOperations(ctx context.Context, projectID string, appID string, body *ScimBulkOperationsRequest, opts ...conjoin.CallOption) (*ScimBulkOperationsResponse, error) {
	var out ScimBulkOperationsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/scim/v2/{project_id}/{app_id}/Bulk",
		PathParams:            []string{projectID, appID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
		Auth:                  conjoin.AuthBearerToken,
		Response:              conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimListGroups(ctx context.Context, projectID string, appID string, opts ...conjoin.CallOption) (*ScimListGroupsResponse, error) {
	var out ScimListGroupsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/scim/v2/{project_id}/{app_id}/Groups",
		PathParams: []string{projectID, appID},
		Auth:       conjoin.AuthBearerToken,
		Response:   conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimCreateGroup(ctx context.Context, projectID string, appID string, body *ScimCreateGroupRequest, opts ...conjoin.CallOption) (*ScimCreateGroupResponse, error) {
	var out ScimCreateGroupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/scim/v2/{project_id}/{app_id}/Groups",
		PathParams:            []string{projectID, appID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
		Auth:                  conjoin.AuthBearerToken,
		Response:              conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimGetGroup(ctx context.Context, projectID string, appID string, id string, opts ...conjoin.CallOption) (*ScimGetGroupResponse, error) {
	var out ScimGetGroupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/scim/v2/{project_id}/{app_id}/Groups/{id}",
		PathParams: []string{projectID, appID, id},
		Auth:       conjoin.AuthBearerToken,
		Response:   conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimReplaceGroup(ctx context.Context, projectID string, appID string, id string, body *ScimReplaceGroupRequest, opts ...conjoin.CallOption) (*ScimReplaceGroupResponse, error) {
	var out ScimReplaceGroupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PUT",
		Path:         "auth/scim/v2/{project_id}/{app_id}/Groups/{id}",
		PathParams:   []string{projectID, appID, id},
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthBearerToken,
		Response:     conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimPatchGroupMembers(ctx context.Context, projectID string, appID string, id string, body *ScimPatchGroupMembersRequest, opts ...conjoin.CallOption) (*ScimPatchGroupMembersResponse, error) {
	var out ScimPatchGroupMembersResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/scim/v2/{project_id}/{app_id}/Groups/{id}",
		PathParams:   []string{projectID, appID, id},
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthBearerToken,
		Response:     conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimDeleteGroup(ctx context.Context, projectID string, appID string, id string, opts ...conjoin.CallOption) error {
	return s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/scim/v2/{project_id}/{app_id}/Groups/{id}",
		PathParams: []string{projectID, appID, id},
		Auth:       conjoin.AuthBearerToken,
		Response:   conjoin.ResponseEmpty,
	}, nil, opts...)
}

func (s *SCIMsService) ScimGetServiceProviderConfig(ctx context.Context, opts ...conjoin.CallOption) (*ScimGetServiceProviderConfigResponse, error) {
	var out ScimGetServiceProviderConfigResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:   "GET",
		Path:     "auth/scim/v2/ServiceProviderConfig",
		Auth:     conjoin.AuthNone,
		Response: conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimGetSchemas(ctx context.Context, opts ...conjoin.CallOption) (*ScimGetSchemasResponse, error) {
	var out ScimGetSchemasResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:   "GET",
		Path:     "auth/scim/v2/Schemas",
		Auth:     conjoin.AuthNone,
		Response: conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimGetResourceTypes(ctx context.Context, opts ...conjoin.CallOption) (*ScimGetResourceTypesResponse, error) {
	var out ScimGetResourceTypesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:   "GET",
		Path:     "auth/scim/v2/ResourceTypes",
		Auth:     conjoin.AuthNone,
		Response: conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimListUsers(ctx context.Context, projectID string, appID string, opts ...conjoin.CallOption) (*ScimListUsersResponse, error) {
	var out ScimListUsersResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/scim/v2/{project_id}/{app_id}/Users",
		PathParams: []string{projectID, appID},
		Auth:       conjoin.AuthBearerToken,
		Response:   conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimCreateUser(ctx context.Context, projectID string, appID string, body *ScimCreateUserRequest, opts ...conjoin.CallOption) (*ScimCreateUserResponse, error) {
	var out ScimCreateUserResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/scim/v2/{project_id}/{app_id}/Users",
		PathParams:            []string{projectID, appID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
		Auth:                  conjoin.AuthBearerToken,
		Response:              conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimGetUser(ctx context.Context, projectID string, appID string, id string, opts ...conjoin.CallOption) (*ScimGetUserResponse, error) {
	var out ScimGetUserResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/scim/v2/{project_id}/{app_id}/Users/{id}",
		PathParams: []string{projectID, appID, id},
		Auth:       conjoin.AuthBearerToken,
		Response:   conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimReplaceUser(ctx context.Context, projectID string, appID string, id string, body *ScimReplaceUserRequest, opts ...conjoin.CallOption) (*ScimReplaceUserResponse, error) {
	var out ScimReplaceUserResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PUT",
		Path:         "auth/scim/v2/{project_id}/{app_id}/Users/{id}",
		PathParams:   []string{projectID, appID, id},
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthBearerToken,
		Response:     conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimPatchUser(ctx context.Context, projectID string, appID string, id string, opts ...conjoin.CallOption) (*ScimPatchUserResponse, error) {
	var out ScimPatchUserResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "auth/scim/v2/{project_id}/{app_id}/Users/{id}",
		PathParams: []string{projectID, appID, id},
		Auth:       conjoin.AuthBearerToken,
		Response:   conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMsService) ScimDeactivateUser(ctx context.Context, projectID string, appID string, id string, opts ...conjoin.CallOption) error {
	return s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/scim/v2/{project_id}/{app_id}/Users/{id}",
		PathParams: []string{projectID, appID, id},
		Auth:       conjoin.AuthBearerToken,
		Response:   conjoin.ResponseEmpty,
	}, nil, opts...)
}
