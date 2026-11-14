package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SSOPortalsService struct {
	client *conjoin.Client
}

func (s *SSOPortalsService) ReadSsoPortalContext(ctx context.Context, opts ...conjoin.CallOption) (*ReadSsoPortalContextResponse, error) {
	var out ReadSsoPortalContextResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/portal/",
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SSOPortalsService) ReadSsoPortalCatalog(ctx context.Context, opts ...conjoin.CallOption) (*ReadSsoPortalCatalogResponse, error) {
	var out ReadSsoPortalCatalogResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/portal/providers",
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SSOPortalsService) StartSsoPortalTest(ctx context.Context, body *StartSsoPortalTestRequest, opts ...conjoin.CallOption) (*StartSsoPortalTestResponse, error) {
	var out StartSsoPortalTestResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/portal/test/start",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
