from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import AUTH_NONE, RequestOptions, scim_bearer_auth
from conjoin_cloud._url import encode_path_param
from conjoin_cloud._wire import wire_names
from conjoin_cloud.generated._models import (
    AuthSCIMScimBulkOperationsRequest,
    AuthSCIMScimBulkOperationsResponse,
    AuthSCIMScimCreateGroupRequest,
    AuthSCIMScimCreateGroupResponse,
    AuthSCIMScimCreateUserRequest,
    AuthSCIMScimCreateUserResponse,
    AuthSCIMScimGetGroupResponse,
    AuthSCIMScimGetResourceTypesResponse,
    AuthSCIMScimGetSchemasResponse,
    AuthSCIMScimGetServiceProviderConfigResponse,
    AuthSCIMScimGetUserResponse,
    AuthSCIMScimListGroupsResponse,
    AuthSCIMScimListUsersResponse,
    AuthSCIMScimPatchGroupMembersRequest,
    AuthSCIMScimPatchGroupMembersResponse,
    AuthSCIMScimPatchUserResponse,
    AuthSCIMScimReplaceGroupRequest,
    AuthSCIMScimReplaceGroupResponse,
    AuthSCIMScimReplaceUserRequest,
    AuthSCIMScimReplaceUserResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


_SCIM_BULK_OPERATIONS_BODY_ALIASES = {
    'operations': 'Operations',
    'fail_on_errors': 'failOnErrors',
}
_SCIM_CREATE_GROUP_BODY_ALIASES = {
    'display_name': 'displayName',
    'external_id': 'externalId',
}
_SCIM_REPLACE_GROUP_BODY_ALIASES = {
    'display_name': 'displayName',
    'external_id': 'externalId',
}
_SCIM_PATCH_GROUP_MEMBERS_BODY_ALIASES = {
    'operations': 'Operations',
}
_SCIM_CREATE_USER_BODY_ALIASES = {
    'external_id': 'externalId',
    'phone_numbers': 'phoneNumbers',
    'user_name': 'userName',
}
_SCIM_REPLACE_USER_BODY_ALIASES = {
    'external_id': 'externalId',
    'phone_numbers': 'phoneNumbers',
    'user_name': 'userName',
}


class AuthSCIMsResource:
    def __init__(self, client: Conjoin, *, scim_token: str | None = None) -> None:
        self._client = client
        self._scim_token = scim_token

    def with_token(self, scim_token: str) -> AuthSCIMsResource:
        return AuthSCIMsResource(self._client, scim_token=scim_token)

    def scim_bulk_operations(
        self,
        project_id: str,
        app_id: str,
        data: AuthSCIMScimBulkOperationsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimBulkOperationsResponse:
        return self._client.request(
            'POST',
            f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Bulk',
            body=wire_names(data, _SCIM_BULK_OPERATIONS_BODY_ALIASES),
            cast_to=AuthSCIMScimBulkOperationsResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    def scim_list_groups(
        self,
        project_id: str,
        app_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimListGroupsResponse:
        return self._client.request(
            'GET',
            f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Groups',
            cast_to=AuthSCIMScimListGroupsResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    def scim_create_group(
        self,
        project_id: str,
        app_id: str,
        data: AuthSCIMScimCreateGroupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimCreateGroupResponse:
        return self._client.request(
            'POST',
            f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Groups',
            body=wire_names(data, _SCIM_CREATE_GROUP_BODY_ALIASES),
            cast_to=AuthSCIMScimCreateGroupResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    def scim_get_group(
        self,
        project_id: str,
        app_id: str,
        id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimGetGroupResponse:
        return self._client.request(
            'GET',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Groups'
                f'/{encode_path_param(id)}'
            ),
            cast_to=AuthSCIMScimGetGroupResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    def scim_replace_group(
        self,
        project_id: str,
        app_id: str,
        id: str,
        data: AuthSCIMScimReplaceGroupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimReplaceGroupResponse:
        return self._client.request(
            'PUT',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Groups'
                f'/{encode_path_param(id)}'
            ),
            body=wire_names(data, _SCIM_REPLACE_GROUP_BODY_ALIASES),
            cast_to=AuthSCIMScimReplaceGroupResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    def scim_patch_group_members(
        self,
        project_id: str,
        app_id: str,
        id: str,
        data: AuthSCIMScimPatchGroupMembersRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimPatchGroupMembersResponse:
        return self._client.request(
            'PATCH',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Groups'
                f'/{encode_path_param(id)}'
            ),
            body=wire_names(data, _SCIM_PATCH_GROUP_MEMBERS_BODY_ALIASES),
            cast_to=AuthSCIMScimPatchGroupMembersResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    def scim_delete_group(
        self,
        project_id: str,
        app_id: str,
        id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> None:
        self._client.request(
            'DELETE',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Groups'
                f'/{encode_path_param(id)}'
            ),
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
        )

    def scim_get_service_provider_config(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimGetServiceProviderConfigResponse:
        return self._client.request(
            'GET',
            'auth/scim/v2/ServiceProviderConfig',
            cast_to=AuthSCIMScimGetServiceProviderConfigResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
            unwrap_data=False,
        )

    def scim_get_schemas(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimGetSchemasResponse:
        return self._client.request(
            'GET',
            'auth/scim/v2/Schemas',
            cast_to=AuthSCIMScimGetSchemasResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
            unwrap_data=False,
        )

    def scim_get_resource_types(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimGetResourceTypesResponse:
        return self._client.request(
            'GET',
            'auth/scim/v2/ResourceTypes',
            cast_to=AuthSCIMScimGetResourceTypesResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
            unwrap_data=False,
        )

    def scim_list_users(
        self,
        project_id: str,
        app_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimListUsersResponse:
        return self._client.request(
            'GET',
            f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Users',
            cast_to=AuthSCIMScimListUsersResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    def scim_create_user(
        self,
        project_id: str,
        app_id: str,
        data: AuthSCIMScimCreateUserRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimCreateUserResponse:
        return self._client.request(
            'POST',
            f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Users',
            body=wire_names(data, _SCIM_CREATE_USER_BODY_ALIASES),
            cast_to=AuthSCIMScimCreateUserResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    def scim_get_user(
        self,
        project_id: str,
        app_id: str,
        id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimGetUserResponse:
        return self._client.request(
            'GET',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Users'
                f'/{encode_path_param(id)}'
            ),
            cast_to=AuthSCIMScimGetUserResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    def scim_replace_user(
        self,
        project_id: str,
        app_id: str,
        id: str,
        data: AuthSCIMScimReplaceUserRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimReplaceUserResponse:
        return self._client.request(
            'PUT',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Users'
                f'/{encode_path_param(id)}'
            ),
            body=wire_names(data, _SCIM_REPLACE_USER_BODY_ALIASES),
            cast_to=AuthSCIMScimReplaceUserResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    def scim_patch_user(
        self,
        project_id: str,
        app_id: str,
        id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimPatchUserResponse:
        return self._client.request(
            'PATCH',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Users'
                f'/{encode_path_param(id)}'
            ),
            cast_to=AuthSCIMScimPatchUserResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    def scim_deactivate_user(
        self,
        project_id: str,
        app_id: str,
        id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> None:
        self._client.request(
            'DELETE',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Users'
                f'/{encode_path_param(id)}'
            ),
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
        )


class AsyncAuthSCIMsResource:
    def __init__(self, client: AsyncConjoin, *, scim_token: str | None = None) -> None:
        self._client = client
        self._scim_token = scim_token

    def with_token(self, scim_token: str) -> AsyncAuthSCIMsResource:
        return AsyncAuthSCIMsResource(self._client, scim_token=scim_token)

    async def scim_bulk_operations(
        self,
        project_id: str,
        app_id: str,
        data: AuthSCIMScimBulkOperationsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimBulkOperationsResponse:
        return await self._client.request(
            'POST',
            f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Bulk',
            body=wire_names(data, _SCIM_BULK_OPERATIONS_BODY_ALIASES),
            cast_to=AuthSCIMScimBulkOperationsResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    async def scim_list_groups(
        self,
        project_id: str,
        app_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimListGroupsResponse:
        return await self._client.request(
            'GET',
            f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Groups',
            cast_to=AuthSCIMScimListGroupsResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    async def scim_create_group(
        self,
        project_id: str,
        app_id: str,
        data: AuthSCIMScimCreateGroupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimCreateGroupResponse:
        return await self._client.request(
            'POST',
            f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Groups',
            body=wire_names(data, _SCIM_CREATE_GROUP_BODY_ALIASES),
            cast_to=AuthSCIMScimCreateGroupResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    async def scim_get_group(
        self,
        project_id: str,
        app_id: str,
        id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimGetGroupResponse:
        return await self._client.request(
            'GET',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Groups'
                f'/{encode_path_param(id)}'
            ),
            cast_to=AuthSCIMScimGetGroupResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    async def scim_replace_group(
        self,
        project_id: str,
        app_id: str,
        id: str,
        data: AuthSCIMScimReplaceGroupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimReplaceGroupResponse:
        return await self._client.request(
            'PUT',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Groups'
                f'/{encode_path_param(id)}'
            ),
            body=wire_names(data, _SCIM_REPLACE_GROUP_BODY_ALIASES),
            cast_to=AuthSCIMScimReplaceGroupResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    async def scim_patch_group_members(
        self,
        project_id: str,
        app_id: str,
        id: str,
        data: AuthSCIMScimPatchGroupMembersRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimPatchGroupMembersResponse:
        return await self._client.request(
            'PATCH',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Groups'
                f'/{encode_path_param(id)}'
            ),
            body=wire_names(data, _SCIM_PATCH_GROUP_MEMBERS_BODY_ALIASES),
            cast_to=AuthSCIMScimPatchGroupMembersResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    async def scim_delete_group(
        self,
        project_id: str,
        app_id: str,
        id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> None:
        await self._client.request(
            'DELETE',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Groups'
                f'/{encode_path_param(id)}'
            ),
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
        )

    async def scim_get_service_provider_config(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimGetServiceProviderConfigResponse:
        return await self._client.request(
            'GET',
            'auth/scim/v2/ServiceProviderConfig',
            cast_to=AuthSCIMScimGetServiceProviderConfigResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
            unwrap_data=False,
        )

    async def scim_get_schemas(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimGetSchemasResponse:
        return await self._client.request(
            'GET',
            'auth/scim/v2/Schemas',
            cast_to=AuthSCIMScimGetSchemasResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
            unwrap_data=False,
        )

    async def scim_get_resource_types(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimGetResourceTypesResponse:
        return await self._client.request(
            'GET',
            'auth/scim/v2/ResourceTypes',
            cast_to=AuthSCIMScimGetResourceTypesResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
            unwrap_data=False,
        )

    async def scim_list_users(
        self,
        project_id: str,
        app_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimListUsersResponse:
        return await self._client.request(
            'GET',
            f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Users',
            cast_to=AuthSCIMScimListUsersResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    async def scim_create_user(
        self,
        project_id: str,
        app_id: str,
        data: AuthSCIMScimCreateUserRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimCreateUserResponse:
        return await self._client.request(
            'POST',
            f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Users',
            body=wire_names(data, _SCIM_CREATE_USER_BODY_ALIASES),
            cast_to=AuthSCIMScimCreateUserResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    async def scim_get_user(
        self,
        project_id: str,
        app_id: str,
        id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimGetUserResponse:
        return await self._client.request(
            'GET',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Users'
                f'/{encode_path_param(id)}'
            ),
            cast_to=AuthSCIMScimGetUserResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    async def scim_replace_user(
        self,
        project_id: str,
        app_id: str,
        id: str,
        data: AuthSCIMScimReplaceUserRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimReplaceUserResponse:
        return await self._client.request(
            'PUT',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Users'
                f'/{encode_path_param(id)}'
            ),
            body=wire_names(data, _SCIM_REPLACE_USER_BODY_ALIASES),
            cast_to=AuthSCIMScimReplaceUserResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    async def scim_patch_user(
        self,
        project_id: str,
        app_id: str,
        id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMScimPatchUserResponse:
        return await self._client.request(
            'PATCH',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Users'
                f'/{encode_path_param(id)}'
            ),
            cast_to=AuthSCIMScimPatchUserResponse,
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
            unwrap_data=False,
        )

    async def scim_deactivate_user(
        self,
        project_id: str,
        app_id: str,
        id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> None:
        await self._client.request(
            'DELETE',
            (
                f'auth/scim/v2/{encode_path_param(project_id)}/{encode_path_param(app_id)}/Users'
                f'/{encode_path_param(id)}'
            ),
            request_options=request_options,
            default_auth=scim_bearer_auth(self._scim_token),
        )
