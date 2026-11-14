import type { ConjoinClient } from '../core/types'
import { createMessagingChannelAnalytics } from '../generated/modules/messaging-channel-analytics'
import { createMessagingContacts } from '../generated/modules/messaging-contact'
import { createMessagingContactProperties } from '../generated/modules/messaging-contact-properties'
import { createMessagingConversations } from '../generated/modules/messaging-conversation'
import { createMessagingEmails } from '../generated/modules/messaging-email'
import { createMessagingEmailSenders } from '../generated/modules/messaging-email-sender'
import { createMessagingEmailSenderPools } from '../generated/modules/messaging-email-sender-pool'
import { createMessagingMultisends } from '../generated/modules/messaging-multisend'
import { createMessagingPhoneNumbers } from '../generated/modules/messaging-phone-number'
import { createMessagingProfiles } from '../generated/modules/messaging-profile'
import { createMessagingSegments } from '../generated/modules/messaging-segment'
import { createMessagingSMs } from '../generated/modules/messaging-sms'
import { createMessagingSMSBrands } from '../generated/modules/messaging-sms-brand'
import { createMessagingSMSCampaigns } from '../generated/modules/messaging-sms-campaign'
import { createMessagingSMSSenders } from '../generated/modules/messaging-sms-sender'
import { createMessagingSMSSenderPools } from '../generated/modules/messaging-sms-sender-pool'
import { createMessagingTemplates } from '../generated/modules/messaging-template'
import { createMessagingVerifications } from '../generated/modules/messaging-verification'

export * from '../generated/modules/messaging-index'

export type MessagingConfig = {
  profileId?: string
}

export function createMessaging(client: ConjoinClient, config: MessagingConfig = {}) {
  const profiled = config.profileId === undefined ? client : client.withScope({ messagingProfileId: config.profileId })

  return {
    emails: createMessagingEmails(profiled),
    sms: createMessagingSMs(profiled),
    multisend: createMessagingMultisends(profiled),
    contacts: createMessagingContacts(profiled),
    contactProperties: createMessagingContactProperties(profiled),
    conversations: createMessagingConversations(profiled),
    segments: createMessagingSegments(profiled),
    templates: createMessagingTemplates(profiled),
    verifications: createMessagingVerifications(profiled),
    analytics: createMessagingChannelAnalytics(profiled),
    emailSenders: createMessagingEmailSenders(profiled),
    emailSenderPools: createMessagingEmailSenderPools(profiled),
    smsSenders: createMessagingSMSSenders(profiled),
    smsSenderPools: createMessagingSMSSenderPools(profiled),
    smsBrands: createMessagingSMSBrands(profiled),
    smsCampaigns: createMessagingSMSCampaigns(profiled),
    phoneNumbers: createMessagingPhoneNumbers(profiled),
    profiles: createMessagingProfiles(profiled),
  }
}
