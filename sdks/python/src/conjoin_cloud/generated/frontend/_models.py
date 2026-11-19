from __future__ import annotations

from collections.abc import Sequence
from typing import Any, TypedDict

from conjoin_cloud._models import ConjoinModel


class AuthAccountBatchLookupItem(ConjoinModel):
    account_id: str
    image_url: str | None
    name: str | None


class AuthClientGetJwksResponse(ConjoinModel):
    keys: Sequence[dict[str, Any]]


class AuthClientGetOidcDiscoveryResponse(ConjoinModel):
    authorization_endpoint: str
    claims_supported: Sequence[str]
    end_session_endpoint: str
    id_token_signing_alg_values_supported: Sequence[str]
    issuer: str
    jwks_uri: str
    response_types_supported: Sequence[str]
    scopes_supported: Sequence[str]
    subject_types_supported: Sequence[str]
    token_endpoint: str
    userinfo_endpoint: str


class AuthClientProcessHandshakeResponse(ConjoinModel):
    access_token_ttl_seconds: float
    account_id: str
    exp: float
    iat: float
    session_id: str


class AuthClientProcessLogoutResponse(ConjoinModel):
    success: bool


class AuthConnectionEnterpriseConfigureSsoPortalConnectionResponse(ConjoinModel):
    app_id: str
    configuration: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    connection_id: str
    date_created: str
    date_updated: str
    identity: str
    is_enterprise: bool
    live_mode: bool
    name: str | None
    organization_id: str | None
    status: str


class AuthConnectionEnterpriseImportSsoPortalMetadataResponse(ConjoinModel):
    app_id: str
    configuration: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    connection_id: str
    date_created: str
    date_updated: str
    identity: str
    is_enterprise: bool
    live_mode: bool
    name: str | None
    organization_id: str | None
    status: str


class AuthConnectionEnterpriseUpdateSsoPortalConnectionResponse(ConjoinModel):
    app_id: str
    configuration: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    connection_id: str
    date_created: str
    date_updated: str
    identity: str
    is_enterprise: bool
    live_mode: bool
    name: str | None
    organization_id: str | None
    status: str


class AuthFlowCompletePasswordResetResponse(ConjoinModel):
    account_id: str | None = None
    mfa: dict[str, Any] | None = None
    redirect_url: str | None = None
    session_id: str | None = None
    state: str | None = None
    status: str | None = None
    step_up: dict[str, Any] | None = None
    trusted_device_token: str | None = None
    verification: dict[str, Any] | None = None
    verification_method: str | None = None


class AuthFlowCompleteSigninResponse(ConjoinModel):
    account_id: str | None = None
    mfa: dict[str, Any] | None = None
    redirect_url: str | None = None
    session_id: str | None = None
    state: str | None = None
    status: str | None = None
    step_up: dict[str, Any] | None = None
    trusted_device_token: str | None = None
    verification: dict[str, Any] | None = None
    verification_method: str | None = None


class AuthFlowCompleteSignupResponse(ConjoinModel):
    account_id: str | None = None
    mfa: dict[str, Any] | None = None
    redirect_url: str | None = None
    session_id: str | None = None
    state: str | None = None
    status: str | None = None
    step_up: dict[str, Any] | None = None
    trusted_device_token: str | None = None
    verification: dict[str, Any] | None = None
    verification_method: str | None = None


class AuthFlowConfirmLinkSignupResponse(ConjoinModel):
    account_id: str | None = None
    mfa: dict[str, Any] | None = None
    redirect_url: str | None = None
    session_id: str | None = None
    state: str | None = None
    status: str | None = None
    step_up: dict[str, Any] | None = None
    trusted_device_token: str | None = None
    verification: dict[str, Any] | None = None
    verification_method: str | None = None


class AuthFlowStartPasswordResetResponse(ConjoinModel):
    account_id: str | None = None
    mfa: dict[str, Any] | None = None
    redirect_url: str | None = None
    session_id: str | None = None
    state: str | None = None
    status: str | None = None
    step_up: dict[str, Any] | None = None
    trusted_device_token: str | None = None
    verification: dict[str, Any] | None = None
    verification_method: str | None = None


class AuthFlowStartSigninResponse(ConjoinModel):
    account_id: str | None = None
    mfa: dict[str, Any] | None = None
    redirect_url: str | None = None
    session_id: str | None = None
    state: str | None = None
    status: str | None = None
    step_up: dict[str, Any] | None = None
    trusted_device_token: str | None = None
    verification: dict[str, Any] | None = None
    verification_method: str | None = None


class AuthFlowStartSignupResponse(ConjoinModel):
    account_id: str | None = None
    mfa: dict[str, Any] | None = None
    redirect_url: str | None = None
    session_id: str | None = None
    state: str | None = None
    status: str | None = None
    step_up: dict[str, Any] | None = None
    trusted_device_token: str | None = None
    verification: dict[str, Any] | None = None
    verification_method: str | None = None


class AuthNativeCompleteSigninResponse(ConjoinModel):
    account_id: str | None = None
    client_handle: dict[str, Any] | None = None
    mfa: dict[str, Any] | None = None
    redirect_url: str | None = None
    session_id: str | None = None
    state: str | None = None
    status: str | None = None
    step_up: dict[str, Any] | None = None
    trusted_device_token: str | None = None
    verification: dict[str, Any] | None = None
    verification_method: str | None = None


class AuthNativeCompleteSignupResponse(ConjoinModel):
    account_id: str | None = None
    client_handle: dict[str, Any] | None = None
    mfa: dict[str, Any] | None = None
    redirect_url: str | None = None
    session_id: str | None = None
    state: str | None = None
    status: str | None = None
    step_up: dict[str, Any] | None = None
    trusted_device_token: str | None = None
    verification: dict[str, Any] | None = None
    verification_method: str | None = None


class AuthNativeConfirmLinkSignupResponse(ConjoinModel):
    account_id: str | None = None
    client_handle: dict[str, Any] | None = None
    mfa: dict[str, Any] | None = None
    redirect_url: str | None = None
    session_id: str | None = None
    state: str | None = None
    status: str | None = None
    step_up: dict[str, Any] | None = None
    trusted_device_token: str | None = None
    verification: dict[str, Any] | None = None
    verification_method: str | None = None


class AuthNativeProcessLogoutResponse(ConjoinModel):
    success: bool


class AuthNativeProcessTokenMintResponse(ConjoinModel):
    access_token: str
    account_id: str
    expires_in: float
    refresh_token: str
    session_id: str
    token_type: Any


class AuthNativeRefreshSessionResponse(ConjoinModel):
    access_token: str
    account_id: str
    expires_in: float
    refresh_token: str
    session_id: str
    token_type: Any


class AuthNativeStartSigninResponse(ConjoinModel):
    account_id: str | None = None
    client_handle: dict[str, Any] | None = None
    mfa: dict[str, Any] | None = None
    redirect_url: str | None = None
    session_id: str | None = None
    state: str | None = None
    status: str | None = None
    step_up: dict[str, Any] | None = None
    trusted_device_token: str | None = None
    verification: dict[str, Any] | None = None
    verification_method: str | None = None


class AuthNativeStartSignupResponse(ConjoinModel):
    account_id: str | None = None
    client_handle: dict[str, Any] | None = None
    mfa: dict[str, Any] | None = None
    redirect_url: str | None = None
    session_id: str | None = None
    state: str | None = None
    status: str | None = None
    step_up: dict[str, Any] | None = None
    trusted_device_token: str | None = None
    verification: dict[str, Any] | None = None
    verification_method: str | None = None


class AuthOrganizationDomainVerifySsoPortalDomainResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    domain: str
    last_checked_at: str | None
    live_mode: bool
    organization_domain_id: str
    organization_id: str
    recheck: dict[str, Any] | None
    verification: dict[str, Any]
    verification_hostname: str
    verification_record_value: str
    verification_token: str


class AuthOrganizationInvitationAcceptResponse(ConjoinModel):
    invitation: dict[str, Any]
    next_action: str


class AuthSSOPortalReadSsoPortalCatalogResponse(ConjoinModel):
    providers: Sequence[dict[str, Any]]


class AuthSSOPortalReadSsoPortalContextResponse(ConjoinModel):
    allowed_providers: Sequence[str]
    organization_id: str
    providers: Sequence[dict[str, Any]]
    require_domain_verification: bool
    setup_intents: Sequence[str]


class AuthSSOPortalStartSsoPortalTestResponse(ConjoinModel):
    redirect_url: str


class AuthSelfListOrganizationsCountResponse(ConjoinModel):
    count: int


class AuthSelfListOrganizationsItem(ConjoinModel):
    account_id: str
    account_organization_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    joined_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    organization_id: str
    roles: Sequence[str] | None = None
    status: str


class AuthSelfListSessionsCountResponse(ConjoinModel):
    count: int


class AuthSelfListSessionsItem(ConjoinModel):
    account_id: str
    app_id: str
    client_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    expires_at: str | None = None
    last_activity: dict[str, Any] | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    revoked_at: str | None = None
    revoked_reason: str | None = None
    session_id: str
    status: str


class AuthSelfReadActiveOrganizationResponse(ConjoinModel):
    active_organization_id: str | None
    active_organization_roles: Sequence[str]


class AuthSelfReadProfileResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    custom_attributes: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    dormant_at: str | None = None
    emails: Sequence[dict[str, Any]] | None = None
    global_roles: Sequence[str] | None = None
    image_url: str | None = None
    last_active_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str | None = None
    phones: Sequence[dict[str, Any]] | None = None
    reference_id: str | None = None
    status: str


class AuthSelfRevokeSessionResponse(ConjoinModel):
    revoked_count: float
    session_ids: Sequence[str] | None = None


class AuthSelfUpdateActiveOrganizationResponse(ConjoinModel):
    active_organization_id: str | None


class AuthSelfUpdateProfileResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    custom_attributes: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    dormant_at: str | None = None
    emails: Sequence[dict[str, Any]] | None = None
    global_roles: Sequence[str] | None = None
    image_url: str | None = None
    last_active_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str | None = None
    phones: Sequence[dict[str, Any]] | None = None
    reference_id: str | None = None
    status: str


class BillingSelfListEntitlementOverridesCountResponse(ConjoinModel):
    count: int


class BillingSelfListEntitlementOverridesItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    effective_from: str
    effective_to: str | None = None
    entity_id: str
    feature_id: str
    included_units: float | None = None
    is_active: bool
    live_mode: bool
    override_id: str
    plan_id: str
    reason: str | None = None
    soft_limit: bool | None = None
    subscription_id: str
    value_type: str


class BillingSelfListPriceBundlesCountResponse(ConjoinModel):
    count: int


class BillingSelfListPriceBundlesItem(ConjoinModel):
    authoring_mode: str
    auto_activate: bool
    compatible_bundle_ids: Sequence[str] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    discount_coupon_id: str | None = None
    entity_id: str
    is_default_tier: bool
    items: Sequence[dict[str, Any]]
    live_mode: bool
    managed_catalog: dict[str, Any] | None = None
    min_tier_rank: float | None = None
    name: str
    price_bundle_id: str
    reference_id: str
    required_tier_group: str | None = None
    status: str
    tier_group: str | None = None
    tier_rank: float | None = None


class CloudBrandingReadPublicProjectResponse(ConjoinModel):
    accessibility: dict[str, Any] | None = None
    animation: dict[str, Any] | None = None
    borders: dict[str, Any] | None = None
    branding_id: str
    colors: dict[str, Any] | None = None
    components: dict[str, Any] | None = None
    date_created: str
    date_updated: str | None = None
    general: dict[str, Any] | None = None
    layout: dict[str, Any] | None = None
    organization: dict[str, Any] | None = None
    project_id: str
    schema_version: float
    shadows: dict[str, Any] | None = None
    spacing: dict[str, Any] | None = None
    typography: dict[str, Any] | None = None


class CloudSDKReadSdkSettingsResponse(ConjoinModel):
    api_url: str
    auth: dict[str, Any] | None
    branding: dict[str, Any] | None
    environment: str
    project_id: str
    relay: dict[str, Any]


class AuthAccountBatchLookupRequest(TypedDict):
    account_ids: Sequence[str]


class AuthFlowCompletePasswordResetRequest(TypedDict):
    new_password: str
    reset_token: str


class _AuthFlowCompleteSigninRequestRequired(TypedDict):
    verification_result: dict[str, Any]


class AuthFlowCompleteSigninRequest(_AuthFlowCompleteSigninRequestRequired, total=False):
    mfa: dict[str, Any]
    remember_device: bool
    trusted_device_token: str


class _AuthFlowCompleteSignupRequestRequired(TypedDict):
    verification_result: dict[str, Any]


class AuthFlowCompleteSignupRequest(_AuthFlowCompleteSignupRequestRequired, total=False):
    password: str


class _AuthFlowConfirmLinkSignupRequestRequired(TypedDict):
    confirm: Any


class AuthFlowConfirmLinkSignupRequest(_AuthFlowConfirmLinkSignupRequestRequired, total=False):
    step_up: dict[str, Any]


class _AuthFlowStartPasswordResetRequestRequired(TypedDict):
    email: str


class AuthFlowStartPasswordResetRequest(_AuthFlowStartPasswordResetRequestRequired, total=False):
    phone: str


class AuthFlowStartSigninRequest(TypedDict, total=False):
    email: str
    password: str
    phone: str
    provider_key: str
    remember_device: bool
    trusted_device_token: str
    verification_option: str


class AuthFlowStartSignupRequest(TypedDict, total=False):
    email: str
    password: str
    phone: str
    provider_key: str
    verification_option: str


class _AuthNativeCompleteSigninRequestRequired(TypedDict):
    verification_result: dict[str, Any]


class AuthNativeCompleteSigninRequest(_AuthNativeCompleteSigninRequestRequired, total=False):
    mfa: dict[str, Any]
    remember_device: bool
    trusted_device_token: str


class _AuthNativeCompleteSignupRequestRequired(TypedDict):
    verification_result: dict[str, Any]


class AuthNativeCompleteSignupRequest(_AuthNativeCompleteSignupRequestRequired, total=False):
    password: str


class _AuthNativeConfirmLinkSignupRequestRequired(TypedDict):
    confirm: Any


class AuthNativeConfirmLinkSignupRequest(_AuthNativeConfirmLinkSignupRequestRequired, total=False):
    step_up: dict[str, Any]


class AuthNativeRefreshSessionRequest(TypedDict, total=False):
    refresh_token: str


class AuthNativeStartSigninRequest(TypedDict, total=False):
    email: str
    password: str
    phone: str
    provider_key: str
    remember_device: bool
    trusted_device_token: str
    verification_option: str


class AuthNativeStartSignupRequest(TypedDict, total=False):
    email: str
    password: str
    phone: str
    provider_key: str
    verification_option: str


class AuthOrganizationDomainVerifySsoPortalDomainRequest(TypedDict):
    domain: str


class _AuthOrganizationInvitationAcceptRequestRequired(TypedDict):
    token: str


class AuthOrganizationInvitationAcceptRequest(
    _AuthOrganizationInvitationAcceptRequestRequired,
    total=False,
):
    account_id: str


class AuthSSOPortalStartSsoPortalTestRequest(TypedDict):
    connection_id: str


class AuthSelfListOrganizationsCountQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthSelfListOrganizationsQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthSelfListSessionsCountQuery(TypedDict, total=False):
    status: str
    include_expired: Any
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthSelfListSessionsQuery(TypedDict, total=False):
    status: str
    include_expired: Any
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthSelfUpdateActiveOrganizationRequest(TypedDict):
    organization_id: str | None


class AuthSelfUpdateProfileRequest(TypedDict, total=False):
    image_url: str | None
    name: str
    primary_email: str
    primary_phone: str


class BillingSelfListEntitlementOverridesCountQuery(TypedDict, total=False):
    feature_id: str
    subscription_id: str
    is_active: Any
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingSelfListEntitlementOverridesQuery(TypedDict, total=False):
    feature_id: str
    subscription_id: str
    is_active: Any
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingSelfListPriceBundlesCountQuery(TypedDict, total=False):
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingSelfListPriceBundlesQuery(TypedDict, total=False):
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudBrandingReadPublicProjectQuery(TypedDict, total=False):
    organization_id: str
