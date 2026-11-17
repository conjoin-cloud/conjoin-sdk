package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListMessageTemplatesQueryContentLimit struct {
	NotEquals any   `json:"not_equals,omitzero"`
	Gt        any   `json:"gt,omitzero"`
	Lt        any   `json:"lt,omitzero"`
	Gte       any   `json:"gte,omitzero"`
	Lte       any   `json:"lte,omitzero"`
	HasAny    []any `json:"has_any,omitzero"`
	HasNone   []any `json:"has_none,omitzero"`
}

type ListMessageTemplatesQueryTags struct {
	IsEmpty                   any      `json:"is_empty,omitzero"`
	Contains                  []string `json:"contains,omitzero"`
	LengthLessThan            any      `json:"length_less_than,omitzero"`
	LengthLessThanOrEquals    any      `json:"length_less_than_or_equals,omitzero"`
	LengthGreaterThan         any      `json:"length_greater_than,omitzero"`
	LengthGreaterThanOrEquals any      `json:"length_greater_than_or_equals,omitzero"`
}

type ListMessageTemplatesQuery struct {
	TemplateID   any                                    `json:"template_id,omitzero"`
	ReferenceID  any                                    `json:"reference_id,omitzero"`
	Title        any                                    `json:"title,omitzero"`
	Channel      any                                    `json:"channel,omitzero"`
	ContentType  any                                    `json:"content_type,omitzero"`
	ContentLimit *ListMessageTemplatesQueryContentLimit `json:"content_limit,omitzero"`
	IsDefault    any                                    `json:"is_default,omitzero"`
	Tags         *ListMessageTemplatesQueryTags         `json:"tags,omitzero"`
	DateCreated  *ListChannelAnalyticsQueryDateCreated  `json:"date_created,omitzero"`
	DateUpdated  *ListChannelAnalyticsQueryDateCreated  `json:"date_updated,omitzero"`
	DateDeleted  *ListChannelAnalyticsQueryDateCreated  `json:"date_deleted,omitzero"`
	DateArchived *ListChannelAnalyticsQueryDateCreated  `json:"date_archived,omitzero"`
	Search       *string                                `json:"search,omitzero"`
	Cursor       *ListChannelAnalyticsQueryCursor       `json:"cursor,omitzero"`
	Sort         map[string]string                      `json:"sort,omitzero"`
	Limit        any                                    `json:"limit,omitzero"`
}

type ListMessageTemplatesItem struct {
	TemplateID       string                    `json:"template_id"`
	ProfileID        string                    `json:"profile_id"`
	ConjoinAccountID string                    `json:"conjoin_account_id"`
	ConjoinProjectID string                    `json:"conjoin_project_id"`
	LiveMode         bool                      `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string]  `json:"reference_id,omitzero"`
	TemplateGroupID  conjoin.Nullable[string]  `json:"template_group_id,omitzero"`
	Channel          string                    `json:"channel"`
	IsOTPTemplate    *bool                     `json:"is_otp_template,omitzero"`
	Title            string                    `json:"title"`
	Description      *string                   `json:"description,omitzero"`
	Language         string                    `json:"language"`
	Content          string                    `json:"content"`
	ContentType      string                    `json:"content_type"`
	ContentLimit     conjoin.Nullable[float64] `json:"content_limit,omitzero"`
	IsDefault        bool                      `json:"is_default"`
	IsFavourite      bool                      `json:"is_favourite"`
	Tags             []string                  `json:"tags,omitzero"`
	DateArchived     conjoin.Nullable[string]  `json:"date_archived,omitzero"`
	DateCreated      string                    `json:"date_created"`
	DateUpdated      string                    `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]  `json:"date_deleted,omitzero"`
}

type CreateMessageTemplateRequest struct {
	ReferenceID     *string                   `json:"reference_id,omitzero"`
	TemplateGroupID *string                   `json:"template_group_id,omitzero"`
	Channel         string                    `json:"channel"`
	IsOTPTemplate   *bool                     `json:"is_otp_template,omitzero"`
	Title           string                    `json:"title"`
	Description     *string                   `json:"description,omitzero"`
	Language        *string                   `json:"language,omitzero"`
	Content         string                    `json:"content"`
	ContentType     string                    `json:"content_type"`
	ContentLimit    conjoin.Nullable[float64] `json:"content_limit,omitzero"`
	IsDefault       *bool                     `json:"is_default,omitzero"`
	IsFavourite     *bool                     `json:"is_favourite,omitzero"`
}

type CreateMessageTemplateResponse = ListMessageTemplatesItem

type ListMessageTemplatesCountQuery = ListMessageTemplatesQuery

type ListMessageTemplatesCountResponse = ListChannelAnalyticsCountResponse

type ReadMessageTemplateResponse = ListMessageTemplatesItem

type DeleteMessageTemplateResponse = ListMessageTemplatesItem

type UpdateMessageTemplateRequest struct {
	TemplateGroupID *string                   `json:"template_group_id,omitzero"`
	Channel         *string                   `json:"channel,omitzero"`
	IsOTPTemplate   *bool                     `json:"is_otp_template,omitzero"`
	Title           *string                   `json:"title,omitzero"`
	Description     *string                   `json:"description,omitzero"`
	Language        *string                   `json:"language,omitzero"`
	Content         *string                   `json:"content,omitzero"`
	ContentType     *string                   `json:"content_type,omitzero"`
	ContentLimit    conjoin.Nullable[float64] `json:"content_limit,omitzero"`
	IsDefault       *bool                     `json:"is_default,omitzero"`
	IsFavourite     *bool                     `json:"is_favourite,omitzero"`
}

type UpdateMessageTemplateResponse = ListMessageTemplatesItem
