package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListEntitiesQuery struct {
	Expand      *string                      `json:"expand,omitzero"`
	IsActive    any                          `json:"is_active,omitzero"`
	DateCreated *ListChargesQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListChargesQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string            `json:"sort,omitzero"`
	Limit       any                          `json:"limit,omitzero"`
}

type ListEntitiesItem struct {
	EntityID    string                   `json:"entity_id"`
	IsActive    bool                     `json:"is_active"`
	DateCreated string                   `json:"date_created"`
	DateUpdated string                   `json:"date_updated"`
	DateDeleted conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateEntityRequestAccountDataCompanyVerificationDocument struct {
	DocumentType *string `json:"document_type"`
	FrontURL     *string `json:"front_url"`
	BackURL      *string `json:"back_url"`
}

type CreateEntityRequestAccountDataCompanyVerification struct {
	Document CreateEntityRequestAccountDataCompanyVerificationDocument `json:"document"`
}

type CreateEntityRequestAccountDataCompany struct {
	Name               string                                             `json:"name"`
	PhoneNumber        string                                             `json:"phone_number"`
	Email              string                                             `json:"email"`
	RegistrationNumber string                                             `json:"registration_number"`
	Structure          string                                             `json:"structure"`
	Tin                string                                             `json:"tin"`
	WebsiteURL         conjoin.Nullable[string]                           `json:"website_url,omitzero"`
	Address            ListCustomersItemAddress                           `json:"address"`
	Verification       *CreateEntityRequestAccountDataCompanyVerification `json:"verification,omitzero"`
}

type CreateEntityRequestAccountDataIndividualsItemAccountRelationship struct {
	Title               string  `json:"title"`
	IsOwner             *bool   `json:"is_owner,omitzero"`
	IsDirector          *bool   `json:"is_director,omitzero"`
	IsExecutive         *bool   `json:"is_executive,omitzero"`
	OwnershipPercentage float64 `json:"ownership_percentage"`
}

type CreateEntityRequestAccountDataIndividualsItem struct {
	IsAccountManager     *bool                                                            `json:"is_account_manager,omitzero"`
	FirstName            string                                                           `json:"first_name"`
	LastName             string                                                           `json:"last_name"`
	PhoneNumber          string                                                           `json:"phone_number"`
	Email                string                                                           `json:"email"`
	Address              ListCustomersItemAddress                                         `json:"address"`
	Gender               string                                                           `json:"gender"`
	Dob                  *string                                                          `json:"dob"`
	IsPoliticallyExposed *bool                                                            `json:"is_politically_exposed,omitzero"`
	Tin                  string                                                           `json:"tin"`
	AccountRelationship  CreateEntityRequestAccountDataIndividualsItemAccountRelationship `json:"account_relationship"`
	Nationality          string                                                           `json:"nationality"`
	Verification         *CreateEntityRequestAccountDataCompanyVerification               `json:"verification,omitzero"`
}

type CreateEntityRequestAccountData struct {
	BusinessType string                                          `json:"business_type"`
	Mcc          *string                                         `json:"mcc,omitzero"`
	Company      CreateEntityRequestAccountDataCompany           `json:"company"`
	Individuals  []CreateEntityRequestAccountDataIndividualsItem `json:"individuals,omitzero"`
	Country      string                                          `json:"country"`
}

type CreateEntityRequestPayments struct {
	IsEnabled                   bool    `json:"is_enabled"`
	StatementDescriptor         *string `json:"statement_descriptor,omitzero"`
	AllowMultiplePaymentMethods *bool   `json:"allow_multiple_payment_methods,omitzero"`
}

type CreateEntityRequestTaxReportingServiceAgreement struct {
	IsAccepted bool   `json:"is_accepted"`
	AcceptedAt string `json:"accepted_at"`
	IPAddress  string `json:"ip_address"`
}

type CreateEntityRequestTaxReportingExchangeSettings struct {
	ApplyB2bExemptions *bool `json:"apply_b2b_exemptions,omitzero"`
	ApplyReverseCharge *bool `json:"apply_reverse_charge,omitzero"`
}

type CreateEntityRequestTaxReporting struct {
	IsEnabled         bool                                             `json:"is_enabled"`
	MerchantTaxNumber string                                           `json:"merchant_tax_number"`
	ServiceAgreement  CreateEntityRequestTaxReportingServiceAgreement  `json:"service_agreement"`
	ExchangeSettings  *CreateEntityRequestTaxReportingExchangeSettings `json:"exchange_settings,omitzero"`
}

type CreateEntityRequestSubscriptionsRenewalNotifications struct {
	IsEnabled  *bool   `json:"is_enabled,omitzero"`
	DaysBefore []int64 `json:"days_before,omitzero"`
}

type CreateEntityRequestSubscriptions struct {
	IsEnabled                    bool                                                  `json:"is_enabled"`
	RenewalNotifications         *CreateEntityRequestSubscriptionsRenewalNotifications `json:"renewal_notifications,omitzero"`
	IncompatibleAddonBehavior    conjoin.Nullable[string]                              `json:"incompatible_addon_behavior,omitzero"`
	CancellationFallbackBehavior conjoin.Nullable[string]                              `json:"cancellation_fallback_behavior,omitzero"`
}

type CreateEntityRequestInvoicingPaymentTerms struct {
	DueDays                *float64 `json:"due_days,omitzero"`
	IncludePaymentLink     *bool    `json:"include_payment_link,omitzero"`
	AllowScheduledPayments *bool    `json:"allow_scheduled_payments,omitzero"`
}

type CreateEntityRequestInvoicingInvoiceFinalisation struct {
	GracePeriodSeconds *float64 `json:"grace_period_seconds,omitzero"`
}

type CreateEntityRequestInvoicingSmartRetries struct {
	IsEnabled       *bool    `json:"is_enabled,omitzero"`
	Strategy        *string  `json:"strategy,omitzero"`
	MaxRetries      *float64 `json:"max_retries,omitzero"`
	MaxDurationDays *float64 `json:"max_duration_days,omitzero"`
}

type CreateEntityRequestInvoicingOverdueEmailReminders struct {
	IsEnabled    *bool     `json:"is_enabled,omitzero"`
	ReminderDays []float64 `json:"reminder_days,omitzero"`
}

type CreateEntityRequestInvoicing struct {
	IsEnabled               bool                                              `json:"is_enabled"`
	InvoiceNumberDelegation *string                                           `json:"invoice_number_delegation,omitzero"`
	AllowInvoicePdfDownload *bool                                             `json:"allow_invoice_pdf_download,omitzero"`
	DefaultMemo             *string                                           `json:"default_memo,omitzero"`
	DefaultFooterText       *string                                           `json:"default_footer_text,omitzero"`
	DefaultPaperSize        *string                                           `json:"default_paper_size,omitzero"`
	PaymentTerms            CreateEntityRequestInvoicingPaymentTerms          `json:"payment_terms"`
	InvoiceFinalisation     CreateEntityRequestInvoicingInvoiceFinalisation   `json:"invoice_finalisation"`
	SmartRetries            CreateEntityRequestInvoicingSmartRetries          `json:"smart_retries"`
	OverdueEmailReminders   CreateEntityRequestInvoicingOverdueEmailReminders `json:"overdue_email_reminders"`
}

type CreateEntityRequest struct {
	AccountData   CreateEntityRequestAccountData    `json:"account_data"`
	Payments      *CreateEntityRequestPayments      `json:"payments,omitzero"`
	TaxReporting  *CreateEntityRequestTaxReporting  `json:"tax_reporting,omitzero"`
	Subscriptions *CreateEntityRequestSubscriptions `json:"subscriptions,omitzero"`
	Invoicing     *CreateEntityRequestInvoicing     `json:"invoicing,omitzero"`
}

type CreateEntityResponse = ListEntitiesItem

type ListEntitiesCountQuery = ListEntitiesQuery

type ListEntitiesCountResponse = ListChargesCountResponse

type OnboardEntitiesRequestPaymentMarketsItem struct {
	Currency string `json:"currency"`
	Country  string `json:"country"`
}

type OnboardEntitiesRequest struct {
	BusinessType      string                                     `json:"business_type"`
	Country           string                                     `json:"country"`
	Company           CreateEntityRequestAccountDataCompany      `json:"company"`
	PaymentMarkets    []OnboardEntitiesRequestPaymentMarketsItem `json:"payment_markets"`
	StripeReturnURL   *string                                    `json:"stripe_return_url,omitzero"`
	StripeRefreshURL  *string                                    `json:"stripe_refresh_url,omitzero"`
	PaystackSecretKey *string                                    `json:"paystack_secret_key,omitzero"`
	PaystackPublicKey *string                                    `json:"paystack_public_key,omitzero"`
}

type OnboardEntitiesResponse = DeleteEntitlementOverrideResponse

type ReadEntityQuery struct {
	Expand *string `json:"expand,omitzero"`
}

type ReadEntityResponse = ListEntitiesItem

type UpdateEntityRequestDataAccountData struct {
	BusinessType *string                                         `json:"business_type,omitzero"`
	Mcc          *string                                         `json:"mcc,omitzero"`
	Company      *CreateEntityRequestAccountDataCompany          `json:"company,omitzero"`
	Individuals  []CreateEntityRequestAccountDataIndividualsItem `json:"individuals,omitzero"`
	Country      *string                                         `json:"country,omitzero"`
}

type UpdateEntityRequestDataPayoutsSchedule struct {
	Interval   string                    `json:"interval"`
	DayOfWeek  conjoin.Nullable[string]  `json:"day_of_week,omitzero"`
	DayOfMonth conjoin.Nullable[float64] `json:"day_of_month,omitzero"`
}

type UpdateEntityRequestDataPayouts struct {
	IsEnabled             *bool                                   `json:"is_enabled,omitzero"`
	DebitNegativeBalances *bool                                   `json:"debit_negative_balances,omitzero"`
	Schedule              *UpdateEntityRequestDataPayoutsSchedule `json:"schedule,omitzero"`
}

type UpdateEntityRequestData struct {
	AccountData            *UpdateEntityRequestDataAccountData `json:"account_data,omitzero"`
	AcceptServiceAgreement *bool                               `json:"accept_service_agreement,omitzero"`
	Payments               *CreateEntityRequestPayments        `json:"payments,omitzero"`
	TaxReporting           *CreateEntityRequestTaxReporting    `json:"tax_reporting,omitzero"`
	Subscriptions          *CreateEntityRequestSubscriptions   `json:"subscriptions,omitzero"`
	Invoicing              *CreateEntityRequestInvoicing       `json:"invoicing,omitzero"`
	Payouts                *UpdateEntityRequestDataPayouts     `json:"payouts,omitzero"`
}

type UpdateEntityRequest struct {
	Data UpdateEntityRequestData `json:"data"`
}

type UpdateEntityResponse = ListEntitiesItem

type CreatePayoutBankAccountRequestData struct {
	AccountNumber     string `json:"account_number"`
	RoutingNumber     string `json:"routing_number"`
	AccountHolderName string `json:"account_holder_name"`
	AccountHolderType string `json:"account_holder_type"`
	Country           string `json:"country"`
	Currency          string `json:"currency"`
}

type CreatePayoutBankAccountRequest struct {
	Data CreatePayoutBankAccountRequestData `json:"data"`
}

type CreatePayoutBankAccountResponse = ListEntitiesItem

type CreateEntityAccountLinkRequest struct {
	ReturnURL  string `json:"return_url"`
	RefreshURL string `json:"refresh_url"`
}

type CreateEntityAccountLinkResponse = DeleteEntitlementOverrideResponse

type SyncEntityOnboardingResponse = DeleteEntitlementOverrideResponse

type CreateEntityPaystackCredentialsRequest struct {
	SecretKey string `json:"secret_key"`
	PublicKey string `json:"public_key"`
}

type CreateEntityPaystackCredentialsResponse = DeleteEntitlementOverrideResponse
