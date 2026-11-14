package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type VerifyEmailSenderResponseMessageQuotas struct {
	MessagesPerSecond float64 `json:"messages_per_second"`
}

type VerifyEmailSenderResponseQueueDetails struct {
	QueueID                 string  `json:"queue_id"`
	Name                    string  `json:"name"`
	RateLimitPerMinute      float64 `json:"rate_limit_per_minute"`
	MaxConcurrentDeliveries float64 `json:"max_concurrent_deliveries"`
}

type VerifyEmailSenderResponse struct {
	SenderID         string                                                  `json:"sender_id"`
	ProfileID        string                                                  `json:"profile_id"`
	ConjoinAccountID string                                                  `json:"conjoin_account_id"`
	ConjoinProjectID string                                                  `json:"conjoin_project_id"`
	LiveMode         bool                                                    `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string]                                `json:"reference_id,omitzero"`
	Sender           string                                                  `json:"sender"`
	Capability       string                                                  `json:"capability"`
	SenderType       string                                                  `json:"sender_type"`
	TrackingDetails  map[string]any                                          `json:"tracking_details,omitzero"`
	IsDefaultSender  *bool                                                   `json:"is_default_sender,omitzero"`
	IsTestSender     *bool                                                   `json:"is_test_sender,omitzero"`
	DNSRecords       []map[string]any                                        `json:"dns_records,omitzero"`
	MessageQuotas    VerifyEmailSenderResponseMessageQuotas                  `json:"message_quotas"`
	QueueDetails     conjoin.Nullable[VerifyEmailSenderResponseQueueDetails] `json:"queue_details,omitzero"`
	SubmittedAt      string                                                  `json:"submitted_at"`
	ProvisionedAt    conjoin.Nullable[string]                                `json:"provisioned_at,omitzero"`
	Status           string                                                  `json:"status"`
	DateCreated      string                                                  `json:"date_created"`
	DateUpdated      string                                                  `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]                                `json:"date_deleted,omitzero"`
}

type ListManyEmailSendersRequestQuery struct {
	SenderID        any   `json:"sender_id,omitzero"`
	IsDefaultSender *bool `json:"is_default_sender,omitzero"`
	IsTestSender    *bool `json:"is_test_sender,omitzero"`
	Status          any   `json:"status,omitzero"`
}

type ListManyEmailSendersRequest struct {
	Cursor *ListContactsRequestCursor        `json:"cursor,omitzero"`
	Filter map[string]bool                   `json:"filter,omitzero"`
	Query  *ListManyEmailSendersRequestQuery `json:"query,omitzero"`
	Search *ListContactsRequestSearch        `json:"search,omitzero"`
	Sort   map[string]string                 `json:"sort,omitzero"`
	Limit  any                               `json:"limit,omitzero"`
}

type ListManyEmailSendersItem = VerifyEmailSenderResponse

type ListOneEmailSenderResponse = VerifyEmailSenderResponse

type DeleteEmailSenderResponse = VerifyEmailSenderResponse

type CreateEmailSenderRequestTrackingOpens struct {
	Track          *bool `json:"track,omitzero"`
	TrackingDomain any   `json:"tracking_domain"`
}

type CreateEmailSenderRequestTrackingUnsubscribes struct {
	Track          *bool  `json:"track,omitzero"`
	TrackingDomain any    `json:"tracking_domain"`
	TrackingURL    string `json:"tracking_url"`
	RedirectURL    string `json:"redirect_url"`
}

type CreateEmailSenderRequestTracking struct {
	Opens        *CreateEmailSenderRequestTrackingOpens        `json:"opens,omitzero"`
	Clicks       *CreateEmailSenderRequestTrackingOpens        `json:"clicks,omitzero"`
	Unsubscribes *CreateEmailSenderRequestTrackingUnsubscribes `json:"unsubscribes,omitzero"`
}

type CreateEmailSenderRequest struct {
	SenderType      *string                           `json:"sender_type,omitzero"`
	Sender          any                               `json:"sender,omitzero"`
	Tracking        *CreateEmailSenderRequestTracking `json:"tracking,omitzero"`
	CreateZone      *bool                             `json:"create_zone,omitzero"`
	Capability      string                            `json:"capability"`
	IsDefaultSender *bool                             `json:"is_default_sender,omitzero"`
	IsTestSender    *bool                             `json:"is_test_sender,omitzero"`
}

type CreateEmailSenderResponse = VerifyEmailSenderResponse

type EnableEmailSenderRequestParams struct {
	SenderID string `json:"sender_id"`
}

type EnableEmailSenderRequest struct {
	Params EnableEmailSenderRequestParams `json:"params"`
}

type EnableEmailSenderResponse = VerifyEmailSenderResponse

type DisableEmailSenderRequest = EnableEmailSenderRequest

type DisableEmailSenderResponse = VerifyEmailSenderResponse

type TransferEmailSenderResponse = VerifyEmailSenderResponse
