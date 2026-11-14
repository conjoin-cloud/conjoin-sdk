from __future__ import annotations

from typing import TYPE_CHECKING

from conjoin_cloud.generated.ai._byok import (
    AsyncAiBYOKsResource,
    AiBYOKsResource,
)
from conjoin_cloud.generated.ai._context import (
    AsyncAiContextsResource,
    AiContextsResource,
)
from conjoin_cloud.generated.ai._inference import (
    AsyncAiInferencesResource,
    AiInferencesResource,
)
from conjoin_cloud.generated.ai._model import (
    AsyncAiModelsResource,
    AiModelsResource,
)
from conjoin_cloud.generated.ai._policy import (
    AsyncAiPoliciesResource,
    AiPoliciesResource,
)
from conjoin_cloud.generated.ai._usage import (
    AsyncAiUsagesResource,
    AiUsagesResource,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AiResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client
        self.byok = AiBYOKsResource(client)
        self.contexts = AiContextsResource(client)
        self.inferences = AiInferencesResource(client)
        self.models = AiModelsResource(client)
        self.policies = AiPoliciesResource(client)
        self.usages = AiUsagesResource(client)


class AsyncAiResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client
        self.byok = AsyncAiBYOKsResource(client)
        self.contexts = AsyncAiContextsResource(client)
        self.inferences = AsyncAiInferencesResource(client)
        self.models = AsyncAiModelsResource(client)
        self.policies = AsyncAiPoliciesResource(client)
        self.usages = AsyncAiUsagesResource(client)
