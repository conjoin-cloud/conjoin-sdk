package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListDisputesQuery struct {
	ChargeID    *string                                       `json:"charge_id,omitzero"`
	Outcome     *string                                       `json:"outcome,omitzero"`
	Reason      *string                                       `json:"reason,omitzero"`
	DateCreated *ListChargesQueryDateCreated                  `json:"date_created,omitzero"`
	DateUpdated *ListChargesQueryDateCreated                  `json:"date_updated,omitzero"`
	DateDeleted conjoin.Nullable[ListChargesQueryDateCreated] `json:"date_deleted,omitzero"`
	Cursor      *ListChargesQueryCursor                       `json:"cursor,omitzero"`
	Sort        map[string]string                             `json:"sort,omitzero"`
	Limit       any                                           `json:"limit,omitzero"`
}

type ListDisputesItem struct {
	DisputeID             string                   `json:"dispute_id"`
	ChargeID              *string                  `json:"charge_id"`
	Outcome               string                   `json:"outcome"`
	Reason                *string                  `json:"reason,omitzero"`
	Amount                int64                    `json:"amount"`
	Currency              string                   `json:"currency"`
	ChargeAmount          *int64                   `json:"charge_amount,omitzero"`
	AcceptedAmount        *int64                   `json:"accepted_amount,omitzero"`
	FundsWithdrawnAmount  *int64                   `json:"funds_withdrawn_amount,omitzero"`
	FundsReinstatedAmount *int64                   `json:"funds_reinstated_amount,omitzero"`
	DisputeFee            *int64                   `json:"dispute_fee,omitzero"`
	IsDisputeFeeReversed  *bool                    `json:"is_dispute_fee_reversed,omitzero"`
	EvidenceDueAt         conjoin.Nullable[string] `json:"evidence_due_at,omitzero"`
	OpenedAt              conjoin.Nullable[string] `json:"opened_at,omitzero"`
	ResolvedAt            conjoin.Nullable[string] `json:"resolved_at,omitzero"`
	DateCreated           string                   `json:"date_created"`
	DateUpdated           string                   `json:"date_updated"`
	DateDeleted           conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ListDisputesCountQuery = ListDisputesQuery

type ListDisputesCountResponse = ListChargesCountResponse

type GetDisputeResponse = ListDisputesItem
