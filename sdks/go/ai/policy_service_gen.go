package ai

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type PoliciesService struct {
	client *conjoin.Client
}

func (s *PoliciesService) CreateCheck(ctx context.Context, body *CreatePolicyCheckRequest, opts ...conjoin.CallOption) (*CreatePolicyCheckResponse, error) {
	var out CreatePolicyCheckResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/policy-checks/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PoliciesService) ListLogs(ctx context.Context, query *ListPolicyLogsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListPolicyLogsItem], error) {
	return conjoin.List[ListPolicyLogsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "ai/policy-logs/",
		Query:  query,
	}, opts...)
}

func (s *PoliciesService) ListLogsCount(ctx context.Context, query *ListPolicyLogsCountQuery, opts ...conjoin.CallOption) (*ListPolicyLogsCountResponse, error) {
	var out ListPolicyLogsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "ai/policy-logs/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PoliciesService) ListRules(ctx context.Context, query *ListPolicyRulesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListPolicyRulesItem], error) {
	return conjoin.List[ListPolicyRulesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "ai/policy-rules/",
		Query:  query,
	}, opts...)
}

func (s *PoliciesService) CreateRule(ctx context.Context, body *CreatePolicyRuleRequest, opts ...conjoin.CallOption) (*CreatePolicyRuleResponse, error) {
	var out CreatePolicyRuleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/policy-rules/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PoliciesService) ListRulesCount(ctx context.Context, query *ListPolicyRulesCountQuery, opts ...conjoin.CallOption) (*ListPolicyRulesCountResponse, error) {
	var out ListPolicyRulesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "ai/policy-rules/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PoliciesService) ReadRule(ctx context.Context, policyRuleID string, opts ...conjoin.CallOption) (*ReadPolicyRuleResponse, error) {
	var out ReadPolicyRuleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "ai/policy-rules/{policy_rule_id}",
		PathParams: []string{policyRuleID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PoliciesService) UpdateRule(ctx context.Context, policyRuleID string, body *UpdatePolicyRuleRequest, opts ...conjoin.CallOption) (*UpdatePolicyRuleResponse, error) {
	var out UpdatePolicyRuleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "ai/policy-rules/{policy_rule_id}",
		PathParams:   []string{policyRuleID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PoliciesService) DeleteRule(ctx context.Context, policyRuleID string, opts ...conjoin.CallOption) (*DeletePolicyRuleResponse, error) {
	var out DeletePolicyRuleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "ai/policy-rules/{policy_rule_id}",
		PathParams: []string{policyRuleID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
