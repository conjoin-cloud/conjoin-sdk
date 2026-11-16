from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingEntityCreateAccountLinkRequest,
    BillingEntityCreateAccountLinkResponse,
    BillingEntityCreatePayoutBankAccountRequest,
    BillingEntityCreatePayoutBankAccountResponse,
    BillingEntityCreatePaystackCredentialsRequest,
    BillingEntityCreatePaystackCredentialsResponse,
    BillingEntityCreateRequest,
    BillingEntityCreateResponse,
    BillingEntityListCountQuery,
    BillingEntityListCountResponse,
    BillingEntityListItem,
    BillingEntityListQuery,
    BillingEntityOnboardRequest,
    BillingEntityOnboardResponse,
    BillingEntityReadQuery,
    BillingEntityReadResponse,
    BillingEntitySyncOnboardingResponse,
    BillingEntityUpdateRequest,
    BillingEntityUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingEntitiesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingEntityListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingEntityListItem]:
        return self._client.request(
            'GET',
            'billing/entities/',
            query=query,
            cast_to=Page[BillingEntityListItem],
            request_options=request_options,
        )

    def create(
        self,
        data: BillingEntityCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityCreateResponse:
        return self._client.request(
            'POST',
            'billing/entities/',
            body=data,
            cast_to=BillingEntityCreateResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: BillingEntityListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityListCountResponse:
        return self._client.request(
            'GET',
            'billing/entities/count',
            query=query,
            cast_to=BillingEntityListCountResponse,
            request_options=request_options,
        )

    def onboard(
        self,
        data: BillingEntityOnboardRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityOnboardResponse:
        return self._client.request(
            'POST',
            'billing/entities/onboard',
            body=data,
            cast_to=BillingEntityOnboardResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
            unwrap_data=False,
        )

    def read(
        self,
        entity_id: str,
        query: BillingEntityReadQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityReadResponse:
        return self._client.request(
            'GET',
            f'billing/entities/{encode_path_param(entity_id)}',
            query=query,
            cast_to=BillingEntityReadResponse,
            request_options=request_options,
        )

    def update(
        self,
        entity_id: str,
        data: BillingEntityUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityUpdateResponse:
        return self._client.request(
            'PATCH',
            f'billing/entities/{encode_path_param(entity_id)}',
            body=data,
            cast_to=BillingEntityUpdateResponse,
            request_options=request_options,
        )

    def create_payout_bank_account(
        self,
        entity_id: str,
        data: BillingEntityCreatePayoutBankAccountRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityCreatePayoutBankAccountResponse:
        return self._client.request(
            'POST',
            f'billing/entities/{encode_path_param(entity_id)}/payout-bank-accounts',
            body=data,
            cast_to=BillingEntityCreatePayoutBankAccountResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def create_account_link(
        self,
        entity_id: str,
        data: BillingEntityCreateAccountLinkRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityCreateAccountLinkResponse:
        return self._client.request(
            'POST',
            f'billing/entities/{encode_path_param(entity_id)}/account-links',
            body=data,
            cast_to=BillingEntityCreateAccountLinkResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
            unwrap_data=False,
        )

    def sync_onboarding(
        self,
        entity_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitySyncOnboardingResponse:
        return self._client.request(
            'POST',
            f'billing/entities/{encode_path_param(entity_id)}/sync',
            cast_to=BillingEntitySyncOnboardingResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
            unwrap_data=False,
        )

    def create_paystack_credentials(
        self,
        entity_id: str,
        data: BillingEntityCreatePaystackCredentialsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityCreatePaystackCredentialsResponse:
        return self._client.request(
            'POST',
            f'billing/entities/{encode_path_param(entity_id)}/paystack-credentials',
            body=data,
            cast_to=BillingEntityCreatePaystackCredentialsResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
            unwrap_data=False,
        )


class AsyncBillingEntitiesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingEntityListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingEntityListItem]:
        return await self._client.request(
            'GET',
            'billing/entities/',
            query=query,
            cast_to=AsyncPage[BillingEntityListItem],
            request_options=request_options,
        )

    async def create(
        self,
        data: BillingEntityCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityCreateResponse:
        return await self._client.request(
            'POST',
            'billing/entities/',
            body=data,
            cast_to=BillingEntityCreateResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: BillingEntityListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityListCountResponse:
        return await self._client.request(
            'GET',
            'billing/entities/count',
            query=query,
            cast_to=BillingEntityListCountResponse,
            request_options=request_options,
        )

    async def onboard(
        self,
        data: BillingEntityOnboardRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityOnboardResponse:
        return await self._client.request(
            'POST',
            'billing/entities/onboard',
            body=data,
            cast_to=BillingEntityOnboardResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
            unwrap_data=False,
        )

    async def read(
        self,
        entity_id: str,
        query: BillingEntityReadQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityReadResponse:
        return await self._client.request(
            'GET',
            f'billing/entities/{encode_path_param(entity_id)}',
            query=query,
            cast_to=BillingEntityReadResponse,
            request_options=request_options,
        )

    async def update(
        self,
        entity_id: str,
        data: BillingEntityUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'billing/entities/{encode_path_param(entity_id)}',
            body=data,
            cast_to=BillingEntityUpdateResponse,
            request_options=request_options,
        )

    async def create_payout_bank_account(
        self,
        entity_id: str,
        data: BillingEntityCreatePayoutBankAccountRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityCreatePayoutBankAccountResponse:
        return await self._client.request(
            'POST',
            f'billing/entities/{encode_path_param(entity_id)}/payout-bank-accounts',
            body=data,
            cast_to=BillingEntityCreatePayoutBankAccountResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def create_account_link(
        self,
        entity_id: str,
        data: BillingEntityCreateAccountLinkRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityCreateAccountLinkResponse:
        return await self._client.request(
            'POST',
            f'billing/entities/{encode_path_param(entity_id)}/account-links',
            body=data,
            cast_to=BillingEntityCreateAccountLinkResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
            unwrap_data=False,
        )

    async def sync_onboarding(
        self,
        entity_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitySyncOnboardingResponse:
        return await self._client.request(
            'POST',
            f'billing/entities/{encode_path_param(entity_id)}/sync',
            cast_to=BillingEntitySyncOnboardingResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
            unwrap_data=False,
        )

    async def create_paystack_credentials(
        self,
        entity_id: str,
        data: BillingEntityCreatePaystackCredentialsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntityCreatePaystackCredentialsResponse:
        return await self._client.request(
            'POST',
            f'billing/entities/{encode_path_param(entity_id)}/paystack-credentials',
            body=data,
            cast_to=BillingEntityCreatePaystackCredentialsResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
            unwrap_data=False,
        )
