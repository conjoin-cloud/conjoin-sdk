package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type InvoicesService struct {
	client *conjoin.Client
}

func (s *InvoicesService) List(ctx context.Context, query *ListInvoicesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListInvoicesItem], error) {
	return conjoin.List[ListInvoicesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/invoices/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *InvoicesService) Create(ctx context.Context, body *CreateInvoiceRequest, opts ...conjoin.CallOption) (*CreateInvoiceResponse, error) {
	var out CreateInvoiceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/invoices/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *InvoicesService) ListCount(ctx context.Context, query *ListInvoicesCountQuery, opts ...conjoin.CallOption) (*ListInvoicesCountResponse, error) {
	var out ListInvoicesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/invoices/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *InvoicesService) Update(ctx context.Context, invoiceID string, body *UpdateInvoiceRequest, opts ...conjoin.CallOption) (*UpdateInvoiceResponse, error) {
	var out UpdateInvoiceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "billing/invoices/{invoice_id}",
		PathParams:   []string{invoiceID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *InvoicesService) Finalize(ctx context.Context, invoiceID string, opts ...conjoin.CallOption) (*FinalizeInvoiceResponse, error) {
	var out FinalizeInvoiceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "billing/invoices/{invoice_id}/finalize",
		PathParams: []string{invoiceID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *InvoicesService) Pay(ctx context.Context, invoiceID string, body *PayInvoiceRequest, opts ...conjoin.CallOption) (*PayInvoiceResponse, error) {
	var out PayInvoiceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/invoices/{invoice_id}/pay",
		PathParams:   []string{invoiceID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *InvoicesService) Void(ctx context.Context, invoiceID string, opts ...conjoin.CallOption) (*VoidInvoiceResponse, error) {
	var out VoidInvoiceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "billing/invoices/{invoice_id}/void",
		PathParams: []string{invoiceID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *InvoicesService) PayOutOfBand(ctx context.Context, invoiceID string, body *PayInvoiceOutOfBandRequest, opts ...conjoin.CallOption) (*PayInvoiceOutOfBandResponse, error) {
	var out PayInvoiceOutOfBandResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/invoices/{invoice_id}/pay-out-of-band",
		PathParams:   []string{invoiceID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *InvoicesService) Send(ctx context.Context, invoiceID string, opts ...conjoin.CallOption) (*SendInvoiceResponse, error) {
	var out SendInvoiceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "billing/invoices/{invoice_id}/send",
		PathParams: []string{invoiceID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *InvoicesService) ExportPdf(ctx context.Context, invoiceID string, opts ...conjoin.CallOption) (*ExportInvoicePdfResponse, error) {
	var out ExportInvoicePdfResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "billing/invoices/{invoice_id}/export",
		PathParams: []string{invoiceID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
