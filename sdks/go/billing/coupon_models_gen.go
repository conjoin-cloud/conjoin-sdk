package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListCouponsQuery struct {
	CouponCode  *string                      `json:"coupon_code,omitzero"`
	ReferenceID *string                      `json:"reference_id,omitzero"`
	IsActive    any                          `json:"is_active,omitzero"`
	ReasonCode  *string                      `json:"reason_code,omitzero"`
	DateCreated *ListChargesQueryDateCreated `json:"date_created,omitzero"`
	DateUpdated *ListChargesQueryDateCreated `json:"date_updated,omitzero"`
	Cursor      *ListChargesQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string            `json:"sort,omitzero"`
	Limit       any                          `json:"limit,omitzero"`
}

type ListCouponsItemAppliesTo struct {
	Scope      string   `json:"scope"`
	ProductIDs []string `json:"product_ids"`
	PriceIDs   []string `json:"price_ids"`
}

type ListCouponsItem struct {
	CouponID         string                   `json:"coupon_id"`
	ReferenceID      string                   `json:"reference_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	Name             string                   `json:"name"`
	CouponCode       string                   `json:"coupon_code"`
	DiscountType     string                   `json:"discount_type"`
	AmountOff        *float64                 `json:"amount_off"`
	PercentOff       *float64                 `json:"percent_off"`
	Currency         conjoin.Nullable[string] `json:"currency,omitzero"`
	Duration         string                   `json:"duration"`
	DurationInCycles *float64                 `json:"duration_in_cycles"`
	AppliesTo        ListCouponsItemAppliesTo `json:"applies_to"`
	MaxRedemptions   *float64                 `json:"max_redemptions"`
	TimesRedeemed    float64                  `json:"times_redeemed"`
	ExpirationDate   *string                  `json:"expiration_date"`
	IsActive         bool                     `json:"is_active"`
	ReasonCode       string                   `json:"reason_code"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateCouponRequestAppliesTo struct {
	Scope      string   `json:"scope"`
	ProductIDs []string `json:"product_ids,omitzero"`
	PriceIDs   []string `json:"price_ids,omitzero"`
}

type CreateCouponRequest struct {
	Name             string                        `json:"name"`
	CouponCode       string                        `json:"coupon_code"`
	DiscountType     string                        `json:"discount_type"`
	AmountOff        *int64                        `json:"amount_off,omitzero"`
	PercentOff       *float64                      `json:"percent_off,omitzero"`
	Currency         *string                       `json:"currency,omitzero"`
	Duration         string                        `json:"duration"`
	DurationInCycles *int64                        `json:"duration_in_cycles,omitzero"`
	AppliesTo        *CreateCouponRequestAppliesTo `json:"applies_to,omitzero"`
	MaxRedemptions   *int64                        `json:"max_redemptions,omitzero"`
	ExpirationDate   *string                       `json:"expiration_date,omitzero"`
	ReasonCode       string                        `json:"reason_code"`
	ReferenceID      *string                       `json:"reference_id,omitzero"`
}

type CreateCouponResponse = ListCouponsItem

type ListCouponsCountQuery = ListCouponsQuery

type ListCouponsCountResponse = ListChargesCountResponse

type UpdateCouponRequest struct {
	Name           *string                       `json:"name,omitzero"`
	IsActive       *bool                         `json:"is_active,omitzero"`
	MaxRedemptions *int64                        `json:"max_redemptions,omitzero"`
	ExpirationDate conjoin.Nullable[string]      `json:"expiration_date,omitzero"`
	AppliesTo      *CreateCouponRequestAppliesTo `json:"applies_to,omitzero"`
}

type UpdateCouponResponse = ListCouponsItem

type DeleteCouponResponse = ListCouponsItem
