package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ConversationsService struct {
	client *conjoin.Client
}

func (s *ConversationsService) List(ctx context.Context, query *ListConversationsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListConversationsItem], error) {
	return conjoin.List[ListConversationsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/conversations/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *ConversationsService) Create(ctx context.Context, body *CreateConversationRequest, opts ...conjoin.CallOption) (*CreateConversationResponse, error) {
	var out CreateConversationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/conversations/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConversationsService) ListMessages(ctx context.Context, conversationID string, query *ListConversationMessagesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListConversationMessagesItem], error) {
	return conjoin.List[ListConversationMessagesItem](ctx, s.client, conjoin.Operation{
		Method:        "GET",
		Path:          "messaging/conversations/{conversation_id}/messages",
		PathParams:    []string{conversationID},
		Query:         query,
		QueryRequired: true,
		Scopes:        []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *ConversationsService) ListRecipients(ctx context.Context, conversationID string, query *ListConversationRecipientsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListConversationRecipientsItem], error) {
	return conjoin.List[ListConversationRecipientsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/conversations/{conversation_id}/recipients",
		PathParams: []string{conversationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *ConversationsService) AddOneRecipient(ctx context.Context, conversationID string, body *AddOneConversationRecipientRequest, opts ...conjoin.CallOption) (*AddOneConversationRecipientResponse, error) {
	var out AddOneConversationRecipientResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/conversations/{conversation_id}/recipients",
		PathParams:            []string{conversationID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConversationsService) ListCount(ctx context.Context, query *ListConversationsCountQuery, opts ...conjoin.CallOption) (*ListConversationsCountResponse, error) {
	var out ListConversationsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/conversations/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConversationsService) ListMessagesCount(ctx context.Context, conversationID string, query *ListConversationMessagesCountQuery, opts ...conjoin.CallOption) (*ListConversationMessagesCountResponse, error) {
	var out ListConversationMessagesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:        "GET",
		Path:          "messaging/conversations/{conversation_id}/messages/count",
		PathParams:    []string{conversationID},
		Query:         query,
		QueryRequired: true,
		Scopes:        []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConversationsService) ListRecipientsCount(ctx context.Context, conversationID string, query *ListConversationRecipientsCountQuery, opts ...conjoin.CallOption) (*ListConversationRecipientsCountResponse, error) {
	var out ListConversationRecipientsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/conversations/{conversation_id}/recipients/count",
		PathParams: []string{conversationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConversationsService) Duplicate(ctx context.Context, conversationID string, body *DuplicateConversationRequest, opts ...conjoin.CallOption) (*DuplicateConversationResponse, error) {
	var out DuplicateConversationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/conversations/{conversation_id}/duplicate",
		PathParams:            []string{conversationID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConversationsService) SendMessage(ctx context.Context, conversationID string, body *SendConversationMessageRequest, opts ...conjoin.CallOption) (any, error) {
	var out any
	err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/conversations/{conversation_id}/send",
		PathParams:            []string{conversationID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...)
	return out, err
}

func (s *ConversationsService) Delete(ctx context.Context, conversationID string, opts ...conjoin.CallOption) (*DeleteConversationResponse, error) {
	var out DeleteConversationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/conversations/{conversation_id}",
		PathParams: []string{conversationID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConversationsService) Update(ctx context.Context, conversationID string, body *UpdateConversationRequest, opts ...conjoin.CallOption) (*UpdateConversationResponse, error) {
	var out UpdateConversationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/conversations/{conversation_id}",
		PathParams:   []string{conversationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConversationsService) Archive(ctx context.Context, conversationID string, opts ...conjoin.CallOption) (*ArchiveConversationResponse, error) {
	var out ArchiveConversationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/conversations/{conversation_id}/archive",
		PathParams:            []string{conversationID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConversationsService) ReadOneRecipient(ctx context.Context, conversationID string, recipientID string, opts ...conjoin.CallOption) (*ReadOneConversationRecipientResponse, error) {
	var out ReadOneConversationRecipientResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/conversations/{conversation_id}/recipients/{recipient_id}",
		PathParams: []string{conversationID, recipientID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConversationsService) DeleteRecipients(ctx context.Context, conversationID string, recipientID string, opts ...conjoin.CallOption) (*DeleteConversationRecipientsResponse, error) {
	var out DeleteConversationRecipientsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/conversations/{conversation_id}/recipients/{recipient_id}",
		PathParams: []string{conversationID, recipientID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConversationsService) AddManyRecipients(ctx context.Context, conversationID string, body *AddManyConversationRecipientsRequest, opts ...conjoin.CallOption) (*conjoin.Page[AddManyConversationRecipientsItem], error) {
	return conjoin.List[AddManyConversationRecipientsItem](ctx, s.client, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/conversations/{conversation_id}/add-recipients",
		PathParams:            []string{conversationID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, opts...)
}
