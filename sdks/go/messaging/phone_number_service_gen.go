package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type PhoneNumbersService struct {
	client *conjoin.Client
}

func (s *PhoneNumbersService) Purchase(ctx context.Context, phoneNumber string, body *PurchasePhoneNumberRequest, opts ...conjoin.CallOption) (*PurchasePhoneNumberResponse, error) {
	var out PurchasePhoneNumberResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/phone-numbers/{phone_number}/provision",
		PathParams:            []string{phoneNumber},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PhoneNumbersService) Update(ctx context.Context, phoneNumber string, projectID string, opts ...conjoin.CallOption) (*UpdatePhoneNumberResponse, error) {
	var out UpdatePhoneNumberResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/phone-numbers/transfer/{phone_number}/project/{project_id}",
		PathParams: []string{phoneNumber, projectID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PhoneNumbersService) ListAvailable(ctx context.Context, query *ListAvailablePhoneNumbersQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListAvailablePhoneNumbersItem], error) {
	return conjoin.List[ListAvailablePhoneNumbersItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/phone-numbers/available",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *PhoneNumbersService) List(ctx context.Context, query *ListPhoneNumbersQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListPhoneNumbersItem], error) {
	return conjoin.List[ListPhoneNumbersItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/phone-numbers/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *PhoneNumbersService) Release(ctx context.Context, phoneNumber string, opts ...conjoin.CallOption) (*ReleasePhoneNumberResponse, error) {
	var out ReleasePhoneNumberResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/phone-numbers/{phone_number}/release",
		PathParams:            []string{phoneNumber},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
