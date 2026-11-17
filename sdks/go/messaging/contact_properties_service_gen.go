package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ContactPropertiesService struct {
	client *conjoin.Client
}

func (s *ContactPropertiesService) List(ctx context.Context, query *ListContactPropertiesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListContactPropertiesItem], error) {
	return conjoin.List[ListContactPropertiesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/contact-properties/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *ContactPropertiesService) CreateContactProperty(ctx context.Context, body *CreateContactPropertyRequest, opts ...conjoin.CallOption) (*CreateContactPropertyResponse, error) {
	var out CreateContactPropertyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/contact-properties/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactPropertiesService) ListCount(ctx context.Context, query *ListContactPropertiesCountQuery, opts ...conjoin.CallOption) (*ListContactPropertiesCountResponse, error) {
	var out ListContactPropertiesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/contact-properties/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactPropertiesService) FetchOneContactProperty(ctx context.Context, contactPropertyID string, opts ...conjoin.CallOption) (*FetchOneContactPropertyResponse, error) {
	var out FetchOneContactPropertyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/contact-properties/{contact_property_id}",
		PathParams: []string{contactPropertyID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContactPropertiesService) DeleteContactProperty(ctx context.Context, contactPropertyID string, opts ...conjoin.CallOption) (*DeleteContactPropertyResponse, error) {
	var out DeleteContactPropertyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/contact-properties/{contact_property_id}",
		PathParams: []string{contactPropertyID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
