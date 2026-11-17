package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SettingsService struct {
	client *conjoin.Client
}

func (s *SettingsService) Read(ctx context.Context, opts ...conjoin.CallOption) (*ReadSettingsResponse, error) {
	var out ReadSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/settings/",
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SettingsService) Update(ctx context.Context, body *UpdateSettingsRequest, opts ...conjoin.CallOption) (*UpdateSettingsResponse, error) {
	var out UpdateSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "billing/settings/",
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
