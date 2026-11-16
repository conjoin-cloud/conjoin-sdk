package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type OrganizationDomainsService struct {
	client *conjoin.Client
}

type VerifySsoPortalDomainHeaders struct {
	PortalTicket conjoin.Credential `header:"x-portal-ticket"`
}

func (s *OrganizationDomainsService) VerifySsoPortalDomain(ctx context.Context, body *VerifySsoPortalDomainRequest, headers VerifySsoPortalDomainHeaders, opts ...conjoin.CallOption) (*VerifySsoPortalDomainResponse, error) {
	var out VerifySsoPortalDomainResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/portal/domains",
		Body:         body,
		BodyRequired: true,
		Headers:      []conjoin.DeclaredHeader{{Name: "x-portal-ticket", Argument: "PortalTicket", Value: headers.PortalTicket, Required: true}},
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
