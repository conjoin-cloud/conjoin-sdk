package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ContactsService struct {
	client *conjoin.Client
}

func (s *ContactsService) Create(ctx context.Context, body *CreateContactRequest, opts ...conjoin.CallOption) (*CreateContactResponse, error) {
	var out CreateContactResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/contacts/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactsService) SuppressMessages(ctx context.Context, contactID string, body *SuppressContactMessagesRequest, opts ...conjoin.CallOption) (*SuppressContactMessagesResponse, error) {
	var out SuppressContactMessagesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/contacts/{contact_id}/unsubscribe",
		PathParams:   []string{contactID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactsService) Update(ctx context.Context, contactID string, body *UpdateContactRequest, opts ...conjoin.CallOption) (*UpdateContactResponse, error) {
	var out UpdateContactResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/contacts/{contact_id}",
		PathParams:   []string{contactID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactsService) Delete(ctx context.Context, contactID string, opts ...conjoin.CallOption) (*DeleteContactResponse, error) {
	var out DeleteContactResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/contacts/{contact_id}",
		PathParams: []string{contactID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactsService) List(ctx context.Context, body *ListContactsRequest, opts ...conjoin.CallOption) (*conjoin.Page[ListContactsItem], error) {
	return conjoin.List[ListContactsItem](ctx, s.client, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/contacts/retrieve",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *ContactsService) AddProperties(ctx context.Context, contactID string, opts ...conjoin.CallOption) (*AddContactPropertiesResponse, error) {
	var out AddContactPropertiesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PUT",
		Path:       "messaging/contacts/{contact_id}/properties",
		PathParams: []string{contactID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactsService) UpdateProperty(ctx context.Context, contactID string, opts ...conjoin.CallOption) (*UpdateContactPropertyResponse, error) {
	var out UpdateContactPropertyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/contacts/{contact_id}/properties",
		PathParams: []string{contactID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactsService) DeleteProperties(ctx context.Context, contactID string, opts ...conjoin.CallOption) (*DeleteContactPropertiesResponse, error) {
	var out DeleteContactPropertiesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/contacts/{contact_id}/properties",
		PathParams: []string{contactID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
