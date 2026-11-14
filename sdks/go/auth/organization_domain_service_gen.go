package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type OrganizationDomainsService struct {
	client *conjoin.Client
}

func (s *OrganizationDomainsService) List(ctx context.Context, organizationID string, query *ListOrganizationDomainsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListOrganizationDomainsItem], error) {
	return conjoin.List[ListOrganizationDomainsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/domains/",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *OrganizationDomainsService) Create(ctx context.Context, organizationID string, body *CreateOrganizationDomainRequest, opts ...conjoin.CallOption) (*CreateOrganizationDomainResponse, error) {
	var out CreateOrganizationDomainResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/organizations/{organization_id}/domains/",
		PathParams:   []string{organizationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationDomainsService) ListCount(ctx context.Context, organizationID string, query *ListOrganizationDomainsCountQuery, opts ...conjoin.CallOption) (*ListOrganizationDomainsCountResponse, error) {
	var out ListOrganizationDomainsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/domains/count",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationDomainsService) Verify(ctx context.Context, organizationID string, domainID string, opts ...conjoin.CallOption) (*VerifyOrganizationDomainResponse, error) {
	var out VerifyOrganizationDomainResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/organizations/{organization_id}/domains/{domain_id}/verify",
		PathParams: []string{organizationID, domainID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationDomainsService) Delete(ctx context.Context, organizationID string, domainID string, opts ...conjoin.CallOption) (*DeleteOrganizationDomainResponse, error) {
	var out DeleteOrganizationDomainResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/organizations/{organization_id}/domains/{domain_id}",
		PathParams: []string{organizationID, domainID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
