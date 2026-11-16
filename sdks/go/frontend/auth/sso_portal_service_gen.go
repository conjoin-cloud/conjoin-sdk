package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SSOPortalsService struct {
	client *conjoin.Client
}

type ReadSsoPortalContextHeaders struct {
	PortalTicket conjoin.Credential `header:"x-portal-ticket"`
}

func (s *SSOPortalsService) ReadSsoPortalContext(ctx context.Context, headers ReadSsoPortalContextHeaders, opts ...conjoin.CallOption) (*ReadSsoPortalContextResponse, error) {
	var out ReadSsoPortalContextResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:  "GET",
		Path:    "auth/portal/",
		Headers: []conjoin.DeclaredHeader{{Name: "x-portal-ticket", Argument: "PortalTicket", Value: headers.PortalTicket, Required: true}},
		Auth:    conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

type ReadSsoPortalCatalogHeaders struct {
	PortalTicket conjoin.Credential `header:"x-portal-ticket"`
}

func (s *SSOPortalsService) ReadSsoPortalCatalog(ctx context.Context, headers ReadSsoPortalCatalogHeaders, opts ...conjoin.CallOption) (*ReadSsoPortalCatalogResponse, error) {
	var out ReadSsoPortalCatalogResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:  "GET",
		Path:    "auth/portal/providers",
		Headers: []conjoin.DeclaredHeader{{Name: "x-portal-ticket", Argument: "PortalTicket", Value: headers.PortalTicket, Required: true}},
		Auth:    conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

type StartSsoPortalTestHeaders struct {
	PortalTicket conjoin.Credential `header:"x-portal-ticket"`
}

func (s *SSOPortalsService) StartSsoPortalTest(ctx context.Context, body *StartSsoPortalTestRequest, headers StartSsoPortalTestHeaders, opts ...conjoin.CallOption) (*StartSsoPortalTestResponse, error) {
	var out StartSsoPortalTestResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/portal/test/start",
		Body:         body,
		BodyRequired: true,
		Headers:      []conjoin.DeclaredHeader{{Name: "x-portal-ticket", Argument: "PortalTicket", Value: headers.PortalTicket, Required: true}},
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
