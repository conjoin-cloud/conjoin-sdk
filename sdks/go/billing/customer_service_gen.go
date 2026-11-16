package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type CustomersService struct {
	client *conjoin.Client
}

func (s *CustomersService) List(ctx context.Context, query *ListCustomersQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListCustomersItem], error) {
	return conjoin.List[ListCustomersItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/customers/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *CustomersService) Create(ctx context.Context, body *CreateCustomerRequest, opts ...conjoin.CallOption) (*CreateCustomerResponse, error) {
	var out CreateCustomerResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/customers/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CustomersService) ListCount(ctx context.Context, query *ListCustomersCountQuery, opts ...conjoin.CallOption) (*ListCustomersCountResponse, error) {
	var out ListCustomersCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/customers/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CustomersService) Read(ctx context.Context, customerID string, opts ...conjoin.CallOption) (*ReadCustomerResponse, error) {
	var out ReadCustomerResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/customers/{customer_id}",
		PathParams: []string{customerID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CustomersService) Update(ctx context.Context, customerID string, body *UpdateCustomerRequest, opts ...conjoin.CallOption) (*UpdateCustomerResponse, error) {
	var out UpdateCustomerResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "billing/customers/{customer_id}",
		PathParams:   []string{customerID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CustomersService) Archive(ctx context.Context, customerID string, opts ...conjoin.CallOption) (*ArchiveCustomerResponse, error) {
	var out ArchiveCustomerResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/customers/{customer_id}/archive",
		PathParams:            []string{customerID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CustomersService) Restore(ctx context.Context, customerID string, opts ...conjoin.CallOption) (*RestoreCustomerResponse, error) {
	var out RestoreCustomerResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/customers/{customer_id}/restore",
		PathParams:            []string{customerID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
