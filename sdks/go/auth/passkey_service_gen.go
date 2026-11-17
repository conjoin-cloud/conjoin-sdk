package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type PasskeysService struct {
	client *conjoin.Client
}

func (s *PasskeysService) List(ctx context.Context, accountID string, query *ListPasskeysQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListPasskeysItem], error) {
	return conjoin.List[ListPasskeysItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/accounts/{account_id}/passkeys/",
		PathParams: []string{accountID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *PasskeysService) ListCount(ctx context.Context, accountID string, query *ListPasskeysCountQuery, opts ...conjoin.CallOption) (*ListPasskeysCountResponse, error) {
	var out ListPasskeysCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/accounts/{account_id}/passkeys/count",
		PathParams: []string{accountID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PasskeysService) Read(ctx context.Context, accountID string, passkeyID string, opts ...conjoin.CallOption) (*ReadPasskeyResponse, error) {
	var out ReadPasskeyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/accounts/{account_id}/passkeys/{passkey_id}",
		PathParams: []string{accountID, passkeyID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

type DeletePasskeyHeaders struct {
	StepUpSessionID string             `header:"Step-Up-Session-ID"`
	StepUpToken     conjoin.Credential `header:"Step-Up-Token"`
}

func (s *PasskeysService) Delete(ctx context.Context, accountID string, passkeyID string, headers DeletePasskeyHeaders, opts ...conjoin.CallOption) (*DeletePasskeyResponse, error) {
	var out DeletePasskeyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/accounts/{account_id}/passkeys/{passkey_id}",
		PathParams: []string{accountID, passkeyID},
		Headers:    []conjoin.DeclaredHeader{{Name: "Step-Up-Session-ID", Argument: "StepUpSessionID", Value: conjoin.Credential(headers.StepUpSessionID), MinLength: 1, MaxLength: 48}, {Name: "Step-Up-Token", Argument: "StepUpToken", Value: headers.StepUpToken, MinLength: 1, MaxLength: 256, Pattern: "^[0-9a-f]+$"}},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
