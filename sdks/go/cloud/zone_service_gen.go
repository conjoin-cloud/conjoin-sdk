package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ZonesService struct {
	client *conjoin.Client
}

func (s *ZonesService) List(ctx context.Context, query *ReadZonesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadZonesItem], error) {
	return conjoin.List[ReadZonesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/zones/",
		Query:  query,
	}, opts...)
}

func (s *ZonesService) Create(ctx context.Context, body *CreateZoneRequest, opts ...conjoin.CallOption) (*CreateZoneResponse, error) {
	var out CreateZoneResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "cloud/zones/",
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ZonesService) ReadCount(ctx context.Context, query *ReadZonesCountQuery, opts ...conjoin.CallOption) (*ReadZonesCountResponse, error) {
	var out ReadZonesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/zones/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ZonesService) Read(ctx context.Context, zoneID string, opts ...conjoin.CallOption) (*ReadZoneResponse, error) {
	var out ReadZoneResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "cloud/zones/{zone_id}",
		PathParams: []string{zoneID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ZonesService) Delete(ctx context.Context, zoneID string, opts ...conjoin.CallOption) (bool, error) {
	var out bool
	err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "cloud/zones/{zone_id}",
		PathParams: []string{zoneID},
	}, &out, opts...)
	return out, err
}

func (s *ZonesService) VerifyDns(ctx context.Context, zoneID string, opts ...conjoin.CallOption) (any, error) {
	var out any
	err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "cloud/zones/{zone_id}/verify",
		PathParams: []string{zoneID},
	}, &out, opts...)
	return out, err
}
