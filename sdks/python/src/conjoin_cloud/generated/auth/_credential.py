from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthCredentialActivateSmsMfaRequest,
    AuthCredentialActivateSmsMfaResponse,
    AuthCredentialActivateTotpRequest,
    AuthCredentialActivateTotpResponse,
    AuthCredentialConsumeTotpRecoveryCodeRequest,
    AuthCredentialConsumeTotpRecoveryCodeResponse,
    AuthCredentialCreatePasswordRequest,
    AuthCredentialCreatePasswordResponse,
    AuthCredentialEnrollSmsMfaRequest,
    AuthCredentialEnrollSmsMfaResponse,
    AuthCredentialEnrollTotpRequest,
    AuthCredentialEnrollTotpResponse,
    AuthCredentialIssueApiKeyRequest,
    AuthCredentialIssueApiKeyResponse,
    AuthCredentialReadApiKeyUsageResponse,
    AuthCredentialRevokeApiKeyRequest,
    AuthCredentialRevokeApiKeyResponse,
    AuthCredentialRotateApiKeyRequest,
    AuthCredentialRotateApiKeyResponse,
    AuthCredentialRotatePasswordRequest,
    AuthCredentialRotatePasswordResponse,
    AuthCredentialRotateTotpRecoveryCodesRequest,
    AuthCredentialRotateTotpRecoveryCodesResponse,
    AuthCredentialSendSmsMfaActivationCodeResponse,
    AuthCredentialSendSmsMfaChallengeResponse,
    AuthCredentialStartPasskeyRegistrationRequest,
    AuthCredentialStartPasskeyRegistrationResponse,
    AuthCredentialStartPasskeyenticationResponse,
    AuthCredentialUpdateApiKeyRequest,
    AuthCredentialUpdateApiKeyResponse,
    AuthCredentialVerifyPasskeyRegistrationRequest,
    AuthCredentialVerifyPasskeyRegistrationResponse,
    AuthCredentialVerifyPasskeyenticationRequest,
    AuthCredentialVerifyPasskeyenticationResponse,
    AuthCredentialVerifySmsMfaRequest,
    AuthCredentialVerifySmsMfaResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthCredentialsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def update_api_key(
        self,
        account_id: str,
        credential_id: str,
        data: AuthCredentialUpdateApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialUpdateApiKeyResponse:
        return self._client.request(
            'PATCH',
            (
                f'auth/accounts/{encode_path_param(account_id)}/credentials'
                f'/{encode_path_param(credential_id)}'
            ),
            body=data,
            cast_to=AuthCredentialUpdateApiKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create_password(
        self,
        account_id: str,
        data: AuthCredentialCreatePasswordRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialCreatePasswordResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/password-credentials',
            body=data,
            cast_to=AuthCredentialCreatePasswordResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def rotate_password(
        self,
        account_id: str,
        data: AuthCredentialRotatePasswordRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialRotatePasswordResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/password-credentials/rotate',
            body=data,
            cast_to=AuthCredentialRotatePasswordResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def enroll_totp(
        self,
        account_id: str,
        data: AuthCredentialEnrollTotpRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialEnrollTotpResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/totp-credentials/enroll',
            body=data,
            cast_to=AuthCredentialEnrollTotpResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def activate_totp(
        self,
        account_id: str,
        data: AuthCredentialActivateTotpRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialActivateTotpResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/totp-credentials/activate',
            body=data,
            cast_to=AuthCredentialActivateTotpResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def rotate_totp_recovery_codes(
        self,
        account_id: str,
        data: AuthCredentialRotateTotpRecoveryCodesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialRotateTotpRecoveryCodesResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/totp-recovery-codes/rotate',
            body=data,
            cast_to=AuthCredentialRotateTotpRecoveryCodesResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def consume_totp_recovery_code(
        self,
        account_id: str,
        data: AuthCredentialConsumeTotpRecoveryCodeRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialConsumeTotpRecoveryCodeResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/totp-recovery-codes/consume',
            body=data,
            cast_to=AuthCredentialConsumeTotpRecoveryCodeResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def enroll_sms_mfa(
        self,
        account_id: str,
        data: AuthCredentialEnrollSmsMfaRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialEnrollSmsMfaResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sms-credentials/enroll',
            body=data,
            cast_to=AuthCredentialEnrollSmsMfaResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def send_sms_mfa_activation_code(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialSendSmsMfaActivationCodeResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sms-credentials/send-activation-code',
            cast_to=AuthCredentialSendSmsMfaActivationCodeResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def activate_sms_mfa(
        self,
        account_id: str,
        data: AuthCredentialActivateSmsMfaRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialActivateSmsMfaResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sms-credentials/activate',
            body=data,
            cast_to=AuthCredentialActivateSmsMfaResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def verify_sms_mfa(
        self,
        account_id: str,
        data: AuthCredentialVerifySmsMfaRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialVerifySmsMfaResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sms-credentials/verify',
            body=data,
            cast_to=AuthCredentialVerifySmsMfaResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def send_sms_mfa_challenge(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialSendSmsMfaChallengeResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sms-credentials/send-challenge',
            cast_to=AuthCredentialSendSmsMfaChallengeResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read_api_key_usage(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialReadApiKeyUsageResponse:
        return self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/api-key-credentials/usage-stats',
            cast_to=AuthCredentialReadApiKeyUsageResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def issue_api_key(
        self,
        account_id: str,
        data: AuthCredentialIssueApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialIssueApiKeyResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/api-key-credentials',
            body=data,
            cast_to=AuthCredentialIssueApiKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def rotate_api_key(
        self,
        account_id: str,
        credential_id: str,
        data: AuthCredentialRotateApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialRotateApiKeyResponse:
        return self._client.request(
            'POST',
            (
                f'auth/accounts/{encode_path_param(account_id)}/credentials'
                f'/{encode_path_param(credential_id)}/rotate'
            ),
            body=data,
            cast_to=AuthCredentialRotateApiKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def revoke_api_key(
        self,
        account_id: str,
        credential_id: str,
        data: AuthCredentialRevokeApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialRevokeApiKeyResponse:
        return self._client.request(
            'POST',
            (
                f'auth/accounts/{encode_path_param(account_id)}/credentials'
                f'/{encode_path_param(credential_id)}/revoke'
            ),
            body=data,
            cast_to=AuthCredentialRevokeApiKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def start_passkey_registration(
        self,
        account_id: str,
        data: AuthCredentialStartPasskeyRegistrationRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialStartPasskeyRegistrationResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/passkey-registrations/start',
            body=data,
            cast_to=AuthCredentialStartPasskeyRegistrationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def verify_passkey_registration(
        self,
        account_id: str,
        data: AuthCredentialVerifyPasskeyRegistrationRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialVerifyPasskeyRegistrationResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/passkey-registrations/verify',
            body=data,
            cast_to=AuthCredentialVerifyPasskeyRegistrationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def start_passkeyentication(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialStartPasskeyenticationResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/passkey-authentications/start',
            cast_to=AuthCredentialStartPasskeyenticationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def verify_passkeyentication(
        self,
        account_id: str,
        data: AuthCredentialVerifyPasskeyenticationRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialVerifyPasskeyenticationResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/passkey-authentications/verify',
            body=data,
            cast_to=AuthCredentialVerifyPasskeyenticationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthCredentialsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def update_api_key(
        self,
        account_id: str,
        credential_id: str,
        data: AuthCredentialUpdateApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialUpdateApiKeyResponse:
        return await self._client.request(
            'PATCH',
            (
                f'auth/accounts/{encode_path_param(account_id)}/credentials'
                f'/{encode_path_param(credential_id)}'
            ),
            body=data,
            cast_to=AuthCredentialUpdateApiKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create_password(
        self,
        account_id: str,
        data: AuthCredentialCreatePasswordRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialCreatePasswordResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/password-credentials',
            body=data,
            cast_to=AuthCredentialCreatePasswordResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def rotate_password(
        self,
        account_id: str,
        data: AuthCredentialRotatePasswordRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialRotatePasswordResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/password-credentials/rotate',
            body=data,
            cast_to=AuthCredentialRotatePasswordResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def enroll_totp(
        self,
        account_id: str,
        data: AuthCredentialEnrollTotpRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialEnrollTotpResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/totp-credentials/enroll',
            body=data,
            cast_to=AuthCredentialEnrollTotpResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def activate_totp(
        self,
        account_id: str,
        data: AuthCredentialActivateTotpRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialActivateTotpResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/totp-credentials/activate',
            body=data,
            cast_to=AuthCredentialActivateTotpResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def rotate_totp_recovery_codes(
        self,
        account_id: str,
        data: AuthCredentialRotateTotpRecoveryCodesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialRotateTotpRecoveryCodesResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/totp-recovery-codes/rotate',
            body=data,
            cast_to=AuthCredentialRotateTotpRecoveryCodesResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def consume_totp_recovery_code(
        self,
        account_id: str,
        data: AuthCredentialConsumeTotpRecoveryCodeRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialConsumeTotpRecoveryCodeResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/totp-recovery-codes/consume',
            body=data,
            cast_to=AuthCredentialConsumeTotpRecoveryCodeResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def enroll_sms_mfa(
        self,
        account_id: str,
        data: AuthCredentialEnrollSmsMfaRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialEnrollSmsMfaResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sms-credentials/enroll',
            body=data,
            cast_to=AuthCredentialEnrollSmsMfaResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def send_sms_mfa_activation_code(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialSendSmsMfaActivationCodeResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sms-credentials/send-activation-code',
            cast_to=AuthCredentialSendSmsMfaActivationCodeResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def activate_sms_mfa(
        self,
        account_id: str,
        data: AuthCredentialActivateSmsMfaRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialActivateSmsMfaResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sms-credentials/activate',
            body=data,
            cast_to=AuthCredentialActivateSmsMfaResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def verify_sms_mfa(
        self,
        account_id: str,
        data: AuthCredentialVerifySmsMfaRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialVerifySmsMfaResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sms-credentials/verify',
            body=data,
            cast_to=AuthCredentialVerifySmsMfaResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def send_sms_mfa_challenge(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialSendSmsMfaChallengeResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sms-credentials/send-challenge',
            cast_to=AuthCredentialSendSmsMfaChallengeResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read_api_key_usage(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialReadApiKeyUsageResponse:
        return await self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/api-key-credentials/usage-stats',
            cast_to=AuthCredentialReadApiKeyUsageResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def issue_api_key(
        self,
        account_id: str,
        data: AuthCredentialIssueApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialIssueApiKeyResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/api-key-credentials',
            body=data,
            cast_to=AuthCredentialIssueApiKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def rotate_api_key(
        self,
        account_id: str,
        credential_id: str,
        data: AuthCredentialRotateApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialRotateApiKeyResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/accounts/{encode_path_param(account_id)}/credentials'
                f'/{encode_path_param(credential_id)}/rotate'
            ),
            body=data,
            cast_to=AuthCredentialRotateApiKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def revoke_api_key(
        self,
        account_id: str,
        credential_id: str,
        data: AuthCredentialRevokeApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialRevokeApiKeyResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/accounts/{encode_path_param(account_id)}/credentials'
                f'/{encode_path_param(credential_id)}/revoke'
            ),
            body=data,
            cast_to=AuthCredentialRevokeApiKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def start_passkey_registration(
        self,
        account_id: str,
        data: AuthCredentialStartPasskeyRegistrationRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialStartPasskeyRegistrationResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/passkey-registrations/start',
            body=data,
            cast_to=AuthCredentialStartPasskeyRegistrationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def verify_passkey_registration(
        self,
        account_id: str,
        data: AuthCredentialVerifyPasskeyRegistrationRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialVerifyPasskeyRegistrationResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/passkey-registrations/verify',
            body=data,
            cast_to=AuthCredentialVerifyPasskeyRegistrationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def start_passkeyentication(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialStartPasskeyenticationResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/passkey-authentications/start',
            cast_to=AuthCredentialStartPasskeyenticationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def verify_passkeyentication(
        self,
        account_id: str,
        data: AuthCredentialVerifyPasskeyenticationRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthCredentialVerifyPasskeyenticationResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/passkey-authentications/verify',
            body=data,
            cast_to=AuthCredentialVerifyPasskeyenticationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
