package ai

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type Client struct {
	BYOKs      *BYOKsService
	Contexts   *ContextsService
	Inferences *InferencesService
	Models     *ModelsService
	Policies   *PoliciesService
	Usages     *UsagesService
}

func New(client *conjoin.Client) *Client {
	return &Client{
		BYOKs:      &BYOKsService{client: client},
		Contexts:   &ContextsService{client: client},
		Inferences: &InferencesService{client: client},
		Models:     &ModelsService{client: client},
		Policies:   &PoliciesService{client: client},
		Usages:     &UsagesService{client: client},
	}
}
