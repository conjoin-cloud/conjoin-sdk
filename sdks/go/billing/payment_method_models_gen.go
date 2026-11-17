package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListPaymentMethodsQuery struct {
	ReferenceID *string                                       `json:"reference_id,omitzero"`
	CustomerID  *string                                       `json:"customer_id,omitzero"`
	Type        *string                                       `json:"type,omitzero"`
	Brand       *string                                       `json:"brand,omitzero"`
	IsActive    any                                           `json:"is_active,omitzero"`
	IsDefault   any                                           `json:"is_default,omitzero"`
	DateCreated *ListChargesQueryDateCreated                  `json:"date_created,omitzero"`
	DateUpdated *ListChargesQueryDateCreated                  `json:"date_updated,omitzero"`
	DateDeleted conjoin.Nullable[ListChargesQueryDateCreated] `json:"date_deleted,omitzero"`
	Cursor      *ListChargesQueryCursor                       `json:"cursor,omitzero"`
	Sort        map[string]string                             `json:"sort,omitzero"`
	Limit       any                                           `json:"limit,omitzero"`
}

type ListPaymentMethodsItem struct {
	EntityID          string                    `json:"entity_id"`
	PaymentMethodID   string                    `json:"payment_method_id"`
	ReferenceID       string                    `json:"reference_id"`
	CustomerID        string                    `json:"customer_id"`
	Name              conjoin.Nullable[string]  `json:"name,omitzero"`
	Type              conjoin.Nullable[string]  `json:"type,omitzero"`
	Brand             conjoin.Nullable[string]  `json:"brand,omitzero"`
	CountryOfIssuance conjoin.Nullable[string]  `json:"country_of_issuance,omitzero"`
	Last4             conjoin.Nullable[string]  `json:"last4,omitzero"`
	ExpMonth          conjoin.Nullable[float64] `json:"exp_month,omitzero"`
	ExpYear           conjoin.Nullable[float64] `json:"exp_year,omitzero"`
	IsDefault         bool                      `json:"is_default"`
	IsActive          bool                      `json:"is_active"`
	DateCreated       string                    `json:"date_created"`
	DateUpdated       string                    `json:"date_updated"`
	DateDeleted       conjoin.Nullable[string]  `json:"date_deleted,omitzero"`
}

type CreatePaymentMethodRequest struct {
	ReferenceID       *string `json:"reference_id,omitzero"`
	CustomerID        string  `json:"customer_id"`
	CustomerCardEmail string  `json:"customer_card_email"`
	Name              *string `json:"name,omitzero"`
	IsDefault         *bool   `json:"is_default,omitzero"`
}

type ListPaymentMethodsCountQuery = ListPaymentMethodsQuery

type ListPaymentMethodsCountResponse = ListChargesCountResponse

type DeletePaymentMethodResponse = ListPaymentMethodsItem
