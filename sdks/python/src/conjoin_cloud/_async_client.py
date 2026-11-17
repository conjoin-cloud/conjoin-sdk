from __future__ import annotations

import inspect
from collections.abc import Awaitable, Callable, Mapping, Sequence
from dataclasses import replace
from typing import Any, TypeVar, cast, overload

import httpx

from conjoin_cloud._async_transport import read_response, send_call
from conjoin_cloud._call import prepare_call
from conjoin_cloud._config import (
    ConjoinScope,
    ResolvedConfig,
    ScopeName,
    resolve_config,
    resolve_scope,
)
from conjoin_cloud._declared_headers import DeclaredHeader
from conjoin_cloud._errors import ConjoinConfigurationError
from conjoin_cloud._models import AsyncPage
from conjoin_cloud._request_options import AuthOverride, DeclaredAuth, RequestOptions
from conjoin_cloud._request_tracing import resolve_conjoin_request_id
from conjoin_cloud._response import WithResponse
from conjoin_cloud._response_parsing import with_response as build_with_response
from conjoin_cloud.generated import AsyncGeneratedResourcesMixin

T = TypeVar("T")


class AsyncConjoin(AsyncGeneratedResourcesMixin):
    config: ResolvedConfig

    def __init__(
        self,
        *,
        api_key: str | None = None,
        publishable_key: str | None = None,
        base_url: str | None = None,
        api_version: str | None = None,
        timeout: float | None = None,
        conjoin_request_id: str | None = None,
        max_retries: int | None = None,
        backoff_seconds: float | None = None,
        max_retry_delay_seconds: float | None = None,
        billing_entity_id: str | None = None,
        messaging_profile_id: str | None = None,
        auth_app_id: str | None = None,
        http_client: httpx.AsyncClient | None = None,
        strict_response_validation: bool = False,
    ) -> None:
        if http_client is not None and not isinstance(http_client, httpx.AsyncClient):
            raise ConjoinConfigurationError("AsyncConjoin requires an httpx.AsyncClient")

        config = resolve_config(
            api_key=api_key,
            publishable_key=publishable_key,
            base_url=base_url,
            api_version=api_version,
            timeout=timeout,
            conjoin_request_id=conjoin_request_id,
            max_retries=max_retries,
            backoff_seconds=backoff_seconds,
            max_retry_delay_seconds=max_retry_delay_seconds,
            strict_response_validation=strict_response_validation,
            scope=ConjoinScope(
                billing_entity_id=billing_entity_id,
                messaging_profile_id=messaging_profile_id,
                auth_app_id=auth_app_id,
            ),
        )
        owned_client = http_client is None
        self._attach(
            config,
            httpx.AsyncClient() if http_client is None else http_client,
            owned_client,
        )

    def _attach(self, config: ResolvedConfig, client: httpx.AsyncClient, owns_client: bool) -> None:
        self.config = config
        self._client = client
        self._owns_client = owns_client
        self.with_response = _AsyncConjoinWithResponse(self)
        self._init_generated_resources()

    def _derive(self, config: ResolvedConfig) -> AsyncConjoin:
        derived = AsyncConjoin.__new__(AsyncConjoin)
        derived._attach(config, self._client, False)
        return derived

    @overload
    async def request(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None = None,
        body: Any = None,
        cast_to: type[T],
        request_options: RequestOptions | Mapping[str, Any] | None = None,
        with_response: bool = False,
        scopes: Sequence[ScopeName] = (),
        accepts_idempotency_key: bool = False,
        default_auth: AuthOverride | DeclaredAuth | None = None,
        declared_headers: Sequence[DeclaredHeader] = (),
        unwrap_data: bool = True,
    ) -> T: ...

    @overload
    async def request(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None = None,
        body: Any = None,
        cast_to: Any = None,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
        with_response: bool = False,
        scopes: Sequence[ScopeName] = (),
        accepts_idempotency_key: bool = False,
        default_auth: AuthOverride | DeclaredAuth | None = None,
        declared_headers: Sequence[DeclaredHeader] = (),
        unwrap_data: bool = True,
    ) -> Any: ...

    async def request(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None = None,
        body: Any = None,
        cast_to: Any = None,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
        with_response: bool = False,
        scopes: Sequence[ScopeName] = (),
        accepts_idempotency_key: bool = False,
        default_auth: AuthOverride | DeclaredAuth | None = None,
        declared_headers: Sequence[DeclaredHeader] = (),
        unwrap_data: bool = True,
    ) -> Any:
        call = prepare_call(
            self.config,
            method,
            path,
            query=query,
            body=body,
            request_options=request_options,
            scopes=scopes,
            accepts_idempotency_key=accepts_idempotency_key,
            default_auth=default_auth,
            declared_headers=declared_headers,
        )
        response = await send_call(self._client, self.config, call, buffer_response=True)
        data, request_id = await read_response(
            response,
            call,
            cast_to=cast_to,
            strict=self.config.strict_response_validation,
            unwrap_data=unwrap_data,
        )

        if isinstance(data, AsyncPage):
            data._fetch_next = self._next_page_fetcher(
                method,
                path,
                query=query,
                body=body,
                cast_to=cast_to,
                request_options=request_options,
                scopes=scopes,
                accepts_idempotency_key=accepts_idempotency_key,
                default_auth=default_auth,
                declared_headers=declared_headers,
            )

        if with_response:
            return build_with_response(response, data, request_id)
        return data

    def _next_page_fetcher(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None,
        body: Any,
        cast_to: Any,
        request_options: RequestOptions | Mapping[str, Any] | None,
        scopes: Sequence[ScopeName],
        accepts_idempotency_key: bool,
        default_auth: AuthOverride | DeclaredAuth | None,
        declared_headers: Sequence[DeclaredHeader],
    ) -> Callable[[str], Awaitable[Any]]:
        async def fetch_next(next_cursor: str) -> Any:
            return await self.request(
                method,
                path,
                query={**(query or {}), "cursor": {"next": next_cursor}},
                body=body,
                cast_to=cast_to,
                request_options=request_options,
                scopes=scopes,
                accepts_idempotency_key=accepts_idempotency_key,
                default_auth=default_auth,
                declared_headers=declared_headers,
            )

        return fetch_next

    def with_scope(
        self,
        *,
        billing_entity_id: str | None = None,
        messaging_profile_id: str | None = None,
        auth_app_id: str | None = None,
    ) -> AsyncConjoin:
        current = self.config.scope
        scope = ConjoinScope(
            billing_entity_id=billing_entity_id
            if billing_entity_id is not None
            else current.billing_entity_id,
            messaging_profile_id=messaging_profile_id
            if messaging_profile_id is not None
            else current.messaging_profile_id,
            auth_app_id=auth_app_id if auth_app_id is not None else current.auth_app_id,
        )
        return self._derive(replace(self.config, scope=resolve_scope(scope)))

    async def with_request_trace(
        self,
        callback: Callable[[AsyncConjoin, str], T | Awaitable[T]],
        request_id: str | None = None,
    ) -> T:
        resolved_request_id = resolve_conjoin_request_id(
            request_id if request_id is not None else self.config.conjoin_request_id
        )
        scoped_client = self._derive(replace(self.config, conjoin_request_id=resolved_request_id))
        result = callback(scoped_client, resolved_request_id)

        if inspect.isawaitable(result):
            return await result

        return cast(T, result)

    async def aclose(self) -> None:
        if self._owns_client:
            await self._client.aclose()

    async def __aenter__(self) -> AsyncConjoin:
        return self

    async def __aexit__(self, exc_type: object, exc: object, traceback: object) -> None:
        await self.aclose()


class _AsyncConjoinWithResponse:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def request(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None = None,
        body: Any = None,
        cast_to: Any = None,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
        scopes: Sequence[ScopeName] = (),
        accepts_idempotency_key: bool = False,
    ) -> WithResponse[Any]:
        return await self._client.request(
            method,
            path,
            query=query,
            body=body,
            cast_to=cast_to,
            request_options=request_options,
            with_response=True,
            scopes=scopes,
            accepts_idempotency_key=accepts_idempotency_key,
        )
