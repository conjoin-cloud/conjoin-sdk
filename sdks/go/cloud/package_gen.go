package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type Client struct {
	APIKeys         *APIKeysService
	Accounts        *AccountsService
	Audits          *AuditsService
	Brandings       *BrandingsService
	Organizations   *OrganizationsService
	Plans           *PlansService
	Projects        *ProjectsService
	PublishableKeys *PublishableKeysService
	Roles           *RolesService
	SKUCatalogs     *SKUCatalogsService
	SpendControls   *SpendControlsService
	Webhooks        *WebhooksService
	Zones           *ZonesService
}

func New(client *conjoin.Client) *Client {
	return &Client{
		APIKeys:         &APIKeysService{client: client},
		Accounts:        &AccountsService{client: client},
		Audits:          &AuditsService{client: client},
		Brandings:       &BrandingsService{client: client},
		Organizations:   &OrganizationsService{client: client},
		Plans:           &PlansService{client: client},
		Projects:        &ProjectsService{client: client},
		PublishableKeys: &PublishableKeysService{client: client},
		Roles:           &RolesService{client: client},
		SKUCatalogs:     &SKUCatalogsService{client: client},
		SpendControls:   &SpendControlsService{client: client},
		Webhooks:        &WebhooksService{client: client},
		Zones:           &ZonesService{client: client},
	}
}
