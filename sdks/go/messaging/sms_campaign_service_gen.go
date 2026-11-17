package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SMSCampaignsService struct {
	client *conjoin.Client
}

func (s *SMSCampaignsService) ListSmsCampaigns(ctx context.Context, query *ListSmsCampaignsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListSmsCampaignsItem], error) {
	return conjoin.List[ListSmsCampaignsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/sms-campaigns/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *SMSCampaignsService) CreateSmsCampaign(ctx context.Context, body *CreateSmsCampaignRequest, opts ...conjoin.CallOption) (*CreateSmsCampaignResponse, error) {
	var out CreateSmsCampaignResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/sms-campaigns/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSCampaignsService) ListSmsCampaignsCount(ctx context.Context, query *ListSmsCampaignsCountQuery, opts ...conjoin.CallOption) (*ListSmsCampaignsCountResponse, error) {
	var out ListSmsCampaignsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/sms-campaigns/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSCampaignsService) ReadSmsCampaign(ctx context.Context, smsCampaignID string, opts ...conjoin.CallOption) (*ReadSmsCampaignResponse, error) {
	var out ReadSmsCampaignResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/sms-campaigns/{sms_campaign_id}",
		PathParams: []string{smsCampaignID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSCampaignsService) UpdateSmsCampaign(ctx context.Context, smsCampaignID string, body *UpdateSmsCampaignRequest, opts ...conjoin.CallOption) (*UpdateSmsCampaignResponse, error) {
	var out UpdateSmsCampaignResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/sms-campaigns/{sms_campaign_id}",
		PathParams:   []string{smsCampaignID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSCampaignsService) DeleteSmsCampaign(ctx context.Context, smsCampaignID string, opts ...conjoin.CallOption) (*DeleteSmsCampaignResponse, error) {
	var out DeleteSmsCampaignResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/sms-campaigns/{sms_campaign_id}",
		PathParams: []string{smsCampaignID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
