package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ClientsService struct {
	client *conjoin.Client
}

func (s *ClientsService) List(ctx context.Context, query *ListClientsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListClientsItem], error) {
	return conjoin.List[ListClientsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "auth/clients/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *ClientsService) Create(ctx context.Context, body *CreateClientRequest, opts ...conjoin.CallOption) (*CreateClientResponse, error) {
	var out CreateClientResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/clients/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ClientsService) ListCount(ctx context.Context, query *ListClientsCountQuery, opts ...conjoin.CallOption) (*ListClientsCountResponse, error) {
	var out ListClientsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/clients/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ClientsService) Read(ctx context.Context, clientID string, opts ...conjoin.CallOption) (*ReadClientResponse, error) {
	var out ReadClientResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/clients/{client_id}",
		PathParams: []string{clientID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
