package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type OrganizationDomainsService struct {
	client *conjoin.Client
}

func (s *OrganizationDomainsService) VerifySsoPortalDomain(ctx context.Context, body *VerifySsoPortalDomainRequest, opts ...conjoin.CallOption) (*VerifySsoPortalDomainResponse, error) {
	var out VerifySsoPortalDomainResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/portal/domains",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
