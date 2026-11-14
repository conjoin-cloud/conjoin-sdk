package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type RolesService struct {
	client *conjoin.Client
}

func (s *RolesService) Read(ctx context.Context, query *ReadRolesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadRolesItem], error) {
	return conjoin.List[ReadRolesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/roles/",
		Query:  query,
	}, opts...)
}

func (s *RolesService) Create(ctx context.Context, body *CreateRoleRequest, opts ...conjoin.CallOption) (*CreateRoleResponse, error) {
	var out CreateRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "cloud/roles/",
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *RolesService) ReadCount(ctx context.Context, query *ReadRolesCountQuery, opts ...conjoin.CallOption) (*ReadRolesCountResponse, error) {
	var out ReadRolesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/roles/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *RolesService) Update(ctx context.Context, roleID string, body *UpdateRoleRequest, opts ...conjoin.CallOption) (*UpdateRoleResponse, error) {
	var out UpdateRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "cloud/roles/{role_id}",
		PathParams:   []string{roleID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
