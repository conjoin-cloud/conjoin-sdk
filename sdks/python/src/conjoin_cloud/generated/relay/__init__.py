from __future__ import annotations

from typing import TYPE_CHECKING

from conjoin_cloud.generated.relay._broadcast import (
    AsyncRelayBroadcastsResource,
    RelayBroadcastsResource,
)
from conjoin_cloud.generated.relay._events import (
    AsyncRelayEventsResource,
    RelayEventsResource,
)
from conjoin_cloud.generated.relay._memorystore import (
    AsyncRelayMemorystoresResource,
    RelayMemorystoresResource,
)
from conjoin_cloud.generated.relay._pipelines import (
    AsyncRelayPipelinesResource,
    RelayPipelinesResource,
)
from conjoin_cloud.generated.relay._queues import (
    AsyncRelayQueuesResource,
    RelayQueuesResource,
)
from conjoin_cloud.generated.relay._scheduler import (
    AsyncRelaySchedulersResource,
    RelaySchedulersResource,
)
from conjoin_cloud.generated.relay._search import (
    AsyncRelaySearchesResource,
    RelaySearchesResource,
)
from conjoin_cloud.generated.relay._settings import (
    AsyncRelaySettingsResource,
    RelaySettingsResource,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class RelayResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client
        self.broadcasts = RelayBroadcastsResource(client)
        self.events = RelayEventsResource(client)
        self.memorystores = RelayMemorystoresResource(client)
        self.pipelines = RelayPipelinesResource(client)
        self.queues = RelayQueuesResource(client)
        self.schedulers = RelaySchedulersResource(client)
        self.searches = RelaySearchesResource(client)
        self.settings = RelaySettingsResource(client)


class AsyncRelayResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client
        self.broadcasts = AsyncRelayBroadcastsResource(client)
        self.events = AsyncRelayEventsResource(client)
        self.memorystores = AsyncRelayMemorystoresResource(client)
        self.pipelines = AsyncRelayPipelinesResource(client)
        self.queues = AsyncRelayQueuesResource(client)
        self.schedulers = AsyncRelaySchedulersResource(client)
        self.searches = AsyncRelaySearchesResource(client)
        self.settings = AsyncRelaySettingsResource(client)
