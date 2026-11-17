from __future__ import annotations

from typing import TYPE_CHECKING

from conjoin_cloud.generated.frontend.auth import AsyncAuthResource, AuthResource
from conjoin_cloud.generated.frontend.cloud import AsyncCloudResource, CloudResource

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class FrontendResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client
        self.auth = AuthResource(client)
        self.cloud = CloudResource(client)


class AsyncFrontendResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client
        self.auth = AsyncAuthResource(client)
        self.cloud = AsyncCloudResource(client)
