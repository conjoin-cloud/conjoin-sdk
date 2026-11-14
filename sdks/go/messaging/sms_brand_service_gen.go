package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SMSBrandsService struct {
	client *conjoin.Client
}

func (s *SMSBrandsService) CreateSmsBrand(ctx context.Context, body *CreateSmsBrandRequest, opts ...conjoin.CallOption) (*CreateSmsBrandResponse, error) {
	var out CreateSmsBrandResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/sms/brands/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSBrandsService) ReadSmsBrand(ctx context.Context, brandID string, opts ...conjoin.CallOption) (*ReadSmsBrandResponse, error) {
	var out ReadSmsBrandResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/sms/brands/{brand_id}",
		PathParams: []string{brandID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSBrandsService) UpdateSmsBrand(ctx context.Context, brandID string, body *UpdateSmsBrandRequest, opts ...conjoin.CallOption) (*UpdateSmsBrandResponse, error) {
	var out UpdateSmsBrandResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/sms/brands/{brand_id}",
		PathParams:   []string{brandID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSBrandsService) DeleteSmsBrand(ctx context.Context, brandID string, opts ...conjoin.CallOption) (*DeleteSmsBrandResponse, error) {
	var out DeleteSmsBrandResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/sms/brands/{brand_id}",
		PathParams: []string{brandID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSBrandsService) ListSmsBrands(ctx context.Context, body *ListSmsBrandsRequest, opts ...conjoin.CallOption) (*conjoin.Page[ListSmsBrandsItem], error) {
	return conjoin.List[ListSmsBrandsItem](ctx, s.client, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/sms/brands/retrieve",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}
