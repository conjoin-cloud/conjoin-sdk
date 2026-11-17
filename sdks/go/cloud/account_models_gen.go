package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadAccountResponseInactivityStatus struct {
	Reason *string `json:"reason"`
	Date   *string `json:"date"`
	Actor  *string `json:"actor"`
}

type ReadAccountResponseServiceAgreement struct {
	IsAccepted bool    `json:"is_accepted"`
	AcceptedAt *string `json:"accepted_at"`
	IPAddress  *string `json:"ip_address"`
}

type ReadAccountResponseOnboardingStatusBilling struct {
	Status      string  `json:"status"`
	CompletedAt *string `json:"completed_at"`
}

type ReadAccountResponseOnboardingStatus struct {
	Billing          ReadAccountResponseOnboardingStatusBilling `json:"billing"`
	ServiceAgreement ReadAccountResponseOnboardingStatusBilling `json:"service_agreement"`
}

type ReadAccountResponse struct {
	CloudAccountID         string                              `json:"cloud_account_id"`
	EntityID               string                              `json:"entity_id"`
	Region                 string                              `json:"region"`
	IsActive               bool                                `json:"is_active"`
	InactivityStatus       ReadAccountResponseInactivityStatus `json:"inactivity_status"`
	ServiceAgreement       ReadAccountResponseServiceAgreement `json:"service_agreement"`
	ApprovedServices       []string                            `json:"approved_services"`
	ServicesInUse          []string                            `json:"services_in_use"`
	PlanID                 *string                             `json:"plan_id"`
	OnboardingStatus       ReadAccountResponseOnboardingStatus `json:"onboarding_status"`
	BillingCustomerID      *string                             `json:"billing_customer_id"`
	BillingSubscriptionID  *string                             `json:"billing_subscription_id"`
	BillingDefaultCurrency *string                             `json:"billing_default_currency"`
	DateCreated            string                              `json:"date_created"`
	DateUpdated            conjoin.Nullable[string]            `json:"date_updated,omitzero"`
	DateDeleted            conjoin.Nullable[string]            `json:"date_deleted,omitzero"`
}

type UpdateAccountRequest struct {
	HasAcceptedTerms bool `json:"has_accepted_terms"`
}

type UpdateAccountResponse = ReadAccountResponse
