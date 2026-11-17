from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AiPolicyCreateCheckRequest,
    AiPolicyCreateCheckResponse,
    AiPolicyCreateRuleRequest,
    AiPolicyCreateRuleResponse,
    AiPolicyDeleteRuleResponse,
    AiPolicyListLogsCountQuery,
    AiPolicyListLogsCountResponse,
    AiPolicyListLogsItem,
    AiPolicyListLogsQuery,
    AiPolicyListRulesCountQuery,
    AiPolicyListRulesCountResponse,
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

    def create_check(
        self,
        data: AiPolicyCreateCheckRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyCreateCheckResponse:
        return self._client.request(
            'POST',
            'ai/policy-checks/',
            body=data,
            cast_to=AiPolicyCreateCheckResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def list_logs(
        self,
        query: AiPolicyListLogsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AiPolicyListLogsItem]:
        return self._client.request(
            'GET',
            'ai/policy-logs/',
            query=query,
            cast_to=Page[AiPolicyListLogsItem],
            request_options=request_options,
        )

    def list_logs_count(
        self,
        query: AiPolicyListLogsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyListLogsCountResponse:
        return self._client.request(
            'GET',
            'ai/policy-logs/count',
            query=query,
            cast_to=AiPolicyListLogsCountResponse,
            request_options=request_options,
        )

    def list_rules(
        self,
        query: AiPolicyListRulesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AiPolicyListRulesItem]:
        return self._client.request(
            'GET',
            'ai/policy-rules/',
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
            'ai/policy-rules/',
            body=data,
            cast_to=AiPolicyCreateRuleResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def list_rules_count(
        self,
        query: AiPolicyListRulesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyListRulesCountResponse:
        return self._client.request(
            'GET',
            'ai/policy-rules/count',
            query=query,
            cast_to=AiPolicyListRulesCountResponse,
            request_options=request_options,
        )

    def read_rule(
        self,
        policy_rule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyReadRuleResponse:
        return self._client.request(
            'GET',
            f'ai/policy-rules/{encode_path_param(policy_rule_id)}',
            cast_to=AiPolicyReadRuleResponse,
            request_options=request_options,
        )

    def update_rule(
        self,
        policy_rule_id: str,
        data: AiPolicyUpdateRuleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyUpdateRuleResponse:
        return self._client.request(
            'PATCH',
            f'ai/policy-rules/{encode_path_param(policy_rule_id)}',
            body=data,
            cast_to=AiPolicyUpdateRuleResponse,
            request_options=request_options,
        )

    def delete_rule(
        self,
        policy_rule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyDeleteRuleResponse:
        return self._client.request(
            'DELETE',
            f'ai/policy-rules/{encode_path_param(policy_rule_id)}',
            cast_to=AiPolicyDeleteRuleResponse,
            request_options=request_options,
        )


class AsyncAiPoliciesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create_check(
        self,
        data: AiPolicyCreateCheckRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyCreateCheckResponse:
        return await self._client.request(
            'POST',
            'ai/policy-checks/',
            body=data,
            cast_to=AiPolicyCreateCheckResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def list_logs(
        self,
        query: AiPolicyListLogsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AiPolicyListLogsItem]:
        return await self._client.request(
            'GET',
            'ai/policy-logs/',
            query=query,
            cast_to=AsyncPage[AiPolicyListLogsItem],
            request_options=request_options,
        )

    async def list_logs_count(
        self,
        query: AiPolicyListLogsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyListLogsCountResponse:
        return await self._client.request(
            'GET',
            'ai/policy-logs/count',
            query=query,
            cast_to=AiPolicyListLogsCountResponse,
            request_options=request_options,
        )

    async def list_rules(
        self,
        query: AiPolicyListRulesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AiPolicyListRulesItem]:
        return await self._client.request(
            'GET',
            'ai/policy-rules/',
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
            'ai/policy-rules/',
            body=data,
            cast_to=AiPolicyCreateRuleResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def list_rules_count(
        self,
        query: AiPolicyListRulesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyListRulesCountResponse:
        return await self._client.request(
            'GET',
            'ai/policy-rules/count',
            query=query,
            cast_to=AiPolicyListRulesCountResponse,
            request_options=request_options,
        )

    async def read_rule(
        self,
        policy_rule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyReadRuleResponse:
        return await self._client.request(
            'GET',
            f'ai/policy-rules/{encode_path_param(policy_rule_id)}',
            cast_to=AiPolicyReadRuleResponse,
            request_options=request_options,
        )

    async def update_rule(
        self,
        policy_rule_id: str,
        data: AiPolicyUpdateRuleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyUpdateRuleResponse:
        return await self._client.request(
            'PATCH',
            f'ai/policy-rules/{encode_path_param(policy_rule_id)}',
            body=data,
            cast_to=AiPolicyUpdateRuleResponse,
            request_options=request_options,
        )

    async def delete_rule(
        self,
        policy_rule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiPolicyDeleteRuleResponse:
        return await self._client.request(
            'DELETE',
            f'ai/policy-rules/{encode_path_param(policy_rule_id)}',
            cast_to=AiPolicyDeleteRuleResponse,
            request_options=request_options,
        )
