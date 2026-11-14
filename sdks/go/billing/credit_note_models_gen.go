package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListCreditNotesQuery struct {
	ReferenceID *string                      `json:"reference_id,omitzero"`
	CustomerID  *string                      `json:"customer_id,omitzero"`
	InvoiceID   *string                      `json:"invoice_id,omitzero"`
	Status      *string                      `json:"status,omitzero"`
	Reason      *string                      `json:"reason,omitzero"`
	DateCreated *ListChargesQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListChargesQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string            `json:"sort,omitzero"`
	Limit       any                          `json:"limit,omitzero"`
}

type ListCreditNotesItemLineItemsItem struct {
	Description string  `json:"description"`
	Amount      float64 `json:"amount"`
	Quantity    float64 `json:"quantity"`
}

type ListCreditNotesItemApplicationsItem struct {
	InvoiceID     string  `json:"invoice_id"`
	AmountApplied float64 `json:"amount_applied"`
	AppliedAt     string  `json:"applied_at"`
}

type ListCreditNotesItem struct {
	CreditNoteID     string                                `json:"credit_note_id"`
	ReferenceID      string                                `json:"reference_id"`
	ConjoinAccountID string                                `json:"conjoin_account_id"`
	ConjoinProjectID string                                `json:"conjoin_project_id"`
	EntityID         string                                `json:"entity_id"`
	LiveMode         bool                                  `json:"live_mode"`
	CustomerID       string                                `json:"customer_id"`
	InvoiceID        conjoin.Nullable[string]              `json:"invoice_id,omitzero"`
	SubscriptionID   conjoin.Nullable[string]              `json:"subscription_id,omitzero"`
	CycleID          conjoin.Nullable[string]              `json:"cycle_id,omitzero"`
	Amount           float64                               `json:"amount"`
	AmountRemaining  float64                               `json:"amount_remaining"`
	Currency         string                                `json:"currency"`
	Status           string                                `json:"status"`
	Reason           string                                `json:"reason"`
	Description      conjoin.Nullable[string]              `json:"description,omitzero"`
	LineItems        []ListCreditNotesItemLineItemsItem    `json:"line_items"`
	Applications     []ListCreditNotesItemApplicationsItem `json:"applications"`
	DateCreated      string                                `json:"date_created"`
	DateUpdated      string                                `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]              `json:"date_deleted,omitzero"`
}

type CreateCreditNoteRequest struct {
	ReferenceID *string `json:"reference_id,omitzero"`
	CustomerID  string  `json:"customer_id"`
	InvoiceID   *string `json:"invoice_id,omitzero"`
	Amount      int64   `json:"amount"`
	Currency    string  `json:"currency"`
	Reason      string  `json:"reason"`
	Description *string `json:"description,omitzero"`
}

type CreateCreditNoteResponse = ListCreditNotesItem

type ListCustomerCreditBalancesQuery struct {
	Currency *string                 `json:"currency,omitzero"`
	Cursor   *ListChargesQueryCursor `json:"cursor,omitzero"`
	Sort     map[string]string       `json:"sort,omitzero"`
	Limit    any                     `json:"limit,omitzero"`
}

type ListCustomerCreditBalancesItem struct {
	CreditBalanceID  string                   `json:"credit_balance_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	CustomerID       string                   `json:"customer_id"`
	Currency         string                   `json:"currency"`
	Balance          float64                  `json:"balance"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
	LiveMode         bool                     `json:"live_mode"`
}

type ListCreditNotesCountQuery = ListCreditNotesQuery

type ListCreditNotesCountResponse = ListChargesCountResponse

type VoidCreditNoteResponse = ListCreditNotesItem

type ListCustomerCreditBalancesCountQuery = ListCustomerCreditBalancesQuery

type ListCustomerCreditBalancesCountResponse = ListChargesCountResponse
