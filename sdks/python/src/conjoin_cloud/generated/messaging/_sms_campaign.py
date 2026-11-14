from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingSMSCampaignCreateSmsCampaignRequest,
    MessagingSMSCampaignCreateSmsCampaignResponse,
    MessagingSMSCampaignDeleteSmsCampaignResponse,
    MessagingSMSCampaignListSmsCampaignsItem,
    MessagingSMSCampaignListSmsCampaignsRequest,
    MessagingSMSCampaignReadSmsCampaignResponse,
    MessagingSMSCampaignUpdateSmsCampaignRequest,
    MessagingSMSCampaignUpdateSmsCampaignResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingSMSCampaignsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create_sms_campaign(
        self,
        data: MessagingSMSCampaignCreateSmsCampaignRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSCampaignCreateSmsCampaignResponse:
        return self._client.request(
            'POST',
            'messaging/sms/campaigns/',
            body=data,
            cast_to=MessagingSMSCampaignCreateSmsCampaignResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def read_sms_campaign(
        self,
        campaign_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSCampaignReadSmsCampaignResponse:
        return self._client.request(
            'GET',
            f'messaging/sms/campaigns/{encode_path_param(campaign_id)}',
            cast_to=MessagingSMSCampaignReadSmsCampaignResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def update_sms_campaign(
        self,
        campaign_id: str,
        data: MessagingSMSCampaignUpdateSmsCampaignRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSCampaignUpdateSmsCampaignResponse:
        return self._client.request(
            'PATCH',
            f'messaging/sms/campaigns/{encode_path_param(campaign_id)}',
            body=data,
            cast_to=MessagingSMSCampaignUpdateSmsCampaignResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_sms_campaign(
        self,
        campaign_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSCampaignDeleteSmsCampaignResponse:
        return self._client.request(
            'DELETE',
            f'messaging/sms/campaigns/{encode_path_param(campaign_id)}',
            cast_to=MessagingSMSCampaignDeleteSmsCampaignResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list_sms_campaigns(
        self,
        data: MessagingSMSCampaignListSmsCampaignsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingSMSCampaignListSmsCampaignsItem]:
        return self._client.request(
            'POST',
            'messaging/sms/campaigns/retrieve',
            body=data,
            cast_to=Page[MessagingSMSCampaignListSmsCampaignsItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingSMSCampaignsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create_sms_campaign(
        self,
        data: MessagingSMSCampaignCreateSmsCampaignRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSCampaignCreateSmsCampaignResponse:
        return await self._client.request(
            'POST',
            'messaging/sms/campaigns/',
            body=data,
            cast_to=MessagingSMSCampaignCreateSmsCampaignResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def read_sms_campaign(
        self,
        campaign_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSCampaignReadSmsCampaignResponse:
        return await self._client.request(
            'GET',
            f'messaging/sms/campaigns/{encode_path_param(campaign_id)}',
            cast_to=MessagingSMSCampaignReadSmsCampaignResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def update_sms_campaign(
        self,
        campaign_id: str,
        data: MessagingSMSCampaignUpdateSmsCampaignRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSCampaignUpdateSmsCampaignResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/sms/campaigns/{encode_path_param(campaign_id)}',
            body=data,
            cast_to=MessagingSMSCampaignUpdateSmsCampaignResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_sms_campaign(
        self,
        campaign_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSCampaignDeleteSmsCampaignResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/sms/campaigns/{encode_path_param(campaign_id)}',
            cast_to=MessagingSMSCampaignDeleteSmsCampaignResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list_sms_campaigns(
        self,
        data: MessagingSMSCampaignListSmsCampaignsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingSMSCampaignListSmsCampaignsItem]:
        return await self._client.request(
            'POST',
            'messaging/sms/campaigns/retrieve',
            body=data,
            cast_to=AsyncPage[MessagingSMSCampaignListSmsCampaignsItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
