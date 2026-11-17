package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadSettingsResponseDefaultInvoiceSettings struct {
	PaymentTermsDays float64                  `json:"payment_terms_days"`
	FooterText       conjoin.Nullable[string] `json:"footer_text,omitzero"`
	GracePeriodHours float64                  `json:"grace_period_hours"`
}

type ReadSettingsResponse struct {
	SettingsID                   string                                      `json:"settings_id"`
	ConjoinAccountID             string                                      `json:"conjoin_account_id"`
	ConjoinProjectID             string                                      `json:"conjoin_project_id"`
	AutoReceiptGeneration        bool                                        `json:"auto_receipt_generation"`
	CreditAutoApply              bool                                        `json:"credit_auto_apply"`
	DefaultCurrency              conjoin.Nullable[string]                    `json:"default_currency,omitzero"`
	DefaultInvoiceSettings       *ReadSettingsResponseDefaultInvoiceSettings `json:"default_invoice_settings,omitzero"`
	TaxReportingEnabled          bool                                        `json:"tax_reporting_enabled"`
	IncompatibleAddonBehavior    string                                      `json:"incompatible_addon_behavior"`
	CancellationFallbackBehavior string                                      `json:"cancellation_fallback_behavior"`
	DateCreated                  string                                      `json:"date_created"`
	DateUpdated                  string                                      `json:"date_updated"`
	DateDeleted                  conjoin.Nullable[string]                    `json:"date_deleted,omitzero"`
	LiveMode                     bool                                        `json:"live_mode"`
}

type UpdateSettingsRequestDefaultInvoiceSettings struct {
	PaymentTermsDays *int64                   `json:"payment_terms_days,omitzero"`
	FooterText       conjoin.Nullable[string] `json:"footer_text,omitzero"`
	GracePeriodHours *int64                   `json:"grace_period_hours,omitzero"`
}

type UpdateSettingsRequest struct {
	AutoReceiptGeneration        *bool                                        `json:"auto_receipt_generation,omitzero"`
	CreditAutoApply              *bool                                        `json:"credit_auto_apply,omitzero"`
	DefaultCurrency              *string                                      `json:"default_currency,omitzero"`
	DefaultInvoiceSettings       *UpdateSettingsRequestDefaultInvoiceSettings `json:"default_invoice_settings,omitzero"`
	TaxReportingEnabled          *bool                                        `json:"tax_reporting_enabled,omitzero"`
	IncompatibleAddonBehavior    *string                                      `json:"incompatible_addon_behavior,omitzero"`
	CancellationFallbackBehavior *string                                      `json:"cancellation_fallback_behavior,omitzero"`
}

type UpdateSettingsResponse = ReadSettingsResponse
