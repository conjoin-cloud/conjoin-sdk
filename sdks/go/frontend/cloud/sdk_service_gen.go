package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SDKsService struct {
	client *conjoin.Client
}

func (s *SDKsService) ReadSdkSettings(ctx context.Context, opts ...conjoin.CallOption) (*ReadSdkSettingsResponse, error) {
	var out ReadSdkSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/client/settings/",
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
