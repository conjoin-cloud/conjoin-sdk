package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ConnectionsService struct {
	client *conjoin.Client
}

func (s *ConnectionsService) ListFirstParty(ctx context.Context, query *ListFirstPartyConnectionsQuery, opts ...conjoin.CallOption) (*ListFirstPartyConnectionsResponse, error) {
	var out ListFirstPartyConnectionsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/connection-configs/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionsService) UpsertFirstParty(ctx context.Context, body *UpsertFirstPartyConnectionRequest, opts ...conjoin.CallOption) (*UpsertFirstPartyConnectionResponse, error) {
	var out UpsertFirstPartyConnectionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/connection-configs/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
