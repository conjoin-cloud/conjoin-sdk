from __future__ import annotations

from typing import TYPE_CHECKING

from conjoin_cloud.generated.frontend.billing._self import (
    AsyncBillingSelvesResource,
    BillingSelvesResource,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client
        self.selves = BillingSelvesResource(client)


class AsyncBillingResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client
        self.selves = AsyncBillingSelvesResource(client)
