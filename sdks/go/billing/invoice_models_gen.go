package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListInvoicesQuery struct {
	InvoiceID      *string                      `json:"invoice_id,omitzero"`
	ReferenceID    *string                      `json:"reference_id,omitzero"`
	CustomerID     *string                      `json:"customer_id,omitzero"`
	SubscriptionID *string                      `json:"subscription_id,omitzero"`
	Status         *string                      `json:"status,omitzero"`
	DateCreated    *ListChargesQueryDateCreated `json:"date_created,omitzero"`
	Cursor         *ListChargesQueryCursor      `json:"cursor,omitzero"`
	Sort           map[string]string            `json:"sort,omitzero"`
	Limit          any                          `json:"limit,omitzero"`
}

type ListInvoicesItemAutomaticFinalisation struct {
	IsEnabled bool                     `json:"is_enabled"`
	Date      conjoin.Nullable[string] `json:"date,omitzero"`
}

type ListInvoicesItemLineItemsItemTiersItem struct {
	StartingUnit float64  `json:"starting_unit"`
	EndingUnit   *float64 `json:"ending_unit"`
	QuantityUsed float64  `json:"quantity_used"`
	UnitAmount   float64  `json:"unit_amount"`
	Subtotal     float64  `json:"subtotal"`
}

type ListInvoicesItemLineItemsItem struct {
	PriceID          conjoin.Nullable[string]                 `json:"price_id,omitzero"`
	DiscountID       conjoin.Nullable[string]                 `json:"discount_id,omitzero"`
	Currency         string                                   `json:"currency"`
	UnitPrice        float64                                  `json:"unit_price"`
	Quantity         float64                                  `json:"quantity"`
	DiscountAmount   float64                                  `json:"discount_amount"`
	Amount           float64                                  `json:"amount"`
	AmountAfterTaxes float64                                  `json:"amount_after_taxes"`
	Description      string                                   `json:"description"`
	SourceBundleID   conjoin.Nullable[string]                 `json:"source_bundle_id,omitzero"`
	Tiers            []ListInvoicesItemLineItemsItemTiersItem `json:"tiers,omitzero"`
}

type ListInvoicesItemCustomFieldsItem struct {
	Name  string `json:"name"`
	Value string `json:"value"`
}

type ListInvoicesItemPaymentSettings struct {
	AllowMultiplePaymentMethods conjoin.Nullable[bool]   `json:"allow_multiple_payment_methods,omitzero"`
	PaymentURL                  conjoin.Nullable[string] `json:"payment_url,omitzero"`
}

type ListInvoicesItemDisplaySettings struct {
	PdfPaperSize *string `json:"pdf_paper_size,omitzero"`
}

type ListInvoicesItem struct {
	InvoiceID             string                                 `json:"invoice_id"`
	ReferenceID           string                                 `json:"reference_id"`
	CustomerID            string                                 `json:"customer_id"`
	PriceIDs              []string                               `json:"price_ids"`
	SubscriptionID        conjoin.Nullable[string]               `json:"subscription_id,omitzero"`
	Subtotal              float64                                `json:"subtotal"`
	TaxAmount             float64                                `json:"tax_amount"`
	AmountDue             float64                                `json:"amount_due"`
	AmountPaid            float64                                `json:"amount_paid"`
	AmountRemaining       float64                                `json:"amount_remaining"`
	Currency              string                                 `json:"currency"`
	ChargeID              conjoin.Nullable[string]               `json:"charge_id,omitzero"`
	PaymentIntentID       conjoin.Nullable[string]               `json:"payment_intent_id,omitzero"`
	Description           *string                                `json:"description,omitzero"`
	FooterText            conjoin.Nullable[string]               `json:"footer_text,omitzero"`
	InvoiceNumber         string                                 `json:"invoice_number"`
	AutomaticFinalisation *ListInvoicesItemAutomaticFinalisation `json:"automatic_finalisation,omitzero"`
	Status                string                                 `json:"status"`
	InvoicingOption       string                                 `json:"invoicing_option"`
	InvoiceURL            conjoin.Nullable[string]               `json:"invoice_url,omitzero"`
	LineItems             []ListInvoicesItemLineItemsItem        `json:"line_items"`
	AttemptedAt           conjoin.Nullable[string]               `json:"attempted_at,omitzero"`
	RetryCount            float64                                `json:"retry_count"`
	CustomFields          []ListInvoicesItemCustomFieldsItem     `json:"custom_fields,omitzero"`
	DueDate               conjoin.Nullable[string]               `json:"due_date,omitzero"`
	IsPaid                bool                                   `json:"is_paid"`
	IsPaidWithoutCharge   bool                                   `json:"is_paid_without_charge"`
	PaymentMethodID       conjoin.Nullable[string]               `json:"payment_method_id,omitzero"`
	PaymentSettings       *ListInvoicesItemPaymentSettings       `json:"payment_settings,omitzero"`
	DisplaySettings       *ListInvoicesItemDisplaySettings       `json:"display_settings,omitzero"`
}

type CreateInvoiceRequestLineItemsItemTiersItem struct {
	StartingUnit int64  `json:"starting_unit"`
	EndingUnit   *int64 `json:"ending_unit"`
	QuantityUsed int64  `json:"quantity_used"`
	UnitAmount   int64  `json:"unit_amount"`
	Subtotal     int64  `json:"subtotal"`
}

type CreateInvoiceRequestLineItemsItem struct {
	PriceID        *string                                      `json:"price_id,omitzero"`
	DiscountID     *string                                      `json:"discount_id,omitzero"`
	Currency       string                                       `json:"currency"`
	UnitPrice      int64                                        `json:"unit_price"`
	Quantity       int64                                        `json:"quantity"`
	Description    *string                                      `json:"description,omitzero"`
	SourceBundleID *string                                      `json:"source_bundle_id,omitzero"`
	Tiers          []CreateInvoiceRequestLineItemsItemTiersItem `json:"tiers,omitzero"`
}

type CreateInvoiceRequestPaymentSettings struct {
	AllowMultiplePaymentMethods *bool `json:"allow_multiple_payment_methods,omitzero"`
}

type CreateInvoiceRequestEmailSettings struct {
	SendEmailWhenFinalised *bool   `json:"send_email_when_finalised,omitzero"`
	CustomerEmail          *string `json:"customer_email,omitzero"`
}

type CreateInvoiceRequestDisplaySettings struct {
	PdfPaperSize string `json:"pdf_paper_size"`
}

type CreateInvoiceRequest struct {
	ReferenceID     *string                              `json:"reference_id,omitzero"`
	CustomerID      string                               `json:"customer_id"`
	SubscriptionID  *string                              `json:"subscription_id,omitzero"`
	Subtotal        *int64                               `json:"subtotal,omitzero"`
	LineItems       []CreateInvoiceRequestLineItemsItem  `json:"line_items,omitzero"`
	TaxAmount       *int64                               `json:"tax_amount,omitzero"`
	Currency        *string                              `json:"currency,omitzero"`
	Description     *string                              `json:"description,omitzero"`
	FooterText      *string                              `json:"footer_text,omitzero"`
	InvoiceNumber   *string                              `json:"invoice_number,omitzero"`
	InvoicingOption string                               `json:"invoicing_option"`
	CustomFields    []ListInvoicesItemCustomFieldsItem   `json:"custom_fields,omitzero"`
	PaymentMethodID *string                              `json:"payment_method_id,omitzero"`
	PaymentSettings *CreateInvoiceRequestPaymentSettings `json:"payment_settings,omitzero"`
	EmailSettings   *CreateInvoiceRequestEmailSettings   `json:"email_settings,omitzero"`
	DisplaySettings *CreateInvoiceRequestDisplaySettings `json:"display_settings,omitzero"`
}

type CreateInvoiceResponse = ListInvoicesItem

type ListInvoicesCountQuery = ListInvoicesQuery

type ListInvoicesCountResponse = ListChargesCountResponse

type UpdateInvoiceRequest struct {
	Description     *string                              `json:"description,omitzero"`
	FooterText      *string                              `json:"footer_text,omitzero"`
	CustomFields    []ListInvoicesItemCustomFieldsItem   `json:"custom_fields,omitzero"`
	PaymentMethodID *string                              `json:"payment_method_id,omitzero"`
	PaymentSettings *CreateInvoiceRequestPaymentSettings `json:"payment_settings,omitzero"`
	DisplaySettings *CreateInvoiceRequestDisplaySettings `json:"display_settings,omitzero"`
}

type UpdateInvoiceResponse = ListInvoicesItem

type FinalizeInvoiceResponse = ListInvoicesItem

type PayInvoiceRequest struct {
	PaymentMethodID             *string `json:"payment_method_id,omitzero"`
	AllowMultiplePaymentMethods *bool   `json:"allow_multiple_payment_methods,omitzero"`
}

type PayInvoiceResponse = ListInvoicesItem

type VoidInvoiceResponse = ListInvoicesItem

type PayInvoiceOutOfBandRequest struct {
	Amount *int64 `json:"amount,omitzero"`
}

type PayInvoiceOutOfBandResponse = ListInvoicesItem

type SendInvoiceResponse = ListInvoicesItem

type ExportInvoicePdfResponse struct {
	PdfURL string `json:"pdf_url"`
}
