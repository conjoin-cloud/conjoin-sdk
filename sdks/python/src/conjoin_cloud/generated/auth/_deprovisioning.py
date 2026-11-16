from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthDeprovisioningDeprovisionAccountRequest,
    AuthDeprovisioningDeprovisionAccountResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthDeprovisioningsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def deprovision_account(
        self,
        account_id: str,
        data: AuthDeprovisioningDeprovisionAccountRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthDeprovisioningDeprovisionAccountResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/deprovision',
            body=data,
            cast_to=AuthDeprovisioningDeprovisionAccountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )


class AsyncAuthDeprovisioningsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def deprovision_account(
        self,
        account_id: str,
        data: AuthDeprovisioningDeprovisionAccountRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthDeprovisioningDeprovisionAccountResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/deprovision',
            body=data,
            cast_to=AuthDeprovisioningDeprovisionAccountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )
