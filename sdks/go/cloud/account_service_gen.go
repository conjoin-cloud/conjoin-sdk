package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type AccountsService struct {
	client *conjoin.Client
}

func (s *AccountsService) Read(ctx context.Context, opts ...conjoin.CallOption) (*ReadAccountResponse, error) {
	var out ReadAccountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/account/",
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) Update(ctx context.Context, body *UpdateAccountRequest, opts ...conjoin.CallOption) (*UpdateAccountResponse, error) {
	var out UpdateAccountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "cloud/account/",
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
