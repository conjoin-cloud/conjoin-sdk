package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ProfilesService struct {
	client *conjoin.Client
}

func (s *ProfilesService) List(ctx context.Context, query *ListProfilesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListProfilesItem], error) {
	return conjoin.List[ListProfilesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/profiles/",
		Query:  query,
	}, opts...)
}

func (s *ProfilesService) Create(ctx context.Context, body *CreateProfileRequest, opts ...conjoin.CallOption) (*CreateProfileResponse, error) {
	var out CreateProfileResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/profiles/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) ListCount(ctx context.Context, query *ListProfilesCountQuery, opts ...conjoin.CallOption) (*ListProfilesCountResponse, error) {
	var out ListProfilesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/profiles/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) Enable(ctx context.Context, profileID string, opts ...conjoin.CallOption) (*EnableProfileResponse, error) {
	var out EnableProfileResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/profiles/{profile_id}/enable",
		PathParams:            []string{profileID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) Disable(ctx context.Context, profileID string, opts ...conjoin.CallOption) (*DisableProfileResponse, error) {
	var out DisableProfileResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/profiles/{profile_id}/disable",
		PathParams:            []string{profileID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) EnableChannels(ctx context.Context, profileID string, body *EnableProfileChannelsRequest, opts ...conjoin.CallOption) (*EnableProfileChannelsResponse, error) {
	var out EnableProfileChannelsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/profiles/{profile_id}/enable-channels",
		PathParams:            []string{profileID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) DisableChannels(ctx context.Context, profileID string, body *DisableProfileChannelsRequest, opts ...conjoin.CallOption) (*DisableProfileChannelsResponse, error) {
	var out DisableProfileChannelsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/profiles/{profile_id}/disable-channels",
		PathParams:            []string{profileID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) Close(ctx context.Context, profileID string, opts ...conjoin.CallOption) (*CloseProfileResponse, error) {
	var out CloseProfileResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/profiles/{profile_id}/close",
		PathParams:            []string{profileID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) Update(ctx context.Context, profileID string, body *UpdateProfileRequest, opts ...conjoin.CallOption) (*UpdateProfileResponse, error) {
	var out UpdateProfileResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/profiles/{profile_id}",
		PathParams:   []string{profileID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) Read(ctx context.Context, profileID string, opts ...conjoin.CallOption) (*ReadProfileResponse, error) {
	var out ReadProfileResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/profiles/{profile_id}",
		PathParams: []string{profileID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) Delete(ctx context.Context, profileID string, opts ...conjoin.CallOption) (*DeleteProfileResponse, error) {
	var out DeleteProfileResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/profiles/{profile_id}",
		PathParams: []string{profileID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
