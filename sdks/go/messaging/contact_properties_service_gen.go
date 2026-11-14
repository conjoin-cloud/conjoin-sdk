package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ContactPropertiesService struct {
	client *conjoin.Client
}

func (s *ContactPropertiesService) CreateContactProperty(ctx context.Context, body *CreateContactPropertyRequest, opts ...conjoin.CallOption) (*CreateContactPropertyResponse, error) {
	var out CreateContactPropertyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/contacts/properties",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactPropertiesService) DeleteMany(ctx context.Context, opts ...conjoin.CallOption) (*DeleteManyContactPropertiesResponse, error) {
	var out DeleteManyContactPropertiesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "DELETE",
		Path:   "messaging/contacts/properties",
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactPropertiesService) FetchOneContactProperty(ctx context.Context, propertyID string, opts ...conjoin.CallOption) (*FetchOneContactPropertyResponse, error) {
	var out FetchOneContactPropertyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/contacts/properties/{property_id}",
		PathParams: []string{propertyID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactPropertiesService) DeleteContactProperty(ctx context.Context, propertyID string, opts ...conjoin.CallOption) (*DeleteContactPropertyResponse, error) {
	var out DeleteContactPropertyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/contacts/properties/{property_id}",
		PathParams: []string{propertyID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactPropertiesService) List(ctx context.Context, opts ...conjoin.CallOption) (*conjoin.Page[ListContactPropertiesItem], error) {
	return conjoin.List[ListContactPropertiesItem](ctx, s.client, conjoin.Operation{
		Method: "POST",
		Path:   "messaging/contacts/properties/retrieve",
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}
