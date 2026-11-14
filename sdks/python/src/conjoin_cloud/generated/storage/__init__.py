from __future__ import annotations

from typing import TYPE_CHECKING

from conjoin_cloud.generated.storage._container import (
    AsyncStorageContainersResource,
    StorageContainersResource,
)
from conjoin_cloud.generated.storage._object import (
    AsyncStorageObjectsResource,
    StorageObjectsResource,
)
from conjoin_cloud.generated.storage._object_acl import (
    AsyncStorageObjectACLsResource,
    StorageObjectACLsResource,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class StorageResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client
        self.containers = StorageContainersResource(client)
        self.objects = StorageObjectsResource(client)
        self.object_acls = StorageObjectACLsResource(client)


class AsyncStorageResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client
        self.containers = AsyncStorageContainersResource(client)
        self.objects = AsyncStorageObjectsResource(client)
        self.object_acls = AsyncStorageObjectACLsResource(client)
