package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type OrganizationInvitationsService struct {
	client *conjoin.Client
}

func (s *OrganizationInvitationsService) Accept(ctx context.Context, body *AcceptOrganizationInvitationRequest, opts ...conjoin.CallOption) (*AcceptOrganizationInvitationResponse, error) {
	var out AcceptOrganizationInvitationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/invitations/accept",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
