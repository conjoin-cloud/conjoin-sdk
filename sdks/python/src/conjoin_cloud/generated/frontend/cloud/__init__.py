from __future__ import annotations

from typing import TYPE_CHECKING

from conjoin_cloud.generated.frontend.cloud._branding import (
    AsyncCloudBrandingsResource,
    CloudBrandingsResource,
)
from conjoin_cloud.generated.frontend.cloud._sdk import (
    AsyncCloudSDKsResource,
    CloudSDKsResource,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client
        self.brandings = CloudBrandingsResource(client)
        self.sd_ks = CloudSDKsResource(client)


class AsyncCloudResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client
        self.brandings = AsyncCloudBrandingsResource(client)
        self.sd_ks = AsyncCloudSDKsResource(client)
