package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type PricesService struct {
	client *conjoin.Client
}

func (s *PricesService) List(ctx context.Context, query *ListPricesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListPricesItem], error) {
	return conjoin.List[ListPricesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/prices/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *PricesService) Create(ctx context.Context, body *CreatePriceRequest, opts ...conjoin.CallOption) (*CreatePriceResponse, error) {
	var out CreatePriceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/prices/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PricesService) ListCount(ctx context.Context, query *ListPricesCountQuery, opts ...conjoin.CallOption) (*ListPricesCountResponse, error) {
	var out ListPricesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/prices/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PricesService) Read(ctx context.Context, priceID string, opts ...conjoin.CallOption) (*ReadPriceResponse, error) {
	var out ReadPriceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/prices/{price_id}",
		PathParams: []string{priceID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PricesService) Update(ctx context.Context, priceID string, body *UpdatePriceRequest, opts ...conjoin.CallOption) (*UpdatePriceResponse, error) {
	var out UpdatePriceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "billing/prices/{price_id}",
		PathParams:   []string{priceID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PricesService) Delete(ctx context.Context, priceID string, opts ...conjoin.CallOption) (*DeletePriceResponse, error) {
	var out DeletePriceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "billing/prices/{price_id}",
		PathParams: []string{priceID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		Response:   conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PricesService) Archive(ctx context.Context, priceID string, opts ...conjoin.CallOption) (*ArchivePriceResponse, error) {
	var out ArchivePriceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "billing/prices/{price_id}/archive",
		PathParams: []string{priceID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PricesService) Restore(ctx context.Context, priceID string, opts ...conjoin.CallOption) (*RestorePriceResponse, error) {
	var out RestorePriceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "billing/prices/{price_id}/restore",
		PathParams: []string{priceID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
