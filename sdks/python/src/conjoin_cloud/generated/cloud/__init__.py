from __future__ import annotations

from typing import TYPE_CHECKING

from conjoin_cloud.generated.cloud._api_key import (
    AsyncCloudAPIKeysResource,
    CloudAPIKeysResource,
)
from conjoin_cloud.generated.cloud._account import (
    AsyncCloudAccountsResource,
    CloudAccountsResource,
)
from conjoin_cloud.generated.cloud._audit import (
    AsyncCloudAuditsResource,
    CloudAuditsResource,
)
from conjoin_cloud.generated.cloud._branding import (
    AsyncCloudBrandingsResource,
    CloudBrandingsResource,
)
from conjoin_cloud.generated.cloud._organization import (
    AsyncCloudOrganizationsResource,
    CloudOrganizationsResource,
)
from conjoin_cloud.generated.cloud._plan import (
    AsyncCloudPlansResource,
    CloudPlansResource,
)
from conjoin_cloud.generated.cloud._project import (
    AsyncCloudProjectsResource,
    CloudProjectsResource,
)
from conjoin_cloud.generated.cloud._publishable_key import (
    AsyncCloudPublishableKeysResource,
    CloudPublishableKeysResource,
)
from conjoin_cloud.generated.cloud._role import (
    AsyncCloudRolesResource,
    CloudRolesResource,
)
from conjoin_cloud.generated.cloud._sku_catalog import (
    AsyncCloudSKUCatalogsResource,
    CloudSKUCatalogsResource,
)
from conjoin_cloud.generated.cloud._spend_control import (
    AsyncCloudSpendControlsResource,
    CloudSpendControlsResource,
)
from conjoin_cloud.generated.cloud._webhook import (
    AsyncCloudWebhooksResource,
    CloudWebhooksResource,
)
from conjoin_cloud.generated.cloud._zone import (
    AsyncCloudZonesResource,
    CloudZonesResource,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client
        self.api_keys = CloudAPIKeysResource(client)
        self.accounts = CloudAccountsResource(client)
        self.audits = CloudAuditsResource(client)
        self.brandings = CloudBrandingsResource(client)
        self.organizations = CloudOrganizationsResource(client)
        self.plans = CloudPlansResource(client)
        self.projects = CloudProjectsResource(client)
        self.publishable_keys = CloudPublishableKeysResource(client)
        self.roles = CloudRolesResource(client)
        self.sku_catalogs = CloudSKUCatalogsResource(client)
        self.spend_controls = CloudSpendControlsResource(client)
        self.webhooks = CloudWebhooksResource(client)
        self.zones = CloudZonesResource(client)


class AsyncCloudResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client
        self.api_keys = AsyncCloudAPIKeysResource(client)
        self.accounts = AsyncCloudAccountsResource(client)
        self.audits = AsyncCloudAuditsResource(client)
        self.brandings = AsyncCloudBrandingsResource(client)
        self.organizations = AsyncCloudOrganizationsResource(client)
        self.plans = AsyncCloudPlansResource(client)
        self.projects = AsyncCloudProjectsResource(client)
        self.publishable_keys = AsyncCloudPublishableKeysResource(client)
        self.roles = AsyncCloudRolesResource(client)
        self.sku_catalogs = AsyncCloudSKUCatalogsResource(client)
        self.spend_controls = AsyncCloudSpendControlsResource(client)
        self.webhooks = AsyncCloudWebhooksResource(client)
        self.zones = AsyncCloudZonesResource(client)
