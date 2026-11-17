package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadWebhooksQuery struct {
	Events *string                 `json:"events,omitzero"`
	Cursor *ReadApiKeysQueryCursor `json:"cursor,omitzero"`
	Sort   map[string]string       `json:"sort,omitzero"`
	Limit  any                     `json:"limit,omitzero"`
}

type ReadWebhooksItem struct {
	CloudAccountID string                   `json:"cloud_account_id"`
	EntityID       string                   `json:"entity_id"`
	WebhookID      string                   `json:"webhook_id"`
	ProjectID      string                   `json:"project_id"`
	Name           *string                  `json:"name,omitzero"`
	Description    *string                  `json:"description,omitzero"`
	URL            string                   `json:"url"`
	Events         []string                 `json:"events"`
	IsActive       bool                     `json:"is_active"`
	DateCreated    string                   `json:"date_created"`
	DateUpdated    conjoin.Nullable[string] `json:"date_updated,omitzero"`
	DateDeleted    conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type RegisterWebhookRequest struct {
	Name        *string  `json:"name,omitzero"`
	Description *string  `json:"description,omitzero"`
	URL         string   `json:"url"`
	Events      []string `json:"events"`
	IsActive    *bool    `json:"is_active,omitzero"`
}

type RegisterWebhookResponse = ReadWebhooksItem

type ReadWebhooksCountQuery = ReadWebhooksQuery

type ReadWebhooksCountResponse = ReadApiKeysCountResponse

type ReadWebhookResponse = ReadWebhooksItem

type UpdateWebhookRequest struct {
	Name        *string  `json:"name,omitzero"`
	Description *string  `json:"description,omitzero"`
	URL         *string  `json:"url,omitzero"`
	Events      []string `json:"events,omitzero"`
	IsActive    *bool    `json:"is_active,omitzero"`
}

type UpdateWebhookResponse = ReadWebhooksItem

type ReadWebhookEventsQuery = ListPublishableKeysQuery

type ReadWebhookEventsItem struct {
	EventID     string `json:"event_id"`
	Description string `json:"description"`
}

type ReadWebhookEventsCountQuery = ListPublishableKeysQuery

type ReadWebhookEventsCountResponse = ReadApiKeysCountResponse
