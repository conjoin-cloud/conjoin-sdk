package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SessionsService struct {
	client *conjoin.Client
}

func (s *SessionsService) List(ctx context.Context, query *ListSessionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListSessionsItem], error) {
	return conjoin.List[ListSessionsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "auth/sessions",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *SessionsService) ListCount(ctx context.Context, query *ListSessionsCountQuery, opts ...conjoin.CallOption) (*ListSessionsCountResponse, error) {
	var out ListSessionsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/sessions/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SessionsService) ReadStats(ctx context.Context, query *ReadSessionStatsQuery, opts ...conjoin.CallOption) (*ReadSessionStatsResponse, error) {
	var out ReadSessionStatsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/sessions/stats",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SessionsService) GetAnalytics(ctx context.Context, query *GetSessionAnalyticsQuery, opts ...conjoin.CallOption) (*GetSessionAnalyticsResponse, error) {
	var out GetSessionAnalyticsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:        "GET",
		Path:          "auth/sessions/analytics",
		Query:         query,
		QueryRequired: true,
		Scopes:        []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SessionsService) Read(ctx context.Context, sessionID string, opts ...conjoin.CallOption) (*ReadSessionResponse, error) {
	var out ReadSessionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/sessions/{session_id}",
		PathParams: []string{sessionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SessionsService) Update(ctx context.Context, sessionID string, body *UpdateSessionRequest, opts ...conjoin.CallOption) (*UpdateSessionResponse, error) {
	var out UpdateSessionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/sessions/{session_id}",
		PathParams:   []string{sessionID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SessionsService) Validate(ctx context.Context, sessionID string, body *ValidateSessionRequest, opts ...conjoin.CallOption) (*ValidateSessionResponse, error) {
	var out ValidateSessionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/sessions/{session_id}/validate",
		PathParams:   []string{sessionID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SessionsService) Revoke(ctx context.Context, sessionID string, opts ...conjoin.CallOption) (*RevokeSessionResponse, error) {
	var out RevokeSessionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/sessions/{session_id}/revoke",
		PathParams: []string{sessionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SessionsService) RevokeAllForAccount(ctx context.Context, accountID string, opts ...conjoin.CallOption) (*RevokeAllSessionsForAccountResponse, error) {
	var out RevokeAllSessionsForAccountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/accounts/{account_id}/sessions/revoke-all",
		PathParams: []string{accountID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SessionsService) BulkRevokeAccount(ctx context.Context, accountID string, body *BulkRevokeAccountSessionsRequest, opts ...conjoin.CallOption) (*BulkRevokeAccountSessionsResponse, error) {
	var out BulkRevokeAccountSessionsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/sessions/revoke",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SessionsService) BulkRevokeClient(ctx context.Context, clientID string, body *BulkRevokeClientSessionsRequest, opts ...conjoin.CallOption) (*BulkRevokeClientSessionsResponse, error) {
	var out BulkRevokeClientSessionsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/clients/{client_id}/sessions/revoke",
		PathParams:   []string{clientID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
