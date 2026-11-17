package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type PhoneNumbersService struct {
	client *conjoin.Client
}

func (s *PhoneNumbersService) List(ctx context.Context, query *ListPhoneNumbersQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListPhoneNumbersItem], error) {
	return conjoin.List[ListPhoneNumbersItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/phone-numbers/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *PhoneNumbersService) Purchase(ctx context.Context, body *PurchasePhoneNumberRequest, opts ...conjoin.CallOption) (*PurchasePhoneNumberResponse, error) {
	var out PurchasePhoneNumberResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/phone-numbers/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PhoneNumbersService) ListCount(ctx context.Context, query *ListPhoneNumbersCountQuery, opts ...conjoin.CallOption) (*ListPhoneNumbersCountResponse, error) {
	var out ListPhoneNumbersCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/phone-numbers/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PhoneNumbersService) Transfer(ctx context.Context, phoneNumberID string, body *TransferPhoneNumberRequest, opts ...conjoin.CallOption) (*TransferPhoneNumberResponse, error) {
	var out TransferPhoneNumberResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/phone-numbers/{phone_number_id}/transfer",
		PathParams:            []string{phoneNumberID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PhoneNumbersService) Release(ctx context.Context, phoneNumberID string, opts ...conjoin.CallOption) (*ReleasePhoneNumberResponse, error) {
	var out ReleasePhoneNumberResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/phone-numbers/{phone_number_id}/release",
		PathParams:            []string{phoneNumberID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PhoneNumbersService) ListAvailable(ctx context.Context, query *ListAvailablePhoneNumbersQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListAvailablePhoneNumbersItem], error) {
	return conjoin.List[ListAvailablePhoneNumbersItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/available-phone-numbers/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}
