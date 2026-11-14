package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListCreditWalletsQuery struct {
	CustomerID  *string                      `json:"customer_id,omitzero"`
	Label       *string                      `json:"label,omitzero"`
	IsActive    any                          `json:"is_active,omitzero"`
	DateCreated *ListChargesQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListChargesQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string            `json:"sort,omitzero"`
	Limit       any                          `json:"limit,omitzero"`
}

type ListCreditWalletsItemAutoTopup struct {
	Enabled         bool                     `json:"enabled"`
	Threshold       float64                  `json:"threshold"`
	TopupAmount     float64                  `json:"topup_amount"`
	PaymentMethodID conjoin.Nullable[string] `json:"payment_method_id,omitzero"`
}

type ListCreditWalletsItem struct {
	WalletID         string                         `json:"wallet_id"`
	ConjoinAccountID string                         `json:"conjoin_account_id"`
	ConjoinProjectID string                         `json:"conjoin_project_id"`
	EntityID         string                         `json:"entity_id"`
	LiveMode         bool                           `json:"live_mode"`
	CustomerID       string                         `json:"customer_id"`
	Currency         string                         `json:"currency"`
	Label            string                         `json:"label"`
	Balance          float64                        `json:"balance"`
	CreditValue      float64                        `json:"credit_value"`
	AutoTopup        ListCreditWalletsItemAutoTopup `json:"auto_topup"`
	IsActive         bool                           `json:"is_active"`
	DateCreated      string                         `json:"date_created"`
	DateUpdated      string                         `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]       `json:"date_deleted,omitzero"`
}

type CreateCreditWalletRequestAutoTopup struct {
	Enabled         *bool    `json:"enabled,omitzero"`
	Threshold       *float64 `json:"threshold,omitzero"`
	TopupAmount     *float64 `json:"topup_amount,omitzero"`
	PaymentMethodID *string  `json:"payment_method_id,omitzero"`
}

type CreateCreditWalletRequest struct {
	CustomerID  string                              `json:"customer_id"`
	Currency    string                              `json:"currency"`
	Label       *string                             `json:"label,omitzero"`
	CreditValue float64                             `json:"credit_value"`
	AutoTopup   *CreateCreditWalletRequestAutoTopup `json:"auto_topup,omitzero"`
}

type CreateCreditWalletResponse = ListCreditWalletsItem

type ListCreditWalletsCountQuery = ListCreditWalletsQuery

type ListCreditWalletsCountResponse = ListChargesCountResponse

type UpdateCreditWalletRequestAutoTopup struct {
	Enabled         *bool                    `json:"enabled,omitzero"`
	Threshold       *float64                 `json:"threshold,omitzero"`
	TopupAmount     *float64                 `json:"topup_amount,omitzero"`
	PaymentMethodID conjoin.Nullable[string] `json:"payment_method_id,omitzero"`
}

type UpdateCreditWalletRequest struct {
	CreditValue *float64                            `json:"credit_value,omitzero"`
	IsActive    *bool                               `json:"is_active,omitzero"`
	AutoTopup   *UpdateCreditWalletRequestAutoTopup `json:"auto_topup,omitzero"`
}

type UpdateCreditWalletResponse = ListCreditWalletsItem

type GrantCreditsRequest struct {
	Amount         int64   `json:"amount"`
	Source         string  `json:"source"`
	ExpirationDate *string `json:"expiration_date,omitzero"`
}

type GrantCreditsResponse struct {
	GrantID          string                   `json:"grant_id"`
	WalletID         string                   `json:"wallet_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	CustomerID       string                   `json:"customer_id"`
	Amount           float64                  `json:"amount"`
	AmountRemaining  float64                  `json:"amount_remaining"`
	Source           string                   `json:"source"`
	ExpirationDate   conjoin.Nullable[string] `json:"expiration_date,omitzero"`
	IsActive         bool                     `json:"is_active"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}
