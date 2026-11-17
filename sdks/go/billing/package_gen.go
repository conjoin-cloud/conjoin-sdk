package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type Client struct {
	Charges               *ChargesService
	Coupons               *CouponsService
	CreditNotes           *CreditNotesService
	CreditWallets         *CreditWalletsService
	Customers             *CustomersService
	Discounts             *DiscountsService
	Disputes              *DisputesService
	Entities              *EntitiesService
	EntitlementFeatures   *EntitlementFeaturesService
	EntitlementOverrides  *EntitlementOverridesService
	FeatureAccesses       *FeatureAccessesService
	Invoices              *InvoicesService
	PaymentIntents        *PaymentIntentsService
	PaymentMethods        *PaymentMethodsService
	PriceBundles          *PriceBundlesService
	Prices                *PricesService
	Products              *ProductsService
	Receipts              *ReceiptsService
	Refunds               *RefundsService
	Settings              *SettingsService
	SubscriptionSchedules *SubscriptionSchedulesService
	Subscriptions         *SubscriptionsService
	TaxJurisdictions      *TaxJurisdictionsService
}

func New(client *conjoin.Client) *Client {
	return &Client{
		Charges:               &ChargesService{client: client},
		Coupons:               &CouponsService{client: client},
		CreditNotes:           &CreditNotesService{client: client},
		CreditWallets:         &CreditWalletsService{client: client},
		Customers:             &CustomersService{client: client},
		Discounts:             &DiscountsService{client: client},
		Disputes:              &DisputesService{client: client},
		Entities:              &EntitiesService{client: client},
		EntitlementFeatures:   &EntitlementFeaturesService{client: client},
		EntitlementOverrides:  &EntitlementOverridesService{client: client},
		FeatureAccesses:       &FeatureAccessesService{client: client},
		Invoices:              &InvoicesService{client: client},
		PaymentIntents:        &PaymentIntentsService{client: client},
		PaymentMethods:        &PaymentMethodsService{client: client},
		PriceBundles:          &PriceBundlesService{client: client},
		Prices:                &PricesService{client: client},
		Products:              &ProductsService{client: client},
		Receipts:              &ReceiptsService{client: client},
		Refunds:               &RefundsService{client: client},
		Settings:              &SettingsService{client: client},
		SubscriptionSchedules: &SubscriptionSchedulesService{client: client},
		Subscriptions:         &SubscriptionsService{client: client},
		TaxJurisdictions:      &TaxJurisdictionsService{client: client},
	}
}
