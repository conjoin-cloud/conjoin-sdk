from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingInvoiceCreateRequest,
    BillingInvoiceCreateResponse,
    BillingInvoiceExportPdfResponse,
    BillingInvoiceFinalizeResponse,
    BillingInvoiceListCountQuery,
    BillingInvoiceListCountResponse,
    BillingInvoiceListItem,
    BillingInvoiceListQuery,
    BillingInvoicePayOutOfBandRequest,
    BillingInvoicePayOutOfBandResponse,
    BillingInvoicePayRequest,
    BillingInvoicePayResponse,
    BillingInvoiceSendResponse,
    BillingInvoiceUpdateRequest,
    BillingInvoiceUpdateResponse,
    BillingInvoiceVoidResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingInvoicesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingInvoiceListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingInvoiceListItem]:
        return self._client.request(
            'GET',
            'billing/invoices/',
            query=query,
            cast_to=Page[BillingInvoiceListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingInvoiceCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceCreateResponse:
        return self._client.request(
            'POST',
            'billing/invoices/',
            body=data,
            cast_to=BillingInvoiceCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingInvoiceListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceListCountResponse:
        return self._client.request(
            'GET',
            'billing/invoices/count',
            query=query,
            cast_to=BillingInvoiceListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def update(
        self,
        invoice_id: str,
        data: BillingInvoiceUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceUpdateResponse:
        return self._client.request(
            'PATCH',
            f'billing/invoices/{encode_path_param(invoice_id)}',
            body=data,
            cast_to=BillingInvoiceUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def finalize(
        self,
        invoice_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceFinalizeResponse:
        return self._client.request(
            'POST',
            f'billing/invoices/{encode_path_param(invoice_id)}/finalize',
            cast_to=BillingInvoiceFinalizeResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def pay(
        self,
        invoice_id: str,
        data: BillingInvoicePayRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoicePayResponse:
        return self._client.request(
            'POST',
            f'billing/invoices/{encode_path_param(invoice_id)}/pay',
            body=data,
            cast_to=BillingInvoicePayResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def void(
        self,
        invoice_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceVoidResponse:
        return self._client.request(
            'POST',
            f'billing/invoices/{encode_path_param(invoice_id)}/void',
            cast_to=BillingInvoiceVoidResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def pay_out_of_band(
        self,
        invoice_id: str,
        data: BillingInvoicePayOutOfBandRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoicePayOutOfBandResponse:
        return self._client.request(
            'POST',
            f'billing/invoices/{encode_path_param(invoice_id)}/pay-out-of-band',
            body=data,
            cast_to=BillingInvoicePayOutOfBandResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def send(
        self,
        invoice_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceSendResponse:
        return self._client.request(
            'POST',
            f'billing/invoices/{encode_path_param(invoice_id)}/send',
            cast_to=BillingInvoiceSendResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def export_pdf(
        self,
        invoice_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceExportPdfResponse:
        return self._client.request(
            'POST',
            f'billing/invoices/{encode_path_param(invoice_id)}/export',
            cast_to=BillingInvoiceExportPdfResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingInvoicesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingInvoiceListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingInvoiceListItem]:
        return await self._client.request(
            'GET',
            'billing/invoices/',
            query=query,
            cast_to=AsyncPage[BillingInvoiceListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingInvoiceCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceCreateResponse:
        return await self._client.request(
            'POST',
            'billing/invoices/',
            body=data,
            cast_to=BillingInvoiceCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingInvoiceListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceListCountResponse:
        return await self._client.request(
            'GET',
            'billing/invoices/count',
            query=query,
            cast_to=BillingInvoiceListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def update(
        self,
        invoice_id: str,
        data: BillingInvoiceUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'billing/invoices/{encode_path_param(invoice_id)}',
            body=data,
            cast_to=BillingInvoiceUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def finalize(
        self,
        invoice_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceFinalizeResponse:
        return await self._client.request(
            'POST',
            f'billing/invoices/{encode_path_param(invoice_id)}/finalize',
            cast_to=BillingInvoiceFinalizeResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def pay(
        self,
        invoice_id: str,
        data: BillingInvoicePayRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoicePayResponse:
        return await self._client.request(
            'POST',
            f'billing/invoices/{encode_path_param(invoice_id)}/pay',
            body=data,
            cast_to=BillingInvoicePayResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def void(
        self,
        invoice_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceVoidResponse:
        return await self._client.request(
            'POST',
            f'billing/invoices/{encode_path_param(invoice_id)}/void',
            cast_to=BillingInvoiceVoidResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def pay_out_of_band(
        self,
        invoice_id: str,
        data: BillingInvoicePayOutOfBandRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoicePayOutOfBandResponse:
        return await self._client.request(
            'POST',
            f'billing/invoices/{encode_path_param(invoice_id)}/pay-out-of-band',
            body=data,
            cast_to=BillingInvoicePayOutOfBandResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def send(
        self,
        invoice_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceSendResponse:
        return await self._client.request(
            'POST',
            f'billing/invoices/{encode_path_param(invoice_id)}/send',
            cast_to=BillingInvoiceSendResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def export_pdf(
        self,
        invoice_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingInvoiceExportPdfResponse:
        return await self._client.request(
            'POST',
            f'billing/invoices/{encode_path_param(invoice_id)}/export',
            cast_to=BillingInvoiceExportPdfResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
