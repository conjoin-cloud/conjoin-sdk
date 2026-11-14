package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListCustomersQuery struct {
	CustomerID  *string                                       `json:"customer_id,omitzero"`
	ReferenceID *string                                       `json:"reference_id,omitzero"`
	DateCreated *ListChargesQueryDateCreated                  `json:"date_created,omitzero"`
	DateUpdated *ListChargesQueryDateCreated                  `json:"date_updated,omitzero"`
	DateDeleted conjoin.Nullable[ListChargesQueryDateCreated] `json:"date_deleted,omitzero"`
	Cursor      *ListChargesQueryCursor                       `json:"cursor,omitzero"`
	Sort        map[string]string                             `json:"sort,omitzero"`
	Limit       any                                           `json:"limit,omitzero"`
}

type ListCustomersItemAddress struct {
	Line1      string  `json:"line1"`
	Line2      *string `json:"line2,omitzero"`
	City       string  `json:"city"`
	State      string  `json:"state"`
	PostalCode string  `json:"postal_code"`
	Country    string  `json:"country"`
}

type ListCustomersItemInvoiceSettings struct {
	PaymentMethod               conjoin.Nullable[string] `json:"payment_method,omitzero"`
	AllowMultiplePaymentMethods conjoin.Nullable[bool]   `json:"allow_multiple_payment_methods,omitzero"`
}

type ListCustomersItemPaymentSettings struct {
	DefaultCurrency conjoin.Nullable[string] `json:"default_currency,omitzero"`
	TaxID           conjoin.Nullable[string] `json:"tax_id,omitzero"`
}

type ListCustomersItem struct {
	EntityID        string                            `json:"entity_id"`
	CustomerID      string                            `json:"customer_id"`
	ReferenceID     string                            `json:"reference_id"`
	Name            conjoin.Nullable[string]          `json:"name,omitzero"`
	Email           string                            `json:"email"`
	Phone           conjoin.Nullable[string]          `json:"phone,omitzero"`
	Address         *ListCustomersItemAddress         `json:"address,omitzero"`
	ShippingAddress *ListCustomersItemAddress         `json:"shipping_address,omitzero"`
	InvoiceSettings *ListCustomersItemInvoiceSettings `json:"invoice_settings,omitzero"`
	PaymentSettings *ListCustomersItemPaymentSettings `json:"payment_settings,omitzero"`
	DateCreated     string                            `json:"date_created"`
	DateUpdated     string                            `json:"date_updated"`
	DateDeleted     conjoin.Nullable[string]          `json:"date_deleted,omitzero"`
}

type CreateCustomerRequestInvoiceSettings struct {
	PaymentMethod               *string `json:"payment_method,omitzero"`
	AllowMultiplePaymentMethods *bool   `json:"allow_multiple_payment_methods,omitzero"`
}

type CreateCustomerRequestPaymentSettings struct {
	DefaultCurrency *string `json:"default_currency,omitzero"`
	TaxID           *string `json:"tax_id,omitzero"`
}

type CreateCustomerRequest struct {
	ReferenceID     *string                               `json:"reference_id,omitzero"`
	Name            *string                               `json:"name,omitzero"`
	Email           string                                `json:"email"`
	Phone           *string                               `json:"phone,omitzero"`
	Address         *ListCustomersItemAddress             `json:"address,omitzero"`
	ShippingAddress *ListCustomersItemAddress             `json:"shipping_address,omitzero"`
	InvoiceSettings *CreateCustomerRequestInvoiceSettings `json:"invoice_settings,omitzero"`
	PaymentSettings *CreateCustomerRequestPaymentSettings `json:"payment_settings,omitzero"`
}

type CreateCustomerResponse = ListCustomersItem

type ListCustomersCountQuery = ListCustomersQuery

type ListCustomersCountResponse = ListChargesCountResponse

type ReadCustomerResponse = ListCustomersItem

type UpdateCustomerRequest struct {
	Name            *string                               `json:"name,omitzero"`
	Email           *string                               `json:"email,omitzero"`
	Phone           *string                               `json:"phone,omitzero"`
	Address         *ListCustomersItemAddress             `json:"address,omitzero"`
	ShippingAddress *ListCustomersItemAddress             `json:"shipping_address,omitzero"`
	InvoiceSettings *CreateCustomerRequestInvoiceSettings `json:"invoice_settings,omitzero"`
	PaymentSettings *CreateCustomerRequestPaymentSettings `json:"payment_settings,omitzero"`
}

type UpdateCustomerResponse = ListCustomersItem

type ArchiveCustomerResponse = ListCustomersItem

type RestoreCustomerResponse = ListCustomersItem
