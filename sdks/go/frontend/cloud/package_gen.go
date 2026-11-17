package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type Client struct {
	Brandings *BrandingsService
	SDKs      *SDKsService
}

func New(client *conjoin.Client) *Client {
	return &Client{
		Brandings: &BrandingsService{client: client},
		SDKs:      &SDKsService{client: client},
	}
}
