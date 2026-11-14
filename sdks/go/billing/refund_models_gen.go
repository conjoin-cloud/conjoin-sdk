package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListRefundsQuery struct {
	RefundID    *string                                       `json:"refund_id,omitzero"`
	ReferenceID *string                                       `json:"reference_id,omitzero"`
	ChargeID    *string                                       `json:"charge_id,omitzero"`
	DateCreated *ListChargesQueryDateCreated                  `json:"date_created,omitzero"`
	DateUpdated *ListChargesQueryDateCreated                  `json:"date_updated,omitzero"`
	DateDeleted conjoin.Nullable[ListChargesQueryDateCreated] `json:"date_deleted,omitzero"`
	Cursor      *ListChargesQueryCursor                       `json:"cursor,omitzero"`
	Sort        map[string]string                             `json:"sort,omitzero"`
	Limit       any                                           `json:"limit,omitzero"`
}

type ListRefundsItem struct {
	EntityID       string                   `json:"entity_id"`
	RefundID       string                   `json:"refund_id"`
	ReferenceID    string                   `json:"reference_id"`
	ChargeID       string                   `json:"charge_id"`
	Status         string                   `json:"status"`
	FulfilmentType string                   `json:"fulfilment_type"`
	Amount         float64                  `json:"amount"`
	Currency       string                   `json:"currency"`
	DateCreated    string                   `json:"date_created"`
	DateUpdated    string                   `json:"date_updated"`
	DateDeleted    conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateRefundRequest struct {
	ReferenceID string `json:"reference_id"`
	ChargeID    string `json:"charge_id"`
	Amount      *int64 `json:"amount,omitzero"`
}

type CreateRefundResponse = ListRefundsItem

type ListRefundsCountQuery = ListRefundsQuery

type ListRefundsCountResponse = ListChargesCountResponse
