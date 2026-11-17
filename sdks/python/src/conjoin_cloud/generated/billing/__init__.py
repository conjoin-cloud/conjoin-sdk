from __future__ import annotations

from typing import TYPE_CHECKING

from conjoin_cloud.generated.billing._charge import (
    AsyncBillingChargesResource,
    BillingChargesResource,
)
from conjoin_cloud.generated.billing._coupon import (
    AsyncBillingCouponsResource,
    BillingCouponsResource,
)
from conjoin_cloud.generated.billing._credit_note import (
    AsyncBillingCreditNotesResource,
    BillingCreditNotesResource,
)
from conjoin_cloud.generated.billing._credit_wallet import (
    AsyncBillingCreditWalletsResource,
    BillingCreditWalletsResource,
)
from conjoin_cloud.generated.billing._customer import (
    AsyncBillingCustomersResource,
    BillingCustomersResource,
)
from conjoin_cloud.generated.billing._discount import (
    AsyncBillingDiscountsResource,
    BillingDiscountsResource,
)
from conjoin_cloud.generated.billing._dispute import (
    AsyncBillingDisputesResource,
    BillingDisputesResource,
)
from conjoin_cloud.generated.billing._entitlement_feature import (
    AsyncBillingEntitlementFeaturesResource,
    BillingEntitlementFeaturesResource,
)
from conjoin_cloud.generated.billing._entitlement_override import (
    AsyncBillingEntitlementOverridesResource,
    BillingEntitlementOverridesResource,
)
from conjoin_cloud.generated.billing._entity import (
    AsyncBillingEntitiesResource,
    BillingEntitiesResource,
)
from conjoin_cloud.generated.billing._feature_access import (
    AsyncBillingFeatureAccessesResource,
    BillingFeatureAccessesResource,
)
from conjoin_cloud.generated.billing._invoice import (
    AsyncBillingInvoicesResource,
    BillingInvoicesResource,
)
from conjoin_cloud.generated.billing._payment_intent import (
    AsyncBillingPaymentIntentsResource,
    BillingPaymentIntentsResource,
)
from conjoin_cloud.generated.billing._payment_method import (
    AsyncBillingPaymentMethodsResource,
    BillingPaymentMethodsResource,
)
from conjoin_cloud.generated.billing._price import (
    AsyncBillingPricesResource,
    BillingPricesResource,
)
from conjoin_cloud.generated.billing._price_bundle import (
    AsyncBillingPriceBundlesResource,
    BillingPriceBundlesResource,
)
from conjoin_cloud.generated.billing._product import (
    AsyncBillingProductsResource,
    BillingProductsResource,
)
from conjoin_cloud.generated.billing._receipt import (
    AsyncBillingReceiptsResource,
    BillingReceiptsResource,
)
from conjoin_cloud.generated.billing._refund import (
    AsyncBillingRefundsResource,
    BillingRefundsResource,
)
from conjoin_cloud.generated.billing._settings import (
    AsyncBillingSettingsResource,
    BillingSettingsResource,
)
from conjoin_cloud.generated.billing._subscription import (
    AsyncBillingSubscriptionsResource,
    BillingSubscriptionsResource,
)
from conjoin_cloud.generated.billing._subscription_schedule import (
    AsyncBillingSubscriptionSchedulesResource,
    BillingSubscriptionSchedulesResource,
)
from conjoin_cloud.generated.billing._tax_jurisdiction import (
    AsyncBillingTaxJurisdictionsResource,
    BillingTaxJurisdictionsResource,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client
        self.charges = BillingChargesResource(client)
        self.coupons = BillingCouponsResource(client)
        self.credit_notes = BillingCreditNotesResource(client)
        self.credit_wallets = BillingCreditWalletsResource(client)
        self.customers = BillingCustomersResource(client)
        self.discounts = BillingDiscountsResource(client)
        self.disputes = BillingDisputesResource(client)
        self.entitlement_features = BillingEntitlementFeaturesResource(client)
        self.entitlement_overrides = BillingEntitlementOverridesResource(client)
        self.entities = BillingEntitiesResource(client)
        self.feature_accesses = BillingFeatureAccessesResource(client)
        self.invoices = BillingInvoicesResource(client)
        self.payment_intents = BillingPaymentIntentsResource(client)
        self.payment_methods = BillingPaymentMethodsResource(client)
        self.prices = BillingPricesResource(client)
        self.price_bundles = BillingPriceBundlesResource(client)
        self.products = BillingProductsResource(client)
        self.receipts = BillingReceiptsResource(client)
        self.refunds = BillingRefundsResource(client)
        self.settings = BillingSettingsResource(client)
        self.subscriptions = BillingSubscriptionsResource(client)
        self.subscription_schedules = BillingSubscriptionSchedulesResource(client)
        self.tax_jurisdictions = BillingTaxJurisdictionsResource(client)


class AsyncBillingResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client
        self.charges = AsyncBillingChargesResource(client)
        self.coupons = AsyncBillingCouponsResource(client)
        self.credit_notes = AsyncBillingCreditNotesResource(client)
        self.credit_wallets = AsyncBillingCreditWalletsResource(client)
        self.customers = AsyncBillingCustomersResource(client)
        self.discounts = AsyncBillingDiscountsResource(client)
        self.disputes = AsyncBillingDisputesResource(client)
        self.entitlement_features = AsyncBillingEntitlementFeaturesResource(client)
        self.entitlement_overrides = AsyncBillingEntitlementOverridesResource(client)
        self.entities = AsyncBillingEntitiesResource(client)
        self.feature_accesses = AsyncBillingFeatureAccessesResource(client)
        self.invoices = AsyncBillingInvoicesResource(client)
        self.payment_intents = AsyncBillingPaymentIntentsResource(client)
        self.payment_methods = AsyncBillingPaymentMethodsResource(client)
        self.prices = AsyncBillingPricesResource(client)
        self.price_bundles = AsyncBillingPriceBundlesResource(client)
        self.products = AsyncBillingProductsResource(client)
        self.receipts = AsyncBillingReceiptsResource(client)
        self.refunds = AsyncBillingRefundsResource(client)
        self.settings = AsyncBillingSettingsResource(client)
        self.subscriptions = AsyncBillingSubscriptionsResource(client)
        self.subscription_schedules = AsyncBillingSubscriptionSchedulesResource(client)
        self.tax_jurisdictions = AsyncBillingTaxJurisdictionsResource(client)
