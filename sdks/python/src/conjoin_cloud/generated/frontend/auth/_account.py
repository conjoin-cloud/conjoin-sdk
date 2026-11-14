from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import AUTH_NONE, RequestOptions
from conjoin_cloud.generated.frontend._models import (
    AuthAccountBatchLookupItem,
    AuthAccountBatchLookupRequest,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthAccountsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def batch_lookup(
        self,
        data: AuthAccountBatchLookupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> list[AuthAccountBatchLookupItem]:
        return self._client.request(
            'POST',
            'auth/client/account-lookups/',
            body=data,
            cast_to=list[AuthAccountBatchLookupItem],
            request_options=request_options,
            default_auth=AUTH_NONE,
        )


class AsyncAuthAccountsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def batch_lookup(
        self,
        data: AuthAccountBatchLookupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> list[AuthAccountBatchLookupItem]:
        return await self._client.request(
            'POST',
            'auth/client/account-lookups/',
            body=data,
            cast_to=list[AuthAccountBatchLookupItem],
            request_options=request_options,
            default_auth=AUTH_NONE,
        )
