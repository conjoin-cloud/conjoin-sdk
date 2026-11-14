from __future__ import annotations

from typing import TYPE_CHECKING

from conjoin_cloud.generated.frontend.auth._account import (
    AsyncAuthAccountsResource,
    AuthAccountsResource,
)
from conjoin_cloud.generated.frontend.auth._client import (
    AsyncAuthClientsResource,
    AuthClientsResource,
)
from conjoin_cloud.generated.frontend.auth._connection_enterprise import (
    AsyncAuthConnectionEnterprisesResource,
    AuthConnectionEnterprisesResource,
)
from conjoin_cloud.generated.frontend.auth._flow import (
    AsyncAuthFlowsResource,
    AuthFlowsResource,
)
from conjoin_cloud.generated.frontend.auth._native import (
    AsyncAuthNativesResource,
    AuthNativesResource,
)
from conjoin_cloud.generated.frontend.auth._organization_domain import (
    AsyncAuthOrganizationDomainsResource,
    AuthOrganizationDomainsResource,
)
from conjoin_cloud.generated.frontend.auth._organization_invitation import (
    AsyncAuthOrganizationInvitationsResource,
    AuthOrganizationInvitationsResource,
)
from conjoin_cloud.generated.frontend.auth._sso_portal import (
    AsyncAuthSSOPortalsResource,
    AuthSSOPortalsResource,
)
from conjoin_cloud.generated.frontend.auth._self import (
    AsyncAuthSelvesResource,
    AuthSelvesResource,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client
        self.accounts = AuthAccountsResource(client)
        self.clients = AuthClientsResource(client)
        self.connection_enterprises = AuthConnectionEnterprisesResource(client)
        self.flows = AuthFlowsResource(client)
        self.natives = AuthNativesResource(client)
        self.organization_domains = AuthOrganizationDomainsResource(client)
        self.organization_invitations = AuthOrganizationInvitationsResource(client)
        self.sso_portals = AuthSSOPortalsResource(client)
        self.selves = AuthSelvesResource(client)


class AsyncAuthResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client
        self.accounts = AsyncAuthAccountsResource(client)
        self.clients = AsyncAuthClientsResource(client)
        self.connection_enterprises = AsyncAuthConnectionEnterprisesResource(client)
        self.flows = AsyncAuthFlowsResource(client)
        self.natives = AsyncAuthNativesResource(client)
        self.organization_domains = AsyncAuthOrganizationDomainsResource(client)
        self.organization_invitations = AsyncAuthOrganizationInvitationsResource(client)
        self.sso_portals = AsyncAuthSSOPortalsResource(client)
        self.selves = AsyncAuthSelvesResource(client)
