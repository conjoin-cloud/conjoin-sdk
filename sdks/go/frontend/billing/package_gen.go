package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type Client struct {
	Selves *SelvesService
}

func New(client *conjoin.Client) *Client {
	return &Client{
		Selves: &SelvesService{client: client},
	}
}
