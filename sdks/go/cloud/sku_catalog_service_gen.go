package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SKUCatalogsService struct {
	client *conjoin.Client
}

func (s *SKUCatalogsService) ReadSkuCatalog(ctx context.Context, query *ReadSkuCatalogQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadSkuCatalogItem], error) {
	return conjoin.List[ReadSkuCatalogItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/skus/",
		Query:  query,
	}, opts...)
}

func (s *SKUCatalogsService) ReadSkuCatalogCount(ctx context.Context, query *ReadSkuCatalogCountQuery, opts ...conjoin.CallOption) (*ReadSkuCatalogCountResponse, error) {
	var out ReadSkuCatalogCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/skus/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SKUCatalogsService) ReadSingleSkuCatalog(ctx context.Context, skuID string, opts ...conjoin.CallOption) (*ReadSingleSkuCatalogResponse, error) {
	var out ReadSingleSkuCatalogResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "cloud/skus/{sku_id}",
		PathParams: []string{skuID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
