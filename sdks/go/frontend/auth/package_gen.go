package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type Client struct {
	Accounts                *AccountsService
	Clients                 *ClientsService
	ConnectionEnterprises   *ConnectionEnterprisesService
	Flows                   *FlowsService
	Natives                 *NativesService
	OrganizationDomains     *OrganizationDomainsService
	OrganizationInvitations *OrganizationInvitationsService
	SSOPortals              *SSOPortalsService
	Selves                  *SelvesService
}

func New(client *conjoin.Client) *Client {
	return &Client{
		Accounts:                &AccountsService{client: client},
		Clients:                 &ClientsService{client: client},
		ConnectionEnterprises:   &ConnectionEnterprisesService{client: client},
		Flows:                   &FlowsService{client: client},
		Natives:                 &NativesService{client: client},
		OrganizationDomains:     &OrganizationDomainsService{client: client},
		OrganizationInvitations: &OrganizationInvitationsService{client: client},
		SSOPortals:              &SSOPortalsService{client: client},
		Selves:                  &SelvesService{client: client},
	}
}
