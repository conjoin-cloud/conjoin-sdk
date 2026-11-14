package relay

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SettingsService struct {
	client *conjoin.Client
}

func (s *SettingsService) Get(ctx context.Context, opts ...conjoin.CallOption) (*GetSettingsResponse, error) {
	var out GetSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "relay/settings/",
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SettingsService) Update(ctx context.Context, body *UpdateSettingsRequest, opts ...conjoin.CallOption) (*UpdateSettingsResponse, error) {
	var out UpdateSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "relay/settings/",
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SettingsService) RotateSigningSecret(ctx context.Context, opts ...conjoin.CallOption) (*RotateSigningSecretResponse, error) {
	var out RotateSigningSecretResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "POST",
		Path:   "relay/settings/signing-secret/rotate",
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SettingsService) RevealSigningSecret(ctx context.Context, opts ...conjoin.CallOption) (*RevealSigningSecretResponse, error) {
	var out RevealSigningSecretResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "relay/settings/signing-secret",
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
