package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type PoliciesService struct {
	client *conjoin.Client
}

func (s *PoliciesService) List(ctx context.Context, organizationID string, query *ListPoliciesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListPoliciesItem], error) {
	return conjoin.List[ListPoliciesItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/policies/",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *PoliciesService) Create(ctx context.Context, organizationID string, body *CreatePolicyRequest, opts ...conjoin.CallOption) (*CreatePolicyResponse, error) {
	var out CreatePolicyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/organizations/{organization_id}/policies/",
		PathParams:   []string{organizationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PoliciesService) ListCount(ctx context.Context, organizationID string, query *ListPoliciesCountQuery, opts ...conjoin.CallOption) (*ListPoliciesCountResponse, error) {
	var out ListPoliciesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/policies/count",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PoliciesService) Read(ctx context.Context, organizationID string, policyID string, opts ...conjoin.CallOption) (*ReadPolicyResponse, error) {
	var out ReadPolicyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/policies/{policy_id}",
		PathParams: []string{organizationID, policyID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PoliciesService) Update(ctx context.Context, organizationID string, policyID string, body *UpdatePolicyRequest, opts ...conjoin.CallOption) (*UpdatePolicyResponse, error) {
	var out UpdatePolicyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/organizations/{organization_id}/policies/{policy_id}",
		PathParams:   []string{organizationID, policyID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PoliciesService) Delete(ctx context.Context, organizationID string, policyID string, opts ...conjoin.CallOption) (*DeletePolicyResponse, error) {
	var out DeletePolicyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/organizations/{organization_id}/policies/{policy_id}",
		PathParams: []string{organizationID, policyID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
