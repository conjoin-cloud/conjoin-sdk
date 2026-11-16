from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AiPolicyCheckRequest,
    AiPolicyCheckResponse,
    AiPolicyCreateRuleRequest,
    AiPolicyCreateRuleResponse,
    AiPolicyDeleteRuleResponse,
    AiPolicyListLogsItem,
    AiPolicyListLogsQuery,
    AiPolicyListRulesItem,
    AiPolicyListRulesQuery,
    AiPolicyReadRuleResponse,
    AiPolicyUpdateRuleRequest,
    AiPolicyUpdateRuleResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AiPoliciesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def check(
        self,
        data: AiPolicyCheckRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyCheckResponse:
        return self._client.request(
            'POST',
            'ai/policy/check',
            body=data,
            cast_to=AiPolicyCheckResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def list_rules(
        self,
        query: AiPolicyListRulesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AiPolicyListRulesItem]:
        return self._client.request(
            'GET',
            'ai/policy/rules',
            query=query,
            cast_to=Page[AiPolicyListRulesItem],
            request_options=request_options,
        )

    def create_rule(
        self,
        data: AiPolicyCreateRuleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyCreateRuleResponse:
        return self._client.request(
            'POST',
            'ai/policy/rules',
            body=data,
            cast_to=AiPolicyCreateRuleResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read_rule(
        self,
        rule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyReadRuleResponse:
        return self._client.request(
            'GET',
            f'ai/policy/rules/{encode_path_param(rule_id)}',
            cast_to=AiPolicyReadRuleResponse,
            request_options=request_options,
        )

    def update_rule(
        self,
        rule_id: str,
        data: AiPolicyUpdateRuleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyUpdateRuleResponse:
        return self._client.request(
            'PATCH',
            f'ai/policy/rules/{encode_path_param(rule_id)}',
            body=data,
            cast_to=AiPolicyUpdateRuleResponse,
            request_options=request_options,
        )

    def delete_rule(
        self,
        rule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyDeleteRuleResponse:
        return self._client.request(
            'DELETE',
            f'ai/policy/rules/{encode_path_param(rule_id)}',
            cast_to=AiPolicyDeleteRuleResponse,
            request_options=request_options,
        )

    def list_logs(
        self,
        query: AiPolicyListLogsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AiPolicyListLogsItem]:
        return self._client.request(
            'GET',
            'ai/policy/logs',
            query=query,
            cast_to=Page[AiPolicyListLogsItem],
            request_options=request_options,
        )


class AsyncAiPoliciesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def check(
        self,
        data: AiPolicyCheckRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyCheckResponse:
        return await self._client.request(
            'POST',
            'ai/policy/check',
            body=data,
            cast_to=AiPolicyCheckResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def list_rules(
        self,
        query: AiPolicyListRulesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AiPolicyListRulesItem]:
        return await self._client.request(
            'GET',
            'ai/policy/rules',
            query=query,
            cast_to=AsyncPage[AiPolicyListRulesItem],
            request_options=request_options,
        )

    async def create_rule(
        self,
        data: AiPolicyCreateRuleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyCreateRuleResponse:
        return await self._client.request(
            'POST',
            'ai/policy/rules',
            body=data,
            cast_to=AiPolicyCreateRuleResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read_rule(
        self,
        rule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyReadRuleResponse:
        return await self._client.request(
            'GET',
            f'ai/policy/rules/{encode_path_param(rule_id)}',
            cast_to=AiPolicyReadRuleResponse,
            request_options=request_options,
        )

    async def update_rule(
        self,
        rule_id: str,
        data: AiPolicyUpdateRuleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyUpdateRuleResponse:
        return await self._client.request(
            'PATCH',
            f'ai/policy/rules/{encode_path_param(rule_id)}',
            body=data,
            cast_to=AiPolicyUpdateRuleResponse,
            request_options=request_options,
        )

    async def delete_rule(
        self,
        rule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyDeleteRuleResponse:
        return await self._client.request(
            'DELETE',
            f'ai/policy/rules/{encode_path_param(rule_id)}',
            cast_to=AiPolicyDeleteRuleResponse,
            request_options=request_options,
        )

    async def list_logs(
        self,
        query: AiPolicyListLogsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AiPolicyListLogsItem]:
        return await self._client.request(
            'GET',
            'ai/policy/logs',
            query=query,
            cast_to=AsyncPage[AiPolicyListLogsItem],
            request_options=request_options,
        )
