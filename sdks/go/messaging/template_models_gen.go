package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateMessageTemplateRequest struct {
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

type CreateMessageTemplateResponse struct {
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

type ListMessageTemplatesRequestQueryContentLimit struct {
	NotEquals *float64  `json:"not_equals,omitzero"`
	Gt        *float64  `json:"gt,omitzero"`
	Lt        *float64  `json:"lt,omitzero"`
	Gte       *float64  `json:"gte,omitzero"`
	Lte       *float64  `json:"lte,omitzero"`
	HasAny    []float64 `json:"has_any,omitzero"`
	HasNone   []float64 `json:"has_none,omitzero"`
}

type ListMessageTemplatesRequestQuery struct {
	TemplateID   any                                                            `json:"template_id,omitzero"`
	Title        any                                                            `json:"title,omitzero"`
	Channel      any                                                            `json:"channel,omitzero"`
	ContentType  any                                                            `json:"content_type,omitzero"`
	ContentLimit conjoin.Nullable[ListMessageTemplatesRequestQueryContentLimit] `json:"content_limit,omitzero"`
	IsDefault    *bool                                                          `json:"is_default,omitzero"`
	Tags         *ListPhoneNumbersQueryQueryType                                `json:"tags,omitzero"`
	DateCreated  *ListChannelAnalyticsRequestQueryDateCreated                   `json:"date_created,omitzero"`
	DateUpdated  *ListChannelAnalyticsRequestQueryDateCreated                   `json:"date_updated,omitzero"`
	DateDeleted  conjoin.Nullable[ListChannelAnalyticsRequestQueryDateCreated]  `json:"date_deleted,omitzero"`
	DateArchived conjoin.Nullable[ListChannelAnalyticsRequestQueryDateCreated]  `json:"date_archived,omitzero"`
}

type ListMessageTemplatesRequest struct {
	Cursor *ListChannelAnalyticsRequestCursor `json:"cursor,omitzero"`
	Filter map[string]bool                    `json:"filter,omitzero"`
	Query  *ListMessageTemplatesRequestQuery  `json:"query,omitzero"`
	Search *ListContactsRequestSearch         `json:"search,omitzero"`
	Sort   map[string]string                  `json:"sort,omitzero"`
	Limit  any                                `json:"limit,omitzero"`
}

type ListMessageTemplatesItem = CreateMessageTemplateResponse

type ReadMessageTemplateResponse = CreateMessageTemplateResponse

type DeleteMessageTemplateResponse = CreateMessageTemplateResponse

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

type UpdateMessageTemplateResponse = CreateMessageTemplateResponse

type DeleteMessageTemplatesRequest struct {
	Query *ListMessageTemplatesRequestQuery `json:"query,omitzero"`
}

type DeleteMessageTemplatesResponseResponse struct {
	Type    string `json:"type"`
	Code    int64  `json:"code"`
	Message string `json:"message"`
}

type DeleteMessageTemplatesResponse struct {
	Response *DeleteMessageTemplatesResponseResponse `json:"response,omitzero"`
}
