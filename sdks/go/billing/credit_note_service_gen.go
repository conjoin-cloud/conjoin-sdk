package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type CreditNotesService struct {
	client *conjoin.Client
}

func (s *CreditNotesService) List(ctx context.Context, query *ListCreditNotesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListCreditNotesItem], error) {
	return conjoin.List[ListCreditNotesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/credit-notes/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *CreditNotesService) Create(ctx context.Context, body *CreateCreditNoteRequest, opts ...conjoin.CallOption) (*CreateCreditNoteResponse, error) {
	var out CreateCreditNoteResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/credit-notes/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CreditNotesService) ListCustomerCreditBalances(ctx context.Context, customerID string, query *ListCustomerCreditBalancesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListCustomerCreditBalancesItem], error) {
	return conjoin.List[ListCustomerCreditBalancesItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/customers/{customer_id}/credit-balances",
		PathParams: []string{customerID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *CreditNotesService) ListCount(ctx context.Context, query *ListCreditNotesCountQuery, opts ...conjoin.CallOption) (*ListCreditNotesCountResponse, error) {
	var out ListCreditNotesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/credit-notes/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CreditNotesService) Void(ctx context.Context, creditNoteID string, opts ...conjoin.CallOption) (*VoidCreditNoteResponse, error) {
	var out VoidCreditNoteResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/credit-notes/{credit_note_id}/void",
		PathParams:            []string{creditNoteID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CreditNotesService) ListCustomerCreditBalancesCount(ctx context.Context, customerID string, query *ListCustomerCreditBalancesCountQuery, opts ...conjoin.CallOption) (*ListCustomerCreditBalancesCountResponse, error) {
	var out ListCustomerCreditBalancesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/customers/{customer_id}/credit-balances/count",
		PathParams: []string{customerID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
