package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListChargesQueryDateCreated struct {
	Equals    *string `json:"equals,omitzero"`
	NotEquals *string `json:"not_equals,omitzero"`
	Gt        *string `json:"gt,omitzero"`
	Lt        *string `json:"lt,omitzero"`
	Gte       *string `json:"gte,omitzero"`
	Lte       *string `json:"lte,omitzero"`
}

type ListChargesQueryCursor struct {
	Prev *string `json:"prev,omitzero"`
	Next *string `json:"next,omitzero"`
}

type ListChargesQuery struct {
	TransactionID *string                                       `json:"transaction_id,omitzero"`
	PaymentType   *string                                       `json:"payment_type,omitzero"`
	DateCreated   *ListChargesQueryDateCreated                  `json:"date_created,omitzero"`
	DateUpdated   *ListChargesQueryDateCreated                  `json:"date_updated,omitzero"`
	DateDeleted   conjoin.Nullable[ListChargesQueryDateCreated] `json:"date_deleted,omitzero"`
	Cursor        *ListChargesQueryCursor                       `json:"cursor,omitzero"`
	Sort          map[string]string                             `json:"sort,omitzero"`
	Limit         any                                           `json:"limit,omitzero"`
}

type ListChargesItem struct {
	EntityID        string                   `json:"entity_id"`
	ChargeID        string                   `json:"charge_id"`
	TransactionID   string                   `json:"transaction_id"`
	TransactionType string                   `json:"transaction_type"`
	PaymentType     string                   `json:"payment_type"`
	Status          string                   `json:"status"`
	Amount          float64                  `json:"amount"`
	Currency        string                   `json:"currency"`
	DateCreated     string                   `json:"date_created"`
	DateUpdated     string                   `json:"date_updated"`
	DateDeleted     conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ListChargesCountQuery = ListChargesQuery

type ListChargesCountResponse struct {
	Count int64 `json:"count"`
}
