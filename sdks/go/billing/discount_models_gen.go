package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListDiscountsQuery struct {
	CustomerID  *string                      `json:"customer_id,omitzero"`
	CouponID    *string                      `json:"coupon_id,omitzero"`
	ReferenceID *string                      `json:"reference_id,omitzero"`
	IsActive    any                          `json:"is_active,omitzero"`
	DateCreated *ListChargesQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListChargesQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string            `json:"sort,omitzero"`
	Limit       any                          `json:"limit,omitzero"`
}

type ListDiscountsItem struct {
	DiscountID         string                    `json:"discount_id"`
	ReferenceID        string                    `json:"reference_id"`
	ConjoinAccountID   string                    `json:"conjoin_account_id"`
	ConjoinProjectID   string                    `json:"conjoin_project_id"`
	EntityID           string                    `json:"entity_id"`
	LiveMode           bool                      `json:"live_mode"`
	CouponID           string                    `json:"coupon_id"`
	CustomerID         string                    `json:"customer_id"`
	SubscriptionID     conjoin.Nullable[string]  `json:"subscription_id,omitzero"`
	InvoiceID          conjoin.Nullable[string]  `json:"invoice_id,omitzero"`
	DiscountAmount     float64                   `json:"discount_amount"`
	Currency           string                    `json:"currency"`
	CyclesApplied      float64                   `json:"cycles_applied"`
	CyclesRemaining    conjoin.Nullable[float64] `json:"cycles_remaining,omitzero"`
	IsActive           bool                      `json:"is_active"`
	StartDate          string                    `json:"start_date"`
	EndDate            conjoin.Nullable[string]  `json:"end_date,omitzero"`
	SourceActivationID conjoin.Nullable[string]  `json:"source_activation_id,omitzero"`
	DateCreated        string                    `json:"date_created"`
	DateUpdated        string                    `json:"date_updated"`
	DateDeleted        conjoin.Nullable[string]  `json:"date_deleted,omitzero"`
}

type CreateDiscountRequest struct {
	CouponID       string  `json:"coupon_id"`
	CustomerID     string  `json:"customer_id"`
	SubscriptionID *string `json:"subscription_id,omitzero"`
	ReferenceID    *string `json:"reference_id,omitzero"`
}

type CreateDiscountResponse = ListDiscountsItem

type ListDiscountsCountQuery = ListDiscountsQuery

type ListDiscountsCountResponse = ListChargesCountResponse

type DeleteDiscountResponse = ListDiscountsItem
