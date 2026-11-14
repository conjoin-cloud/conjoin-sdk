from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthAccountAddEmailRequest,
    AuthAccountAddEmailResponse,
    AuthAccountAddPhoneRequest,
    AuthAccountAddPhoneResponse,
    AuthAccountCreateRequest,
    AuthAccountCreateResponse,
    AuthAccountDeleteResponse,
    AuthAccountExportResponse,
    AuthAccountGrantGlobalRoleRequest,
    AuthAccountGrantGlobalRoleResponse,
    AuthAccountImportPasswordHashesRequest,
    AuthAccountImportPasswordHashesResponse,
    AuthAccountListCountQuery,
    AuthAccountListCountResponse,
    AuthAccountListCredentialsCountQuery,
    AuthAccountListCredentialsCountResponse,
    AuthAccountListCredentialsItem,
    AuthAccountListCredentialsQuery,
    AuthAccountListItem,
    AuthAccountListOrganizationMembershipsCountQuery,
    AuthAccountListOrganizationMembershipsCountResponse,
    AuthAccountListOrganizationMembershipsItem,
    AuthAccountListOrganizationMembershipsQuery,
    AuthAccountListQuery,
    AuthAccountMergeRequest,
    AuthAccountMergeResponse,
    AuthAccountReadCredentialResponse,
    AuthAccountReadResponse,
    AuthAccountRemoveCredentialResponse,
    AuthAccountRemoveEmailRequest,
    AuthAccountRemoveEmailResponse,
    AuthAccountRemovePhoneRequest,
    AuthAccountRemovePhoneResponse,
    AuthAccountRevokeGlobalRoleRequest,
    AuthAccountRevokeGlobalRoleResponse,
    AuthAccountUpdateRequest,
    AuthAccountUpdateResponse,
    AuthAccountVerifyCredentialMfaTotpRequest,
    AuthAccountVerifyCredentialMfaTotpResponse,
    AuthAccountVerifyCredentialRequest,
    AuthAccountVerifyCredentialResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthAccountsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_credentials(
        self,
        account_id: str,
        query: AuthAccountListCredentialsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthAccountListCredentialsItem]:
        return self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/credentials',
            query=query,
            cast_to=Page[AuthAccountListCredentialsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def verify_credential(
        self,
        account_id: str,
        data: AuthAccountVerifyCredentialRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountVerifyCredentialResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/credentials/verify',
            body=data,
            cast_to=AuthAccountVerifyCredentialResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def verify_credential_mfa_totp(
        self,
        account_id: str,
        data: AuthAccountVerifyCredentialMfaTotpRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountVerifyCredentialMfaTotpResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/totp-credentials/verify',
            body=data,
            cast_to=AuthAccountVerifyCredentialMfaTotpResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_credentials_count(
        self,
        account_id: str,
        query: AuthAccountListCredentialsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountListCredentialsCountResponse:
        return self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/credentials/count',
            query=query,
            cast_to=AuthAccountListCredentialsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read_credential(
        self,
        account_id: str,
        credential_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountReadCredentialResponse:
        return self._client.request(
            'GET',
            (
                f'auth/accounts/{encode_path_param(account_id)}/credentials'
                f'/{encode_path_param(credential_id)}'
            ),
            cast_to=AuthAccountReadCredentialResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def remove_credential(
        self,
        account_id: str,
        credential_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRemoveCredentialResponse:
        return self._client.request(
            'POST',
            (
                f'auth/accounts/{encode_path_param(account_id)}/credentials'
                f'/{encode_path_param(credential_id)}/remove'
            ),
            cast_to=AuthAccountRemoveCredentialResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list(
        self,
        query: AuthAccountListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthAccountListItem]:
        return self._client.request(
            'GET',
            'auth/accounts/',
            query=query,
            cast_to=Page[AuthAccountListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create(
        self,
        data: AuthAccountCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountCreateResponse:
        return self._client.request(
            'POST',
            'auth/accounts/',
            body=data,
            cast_to=AuthAccountCreateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_organization_memberships(
        self,
        account_id: str,
        query: AuthAccountListOrganizationMembershipsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthAccountListOrganizationMembershipsItem]:
        return self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/organizations',
            query=query,
            cast_to=Page[AuthAccountListOrganizationMembershipsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_count(
        self,
        query: AuthAccountListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountListCountResponse:
        return self._client.request(
            'GET',
            'auth/accounts/count',
            query=query,
            cast_to=AuthAccountListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def merge(
        self,
        data: AuthAccountMergeRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountMergeResponse:
        return self._client.request(
            'POST',
            'auth/accounts/merge',
            body=data,
            cast_to=AuthAccountMergeResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountReadResponse:
        return self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}',
            cast_to=AuthAccountReadResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update(
        self,
        account_id: str,
        data: AuthAccountUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountUpdateResponse:
        return self._client.request(
            'PATCH',
            f'auth/accounts/{encode_path_param(account_id)}',
            body=data,
            cast_to=AuthAccountUpdateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def delete(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountDeleteResponse:
        return self._client.request(
            'DELETE',
            f'auth/accounts/{encode_path_param(account_id)}',
            cast_to=AuthAccountDeleteResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def add_email(
        self,
        account_id: str,
        data: AuthAccountAddEmailRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountAddEmailResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/emails/add',
            body=data,
            cast_to=AuthAccountAddEmailResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def remove_email(
        self,
        account_id: str,
        data: AuthAccountRemoveEmailRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRemoveEmailResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/emails/remove',
            body=data,
            cast_to=AuthAccountRemoveEmailResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def add_phone(
        self,
        account_id: str,
        data: AuthAccountAddPhoneRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountAddPhoneResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/phones/add',
            body=data,
            cast_to=AuthAccountAddPhoneResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def remove_phone(
        self,
        account_id: str,
        data: AuthAccountRemovePhoneRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRemovePhoneResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/phones/remove',
            body=data,
            cast_to=AuthAccountRemovePhoneResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def grant_global_role(
        self,
        account_id: str,
        data: AuthAccountGrantGlobalRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountGrantGlobalRoleResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/global-roles/grant',
            body=data,
            cast_to=AuthAccountGrantGlobalRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def revoke_global_role(
        self,
        account_id: str,
        data: AuthAccountRevokeGlobalRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRevokeGlobalRoleResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/global-roles/revoke',
            body=data,
            cast_to=AuthAccountRevokeGlobalRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_organization_memberships_count(
        self,
        account_id: str,
        query: AuthAccountListOrganizationMembershipsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountListOrganizationMembershipsCountResponse:
        return self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/organizations/count',
            query=query,
            cast_to=AuthAccountListOrganizationMembershipsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def export(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountExportResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/export',
            cast_to=AuthAccountExportResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def import_password_hashes(
        self,
        data: AuthAccountImportPasswordHashesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountImportPasswordHashesResponse:
        return self._client.request(
            'POST',
            'auth/accounts/import-password-hashes',
            body=data,
            cast_to=AuthAccountImportPasswordHashesResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthAccountsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_credentials(
        self,
        account_id: str,
        query: AuthAccountListCredentialsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthAccountListCredentialsItem]:
        return await self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/credentials',
            query=query,
            cast_to=AsyncPage[AuthAccountListCredentialsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def verify_credential(
        self,
        account_id: str,
        data: AuthAccountVerifyCredentialRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountVerifyCredentialResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/credentials/verify',
            body=data,
            cast_to=AuthAccountVerifyCredentialResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def verify_credential_mfa_totp(
        self,
        account_id: str,
        data: AuthAccountVerifyCredentialMfaTotpRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountVerifyCredentialMfaTotpResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/totp-credentials/verify',
            body=data,
            cast_to=AuthAccountVerifyCredentialMfaTotpResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_credentials_count(
        self,
        account_id: str,
        query: AuthAccountListCredentialsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountListCredentialsCountResponse:
        return await self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/credentials/count',
            query=query,
            cast_to=AuthAccountListCredentialsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read_credential(
        self,
        account_id: str,
        credential_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountReadCredentialResponse:
        return await self._client.request(
            'GET',
            (
                f'auth/accounts/{encode_path_param(account_id)}/credentials'
                f'/{encode_path_param(credential_id)}'
            ),
            cast_to=AuthAccountReadCredentialResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def remove_credential(
        self,
        account_id: str,
        credential_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRemoveCredentialResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/accounts/{encode_path_param(account_id)}/credentials'
                f'/{encode_path_param(credential_id)}/remove'
            ),
            cast_to=AuthAccountRemoveCredentialResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list(
        self,
        query: AuthAccountListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthAccountListItem]:
        return await self._client.request(
            'GET',
            'auth/accounts/',
            query=query,
            cast_to=AsyncPage[AuthAccountListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create(
        self,
        data: AuthAccountCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountCreateResponse:
        return await self._client.request(
            'POST',
            'auth/accounts/',
            body=data,
            cast_to=AuthAccountCreateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_organization_memberships(
        self,
        account_id: str,
        query: AuthAccountListOrganizationMembershipsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthAccountListOrganizationMembershipsItem]:
        return await self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/organizations',
            query=query,
            cast_to=AsyncPage[AuthAccountListOrganizationMembershipsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_count(
        self,
        query: AuthAccountListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountListCountResponse:
        return await self._client.request(
            'GET',
            'auth/accounts/count',
            query=query,
            cast_to=AuthAccountListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def merge(
        self,
        data: AuthAccountMergeRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountMergeResponse:
        return await self._client.request(
            'POST',
            'auth/accounts/merge',
            body=data,
            cast_to=AuthAccountMergeResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountReadResponse:
        return await self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}',
            cast_to=AuthAccountReadResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update(
        self,
        account_id: str,
        data: AuthAccountUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'auth/accounts/{encode_path_param(account_id)}',
            body=data,
            cast_to=AuthAccountUpdateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def delete(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'auth/accounts/{encode_path_param(account_id)}',
            cast_to=AuthAccountDeleteResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def add_email(
        self,
        account_id: str,
        data: AuthAccountAddEmailRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountAddEmailResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/emails/add',
            body=data,
            cast_to=AuthAccountAddEmailResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def remove_email(
        self,
        account_id: str,
        data: AuthAccountRemoveEmailRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRemoveEmailResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/emails/remove',
            body=data,
            cast_to=AuthAccountRemoveEmailResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def add_phone(
        self,
        account_id: str,
        data: AuthAccountAddPhoneRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountAddPhoneResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/phones/add',
            body=data,
            cast_to=AuthAccountAddPhoneResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def remove_phone(
        self,
        account_id: str,
        data: AuthAccountRemovePhoneRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRemovePhoneResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/phones/remove',
            body=data,
            cast_to=AuthAccountRemovePhoneResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def grant_global_role(
        self,
        account_id: str,
        data: AuthAccountGrantGlobalRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountGrantGlobalRoleResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/global-roles/grant',
            body=data,
            cast_to=AuthAccountGrantGlobalRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def revoke_global_role(
        self,
        account_id: str,
        data: AuthAccountRevokeGlobalRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRevokeGlobalRoleResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/global-roles/revoke',
            body=data,
            cast_to=AuthAccountRevokeGlobalRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_organization_memberships_count(
        self,
        account_id: str,
        query: AuthAccountListOrganizationMembershipsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountListOrganizationMembershipsCountResponse:
        return await self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/organizations/count',
            query=query,
            cast_to=AuthAccountListOrganizationMembershipsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def export(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountExportResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/export',
            cast_to=AuthAccountExportResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def import_password_hashes(
        self,
        data: AuthAccountImportPasswordHashesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountImportPasswordHashesResponse:
        return await self._client.request(
            'POST',
            'auth/accounts/import-password-hashes',
            body=data,
            cast_to=AuthAccountImportPasswordHashesResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
