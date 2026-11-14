package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type Client struct {
	ChannelAnalytics  *ChannelAnalyticsService
	ContactProperties *ContactPropertiesService
	Contacts          *ContactsService
	Conversations     *ConversationsService
	EmailSenderPools  *EmailSenderPoolsService
	EmailSenders      *EmailSendersService
	Emails            *EmailsService
	Multisends        *MultisendsService
	PhoneNumbers      *PhoneNumbersService
	Profiles          *ProfilesService
	SMSBrands         *SMSBrandsService
	SMSCampaigns      *SMSCampaignsService
	SMSSenderPools    *SMSSenderPoolsService
	SMSSenders        *SMSSendersService
	SMs               *SMsService
	Segments          *SegmentsService
	Templates         *TemplatesService
	Verifications     *VerificationsService
}

func New(client *conjoin.Client) *Client {
	return &Client{
		ChannelAnalytics:  &ChannelAnalyticsService{client: client},
		ContactProperties: &ContactPropertiesService{client: client},
		Contacts:          &ContactsService{client: client},
		Conversations:     &ConversationsService{client: client},
		EmailSenderPools:  &EmailSenderPoolsService{client: client},
		EmailSenders:      &EmailSendersService{client: client},
		Emails:            &EmailsService{client: client},
		Multisends:        &MultisendsService{client: client},
		PhoneNumbers:      &PhoneNumbersService{client: client},
		Profiles:          &ProfilesService{client: client},
		SMSBrands:         &SMSBrandsService{client: client},
		SMSCampaigns:      &SMSCampaignsService{client: client},
		SMSSenderPools:    &SMSSenderPoolsService{client: client},
		SMSSenders:        &SMSSendersService{client: client},
		SMs:               &SMsService{client: client},
		Segments:          &SegmentsService{client: client},
		Templates:         &TemplatesService{client: client},
		Verifications:     &VerificationsService{client: client},
	}
}
