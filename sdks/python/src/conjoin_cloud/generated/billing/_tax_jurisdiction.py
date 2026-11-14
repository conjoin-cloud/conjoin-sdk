from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud.generated._models import (
    BillingTaxJurisdictionListCountQuery,
    BillingTaxJurisdictionListCountResponse,
    BillingTaxJurisdictionListItem,
    BillingTaxJurisdictionListQuery,
    BillingTaxJurisdictionQueryTaxRateQuery,
    BillingTaxJurisdictionQueryTaxRateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingTaxJurisdictionsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingTaxJurisdictionListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingTaxJurisdictionListItem]:
        return self._client.request(
            'GET',
            'billing/tax-jurisdictions/',
            query=query,
            cast_to=Page[BillingTaxJurisdictionListItem],
            request_options=request_options,
        )

    def list_count(
        self,
        query: BillingTaxJurisdictionListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingTaxJurisdictionListCountResponse:
        return self._client.request(
            'GET',
            'billing/tax-jurisdictions/count',
            query=query,
            cast_to=BillingTaxJurisdictionListCountResponse,
            request_options=request_options,
        )

    def query_tax_rate(
        self,
        query: BillingTaxJurisdictionQueryTaxRateQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingTaxJurisdictionQueryTaxRateResponse:
        return self._client.request(
            'GET',
            'billing/tax-jurisdictions/effective-rates',
            query=query,
            cast_to=BillingTaxJurisdictionQueryTaxRateResponse,
            request_options=request_options,
        )


class AsyncBillingTaxJurisdictionsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingTaxJurisdictionListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingTaxJurisdictionListItem]:
        return await self._client.request(
            'GET',
            'billing/tax-jurisdictions/',
            query=query,
            cast_to=AsyncPage[BillingTaxJurisdictionListItem],
            request_options=request_options,
        )

    async def list_count(
        self,
        query: BillingTaxJurisdictionListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingTaxJurisdictionListCountResponse:
        return await self._client.request(
            'GET',
            'billing/tax-jurisdictions/count',
            query=query,
            cast_to=BillingTaxJurisdictionListCountResponse,
            request_options=request_options,
        )

    async def query_tax_rate(
        self,
        query: BillingTaxJurisdictionQueryTaxRateQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingTaxJurisdictionQueryTaxRateResponse:
        return await self._client.request(
            'GET',
            'billing/tax-jurisdictions/effective-rates',
            query=query,
            cast_to=BillingTaxJurisdictionQueryTaxRateResponse,
            request_options=request_options,
        )
