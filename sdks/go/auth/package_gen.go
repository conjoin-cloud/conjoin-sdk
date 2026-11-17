package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type Client struct {
	AccountRecoveries           *AccountRecoveriesService
	Accounts                    *AccountsService
	Apps                        *AppsService
	Authorizations              *AuthorizationsService
	Clients                     *ClientsService
	ConnectionEnterprises       *ConnectionEnterprisesService
	Connections                 *ConnectionsService
	Credentials                 *CredentialsService
	Deprovisionings             *DeprovisioningsService
	Flows                       *FlowsService
	Guards                      *GuardsService
	Identities                  *IdentitiesService
	OrganizationDomains         *OrganizationDomainsService
	OrganizationGroups          *OrganizationGroupsService
	OrganizationInvitations     *OrganizationInvitationsService
	OrganizationMemberships     *OrganizationMembershipsService
	OrganizationPermissions     *OrganizationPermissionsService
	OrganizationRolePermissions *OrganizationRolePermissionsService
	OrganizationRoles           *OrganizationRolesService
	Organizations               *OrganizationsService
	Passkeys                    *PasskeysService
	Policies                    *PoliciesService
	ResourceGrants              *ResourceGrantsService
	RoleAssignmentLogs          *RoleAssignmentLogsService
	SCIMManagements             *SCIMManagementsService
	SCIMs                       *SCIMsService
	SLOs                        *SLOsService
	SSOPortals                  *SSOPortalsService
	Sessions                    *SessionsService
	StepUps                     *StepUpsService
	TrustedDevices              *TrustedDevicesService
}

func New(client *conjoin.Client) *Client {
	return &Client{
		AccountRecoveries:           &AccountRecoveriesService{client: client},
		Accounts:                    &AccountsService{client: client},
		Apps:                        &AppsService{client: client},
		Authorizations:              &AuthorizationsService{client: client},
		Clients:                     &ClientsService{client: client},
		ConnectionEnterprises:       &ConnectionEnterprisesService{client: client},
		Connections:                 &ConnectionsService{client: client},
		Credentials:                 &CredentialsService{client: client},
		Deprovisionings:             &DeprovisioningsService{client: client},
		Flows:                       &FlowsService{client: client},
		Guards:                      &GuardsService{client: client},
		Identities:                  &IdentitiesService{client: client},
		OrganizationDomains:         &OrganizationDomainsService{client: client},
		OrganizationGroups:          &OrganizationGroupsService{client: client},
		OrganizationInvitations:     &OrganizationInvitationsService{client: client},
		OrganizationMemberships:     &OrganizationMembershipsService{client: client},
		OrganizationPermissions:     &OrganizationPermissionsService{client: client},
		OrganizationRolePermissions: &OrganizationRolePermissionsService{client: client},
		OrganizationRoles:           &OrganizationRolesService{client: client},
		Organizations:               &OrganizationsService{client: client},
		Passkeys:                    &PasskeysService{client: client},
		Policies:                    &PoliciesService{client: client},
		ResourceGrants:              &ResourceGrantsService{client: client},
		RoleAssignmentLogs:          &RoleAssignmentLogsService{client: client},
		SCIMManagements:             &SCIMManagementsService{client: client},
		SCIMs:                       &SCIMsService{client: client},
		SLOs:                        &SLOsService{client: client},
		SSOPortals:                  &SSOPortalsService{client: client},
		Sessions:                    &SessionsService{client: client},
		StepUps:                     &StepUpsService{client: client},
		TrustedDevices:              &TrustedDevicesService{client: client},
	}
}
