package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type EntitiesService struct {
	client *conjoin.Client
}

func (s *EntitiesService) List(ctx context.Context, query *ListEntitiesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListEntitiesItem], error) {
	return conjoin.List[ListEntitiesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/entities/",
		Query:  query,
	}, opts...)
}

func (s *EntitiesService) Create(ctx context.Context, body *CreateEntityRequest, opts ...conjoin.CallOption) (*CreateEntityResponse, error) {
	var out CreateEntityResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/entities/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitiesService) ListCount(ctx context.Context, query *ListEntitiesCountQuery, opts ...conjoin.CallOption) (*ListEntitiesCountResponse, error) {
	var out ListEntitiesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/entities/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitiesService) Onboard(ctx context.Context, body *OnboardEntitiesRequest, opts ...conjoin.CallOption) (*OnboardEntitiesResponse, error) {
	var out OnboardEntitiesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/entities/onboard",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
		Response:              conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitiesService) Read(ctx context.Context, entityID string, query *ReadEntityQuery, opts ...conjoin.CallOption) (*ReadEntityResponse, error) {
	var out ReadEntityResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/entities/{entity_id}",
		PathParams: []string{entityID},
		Query:      query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitiesService) Update(ctx context.Context, entityID string, body *UpdateEntityRequest, opts ...conjoin.CallOption) (*UpdateEntityResponse, error) {
	var out UpdateEntityResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "billing/entities/{entity_id}",
		PathParams:   []string{entityID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitiesService) CreatePayoutBankAccount(ctx context.Context, entityID string, body *CreatePayoutBankAccountRequest, opts ...conjoin.CallOption) (*CreatePayoutBankAccountResponse, error) {
	var out CreatePayoutBankAccountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/entities/{entity_id}/payout-bank-accounts",
		PathParams:            []string{entityID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitiesService) CreateAccountLink(ctx context.Context, entityID string, body *CreateEntityAccountLinkRequest, opts ...conjoin.CallOption) (*CreateEntityAccountLinkResponse, error) {
	var out CreateEntityAccountLinkResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/entities/{entity_id}/account-links",
		PathParams:            []string{entityID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
		Response:              conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitiesService) SyncOnboarding(ctx context.Context, entityID string, opts ...conjoin.CallOption) (*SyncEntityOnboardingResponse, error) {
	var out SyncEntityOnboardingResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/entities/{entity_id}/sync",
		PathParams:            []string{entityID},
		AcceptsIdempotencyKey: true,
		Response:              conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitiesService) CreatePaystackCredentials(ctx context.Context, entityID string, body *CreateEntityPaystackCredentialsRequest, opts ...conjoin.CallOption) (*CreateEntityPaystackCredentialsResponse, error) {
	var out CreateEntityPaystackCredentialsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/entities/{entity_id}/paystack-credentials",
		PathParams:            []string{entityID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
		Response:              conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
