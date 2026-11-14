from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthGuardAddAnonymousIpsRequest,
    AuthGuardAddAnonymousIpsResponse,
    AuthGuardAddTrustedDomainRequest,
    AuthGuardAddTrustedDomainResponse,
    AuthGuardAddTrustedEmailRequest,
    AuthGuardAddTrustedEmailResponse,
    AuthGuardAddTrustedIpRequest,
    AuthGuardAddTrustedIpResponse,
    AuthGuardCreateRuleRequest,
    AuthGuardCreateRuleResponse,
    AuthGuardDeleteRuleResponse,
    AuthGuardListAnonymousIpsResponse,
    AuthGuardListEventsCountQuery,
    AuthGuardListEventsCountResponse,
    AuthGuardListEventsItem,
    AuthGuardListEventsQuery,
    AuthGuardListRulesCountQuery,
    AuthGuardListRulesCountResponse,
    AuthGuardListRulesItem,
    AuthGuardListRulesQuery,
    AuthGuardReadRuleResponse,
    AuthGuardRemoveAnonymousIpsRequest,
    AuthGuardRemoveAnonymousIpsResponse,
    AuthGuardRemoveTrustedDomainRequest,
    AuthGuardRemoveTrustedDomainResponse,
    AuthGuardRemoveTrustedEmailRequest,
    AuthGuardRemoveTrustedEmailResponse,
    AuthGuardRemoveTrustedIpRequest,
    AuthGuardRemoveTrustedIpResponse,
    AuthGuardUpdateRuleRequest,
    AuthGuardUpdateRuleResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthGuardsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_rules(
        self,
        query: AuthGuardListRulesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthGuardListRulesItem]:
        return self._client.request(
            'GET',
            'auth/guard-rules',
            query=query,
            cast_to=Page[AuthGuardListRulesItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create_rule(
        self,
        data: AuthGuardCreateRuleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardCreateRuleResponse:
        return self._client.request(
            'POST',
            'auth/guard-rules',
            body=data,
            cast_to=AuthGuardCreateRuleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_rules_count(
        self,
        query: AuthGuardListRulesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardListRulesCountResponse:
        return self._client.request(
            'GET',
            'auth/guard-rules/count',
            query=query,
            cast_to=AuthGuardListRulesCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read_rule(
        self,
        guard_rule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardReadRuleResponse:
        return self._client.request(
            'GET',
            f'auth/guard-rules/{encode_path_param(guard_rule_id)}',
            cast_to=AuthGuardReadRuleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update_rule(
        self,
        guard_rule_id: str,
        data: AuthGuardUpdateRuleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardUpdateRuleResponse:
        return self._client.request(
            'PATCH',
            f'auth/guard-rules/{encode_path_param(guard_rule_id)}',
            body=data,
            cast_to=AuthGuardUpdateRuleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def delete_rule(
        self,
        guard_rule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardDeleteRuleResponse:
        return self._client.request(
            'DELETE',
            f'auth/guard-rules/{encode_path_param(guard_rule_id)}',
            cast_to=AuthGuardDeleteRuleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_events(
        self,
        query: AuthGuardListEventsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthGuardListEventsItem]:
        return self._client.request(
            'GET',
            'auth/guard-events',
            query=query,
            cast_to=Page[AuthGuardListEventsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_events_count(
        self,
        query: AuthGuardListEventsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardListEventsCountResponse:
        return self._client.request(
            'GET',
            'auth/guard-events/count',
            query=query,
            cast_to=AuthGuardListEventsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def add_trusted_ip(
        self,
        data: AuthGuardAddTrustedIpRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardAddTrustedIpResponse:
        return self._client.request(
            'POST',
            'auth/guard-trusted-ips',
            body=data,
            cast_to=AuthGuardAddTrustedIpResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def remove_trusted_ip(
        self,
        data: AuthGuardRemoveTrustedIpRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardRemoveTrustedIpResponse:
        return self._client.request(
            'POST',
            'auth/guard-trusted-ips/remove',
            body=data,
            cast_to=AuthGuardRemoveTrustedIpResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def add_trusted_email(
        self,
        data: AuthGuardAddTrustedEmailRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardAddTrustedEmailResponse:
        return self._client.request(
            'POST',
            'auth/guard-trusted-emails',
            body=data,
            cast_to=AuthGuardAddTrustedEmailResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def remove_trusted_email(
        self,
        data: AuthGuardRemoveTrustedEmailRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardRemoveTrustedEmailResponse:
        return self._client.request(
            'POST',
            'auth/guard-trusted-emails/remove',
            body=data,
            cast_to=AuthGuardRemoveTrustedEmailResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def add_trusted_domain(
        self,
        data: AuthGuardAddTrustedDomainRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardAddTrustedDomainResponse:
        return self._client.request(
            'POST',
            'auth/guard-trusted-domains',
            body=data,
            cast_to=AuthGuardAddTrustedDomainResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def remove_trusted_domain(
        self,
        data: AuthGuardRemoveTrustedDomainRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardRemoveTrustedDomainResponse:
        return self._client.request(
            'POST',
            'auth/guard-trusted-domains/remove',
            body=data,
            cast_to=AuthGuardRemoveTrustedDomainResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_anonymous_ips(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardListAnonymousIpsResponse:
        return self._client.request(
            'GET',
            'auth/guard-anonymous-ips',
            cast_to=AuthGuardListAnonymousIpsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def add_anonymous_ips(
        self,
        data: AuthGuardAddAnonymousIpsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardAddAnonymousIpsResponse:
        return self._client.request(
            'POST',
            'auth/guard-anonymous-ips',
            body=data,
            cast_to=AuthGuardAddAnonymousIpsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def remove_anonymous_ips(
        self,
        data: AuthGuardRemoveAnonymousIpsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardRemoveAnonymousIpsResponse:
        return self._client.request(
            'POST',
            'auth/guard-anonymous-ips/remove',
            body=data,
            cast_to=AuthGuardRemoveAnonymousIpsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthGuardsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_rules(
        self,
        query: AuthGuardListRulesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthGuardListRulesItem]:
        return await self._client.request(
            'GET',
            'auth/guard-rules',
            query=query,
            cast_to=AsyncPage[AuthGuardListRulesItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create_rule(
        self,
        data: AuthGuardCreateRuleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardCreateRuleResponse:
        return await self._client.request(
            'POST',
            'auth/guard-rules',
            body=data,
            cast_to=AuthGuardCreateRuleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_rules_count(
        self,
        query: AuthGuardListRulesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardListRulesCountResponse:
        return await self._client.request(
            'GET',
            'auth/guard-rules/count',
            query=query,
            cast_to=AuthGuardListRulesCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read_rule(
        self,
        guard_rule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardReadRuleResponse:
        return await self._client.request(
            'GET',
            f'auth/guard-rules/{encode_path_param(guard_rule_id)}',
            cast_to=AuthGuardReadRuleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update_rule(
        self,
        guard_rule_id: str,
        data: AuthGuardUpdateRuleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardUpdateRuleResponse:
        return await self._client.request(
            'PATCH',
            f'auth/guard-rules/{encode_path_param(guard_rule_id)}',
            body=data,
            cast_to=AuthGuardUpdateRuleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def delete_rule(
        self,
        guard_rule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardDeleteRuleResponse:
        return await self._client.request(
            'DELETE',
            f'auth/guard-rules/{encode_path_param(guard_rule_id)}',
            cast_to=AuthGuardDeleteRuleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_events(
        self,
        query: AuthGuardListEventsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthGuardListEventsItem]:
        return await self._client.request(
            'GET',
            'auth/guard-events',
            query=query,
            cast_to=AsyncPage[AuthGuardListEventsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_events_count(
        self,
        query: AuthGuardListEventsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardListEventsCountResponse:
        return await self._client.request(
            'GET',
            'auth/guard-events/count',
            query=query,
            cast_to=AuthGuardListEventsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def add_trusted_ip(
        self,
        data: AuthGuardAddTrustedIpRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardAddTrustedIpResponse:
        return await self._client.request(
            'POST',
            'auth/guard-trusted-ips',
            body=data,
            cast_to=AuthGuardAddTrustedIpResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def remove_trusted_ip(
        self,
        data: AuthGuardRemoveTrustedIpRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardRemoveTrustedIpResponse:
        return await self._client.request(
            'POST',
            'auth/guard-trusted-ips/remove',
            body=data,
            cast_to=AuthGuardRemoveTrustedIpResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def add_trusted_email(
        self,
        data: AuthGuardAddTrustedEmailRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardAddTrustedEmailResponse:
        return await self._client.request(
            'POST',
            'auth/guard-trusted-emails',
            body=data,
            cast_to=AuthGuardAddTrustedEmailResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def remove_trusted_email(
        self,
        data: AuthGuardRemoveTrustedEmailRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardRemoveTrustedEmailResponse:
        return await self._client.request(
            'POST',
            'auth/guard-trusted-emails/remove',
            body=data,
            cast_to=AuthGuardRemoveTrustedEmailResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def add_trusted_domain(
        self,
        data: AuthGuardAddTrustedDomainRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardAddTrustedDomainResponse:
        return await self._client.request(
            'POST',
            'auth/guard-trusted-domains',
            body=data,
            cast_to=AuthGuardAddTrustedDomainResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def remove_trusted_domain(
        self,
        data: AuthGuardRemoveTrustedDomainRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardRemoveTrustedDomainResponse:
        return await self._client.request(
            'POST',
            'auth/guard-trusted-domains/remove',
            body=data,
            cast_to=AuthGuardRemoveTrustedDomainResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_anonymous_ips(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardListAnonymousIpsResponse:
        return await self._client.request(
            'GET',
            'auth/guard-anonymous-ips',
            cast_to=AuthGuardListAnonymousIpsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def add_anonymous_ips(
        self,
        data: AuthGuardAddAnonymousIpsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardAddAnonymousIpsResponse:
        return await self._client.request(
            'POST',
            'auth/guard-anonymous-ips',
            body=data,
            cast_to=AuthGuardAddAnonymousIpsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def remove_anonymous_ips(
        self,
        data: AuthGuardRemoveAnonymousIpsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthGuardRemoveAnonymousIpsResponse:
        return await self._client.request(
            'POST',
            'auth/guard-anonymous-ips/remove',
            body=data,
            cast_to=AuthGuardRemoveAnonymousIpsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
