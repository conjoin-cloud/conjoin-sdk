package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SMSCampaignsService struct {
	client *conjoin.Client
}

func (s *SMSCampaignsService) CreateSmsCampaign(ctx context.Context, body *CreateSmsCampaignRequest, opts ...conjoin.CallOption) (*CreateSmsCampaignResponse, error) {
	var out CreateSmsCampaignResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/sms/campaigns/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSCampaignsService) ReadSmsCampaign(ctx context.Context, campaignID string, opts ...conjoin.CallOption) (*ReadSmsCampaignResponse, error) {
	var out ReadSmsCampaignResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/sms/campaigns/{campaign_id}",
		PathParams: []string{campaignID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSCampaignsService) UpdateSmsCampaign(ctx context.Context, campaignID string, body *UpdateSmsCampaignRequest, opts ...conjoin.CallOption) (*UpdateSmsCampaignResponse, error) {
	var out UpdateSmsCampaignResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/sms/campaigns/{campaign_id}",
		PathParams:   []string{campaignID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSCampaignsService) DeleteSmsCampaign(ctx context.Context, campaignID string, opts ...conjoin.CallOption) (*DeleteSmsCampaignResponse, error) {
	var out DeleteSmsCampaignResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/sms/campaigns/{campaign_id}",
		PathParams: []string{campaignID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSCampaignsService) ListSmsCampaigns(ctx context.Context, body *ListSmsCampaignsRequest, opts ...conjoin.CallOption) (*conjoin.Page[ListSmsCampaignsItem], error) {
	return conjoin.List[ListSmsCampaignsItem](ctx, s.client, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/sms/campaigns/retrieve",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}
