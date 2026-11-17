package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ProductsService struct {
	client *conjoin.Client
}

func (s *ProductsService) List(ctx context.Context, query *ListProductsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListProductsItem], error) {
	return conjoin.List[ListProductsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/products/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *ProductsService) Create(ctx context.Context, body *CreateProductRequest, opts ...conjoin.CallOption) (*CreateProductResponse, error) {
	var out CreateProductResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/products/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProductsService) ListCount(ctx context.Context, query *ListProductsCountQuery, opts ...conjoin.CallOption) (*ListProductsCountResponse, error) {
	var out ListProductsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/products/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProductsService) Read(ctx context.Context, productID string, opts ...conjoin.CallOption) (*ReadProductResponse, error) {
	var out ReadProductResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/products/{product_id}",
		PathParams: []string{productID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProductsService) Update(ctx context.Context, productID string, body *UpdateProductRequest, opts ...conjoin.CallOption) (*UpdateProductResponse, error) {
	var out UpdateProductResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "billing/products/{product_id}",
		PathParams:   []string{productID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProductsService) Delete(ctx context.Context, productID string, opts ...conjoin.CallOption) (*DeleteProductResponse, error) {
	var out DeleteProductResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "billing/products/{product_id}",
		PathParams: []string{productID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		Response:   conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProductsService) Archive(ctx context.Context, productID string, opts ...conjoin.CallOption) (*ArchiveProductResponse, error) {
	var out ArchiveProductResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/products/{product_id}/archive",
		PathParams:            []string{productID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ProductsService) Restore(ctx context.Context, productID string, opts ...conjoin.CallOption) (*RestoreProductResponse, error) {
	var out RestoreProductResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/products/{product_id}/restore",
		PathParams:            []string{productID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
