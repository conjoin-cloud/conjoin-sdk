from __future__ import annotations

from typing import TYPE_CHECKING

from conjoin_cloud.generated.messaging._channel_analytics import (
    AsyncMessagingChannelAnalyticsResource,
    MessagingChannelAnalyticsResource,
)
from conjoin_cloud.generated.messaging._contact import (
    AsyncMessagingContactsResource,
    MessagingContactsResource,
)
from conjoin_cloud.generated.messaging._contact_properties import (
    AsyncMessagingContactPropertiesResource,
    MessagingContactPropertiesResource,
)
from conjoin_cloud.generated.messaging._conversation import (
    AsyncMessagingConversationsResource,
    MessagingConversationsResource,
)
from conjoin_cloud.generated.messaging._email import (
    AsyncMessagingEmailsResource,
    MessagingEmailsResource,
)
from conjoin_cloud.generated.messaging._email_sender import (
    AsyncMessagingEmailSendersResource,
    MessagingEmailSendersResource,
)
from conjoin_cloud.generated.messaging._email_sender_pool import (
    AsyncMessagingEmailSenderPoolsResource,
    MessagingEmailSenderPoolsResource,
)
from conjoin_cloud.generated.messaging._multisend import (
    AsyncMessagingMultisendsResource,
    MessagingMultisendsResource,
)
from conjoin_cloud.generated.messaging._phone_number import (
    AsyncMessagingPhoneNumbersResource,
    MessagingPhoneNumbersResource,
)
from conjoin_cloud.generated.messaging._profile import (
    AsyncMessagingProfilesResource,
    MessagingProfilesResource,
)
from conjoin_cloud.generated.messaging._sms import (
    AsyncMessagingSMsResource,
    MessagingSMsResource,
)
from conjoin_cloud.generated.messaging._sms_brand import (
    AsyncMessagingSMSBrandsResource,
    MessagingSMSBrandsResource,
)
from conjoin_cloud.generated.messaging._sms_campaign import (
    AsyncMessagingSMSCampaignsResource,
    MessagingSMSCampaignsResource,
)
from conjoin_cloud.generated.messaging._sms_sender import (
    AsyncMessagingSMSSendersResource,
    MessagingSMSSendersResource,
)
from conjoin_cloud.generated.messaging._sms_sender_pool import (
    AsyncMessagingSMSSenderPoolsResource,
    MessagingSMSSenderPoolsResource,
)
from conjoin_cloud.generated.messaging._segment import (
    AsyncMessagingSegmentsResource,
    MessagingSegmentsResource,
)
from conjoin_cloud.generated.messaging._template import (
    AsyncMessagingTemplatesResource,
    MessagingTemplatesResource,
)
from conjoin_cloud.generated.messaging._verification import (
    AsyncMessagingVerificationsResource,
    MessagingVerificationsResource,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client
        self.channel_analytics = MessagingChannelAnalyticsResource(client)
        self.contacts = MessagingContactsResource(client)
        self.contact_properties = MessagingContactPropertiesResource(client)
        self.conversations = MessagingConversationsResource(client)
        self.emails = MessagingEmailsResource(client)
        self.email_senders = MessagingEmailSendersResource(client)
        self.email_sender_pools = MessagingEmailSenderPoolsResource(client)
        self.multisends = MessagingMultisendsResource(client)
        self.phone_numbers = MessagingPhoneNumbersResource(client)
        self.profiles = MessagingProfilesResource(client)
        self.sms = MessagingSMsResource(client)
        self.sms_brands = MessagingSMSBrandsResource(client)
        self.sms_campaigns = MessagingSMSCampaignsResource(client)
        self.sms_senders = MessagingSMSSendersResource(client)
        self.sms_sender_pools = MessagingSMSSenderPoolsResource(client)
        self.segments = MessagingSegmentsResource(client)
        self.templates = MessagingTemplatesResource(client)
        self.verifications = MessagingVerificationsResource(client)


class AsyncMessagingResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client
        self.channel_analytics = AsyncMessagingChannelAnalyticsResource(client)
        self.contacts = AsyncMessagingContactsResource(client)
        self.contact_properties = AsyncMessagingContactPropertiesResource(client)
        self.conversations = AsyncMessagingConversationsResource(client)
        self.emails = AsyncMessagingEmailsResource(client)
        self.email_senders = AsyncMessagingEmailSendersResource(client)
        self.email_sender_pools = AsyncMessagingEmailSenderPoolsResource(client)
        self.multisends = AsyncMessagingMultisendsResource(client)
        self.phone_numbers = AsyncMessagingPhoneNumbersResource(client)
        self.profiles = AsyncMessagingProfilesResource(client)
        self.sms = AsyncMessagingSMsResource(client)
        self.sms_brands = AsyncMessagingSMSBrandsResource(client)
        self.sms_campaigns = AsyncMessagingSMSCampaignsResource(client)
        self.sms_senders = AsyncMessagingSMSSendersResource(client)
        self.sms_sender_pools = AsyncMessagingSMSSenderPoolsResource(client)
        self.segments = AsyncMessagingSegmentsResource(client)
        self.templates = AsyncMessagingTemplatesResource(client)
        self.verifications = AsyncMessagingVerificationsResource(client)
