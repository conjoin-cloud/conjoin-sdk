package storage

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type Client struct {
	Containers *ContainersService
	ObjectACLs *ObjectACLsService
	Objects    *ObjectsService
}

func New(client *conjoin.Client) *Client {
	return &Client{
		Containers: &ContainersService{client: client},
		ObjectACLs: &ObjectACLsService{client: client},
		Objects:    &ObjectsService{client: client},
	}
}
