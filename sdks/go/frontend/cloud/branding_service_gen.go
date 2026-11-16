package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type BrandingsService struct {
	client *conjoin.Client
}

func (s *BrandingsService) ReadPublicProject(ctx context.Context, query *ReadPublicProjectBrandingQuery, opts ...conjoin.CallOption) (*ReadPublicProjectBrandingResponse, error) {
	var out ReadPublicProjectBrandingResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/client/branding/",
		Query:  query,
		Auth:   conjoin.AuthPublishableKey,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
