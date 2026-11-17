package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ProjectsService struct {
	client *conjoin.Client
}

func (s *ProjectsService) List(ctx context.Context, organizationID string, query *ReadProjectsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadProjectsItem], error) {
	return conjoin.List[ReadProjectsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "cloud/organizations/{organization_id}/projects/",
		PathParams: []string{organizationID},
		Query:      query,
	}, opts...)
}

func (s *ProjectsService) Create(ctx context.Context, organizationID string, body *CreateProjectRequest, opts ...conjoin.CallOption) (*CreateProjectResponse, error) {
	var out CreateProjectResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "cloud/organizations/{organization_id}/projects/",
		PathParams:            []string{organizationID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProjectsService) ReadCount(ctx context.Context, organizationID string, query *ReadProjectsCountQuery, opts ...conjoin.CallOption) (*ReadProjectsCountResponse, error) {
	var out ReadProjectsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "cloud/organizations/{organization_id}/projects/count",
		PathParams: []string{organizationID},
		Query:      query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProjectsService) Read(ctx context.Context, projectID string, opts ...conjoin.CallOption) (*ReadProjectResponse, error) {
	var out ReadProjectResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "cloud/projects/{project_id}",
		PathParams: []string{projectID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProjectsService) Update(ctx context.Context, projectID string, body *UpdateProjectRequest, opts ...conjoin.CallOption) (*UpdateProjectResponse, error) {
	var out UpdateProjectResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "cloud/projects/{project_id}",
		PathParams:   []string{projectID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
