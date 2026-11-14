package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListChannelAnalyticsItemClicks struct {
	UniqueClicks float64 `json:"unique_clicks"`
	TotalClicks  float64 `json:"total_clicks"`
}

type ListChannelAnalyticsItemOpens struct {
	UniqueOpens float64 `json:"unique_opens"`
	TotalOpens  float64 `json:"total_opens"`
}

type ListChannelAnalyticsItemDeliveries struct {
	TotalDeliveries float64 `json:"total_deliveries"`
}

type ListChannelAnalyticsItemComplaints struct {
	TotalComplaints float64 `json:"total_complaints"`
}

type ListChannelAnalyticsItemRejections struct {
	TotalRejections float64 `json:"total_rejections"`
}

type ListChannelAnalyticsItemBounces struct {
	TotalBounces float64 `json:"total_bounces"`
}

type ListChannelAnalyticsItemFailures struct {
	TotalFailures float64 `json:"total_failures"`
}

type ListChannelAnalyticsItemSubscribes struct {
	TotalSubscribes float64 `json:"total_subscribes"`
}

type ListChannelAnalyticsItemUnsubscribes struct {
	TotalUnsubscribes float64 `json:"total_unsubscribes"`
}

type ListChannelAnalyticsItem struct {
	ProfileID         string                               `json:"profile_id"`
	ConjoinAccountID  string                               `json:"conjoin_account_id"`
	ConjoinProjectID  string                               `json:"conjoin_project_id"`
	LiveMode          bool                                 `json:"live_mode"`
	AnalyticsID       string                               `json:"analytics_id"`
	ConversationID    *string                              `json:"conversation_id"`
	MessageRequestID  string                               `json:"message_request_id"`
	ChannelID         string                               `json:"channel_id"`
	TotalMessageCount float64                              `json:"total_message_count"`
	Clicks            ListChannelAnalyticsItemClicks       `json:"clicks"`
	Opens             ListChannelAnalyticsItemOpens        `json:"opens"`
	Deliveries        ListChannelAnalyticsItemDeliveries   `json:"deliveries"`
	Complaints        ListChannelAnalyticsItemComplaints   `json:"complaints"`
	Rejections        ListChannelAnalyticsItemRejections   `json:"rejections"`
	Bounces           ListChannelAnalyticsItemBounces      `json:"bounces"`
	Failures          ListChannelAnalyticsItemFailures     `json:"failures"`
	Subscribes        ListChannelAnalyticsItemSubscribes   `json:"subscribes"`
	Unsubscribes      ListChannelAnalyticsItemUnsubscribes `json:"unsubscribes"`
	DateCreated       string                               `json:"date_created"`
	DateUpdated       string                               `json:"date_updated"`
	DateDeleted       conjoin.Nullable[string]             `json:"date_deleted,omitzero"`
}

type GenerateChannelAnalyticsSummariesResponse = ListChannelAnalyticsItem

type CreateChannelAnalyticsReportResponse = ListChannelAnalyticsItem
