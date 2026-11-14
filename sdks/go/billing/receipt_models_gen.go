package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListReceiptsQuery struct {
	Status      *string                                       `json:"status,omitzero"`
	ChargeID    *string                                       `json:"charge_id,omitzero"`
	DateCreated *ListChargesQueryDateCreated                  `json:"date_created,omitzero"`
	DateUpdated *ListChargesQueryDateCreated                  `json:"date_updated,omitzero"`
	DateDeleted conjoin.Nullable[ListChargesQueryDateCreated] `json:"date_deleted,omitzero"`
	Cursor      *ListChargesQueryCursor                       `json:"cursor,omitzero"`
	Sort        map[string]string                             `json:"sort,omitzero"`
	Limit       any                                           `json:"limit,omitzero"`
}

type ListReceiptsItem struct {
	ReceiptID   string  `json:"receipt_id"`
	ChargeID    string  `json:"charge_id"`
	EntityID    string  `json:"entity_id"`
	Status      string  `json:"status"`
	PdfURL      *string `json:"pdf_url"`
	ErrorReason *string `json:"error_reason"`
	Amount      float64 `json:"amount"`
	Currency    string  `json:"currency"`
	CustomerID  *string `json:"customer_id"`
	DateCreated string  `json:"date_created"`
	DateUpdated *string `json:"date_updated"`
	DateDeleted *string `json:"date_deleted"`
}

type ListReceiptsCountQuery = ListReceiptsQuery

type ListReceiptsCountResponse = ListChargesCountResponse

type ReadReceiptResponse = ListReceiptsItem
