package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type TaxJurisdictionsService struct {
	client *conjoin.Client
}

func (s *TaxJurisdictionsService) List(ctx context.Context, query *ListTaxJurisdictionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListTaxJurisdictionsItem], error) {
	return conjoin.List[ListTaxJurisdictionsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/tax-jurisdictions/",
		Query:  query,
	}, opts...)
}

func (s *TaxJurisdictionsService) ListCount(ctx context.Context, query *ListTaxJurisdictionsCountQuery, opts ...conjoin.CallOption) (*ListTaxJurisdictionsCountResponse, error) {
	var out ListTaxJurisdictionsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/tax-jurisdictions/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *TaxJurisdictionsService) QueryTaxRate(ctx context.Context, query *QueryTaxRateQuery, opts ...conjoin.CallOption) (*QueryTaxRateResponse, error) {
	var out QueryTaxRateResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:        "GET",
		Path:          "billing/tax-jurisdictions/effective-rates",
		Query:         query,
		QueryRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
