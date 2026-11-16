package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type AppsService struct {
	client *conjoin.Client
}

func (s *AppsService) List(ctx context.Context, query *ListAppsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListAppsItem], error) {
	return conjoin.List[ListAppsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "auth/apps/",
		Query:  query,
	}, opts...)
}

func (s *AppsService) Create(ctx context.Context, body *CreateAppRequest, opts ...conjoin.CallOption) (*CreateAppResponse, error) {
	var out CreateAppResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/apps/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AppsService) ListCount(ctx context.Context, query *ListAppsCountQuery, opts ...conjoin.CallOption) (*ListAppsCountResponse, error) {
	var out ListAppsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/apps/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AppsService) Read(ctx context.Context, appID string, opts ...conjoin.CallOption) (*ReadAppResponse, error) {
	var out ReadAppResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/apps/{app_id}",
		PathParams: []string{appID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AppsService) Update(ctx context.Context, appID string, body *UpdateAppRequest, opts ...conjoin.CallOption) (*UpdateAppResponse, error) {
	var out UpdateAppResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/apps/{app_id}",
		PathParams:   []string{appID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AppsService) UpdateSettings(ctx context.Context, appID string, body *UpdateAppSettingsRequest, opts ...conjoin.CallOption) (*UpdateAppSettingsResponse, error) {
	var out UpdateAppSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/apps/{app_id}/settings",
		PathParams:   []string{appID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AppsService) RotateSigningKeys(ctx context.Context, appID string, opts ...conjoin.CallOption) (*RotateAppSigningKeysResponse, error) {
	var out RotateAppSigningKeysResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/apps/{app_id}/signing-keys/rotate",
		PathParams:            []string{appID},
		AcceptsIdempotencyKey: true,
		Response:              conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
