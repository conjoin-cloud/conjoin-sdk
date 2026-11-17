package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListChannelAnalyticsQueryDateCreated struct {
	Equals    *string `json:"equals,omitzero"`
	NotEquals *string `json:"not_equals,omitzero"`
	Gt        *string `json:"gt,omitzero"`
	Lt        *string `json:"lt,omitzero"`
	Gte       *string `json:"gte,omitzero"`
	Lte       *string `json:"lte,omitzero"`
}

type ListChannelAnalyticsQueryCursor struct {
	Prev *string `json:"prev,omitzero"`
	Next *string `json:"next,omitzero"`
}

type ListChannelAnalyticsQuery struct {
	ReferenceID      any                                   `json:"reference_id,omitzero"`
	MessageRequestID any                                   `json:"message_request_id,omitzero"`
	ConversationID   any                                   `json:"conversation_id,omitzero"`
	ChannelID        any                                   `json:"channel_id,omitzero"`
	DateCreated      *ListChannelAnalyticsQueryDateCreated `json:"date_created,omitzero"`
	DateUpdated      *ListChannelAnalyticsQueryDateCreated `json:"date_updated,omitzero"`
	Cursor           *ListChannelAnalyticsQueryCursor      `json:"cursor,omitzero"`
	Sort             map[string]string                     `json:"sort,omitzero"`
	Limit            any                                   `json:"limit,omitzero"`
}

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

type CreateChannelAnalyticsReportRequestDocument struct {
	SendAsLink  *bool   `json:"send_as_link,omitzero"`
	Title       *string `json:"title,omitzero"`
	Author      *string `json:"author,omitzero"`
	Subject     *string `json:"subject,omitzero"`
	Keywords    *string `json:"keywords,omitzero"`
	Password    *string `json:"password,omitzero"`
	Orientation *string `json:"orientation,omitzero"`
	PageSize    *string `json:"page_size,omitzero"`
	Margin      any     `json:"margin,omitzero"`
	Version     *string `json:"version,omitzero"`
}

type CreateChannelAnalyticsReportRequest struct {
	MessageRequestID string                                       `json:"message_request_id"`
	ChannelID        string                                       `json:"channel_id"`
	Duration         string                                       `json:"duration"`
	Document         *CreateChannelAnalyticsReportRequestDocument `json:"document,omitzero"`
}

type CreateChannelAnalyticsReportResponse struct {
	URL string `json:"url"`
}

type ListChannelAnalyticsCountQuery = ListChannelAnalyticsQuery

type ListChannelAnalyticsCountResponse struct {
	Count int64 `json:"count"`
}

type GenerateChannelAnalyticsSummariesQuery struct {
	ChannelID string `json:"channel_id"`
	Duration  string `json:"duration"`
}

type GenerateChannelAnalyticsSummariesResponseOpens struct {
	Total  float64 `json:"total"`
	Unique float64 `json:"unique"`
	Rate   float64 `json:"rate"`
}

type GenerateChannelAnalyticsSummariesResponseDeliveries struct {
	Total float64 `json:"total"`
	Rate  float64 `json:"rate"`
}

type GenerateChannelAnalyticsSummariesResponsePeriodsItem struct {
	Label             string  `json:"label"`
	PeriodStart       string  `json:"period_start"`
	TotalMessageCount float64 `json:"total_message_count"`
	TotalDeliveries   float64 `json:"total_deliveries"`
	TotalFailures     float64 `json:"total_failures"`
	TotalRejections   float64 `json:"total_rejections"`
	TotalComplaints   float64 `json:"total_complaints"`
	TotalBounces      float64 `json:"total_bounces"`
	TotalOpens        float64 `json:"total_opens"`
	TotalClicks       float64 `json:"total_clicks"`
}

type GenerateChannelAnalyticsSummariesResponse struct {
	ChannelID         string                                                 `json:"channel_id"`
	Duration          string                                                 `json:"duration"`
	Label             string                                                 `json:"label"`
	PeriodStart       string                                                 `json:"period_start"`
	PeriodEnd         string                                                 `json:"period_end"`
	TotalMessageCount float64                                                `json:"total_message_count"`
	Opens             GenerateChannelAnalyticsSummariesResponseOpens         `json:"opens"`
	Clicks            GenerateChannelAnalyticsSummariesResponseOpens         `json:"clicks"`
	Deliveries        GenerateChannelAnalyticsSummariesResponseDeliveries    `json:"deliveries"`
	Failures          GenerateChannelAnalyticsSummariesResponseDeliveries    `json:"failures"`
	Rejections        GenerateChannelAnalyticsSummariesResponseDeliveries    `json:"rejections"`
	Complaints        GenerateChannelAnalyticsSummariesResponseDeliveries    `json:"complaints"`
	Bounces           GenerateChannelAnalyticsSummariesResponseDeliveries    `json:"bounces"`
	Subscribes        GenerateChannelAnalyticsSummariesResponseDeliveries    `json:"subscribes"`
	Unsubscribes      GenerateChannelAnalyticsSummariesResponseDeliveries    `json:"unsubscribes"`
	Periods           []GenerateChannelAnalyticsSummariesResponsePeriodsItem `json:"periods"`
}

type IncrementChannelAnalyticsOpensRequest struct {
	TotalOpens  int64  `json:"total_opens"`
	UniqueOpens *int64 `json:"unique_opens,omitzero"`
}

type IncrementChannelAnalyticsOpensResponse = ListChannelAnalyticsItem

type IncrementChannelAnalyticsClicksRequest struct {
	TotalClicks  int64  `json:"total_clicks"`
	UniqueClicks *int64 `json:"unique_clicks,omitzero"`
}

type IncrementChannelAnalyticsClicksResponse = ListChannelAnalyticsItem

type IncrementChannelAnalyticsDeliveriesRequest struct {
	TotalDeliveries int64 `json:"total_deliveries"`
}

type IncrementChannelAnalyticsDeliveriesResponse = ListChannelAnalyticsItem

type IncrementChannelAnalyticsSubscribesRequest struct {
	TotalSubscribes int64 `json:"total_subscribes"`
}

type IncrementChannelAnalyticsSubscribesResponse = ListChannelAnalyticsItem

type IncrementChannelAnalyticsUnsubscribesRequest struct {
	TotalUnsubscribes int64 `json:"total_unsubscribes"`
}

type IncrementChannelAnalyticsUnsubscribesResponse = ListChannelAnalyticsItem
