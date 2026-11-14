package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListPaymentIntentsQuery struct {
	PaymentIntentID *string                                       `json:"payment_intent_id,omitzero"`
	ReferenceID     *string                                       `json:"reference_id,omitzero"`
	CustomerID      *string                                       `json:"customer_id,omitzero"`
	DateCreated     *ListChargesQueryDateCreated                  `json:"date_created,omitzero"`
	DateUpdated     *ListChargesQueryDateCreated                  `json:"date_updated,omitzero"`
	DateDeleted     conjoin.Nullable[ListChargesQueryDateCreated] `json:"date_deleted,omitzero"`
	Cursor          *ListChargesQueryCursor                       `json:"cursor,omitzero"`
	Sort            map[string]string                             `json:"sort,omitzero"`
	Limit           any                                           `json:"limit,omitzero"`
}

type ListPaymentIntentsItem struct {
	EntityID           string                   `json:"entity_id"`
	PaymentIntentID    string                   `json:"payment_intent_id"`
	ReferenceID        string                   `json:"reference_id"`
	LookupKey          conjoin.Nullable[string] `json:"lookup_key,omitzero"`
	CustomerID         conjoin.Nullable[string] `json:"customer_id,omitzero"`
	Description        *string                  `json:"description,omitzero"`
	PriceID            conjoin.Nullable[string] `json:"price_id,omitzero"`
	Amount             float64                  `json:"amount"`
	Currency           string                   `json:"currency"`
	PaymentMethodTypes []string                 `json:"payment_method_types,omitzero"`
	PaymentMethodID    conjoin.Nullable[string] `json:"payment_method_id,omitzero"`
	ReceiptEmail       conjoin.Nullable[string] `json:"receipt_email,omitzero"`
	SetupFutureUsage   conjoin.Nullable[string] `json:"setup_future_usage,omitzero"`
	Status             string                   `json:"status"`
	DateCreated        string                   `json:"date_created"`
	DateUpdated        string                   `json:"date_updated"`
	DateDeleted        conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreatePaymentIntentRequest struct {
	ReferenceID         *string  `json:"reference_id,omitzero"`
	CustomerID          string   `json:"customer_id"`
	Description         *string  `json:"description,omitzero"`
	PriceID             *string  `json:"price_id,omitzero"`
	Amount              *int64   `json:"amount,omitzero"`
	Currency            string   `json:"currency"`
	PaymentMethodTypes  []string `json:"payment_method_types,omitzero"`
	PaymentMethodID     *string  `json:"payment_method_id,omitzero"`
	ReceiptEmail        *string  `json:"receipt_email,omitzero"`
	CustomerTaxID       *string  `json:"customer_tax_id,omitzero"`
	SetupFutureUsage    *string  `json:"setup_future_usage,omitzero"`
	DisableTaxReporting *bool    `json:"disable_tax_reporting,omitzero"`
}

type ListPaymentIntentsCountQuery = ListPaymentIntentsQuery

type ListPaymentIntentsCountResponse = ListChargesCountResponse

type VerifyPaymentIntentResponse = ListPaymentIntentsItem
