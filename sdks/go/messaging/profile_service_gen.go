package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ProfilesService struct {
	client *conjoin.Client
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

func (s *ProfilesService) Enable(ctx context.Context, profileID string, opts ...conjoin.CallOption) (*EnableProfileResponse, error) {
	var out EnableProfileResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/profiles/{profile_id}/enable",
		PathParams: []string{profileID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) Disable(ctx context.Context, profileID string, opts ...conjoin.CallOption) (*DisableProfileResponse, error) {
	var out DisableProfileResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/profiles/{profile_id}/disable",
		PathParams: []string{profileID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) Close(ctx context.Context, profileID string, opts ...conjoin.CallOption) (*CloseProfileResponse, error) {
	var out CloseProfileResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/profiles/{profile_id}/close",
		PathParams: []string{profileID},
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

func (s *ProfilesService) UpdateEmailConfig(ctx context.Context, profileID string, body *UpdateProfileEmailConfigRequest, opts ...conjoin.CallOption) (*UpdateProfileEmailConfigResponse, error) {
	var out UpdateProfileEmailConfigResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/profiles/{profile_id}/emails-config",
		PathParams:   []string{profileID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) UpdateMultisendConfig(ctx context.Context, profileID string, body *UpdateProfileMultisendConfigRequest, opts ...conjoin.CallOption) (*UpdateProfileMultisendConfigResponse, error) {
	var out UpdateProfileMultisendConfigResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/profiles/{profile_id}/multisend-config",
		PathParams:   []string{profileID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) UpdateVerificationsConfig(ctx context.Context, profileID string, body *UpdateProfileVerificationsConfigRequest, opts ...conjoin.CallOption) (*UpdateProfileVerificationsConfigResponse, error) {
	var out UpdateProfileVerificationsConfigResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/profiles/{profile_id}/verifications-config",
		PathParams:   []string{profileID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProfilesService) List(ctx context.Context, body *ListProfilesRequest, opts ...conjoin.CallOption) (*conjoin.Page[ListProfilesItem], error) {
	return conjoin.List[ListProfilesItem](ctx, s.client, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/profiles/retrieve",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
		Cursor:                conjoin.CursorInBody,
	}, opts...)
}
