from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import AUTH_NONE, RequestOptions
from conjoin_cloud.generated.frontend._models import (
    AuthOrganizationInvitationAcceptRequest,
    AuthOrganizationInvitationAcceptResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthOrganizationInvitationsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def accept(
        self,
        data: AuthOrganizationInvitationAcceptRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationInvitationAcceptResponse:
        return self._client.request(
            'POST',
            'auth/client/invitations/accept',
            body=data,
            cast_to=AuthOrganizationInvitationAcceptResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )


class AsyncAuthOrganizationInvitationsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def accept(
        self,
        data: AuthOrganizationInvitationAcceptRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationInvitationAcceptResponse:
        return await self._client.request(
            'POST',
            'auth/client/invitations/accept',
            body=data,
            cast_to=AuthOrganizationInvitationAcceptResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )
