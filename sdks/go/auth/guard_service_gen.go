package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type GuardsService struct {
	client *conjoin.Client
}

func (s *GuardsService) ListRules(ctx context.Context, query *ListGuardRulesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListGuardRulesItem], error) {
	return conjoin.List[ListGuardRulesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "auth/guard-rules",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *GuardsService) CreateRule(ctx context.Context, body *CreateGuardRuleRequest, opts ...conjoin.CallOption) (*CreateGuardRuleResponse, error) {
	var out CreateGuardRuleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/guard-rules",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) ListRulesCount(ctx context.Context, query *ListGuardRulesCountQuery, opts ...conjoin.CallOption) (*ListGuardRulesCountResponse, error) {
	var out ListGuardRulesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/guard-rules/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) ReadRule(ctx context.Context, guardRuleID string, opts ...conjoin.CallOption) (*ReadGuardRuleResponse, error) {
	var out ReadGuardRuleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/guard-rules/{guard_rule_id}",
		PathParams: []string{guardRuleID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) UpdateRule(ctx context.Context, guardRuleID string, body *UpdateGuardRuleRequest, opts ...conjoin.CallOption) (*UpdateGuardRuleResponse, error) {
	var out UpdateGuardRuleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/guard-rules/{guard_rule_id}",
		PathParams:   []string{guardRuleID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) DeleteRule(ctx context.Context, guardRuleID string, opts ...conjoin.CallOption) (*DeleteGuardRuleResponse, error) {
	var out DeleteGuardRuleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/guard-rules/{guard_rule_id}",
		PathParams: []string{guardRuleID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) ListEvents(ctx context.Context, query *ListGuardEventsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListGuardEventsItem], error) {
	return conjoin.List[ListGuardEventsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "auth/guard-events",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *GuardsService) ListEventsCount(ctx context.Context, query *ListGuardEventsCountQuery, opts ...conjoin.CallOption) (*ListGuardEventsCountResponse, error) {
	var out ListGuardEventsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/guard-events/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) AddTrustedIp(ctx context.Context, body *AddGuardTrustedIpRequest, opts ...conjoin.CallOption) (*AddGuardTrustedIpResponse, error) {
	var out AddGuardTrustedIpResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/guard-trusted-ips",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) RemoveTrustedIp(ctx context.Context, body *RemoveGuardTrustedIpRequest, opts ...conjoin.CallOption) (*RemoveGuardTrustedIpResponse, error) {
	var out RemoveGuardTrustedIpResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/guard-trusted-ips/remove",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) AddTrustedEmail(ctx context.Context, body *AddGuardTrustedEmailRequest, opts ...conjoin.CallOption) (*AddGuardTrustedEmailResponse, error) {
	var out AddGuardTrustedEmailResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/guard-trusted-emails",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) RemoveTrustedEmail(ctx context.Context, body *RemoveGuardTrustedEmailRequest, opts ...conjoin.CallOption) (*RemoveGuardTrustedEmailResponse, error) {
	var out RemoveGuardTrustedEmailResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/guard-trusted-emails/remove",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) AddTrustedDomain(ctx context.Context, body *AddGuardTrustedDomainRequest, opts ...conjoin.CallOption) (*AddGuardTrustedDomainResponse, error) {
	var out AddGuardTrustedDomainResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/guard-trusted-domains",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) RemoveTrustedDomain(ctx context.Context, body *RemoveGuardTrustedDomainRequest, opts ...conjoin.CallOption) (*RemoveGuardTrustedDomainResponse, error) {
	var out RemoveGuardTrustedDomainResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/guard-trusted-domains/remove",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) ListAnonymousIps(ctx context.Context, opts ...conjoin.CallOption) (*ListGuardAnonymousIpsResponse, error) {
	var out ListGuardAnonymousIpsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/guard-anonymous-ips",
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) AddAnonymousIps(ctx context.Context, body *AddGuardAnonymousIpsRequest, opts ...conjoin.CallOption) (*AddGuardAnonymousIpsResponse, error) {
	var out AddGuardAnonymousIpsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/guard-anonymous-ips",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *GuardsService) RemoveAnonymousIps(ctx context.Context, body *RemoveGuardAnonymousIpsRequest, opts ...conjoin.CallOption) (*RemoveGuardAnonymousIpsResponse, error) {
	var out RemoveGuardAnonymousIpsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/guard-anonymous-ips/remove",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
