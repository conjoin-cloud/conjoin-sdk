package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SelvesService struct {
	client *conjoin.Client
}

func (s *SelvesService) ListOrganizations(ctx context.Context, query *ListSelfOrganizationsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListSelfOrganizationsItem], error) {
	return conjoin.List[ListSelfOrganizationsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "auth/self/organizations",
		Query:  query,
		Auth:   conjoin.AuthNone,
	}, opts...)
}

func (s *SelvesService) ListSessions(ctx context.Context, query *ListSelfSessionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListSelfSessionsItem], error) {
	return conjoin.List[ListSelfSessionsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "auth/self/sessions",
		Query:  query,
		Auth:   conjoin.AuthNone,
	}, opts...)
}

func (s *SelvesService) ReadProfile(ctx context.Context, opts ...conjoin.CallOption) (*ReadSelfProfileResponse, error) {
	var out ReadSelfProfileResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/self/",
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SelvesService) UpdateProfile(ctx context.Context, body *UpdateSelfProfileRequest, opts ...conjoin.CallOption) (*UpdateSelfProfileResponse, error) {
	var out UpdateSelfProfileResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/self/",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SelvesService) ListSessionsCount(ctx context.Context, query *ListSelfSessionsCountQuery, opts ...conjoin.CallOption) (*ListSelfSessionsCountResponse, error) {
	var out ListSelfSessionsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/self/sessions/count",
		Query:  query,
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SelvesService) RevokeSession(ctx context.Context, sessionID string, opts ...conjoin.CallOption) (*RevokeSelfSessionResponse, error) {
	var out RevokeSelfSessionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/self/sessions/{session_id}",
		PathParams: []string{sessionID},
		Auth:       conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SelvesService) ListOrganizationsCount(ctx context.Context, query *ListSelfOrganizationsCountQuery, opts ...conjoin.CallOption) (*ListSelfOrganizationsCountResponse, error) {
	var out ListSelfOrganizationsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/self/organizations/count",
		Query:  query,
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SelvesService) ReadActiveOrganization(ctx context.Context, opts ...conjoin.CallOption) (*ReadSelfActiveOrganizationResponse, error) {
	var out ReadSelfActiveOrganizationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/self/active-organization",
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SelvesService) UpdateActiveOrganization(ctx context.Context, body *UpdateSelfActiveOrganizationRequest, opts ...conjoin.CallOption) (*UpdateSelfActiveOrganizationResponse, error) {
	var out UpdateSelfActiveOrganizationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/self/active-organization",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
