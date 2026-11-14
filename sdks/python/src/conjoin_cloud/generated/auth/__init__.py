from __future__ import annotations

from typing import TYPE_CHECKING

from conjoin_cloud.generated.auth._account import (
    AsyncAuthAccountsResource,
    AuthAccountsResource,
)
from conjoin_cloud.generated.auth._account_recovery import (
    AsyncAuthAccountRecoveriesResource,
    AuthAccountRecoveriesResource,
)
from conjoin_cloud.generated.auth._app import (
    AsyncAuthAppsResource,
    AuthAppsResource,
)
from conjoin_cloud.generated.auth._authorization import (
    AsyncAuthAuthorizationsResource,
    AuthAuthorizationsResource,
)
from conjoin_cloud.generated.auth._client import (
    AsyncAuthClientsResource,
    AuthClientsResource,
)
from conjoin_cloud.generated.auth._connection import (
    AsyncAuthConnectionsResource,
    AuthConnectionsResource,
)
from conjoin_cloud.generated.auth._connection_enterprise import (
    AsyncAuthConnectionEnterprisesResource,
    AuthConnectionEnterprisesResource,
)
from conjoin_cloud.generated.auth._credential import (
    AsyncAuthCredentialsResource,
    AuthCredentialsResource,
)
from conjoin_cloud.generated.auth._deprovisioning import (
    AsyncAuthDeprovisioningsResource,
    AuthDeprovisioningsResource,
)
from conjoin_cloud.generated.auth._flow import (
    AsyncAuthFlowsResource,
    AuthFlowsResource,
)
from conjoin_cloud.generated.auth._guard import (
    AsyncAuthGuardsResource,
    AuthGuardsResource,
)
from conjoin_cloud.generated.auth._identity import (
    AsyncAuthIdentitiesResource,
    AuthIdentitiesResource,
)
from conjoin_cloud.generated.auth._organization import (
    AsyncAuthOrganizationsResource,
    AuthOrganizationsResource,
)
from conjoin_cloud.generated.auth._organization_domain import (
    AsyncAuthOrganizationDomainsResource,
    AuthOrganizationDomainsResource,
)
from conjoin_cloud.generated.auth._organization_group import (
    AsyncAuthOrganizationGroupsResource,
    AuthOrganizationGroupsResource,
)
from conjoin_cloud.generated.auth._organization_invitation import (
    AsyncAuthOrganizationInvitationsResource,
    AuthOrganizationInvitationsResource,
)
from conjoin_cloud.generated.auth._organization_membership import (
    AsyncAuthOrganizationMembershipsResource,
    AuthOrganizationMembershipsResource,
)
from conjoin_cloud.generated.auth._organization_permission import (
    AsyncAuthOrganizationPermissionsResource,
    AuthOrganizationPermissionsResource,
)
from conjoin_cloud.generated.auth._organization_role import (
    AsyncAuthOrganizationRolesResource,
    AuthOrganizationRolesResource,
)
from conjoin_cloud.generated.auth._organization_role_permission import (
    AsyncAuthOrganizationRolePermissionsResource,
    AuthOrganizationRolePermissionsResource,
)
from conjoin_cloud.generated.auth._passkey import (
    AsyncAuthPasskeysResource,
    AuthPasskeysResource,
)
from conjoin_cloud.generated.auth._policy import (
    AsyncAuthPoliciesResource,
    AuthPoliciesResource,
)
from conjoin_cloud.generated.auth._resource_grant import (
    AsyncAuthResourceGrantsResource,
    AuthResourceGrantsResource,
)
from conjoin_cloud.generated.auth._role_assignment_log import (
    AsyncAuthRoleAssignmentLogsResource,
    AuthRoleAssignmentLogsResource,
)
from conjoin_cloud.generated.auth._scim import (
    AsyncAuthSCIMsResource,
    AuthSCIMsResource,
)
from conjoin_cloud.generated.auth._scim_management import (
    AsyncAuthSCIMManagementsResource,
    AuthSCIMManagementsResource,
)
from conjoin_cloud.generated.auth._slo import (
    AsyncAuthSLOsResource,
    AuthSLOsResource,
)
from conjoin_cloud.generated.auth._sso_portal import (
    AsyncAuthSSOPortalsResource,
    AuthSSOPortalsResource,
)
from conjoin_cloud.generated.auth._session import (
    AsyncAuthSessionsResource,
    AuthSessionsResource,
)
from conjoin_cloud.generated.auth._step_up import (
    AsyncAuthStepUpsResource,
    AuthStepUpsResource,
)
from conjoin_cloud.generated.auth._trusted_device import (
    AsyncAuthTrustedDevicesResource,
    AuthTrustedDevicesResource,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client
        self.accounts = AuthAccountsResource(client)
        self.account_recoveries = AuthAccountRecoveriesResource(client)
        self.apps = AuthAppsResource(client)
        self.authorizations = AuthAuthorizationsResource(client)
        self.clients = AuthClientsResource(client)
        self.connections = AuthConnectionsResource(client)
        self.connection_enterprises = AuthConnectionEnterprisesResource(client)
        self.credentials = AuthCredentialsResource(client)
        self.deprovisionings = AuthDeprovisioningsResource(client)
        self.flows = AuthFlowsResource(client)
        self.guards = AuthGuardsResource(client)
        self.identities = AuthIdentitiesResource(client)
        self.organizations = AuthOrganizationsResource(client)
        self.organization_domains = AuthOrganizationDomainsResource(client)
        self.organization_groups = AuthOrganizationGroupsResource(client)
        self.organization_invitations = AuthOrganizationInvitationsResource(client)
        self.organization_memberships = AuthOrganizationMembershipsResource(client)
        self.organization_permissions = AuthOrganizationPermissionsResource(client)
        self.organization_roles = AuthOrganizationRolesResource(client)
        self.organization_role_permissions = AuthOrganizationRolePermissionsResource(client)
        self.passkeys = AuthPasskeysResource(client)
        self.policies = AuthPoliciesResource(client)
        self.resource_grants = AuthResourceGrantsResource(client)
        self.role_assignment_logs = AuthRoleAssignmentLogsResource(client)
        self.scim = AuthSCIMsResource(client)
        self.scim_managements = AuthSCIMManagementsResource(client)
        self.slo = AuthSLOsResource(client)
        self.sso_portals = AuthSSOPortalsResource(client)
        self.sessions = AuthSessionsResource(client)
        self.step_ups = AuthStepUpsResource(client)
        self.trusted_devices = AuthTrustedDevicesResource(client)


class AsyncAuthResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client
        self.accounts = AsyncAuthAccountsResource(client)
        self.account_recoveries = AsyncAuthAccountRecoveriesResource(client)
        self.apps = AsyncAuthAppsResource(client)
        self.authorizations = AsyncAuthAuthorizationsResource(client)
        self.clients = AsyncAuthClientsResource(client)
        self.connections = AsyncAuthConnectionsResource(client)
        self.connection_enterprises = AsyncAuthConnectionEnterprisesResource(client)
        self.credentials = AsyncAuthCredentialsResource(client)
        self.deprovisionings = AsyncAuthDeprovisioningsResource(client)
        self.flows = AsyncAuthFlowsResource(client)
        self.guards = AsyncAuthGuardsResource(client)
        self.identities = AsyncAuthIdentitiesResource(client)
        self.organizations = AsyncAuthOrganizationsResource(client)
        self.organization_domains = AsyncAuthOrganizationDomainsResource(client)
        self.organization_groups = AsyncAuthOrganizationGroupsResource(client)
        self.organization_invitations = AsyncAuthOrganizationInvitationsResource(client)
        self.organization_memberships = AsyncAuthOrganizationMembershipsResource(client)
        self.organization_permissions = AsyncAuthOrganizationPermissionsResource(client)
        self.organization_roles = AsyncAuthOrganizationRolesResource(client)
        self.organization_role_permissions = AsyncAuthOrganizationRolePermissionsResource(client)
        self.passkeys = AsyncAuthPasskeysResource(client)
        self.policies = AsyncAuthPoliciesResource(client)
        self.resource_grants = AsyncAuthResourceGrantsResource(client)
        self.role_assignment_logs = AsyncAuthRoleAssignmentLogsResource(client)
        self.scim = AsyncAuthSCIMsResource(client)
        self.scim_managements = AsyncAuthSCIMManagementsResource(client)
        self.slo = AsyncAuthSLOsResource(client)
        self.sso_portals = AsyncAuthSSOPortalsResource(client)
        self.sessions = AsyncAuthSessionsResource(client)
        self.step_ups = AsyncAuthStepUpsResource(client)
        self.trusted_devices = AsyncAuthTrustedDevicesResource(client)
