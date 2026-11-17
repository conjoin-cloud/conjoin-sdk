from __future__ import annotations

from collections.abc import Sequence
from typing import Any, TypedDict

from pydantic import Field

from conjoin_cloud._models import ConjoinModel


class AiBYOKCreateByokConfigResponse(ConjoinModel):
    allowed_models: Sequence[str]
    byok_config_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    endpoint_url: str | None
    has_api_key: bool
    is_enabled: bool
    live_mode: bool
    metadata: dict[str, Any]
    provider: str
    provider_name: str
    reference_id: str | None
    status: str


class AiBYOKDeleteByokConfigResponse(ConjoinModel):
    allowed_models: Sequence[str]
    byok_config_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    endpoint_url: str | None
    has_api_key: bool
    is_enabled: bool
    live_mode: bool
    metadata: dict[str, Any]
    provider: str
    provider_name: str
    reference_id: str | None
    status: str


class AiBYOKListByokConfigsCountResponse(ConjoinModel):
    count: int


class AiBYOKListByokConfigsItem(ConjoinModel):
    allowed_models: Sequence[str]
    byok_config_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    endpoint_url: str | None
    has_api_key: bool
    is_enabled: bool
    live_mode: bool
    metadata: dict[str, Any]
    provider: str
    provider_name: str
    reference_id: str | None
    status: str


class AiBYOKReadByokConfigResponse(ConjoinModel):
    allowed_models: Sequence[str]
    byok_config_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    endpoint_url: str | None
    has_api_key: bool
    is_enabled: bool
    live_mode: bool
    metadata: dict[str, Any]
    provider: str
    provider_name: str
    reference_id: str | None
    status: str


class AiBYOKTestByokConnectionResponse(ConjoinModel):
    connected: bool
    message: str
    provider: str


class AiBYOKUpdateByokConfigResponse(ConjoinModel):
    allowed_models: Sequence[str]
    byok_config_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    endpoint_url: str | None
    has_api_key: bool
    is_enabled: bool
    live_mode: bool
    metadata: dict[str, Any]
    provider: str
    provider_name: str
    reference_id: str | None
    status: str


class AiContextCreateIndexResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    document_count: float
    embedding_dimensions: float
    embedding_model: str
    index_id: str
    last_synced_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any]
    name: str
    reference_id: str | None
    source_config: dict[str, Any]
    source_type: str
    status: str
    sync_status: str
    total_size_bytes: float


class AiContextCreateQueryResponse(ConjoinModel):
    latency_ms: float
    modes_used: Sequence[str]
    query_id: str
    results: Sequence[dict[str, Any]]
    total_results: float


class AiContextDeleteIndexResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    document_count: float
    embedding_dimensions: float
    embedding_model: str
    index_id: str
    last_synced_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any]
    name: str
    reference_id: str | None
    source_config: dict[str, Any]
    source_type: str
    status: str
    sync_status: str
    total_size_bytes: float


class AiContextListIndexesCountResponse(ConjoinModel):
    count: int


class AiContextListIndexesItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    document_count: float
    embedding_dimensions: float
    embedding_model: str
    index_id: str
    last_synced_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any]
    name: str
    reference_id: str | None
    source_config: dict[str, Any]
    source_type: str
    status: str
    sync_status: str
    total_size_bytes: float


class AiContextListQueriesCountResponse(ConjoinModel):
    count: int


class AiContextListQueriesItem(ConjoinModel):
    agentic_reads_count: float
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    fulltext_results_count: float
    index_ids: Sequence[str]
    latency_ms: float
    live_mode: bool
    modes_used: Sequence[str]
    queried_at: str
    query_id: str
    token_cost_usd: float
    total_results_returned: float
    vector_results_count: float


class AiContextReadIndexResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    document_count: float
    embedding_dimensions: float
    embedding_model: str
    index_id: str
    last_synced_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any]
    name: str
    reference_id: str | None
    source_config: dict[str, Any]
    source_type: str
    status: str
    sync_status: str
    total_size_bytes: float


class AiContextSyncIndexResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    document_count: float
    embedding_dimensions: float
    embedding_model: str
    index_id: str
    last_synced_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any]
    name: str
    reference_id: str | None
    source_config: dict[str, Any]
    source_type: str
    status: str
    sync_status: str
    total_size_bytes: float


class AiInferenceCreateAiBestOfNResponse(ConjoinModel):
    candidates: Sequence[dict[str, Any]]
    cost_usd: float
    latency_ms: float
    model: str
    n: float
    request_id: str
    request_type: str
    selected: dict[str, Any]
    token_usage: dict[str, Any]


class AiInferenceCreateAiMultiModelResponse(ConjoinModel):
    cost_usd: float
    latency_ms: float
    models: Sequence[str]
    request_id: str
    request_type: str
    results: Sequence[dict[str, Any]]
    synthesis: dict[str, Any] | None
    token_usage: dict[str, Any]


class AiInferenceCreateChatCompletionResponse(ConjoinModel):
    conjoin: dict[str, Any] = Field(..., alias='_conjoin')
    choices: Sequence[dict[str, Any]]
    created: float
    id: str
    model: str
    object: Any
    usage: dict[str, Any]


class AiInferenceListRequestsCountResponse(ConjoinModel):
    count: int


class AiInferenceListRequestsItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    context_used: bool
    cost_usd: float
    date_created: str
    date_updated: str
    is_byok: bool
    latency_ms: float
    live_mode: bool
    model: str
    policy_applied: bool
    provider: str
    request_id: str
    request_type: str
    status: str
    streaming_enabled: bool
    token_usage: dict[str, Any]
    trace_source: str | None = None


class AiInferenceReadRequestResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    context_used: bool
    cost_usd: float
    date_created: str
    date_updated: str
    is_byok: bool
    latency_ms: float
    live_mode: bool
    model: str
    policy_applied: bool
    provider: str
    request_id: str
    request_type: str
    status: str
    streaming_enabled: bool
    token_usage: dict[str, Any]
    trace_source: str | None = None


class AiModelListCountResponse(ConjoinModel):
    count: int


class AiModelListItem(ConjoinModel):
    capabilities: dict[str, Any]
    context_window: float
    date_created: str
    date_updated: str | None
    deprecation_date: str | None = None
    display_name: str
    is_active: bool
    max_output_tokens: float
    model_id: str
    plan_availability: str
    pricing: dict[str, Any]
    release_date: str | None = None
    vendor: str


class AiModelReadResponse(ConjoinModel):
    capabilities: dict[str, Any]
    context_window: float
    date_created: str
    date_updated: str | None
    deprecation_date: str | None = None
    display_name: str
    is_active: bool
    max_output_tokens: float
    model_id: str
    plan_availability: str
    pricing: dict[str, Any]
    release_date: str | None = None
    vendor: str


class AiPolicyCreateCheckResponse(ConjoinModel):
    action_taken: str
    allowed: bool
    matched_rules: Sequence[dict[str, Any]]
    transformed_content: str | None = None


class AiPolicyCreateRuleResponse(ConjoinModel):
    action: str
    config: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None
    description: str | None = None
    direction: str
    is_active: bool
    live_mode: bool
    metadata: dict[str, Any]
    name: str
    priority: float
    reference_id: str | None
    rule_id: str
    rule_type: str
    status: str


class AiPolicyDeleteRuleResponse(ConjoinModel):
    action: str
    config: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None
    description: str | None = None
    direction: str
    is_active: bool
    live_mode: bool
    metadata: dict[str, Any]
    name: str
    priority: float
    reference_id: str | None
    rule_id: str
    rule_type: str
    status: str


class AiPolicyListLogsCountResponse(ConjoinModel):
    count: int


class AiPolicyListLogsItem(ConjoinModel):
    action_taken: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    detections: Sequence[dict[str, Any]]
    direction: str
    live_mode: bool
    log_id: str
    logged_at: str
    request_id: str
    rule_id: str
    rule_type: str
    severity: str


class AiPolicyListRulesCountResponse(ConjoinModel):
    count: int


class AiPolicyListRulesItem(ConjoinModel):
    action: str
    config: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None
    description: str | None = None
    direction: str
    is_active: bool
    live_mode: bool
    metadata: dict[str, Any]
    name: str
    priority: float
    reference_id: str | None
    rule_id: str
    rule_type: str
    status: str


class AiPolicyReadRuleResponse(ConjoinModel):
    action: str
    config: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None
    description: str | None = None
    direction: str
    is_active: bool
    live_mode: bool
    metadata: dict[str, Any]
    name: str
    priority: float
    reference_id: str | None
    rule_id: str
    rule_type: str
    status: str


class AiPolicyUpdateRuleResponse(ConjoinModel):
    action: str
    config: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None
    description: str | None = None
    direction: str
    is_active: bool
    live_mode: bool
    metadata: dict[str, Any]
    name: str
    priority: float
    reference_id: str | None
    rule_id: str
    rule_type: str
    status: str


class AiUsageListRecordsCountResponse(ConjoinModel):
    count: int


class AiUsageListRecordsItem(ConjoinModel):
    billing_period: str
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    cost_usd: float
    date_created: str
    input_tokens: float
    is_billable: bool
    latency_ms: float
    live_mode: bool
    model: str | None = None
    output_tokens: float
    provider: str | None = None
    record_id: str
    record_type: str
    recorded_at: str
    request_id: str | None = None
    total_tokens: float
    trace_source: str | None = None


class AiUsageReadSummaryResponse(ConjoinModel):
    billing_period: str
    breakdown_by_model: Sequence[dict[str, Any]]
    breakdown_by_provider: Sequence[dict[str, Any]]
    breakdown_by_type: Sequence[dict[str, Any]]
    total_cost_usd: float
    total_requests: float
    total_tokens: float


class AuthAccountAddEmailResponse(ConjoinModel):
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


class AuthAccountAddPhoneResponse(ConjoinModel):
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


class AuthAccountCreateResponse(ConjoinModel):
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


class AuthAccountDeleteResponse(ConjoinModel):
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


class AuthAccountExportResponse(ConjoinModel):
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


class AuthAccountGrantGlobalRoleResponse(ConjoinModel):
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


class AuthAccountImportPasswordHashesResponse(ConjoinModel):
    created: float
    failed: float
    results: Sequence[dict[str, Any]]
    total: float


class AuthAccountListCountResponse(ConjoinModel):
    count: int


class AuthAccountListCredentialsCountResponse(ConjoinModel):
    count: int


class AuthAccountListCredentialsItem(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthAccountListItem(ConjoinModel):
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


class AuthAccountListOrganizationMembershipsCountResponse(ConjoinModel):
    count: int


class AuthAccountListOrganizationMembershipsItem(ConjoinModel):
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


class AuthAccountMergeResponse(ConjoinModel):
    merged_into: str


class AuthAccountReadCredentialResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthAccountReadResponse(ConjoinModel):
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


class AuthAccountRecoveryAdminResetAccountResponse(ConjoinModel):
    removed_credential_count: float


class AuthAccountRecoveryCompleteRecoveryResponse(ConjoinModel):
    account_id: str | None = None
    expires_at: str | None = None
    recovery_token: str | None = None
    status: str


class AuthAccountRecoveryStartRecoveryResponse(ConjoinModel):
    account_id: str | None = None
    expires_at: str | None = None
    recovery_token: str | None = None
    status: str


class AuthAccountRecoveryVerifyRecoveryResponse(ConjoinModel):
    account_id: str | None = None
    expires_at: str | None = None
    recovery_token: str | None = None
    status: str


class AuthAccountRemoveCredentialResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthAccountRemoveEmailResponse(ConjoinModel):
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


class AuthAccountRemovePhoneResponse(ConjoinModel):
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


class AuthAccountRevokeGlobalRoleResponse(ConjoinModel):
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


class AuthAccountUpdateResponse(ConjoinModel):
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


class AuthAccountVerifyCredentialMfaTotpResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthAccountVerifyCredentialResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthAppCreateResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    settings: dict[str, Any] | None = None
    slug: str
    support_email: str | None = None


class AuthAppListCountResponse(ConjoinModel):
    count: int


class AuthAppListItem(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    settings: dict[str, Any] | None = None
    slug: str
    support_email: str | None = None


class AuthAppReadResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    settings: dict[str, Any] | None = None
    slug: str
    support_email: str | None = None


class AuthAppRotateSigningKeysResponse(ConjoinModel):
    response: Any | None = None


class AuthAppUpdateResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    settings: dict[str, Any] | None = None
    slug: str
    support_email: str | None = None


class AuthAppUpdateSettingsResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    settings: dict[str, Any] | None = None
    slug: str
    support_email: str | None = None


class AuthAuthorizationAuthorizeActionResponse(ConjoinModel):
    allowed: bool
    evaluated_permissions: Sequence[str]
    missing: Sequence[str]


class AuthAuthorizationCheckRoleResponse(ConjoinModel):
    has_role: bool


class AuthAuthorizationReadEffectivePermissionsResponse(ConjoinModel):
    permissions: Sequence[str]
    roles: Sequence[str]


class AuthClientCreateResponse(ConjoinModel):
    app_id: str
    auth_status: str | None = None
    client_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    device_config: dict[str, Any] | None = None
    device_id: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    mfa_option: str | None = None
    reference_id: str | None = None
    user_agent: str | None = None
    user_ip: str | None = None
    verification_option: str | None = None


class AuthClientListCountResponse(ConjoinModel):
    count: int


class AuthClientListItem(ConjoinModel):
    app_id: str
    auth_status: str | None = None
    client_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    device_config: dict[str, Any] | None = None
    device_id: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    mfa_option: str | None = None
    reference_id: str | None = None
    user_agent: str | None = None
    user_ip: str | None = None
    verification_option: str | None = None


class AuthClientReadResponse(ConjoinModel):
    app_id: str
    auth_status: str | None = None
    client_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    device_config: dict[str, Any] | None = None
    device_id: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    mfa_option: str | None = None
    reference_id: str | None = None
    user_agent: str | None = None
    user_ip: str | None = None
    verification_option: str | None = None


class AuthConnectionEnterpriseActivateEnterpriseConnectionSigningKeyResponse(ConjoinModel):
    signing_keys: Sequence[dict[str, Any]]


class AuthConnectionEnterpriseCancelEnterpriseConnectionSigningKeyResponse(ConjoinModel):
    signing_keys: Sequence[dict[str, Any]]


class AuthConnectionEnterpriseCreateEnterpriseConnectionResponse(ConjoinModel):
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


class AuthConnectionEnterpriseDeleteEnterpriseConnectionResponse(ConjoinModel):
    deleted: Any


class AuthConnectionEnterpriseDisableEnterpriseConnectionResponse(ConjoinModel):
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


class AuthConnectionEnterpriseEnableEnterpriseConnectionResponse(ConjoinModel):
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


class AuthConnectionEnterpriseImportEnterpriseSamlMetadataResponse(ConjoinModel):
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


class AuthConnectionEnterpriseListEnterpriseConnectionsCountResponse(ConjoinModel):
    count: int


class AuthConnectionEnterpriseListEnterpriseConnectionsItem(ConjoinModel):
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


class AuthConnectionEnterpriseReadEnterpriseConnectionResponse(ConjoinModel):
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


class AuthConnectionEnterpriseRevokeEnterpriseConnectionSigningKeyResponse(ConjoinModel):
    signing_keys: Sequence[dict[str, Any]]


class AuthConnectionEnterpriseRotateEnterpriseConnectionSigningKeyResponse(ConjoinModel):
    signing_keys: Sequence[dict[str, Any]]


class AuthConnectionEnterpriseSyncEnterpriseSamlMetadataResponse(ConjoinModel):
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


class AuthConnectionEnterpriseUpdateEnterpriseConnectionResponse(ConjoinModel):
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


class AuthConnectionListFirstPartyResponse(ConjoinModel):
    connections: Sequence[dict[str, Any]]


class AuthConnectionUpsertFirstPartyResponse(ConjoinModel):
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


class AuthCredentialActivateSmsMfaResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialActivateTotpResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialConsumeTotpRecoveryCodeResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialCreatePasswordResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialEnrollSmsMfaResponse(ConjoinModel):
    credential_id: str


class AuthCredentialEnrollTotpResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialIssueApiKeyResponse(ConjoinModel):
    api_key: str
    credential: dict[str, Any]


class AuthCredentialReadApiKeyUsageResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialRevokeApiKeyResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialRotateApiKeyResponse(ConjoinModel):
    api_key: str
    credential_id: str


class AuthCredentialRotatePasswordResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialRotateTotpRecoveryCodesResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialSendSmsMfaActivationCodeResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialSendSmsMfaChallengeResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialStartPasskeyRegistrationResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialStartPasskeyenticationResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialUpdateApiKeyResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialVerifyPasskeyRegistrationResponse(ConjoinModel):
    credential_id: str


class AuthCredentialVerifyPasskeyenticationResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthCredentialVerifySmsMfaResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    credential_id: str
    data: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    kind: str
    live_mode: bool
    metadata: dict[str, Any] | None = None


class AuthDeprovisioningDeprovisionAccountResponse(ConjoinModel):
    action_taken: str


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


class AuthGuardAddAnonymousIpsResponse(ConjoinModel):
    ips: Sequence[str]


class AuthGuardAddTrustedDomainResponse(ConjoinModel):
    domain: str


class AuthGuardAddTrustedEmailResponse(ConjoinModel):
    email: str


class AuthGuardAddTrustedIpResponse(ConjoinModel):
    added_at: str | None = None
    ip: str


class AuthGuardCreateRuleResponse(ConjoinModel):
    action: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None
    description: str | None = None
    expires_at: str | None = None
    is_enabled: bool | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    predicate: dict[str, Any]
    rule_id: str


class AuthGuardDeleteRuleResponse(ConjoinModel):
    deleted: Any


class AuthGuardListAnonymousIpsResponse(ConjoinModel):
    ips: Sequence[str]


class AuthGuardListEventsCountResponse(ConjoinModel):
    count: int


class AuthGuardListEventsItem(ConjoinModel):
    account_id: str | None = None
    action_taken: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    details: dict[str, Any] | None = None
    event_id: str
    event_type: str
    ip_address: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    user_agent: str | None = None


class AuthGuardListRulesCountResponse(ConjoinModel):
    count: int


class AuthGuardListRulesItem(ConjoinModel):
    action: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None
    description: str | None = None
    expires_at: str | None = None
    is_enabled: bool | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    predicate: dict[str, Any]
    rule_id: str


class AuthGuardReadRuleResponse(ConjoinModel):
    action: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None
    description: str | None = None
    expires_at: str | None = None
    is_enabled: bool | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    predicate: dict[str, Any]
    rule_id: str


class AuthGuardRemoveAnonymousIpsResponse(ConjoinModel):
    ips: Sequence[str]


class AuthGuardRemoveTrustedDomainResponse(ConjoinModel):
    domain: str


class AuthGuardRemoveTrustedEmailResponse(ConjoinModel):
    email: str


class AuthGuardRemoveTrustedIpResponse(ConjoinModel):
    added_at: str | None = None
    ip: str


class AuthGuardUpdateRuleResponse(ConjoinModel):
    action: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None
    description: str | None = None
    expires_at: str | None = None
    is_enabled: bool | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    predicate: dict[str, Any]
    rule_id: str


class AuthIdentityDiscoverAccountResponse(ConjoinModel):
    account_id: str | None
    reason: str | None = None


class AuthIdentityLinkResponse(ConjoinModel):
    resolved_account_id: str


class AuthOrganizationCreateResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    image_url: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    owner_account_id: str | None = None
    reference_id: str | None = None
    settings: dict[str, Any] | None = None
    slug: str
    total_members: float | None = None


class AuthOrganizationDeleteResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    image_url: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    owner_account_id: str | None = None
    reference_id: str | None = None
    settings: dict[str, Any] | None = None
    slug: str
    total_members: float | None = None


class AuthOrganizationDomainCreateResponse(ConjoinModel):
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


class AuthOrganizationDomainDeleteResponse(ConjoinModel):
    deleted: Any


class AuthOrganizationDomainListCountResponse(ConjoinModel):
    count: int


class AuthOrganizationDomainListItem(ConjoinModel):
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


class AuthOrganizationDomainVerifyResponse(ConjoinModel):
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


class AuthOrganizationGroupAddGroupMemberResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    external_id: str | None = None
    group_id: str
    image_url: str | None = None
    last_synced_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    provisioning_source: str | None = None
    reference_id: str | None = None
    roles: Sequence[str] | None = None
    slug: str
    sync_locked: bool | None = None
    total_members: float | None = None


class AuthOrganizationGroupBulkSyncGroupMembersResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    external_id: str | None = None
    group_id: str
    image_url: str | None = None
    last_synced_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    provisioning_source: str | None = None
    reference_id: str | None = None
    roles: Sequence[str] | None = None
    slug: str
    sync_locked: bool | None = None
    total_members: float | None = None


class AuthOrganizationGroupCreateGroupResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    external_id: str | None = None
    group_id: str
    image_url: str | None = None
    last_synced_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    provisioning_source: str | None = None
    reference_id: str | None = None
    roles: Sequence[str] | None = None
    slug: str
    sync_locked: bool | None = None
    total_members: float | None = None


class AuthOrganizationGroupDeleteGroupResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    external_id: str | None = None
    group_id: str
    image_url: str | None = None
    last_synced_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    provisioning_source: str | None = None
    reference_id: str | None = None
    roles: Sequence[str] | None = None
    slug: str
    sync_locked: bool | None = None
    total_members: float | None = None


class AuthOrganizationGroupListGroupMembersCountResponse(ConjoinModel):
    count: int


class AuthOrganizationGroupListGroupMembersItem(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    group_id: str
    group_membership_id: str
    joined_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    organization_id: str
    status: str


class AuthOrganizationGroupListGroupsCountResponse(ConjoinModel):
    count: int


class AuthOrganizationGroupListGroupsItem(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    external_id: str | None = None
    group_id: str
    image_url: str | None = None
    last_synced_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    provisioning_source: str | None = None
    reference_id: str | None = None
    roles: Sequence[str] | None = None
    slug: str
    sync_locked: bool | None = None
    total_members: float | None = None


class AuthOrganizationGroupRemoveGroupMemberResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    external_id: str | None = None
    group_id: str
    image_url: str | None = None
    last_synced_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    provisioning_source: str | None = None
    reference_id: str | None = None
    roles: Sequence[str] | None = None
    slug: str
    sync_locked: bool | None = None
    total_members: float | None = None


class AuthOrganizationGroupUpdateGroupResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    external_id: str | None = None
    group_id: str
    image_url: str | None = None
    last_synced_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    provisioning_source: str | None = None
    reference_id: str | None = None
    roles: Sequence[str] | None = None
    slug: str
    sync_locked: bool | None = None
    total_members: float | None = None


class AuthOrganizationInvitationCreateInvitationResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str
    expires_at: str | None = None
    invitation_id: str
    invitation_url: str
    invited_by_account_id: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str | None = None
    organization_id: str
    reference_id: str
    roles: Sequence[str] | None = None
    status: str
    used_at: str | None = None


class AuthOrganizationInvitationListInvitationsCountResponse(ConjoinModel):
    count: int


class AuthOrganizationInvitationListInvitationsItem(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str
    expires_at: str | None = None
    invitation_id: str
    invited_by_account_id: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str | None = None
    organization_id: str
    reference_id: str
    roles: Sequence[str] | None = None
    status: str
    used_at: str | None = None


class AuthOrganizationInvitationResendInvitationResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str
    expires_at: str | None = None
    invitation_id: str
    invitation_url: str
    invited_by_account_id: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str | None = None
    organization_id: str
    reference_id: str
    roles: Sequence[str] | None = None
    status: str
    used_at: str | None = None


class AuthOrganizationInvitationRevokeInvitationResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str
    expires_at: str | None = None
    invitation_id: str
    invited_by_account_id: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str | None = None
    organization_id: str
    reference_id: str
    roles: Sequence[str] | None = None
    status: str
    used_at: str | None = None


class AuthOrganizationListCountResponse(ConjoinModel):
    count: int


class AuthOrganizationListItem(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    image_url: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    owner_account_id: str | None = None
    reference_id: str | None = None
    settings: dict[str, Any] | None = None
    slug: str
    total_members: float | None = None


class AuthOrganizationMembershipCreateMembershipResponse(ConjoinModel):
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


class AuthOrganizationMembershipDeleteMembershipResponse(ConjoinModel):
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


class AuthOrganizationMembershipGrantOrgAccountRoleResponse(ConjoinModel):
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


class AuthOrganizationMembershipListMembershipsCountResponse(ConjoinModel):
    count: int


class AuthOrganizationMembershipListMembershipsItem(ConjoinModel):
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


class AuthOrganizationMembershipRevokeOrgAccountRoleResponse(ConjoinModel):
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


class AuthOrganizationMembershipUpdateMembershipResponse(ConjoinModel):
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


class AuthOrganizationPermissionArchiveOrgPermissionResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    permission_id: str
    reference_id: str | None = None


class AuthOrganizationPermissionCreateOrgPermissionResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    permission_id: str
    reference_id: str | None = None


class AuthOrganizationPermissionDeleteOrgPermissionResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    permission_id: str
    reference_id: str | None = None


class AuthOrganizationPermissionListOrgPermissionsCountResponse(ConjoinModel):
    count: int


class AuthOrganizationPermissionListOrgPermissionsItem(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    permission_id: str
    reference_id: str | None = None


class AuthOrganizationPermissionReadOrgPermissionResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    permission_id: str
    reference_id: str | None = None


class AuthOrganizationPermissionRestoreOrgPermissionResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    permission_id: str
    reference_id: str | None = None


class AuthOrganizationPermissionUpdateOrgPermissionResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    permission_id: str
    reference_id: str | None = None


class AuthOrganizationReadResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    image_url: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    owner_account_id: str | None = None
    reference_id: str | None = None
    settings: dict[str, Any] | None = None
    slug: str
    total_members: float | None = None


class AuthOrganizationRoleArchiveOrgRoleResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    parent_role_id: str | None = None
    reference_id: str | None = None
    role_id: str
    scope: str | None = None


class AuthOrganizationRoleCreateOrgRoleResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    parent_role_id: str | None = None
    reference_id: str | None = None
    role_id: str
    scope: str | None = None


class AuthOrganizationRoleDeleteOrgRoleResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    parent_role_id: str | None = None
    reference_id: str | None = None
    role_id: str
    scope: str | None = None


class AuthOrganizationRoleListOrgRolesCountResponse(ConjoinModel):
    count: int


class AuthOrganizationRoleListOrgRolesItem(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    parent_role_id: str | None = None
    reference_id: str | None = None
    role_id: str
    scope: str | None = None


class AuthOrganizationRolePermissionAssignOrgRolePermissionItem(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    organization_id: str
    permission_id: str
    role_id: str
    role_permission_id: str


class AuthOrganizationRolePermissionListOrgRolePermissionsCountResponse(ConjoinModel):
    count: int


class AuthOrganizationRolePermissionListOrgRolePermissionsItem(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    organization_id: str
    permission_id: str
    permission_key: str | None
    role_id: str
    role_permission_id: str


class AuthOrganizationRolePermissionRemoveRolePermissionResponse(ConjoinModel):
    removed_count: int


class AuthOrganizationRoleReadOrgRoleResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    parent_role_id: str | None = None
    reference_id: str | None = None
    role_id: str
    scope: str | None = None


class AuthOrganizationRoleRestoreOrgRoleResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    parent_role_id: str | None = None
    reference_id: str | None = None
    role_id: str
    scope: str | None = None


class AuthOrganizationRoleUpdateOrgRoleResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    creator_account_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    identifier: str
    key: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    parent_role_id: str | None = None
    reference_id: str | None = None
    role_id: str
    scope: str | None = None


class AuthOrganizationUpdateResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    image_url: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    owner_account_id: str | None = None
    reference_id: str | None = None
    settings: dict[str, Any] | None = None
    slug: str
    total_members: float | None = None


class AuthOrganizationUpdateSettingsResponse(ConjoinModel):
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    image_url: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    owner_account_id: str | None = None
    reference_id: str | None = None
    settings: dict[str, Any] | None = None
    slug: str
    total_members: float | None = None


class AuthPasskeyDeleteResponse(ConjoinModel):
    aaguid: str | None = None
    credential_id: str
    date_created: str
    kind: str
    last_used_at: str | None = None
    last_verified_at: str | None = None
    set_at: str | None = None
    status: str
    transports: Sequence[str] | None = None


class AuthPasskeyListCountResponse(ConjoinModel):
    count: int


class AuthPasskeyListItem(ConjoinModel):
    aaguid: str | None = None
    credential_id: str
    date_created: str
    kind: str
    last_used_at: str | None = None
    last_verified_at: str | None = None
    set_at: str | None = None
    status: str
    transports: Sequence[str] | None = None


class AuthPasskeyReadResponse(ConjoinModel):
    aaguid: str | None = None
    credential_id: str
    date_created: str
    kind: str
    last_used_at: str | None = None
    last_verified_at: str | None = None
    set_at: str | None = None
    status: str
    transports: Sequence[str] | None = None


class AuthPolicyCreateResponse(ConjoinModel):
    app_id: str
    conditions: Sequence[dict[str, Any]] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    effect: str
    is_enabled: bool | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    permission_keys: Sequence[str] | None = None
    policy_id: str
    priority: float | None = None
    reference_id: str | None = None


class AuthPolicyDeleteResponse(ConjoinModel):
    app_id: str
    conditions: Sequence[dict[str, Any]] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    effect: str
    is_enabled: bool | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    permission_keys: Sequence[str] | None = None
    policy_id: str
    priority: float | None = None
    reference_id: str | None = None


class AuthPolicyListCountResponse(ConjoinModel):
    count: int


class AuthPolicyListItem(ConjoinModel):
    app_id: str
    conditions: Sequence[dict[str, Any]] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    effect: str
    is_enabled: bool | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    permission_keys: Sequence[str] | None = None
    policy_id: str
    priority: float | None = None
    reference_id: str | None = None


class AuthPolicyReadResponse(ConjoinModel):
    app_id: str
    conditions: Sequence[dict[str, Any]] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    effect: str
    is_enabled: bool | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    permission_keys: Sequence[str] | None = None
    policy_id: str
    priority: float | None = None
    reference_id: str | None = None


class AuthPolicyUpdateResponse(ConjoinModel):
    app_id: str
    conditions: Sequence[dict[str, Any]] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    effect: str
    is_enabled: bool | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    organization_id: str
    permission_keys: Sequence[str] | None = None
    policy_id: str
    priority: float | None = None
    reference_id: str | None = None


class AuthResourceGrantCheckResourcePermissionResponse(ConjoinModel):
    allowed: bool
    granted_permissions: Sequence[str]


class AuthResourceGrantGrantResourcePermissionResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    granted_at: str | None = None
    granted_by_account_id: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    organization_id: str
    permission_keys: Sequence[str] | None = None
    resource_grant_id: str
    resource_id: str
    resource_type: str


class AuthResourceGrantListCountResponse(ConjoinModel):
    count: int


class AuthResourceGrantListItem(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    granted_at: str | None = None
    granted_by_account_id: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    organization_id: str
    permission_keys: Sequence[str] | None = None
    resource_grant_id: str
    resource_id: str
    resource_type: str


class AuthResourceGrantRevokeResourcePermissionResponse(ConjoinModel):
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    granted_at: str | None = None
    granted_by_account_id: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    organization_id: str
    permission_keys: Sequence[str] | None = None
    resource_grant_id: str
    resource_id: str
    resource_type: str


class AuthRoleAssignmentLogListCountResponse(ConjoinModel):
    count: int


class AuthRoleAssignmentLogListItem(ConjoinModel):
    account_id: str
    action: str
    app_id: str
    assignment_log_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    context: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    organization_id: str
    performed_at: str | None = None
    performed_by_account_id: str | None = None
    role_key: str


class AuthSCIMManagementReadScimSettingsResponse(ConjoinModel):
    bearer_token_configured: bool
    deprovision_policy: str = Field(..., alias='deprovisionPolicy')
    group_attribute_mapping: dict[str, Any] = Field(..., alias='groupAttributeMapping')
    limits: dict[str, Any] | None = None
    rate_limits: dict[str, Any] | None = Field(None, alias='rateLimits')
    role_mapping_rules: Sequence[dict[str, Any]] = Field(..., alias='roleMappingRules')
    user_attribute_mapping: dict[str, Any] = Field(..., alias='userAttributeMapping')


class AuthSCIMManagementReconcileScimGroupMembersResponse(ConjoinModel):
    status: str


class AuthSCIMManagementReconcileScimGroupsResponse(ConjoinModel):
    status: str


class AuthSCIMManagementReconcileScimUsersResponse(ConjoinModel):
    status: str


class AuthSCIMManagementSyncScimRolesForGroupResponse(ConjoinModel):
    status: str


class AuthSCIMManagementSyncScimRolesForMemberResponse(ConjoinModel):
    status: str


class AuthSCIMManagementUpdateScimSettingsResponse(ConjoinModel):
    status: str


class AuthSCIMScimBulkOperationsResponse(ConjoinModel):
    operations: Sequence[dict[str, Any]] | None = Field(None, alias='Operations')
    schemas: Sequence[str]


class AuthSCIMScimCreateGroupResponse(ConjoinModel):
    display_name: str = Field(..., alias='displayName')
    external_id: str | None = Field(None, alias='externalId')
    id: str | None = None
    members: Sequence[dict[str, Any]] | None = None
    meta: dict[str, Any] | None = None
    schemas: Sequence[str]


class AuthSCIMScimCreateUserResponse(ConjoinModel):
    active: bool | None = None
    emails: Sequence[dict[str, Any]] | None = None
    external_id: str | None = Field(None, alias='externalId')
    id: str | None = None
    meta: dict[str, Any] | None = None
    name: dict[str, Any] | None = None
    phone_numbers: Sequence[dict[str, Any]] | None = Field(None, alias='phoneNumbers')
    photos: Sequence[dict[str, Any]] | None = None
    schemas: Sequence[str]
    user_name: str | None = Field(None, alias='userName')


class AuthSCIMScimGetGroupResponse(ConjoinModel):
    display_name: str = Field(..., alias='displayName')
    external_id: str | None = Field(None, alias='externalId')
    id: str | None = None
    members: Sequence[dict[str, Any]] | None = None
    meta: dict[str, Any] | None = None
    schemas: Sequence[str]


class AuthSCIMScimGetResourceTypesResponse(ConjoinModel):
    resources: Sequence[dict[str, Any]] | None = Field(None, alias='Resources')
    schemas: Sequence[str]
    total_results: float | None = Field(None, alias='totalResults')


class AuthSCIMScimGetSchemasResponse(ConjoinModel):
    resources: Sequence[dict[str, Any]] | None = Field(None, alias='Resources')
    schemas: Sequence[str]
    total_results: float | None = Field(None, alias='totalResults')


class AuthSCIMScimGetServiceProviderConfigResponse(ConjoinModel):
    authentication_schemes: Sequence[dict[str, Any]] | None = Field(
        None,
        alias='authenticationSchemes',
    )
    bulk: dict[str, Any] | None = None
    change_password: dict[str, Any] | None = Field(None, alias='changePassword')
    documentation_uri: str | None = Field(None, alias='documentationUri')
    etag: dict[str, Any] | None = None
    filter: dict[str, Any] | None = None
    patch: dict[str, Any] | None = None
    schemas: Sequence[str]
    sort: dict[str, Any] | None = None


class AuthSCIMScimGetUserResponse(ConjoinModel):
    active: bool | None = None
    emails: Sequence[dict[str, Any]] | None = None
    external_id: str | None = Field(None, alias='externalId')
    id: str | None = None
    meta: dict[str, Any] | None = None
    name: dict[str, Any] | None = None
    phone_numbers: Sequence[dict[str, Any]] | None = Field(None, alias='phoneNumbers')
    photos: Sequence[dict[str, Any]] | None = None
    schemas: Sequence[str]
    user_name: str | None = Field(None, alias='userName')


class AuthSCIMScimListGroupsResponse(ConjoinModel):
    resources: Sequence[dict[str, Any]] | None = Field(None, alias='Resources')
    items_per_page: float | None = Field(None, alias='itemsPerPage')
    schemas: Sequence[str]
    start_index: float | None = Field(None, alias='startIndex')
    total_results: float = Field(..., alias='totalResults')


class AuthSCIMScimListUsersResponse(ConjoinModel):
    resources: Sequence[dict[str, Any]] | None = Field(None, alias='Resources')
    items_per_page: float | None = Field(None, alias='itemsPerPage')
    schemas: Sequence[str]
    start_index: float | None = Field(None, alias='startIndex')
    total_results: float = Field(..., alias='totalResults')


class AuthSCIMScimPatchGroupMembersResponse(ConjoinModel):
    display_name: str = Field(..., alias='displayName')
    external_id: str | None = Field(None, alias='externalId')
    id: str | None = None
    members: Sequence[dict[str, Any]] | None = None
    meta: dict[str, Any] | None = None
    schemas: Sequence[str]


class AuthSCIMScimPatchUserResponse(ConjoinModel):
    active: bool | None = None
    emails: Sequence[dict[str, Any]] | None = None
    external_id: str | None = Field(None, alias='externalId')
    id: str | None = None
    meta: dict[str, Any] | None = None
    name: dict[str, Any] | None = None
    phone_numbers: Sequence[dict[str, Any]] | None = Field(None, alias='phoneNumbers')
    photos: Sequence[dict[str, Any]] | None = None
    schemas: Sequence[str]
    user_name: str | None = Field(None, alias='userName')


class AuthSCIMScimReplaceGroupResponse(ConjoinModel):
    display_name: str = Field(..., alias='displayName')
    external_id: str | None = Field(None, alias='externalId')
    id: str | None = None
    members: Sequence[dict[str, Any]] | None = None
    meta: dict[str, Any] | None = None
    schemas: Sequence[str]


class AuthSCIMScimReplaceUserResponse(ConjoinModel):
    active: bool | None = None
    emails: Sequence[dict[str, Any]] | None = None
    external_id: str | None = Field(None, alias='externalId')
    id: str | None = None
    meta: dict[str, Any] | None = None
    name: dict[str, Any] | None = None
    phone_numbers: Sequence[dict[str, Any]] | None = Field(None, alias='phoneNumbers')
    photos: Sequence[dict[str, Any]] | None = None
    schemas: Sequence[str]
    user_name: str | None = Field(None, alias='userName')


class AuthSLOOidcLogoutResponse(ConjoinModel):
    logout_request_xml: str | None = None
    logout_response_xml: str | None = None
    logout_url: str | None = None
    status: str | None = None


class AuthSLOSamlIdpLogoutResponse(ConjoinModel):
    logout_request_xml: str | None = None
    logout_response_xml: str | None = None
    logout_url: str | None = None
    status: str | None = None


class AuthSLOSamlSpLogoutResponse(ConjoinModel):
    logout_request_xml: str | None = None
    logout_response_xml: str | None = None
    logout_url: str | None = None
    status: str | None = None


class AuthSSOPortalMintSsoPortalTicketResponse(ConjoinModel):
    portal_url: str
    secret: str
    ticket: dict[str, Any]


class AuthSSOPortalReadSsoPortalSettingsResponse(ConjoinModel):
    allowed_providers: Sequence[str]
    require_domain_verification: bool
    setup_intents: Sequence[str]


class AuthSSOPortalRevokeSsoPortalTicketResponse(ConjoinModel):
    revoked: Any


class AuthSSOPortalUpdateSsoPortalSettingsResponse(ConjoinModel):
    allowed_providers: Sequence[str]
    require_domain_verification: bool
    setup_intents: Sequence[str]


class AuthSessionBulkRevokeAccountResponse(ConjoinModel):
    revoked_count: float
    session_ids: Sequence[str] | None = None


class AuthSessionBulkRevokeClientResponse(ConjoinModel):
    revoked_count: float
    session_ids: Sequence[str] | None = None


class AuthSessionGetAnalyticsResponse(ConjoinModel):
    data: Sequence[dict[str, Any]]


class AuthSessionListCountResponse(ConjoinModel):
    count: int


class AuthSessionListItem(ConjoinModel):
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


class AuthSessionReadResponse(ConjoinModel):
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


class AuthSessionReadStatsResponse(ConjoinModel):
    active_client_count: float
    active_session_count: float


class AuthSessionRevokeAllForAccountResponse(ConjoinModel):
    revoked_count: float
    session_ids: Sequence[str] | None = None


class AuthSessionRevokeResponse(ConjoinModel):
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


class AuthSessionUpdateResponse(ConjoinModel):
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


class AuthSessionValidateResponse(ConjoinModel):
    account_id: str | None = None
    errors: Sequence[str] | None = None
    session_id: str | None = None
    valid: bool


class AuthStepUpRequestResponse(ConjoinModel):
    available_methods: Sequence[str]
    challenge_id: str


class AuthStepUpValidateResponse(ConjoinModel):
    valid: bool


class AuthStepUpVerifyResponse(ConjoinModel):
    expires_in: int
    step_up_token: str


class AuthTrustedDeviceListCountResponse(ConjoinModel):
    count: int


class AuthTrustedDeviceListItem(ConjoinModel):
    absolute_expires_at: str | None = None
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    expires_at: str | None = None
    ip_prefix: str | None = None
    label: str | None = None
    last_used_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    status: str
    trusted_at: str | None = None
    trusted_device_id: str
    user_agent: str | None = None


class AuthTrustedDeviceRevokeAllResponse(ConjoinModel):
    revoked_count: float


class AuthTrustedDeviceRevokeResponse(ConjoinModel):
    absolute_expires_at: str | None = None
    account_id: str
    app_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    expires_at: str | None = None
    ip_prefix: str | None = None
    label: str | None = None
    last_used_at: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    status: str
    trusted_at: str | None = None
    trusted_device_id: str
    user_agent: str | None = None


class BillingChargeListCountResponse(ConjoinModel):
    count: int


class BillingChargeListItem(ConjoinModel):
    amount: float
    charge_id: str
    currency: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    payment_type: str
    status: str
    transaction_id: str
    transaction_type: str


class BillingCouponCreateResponse(ConjoinModel):
    amount_off: float | None
    applies_to: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    coupon_code: str
    coupon_id: str
    currency: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    discount_type: str
    duration: str
    duration_in_cycles: float | None
    expiration_date: str | None
    is_active: bool
    live_mode: bool
    max_redemptions: float | None
    name: str
    percent_off: float | None
    reason_code: str
    reference_id: str
    times_redeemed: float


class BillingCouponDeleteResponse(ConjoinModel):
    amount_off: float | None
    applies_to: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    coupon_code: str
    coupon_id: str
    currency: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    discount_type: str
    duration: str
    duration_in_cycles: float | None
    expiration_date: str | None
    is_active: bool
    live_mode: bool
    max_redemptions: float | None
    name: str
    percent_off: float | None
    reason_code: str
    reference_id: str
    times_redeemed: float


class BillingCouponListCountResponse(ConjoinModel):
    count: int


class BillingCouponListItem(ConjoinModel):
    amount_off: float | None
    applies_to: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    coupon_code: str
    coupon_id: str
    currency: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    discount_type: str
    duration: str
    duration_in_cycles: float | None
    expiration_date: str | None
    is_active: bool
    live_mode: bool
    max_redemptions: float | None
    name: str
    percent_off: float | None
    reason_code: str
    reference_id: str
    times_redeemed: float


class BillingCouponUpdateResponse(ConjoinModel):
    amount_off: float | None
    applies_to: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    coupon_code: str
    coupon_id: str
    currency: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    discount_type: str
    duration: str
    duration_in_cycles: float | None
    expiration_date: str | None
    is_active: bool
    live_mode: bool
    max_redemptions: float | None
    name: str
    percent_off: float | None
    reason_code: str
    reference_id: str
    times_redeemed: float


class BillingCreditNoteCreateResponse(ConjoinModel):
    amount: float
    amount_remaining: float
    applications: Sequence[dict[str, Any]]
    conjoin_account_id: str
    conjoin_project_id: str
    credit_note_id: str
    currency: str
    customer_id: str
    cycle_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    entity_id: str
    invoice_id: str | None = None
    line_items: Sequence[dict[str, Any]]
    live_mode: bool
    reason: str
    reference_id: str
    status: str
    subscription_id: str | None = None


class BillingCreditNoteListCountResponse(ConjoinModel):
    count: int


class BillingCreditNoteListCustomerCreditBalancesCountResponse(ConjoinModel):
    count: int


class BillingCreditNoteListCustomerCreditBalancesItem(ConjoinModel):
    balance: float
    conjoin_account_id: str
    conjoin_project_id: str
    credit_balance_id: str
    currency: str
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool


class BillingCreditNoteListItem(ConjoinModel):
    amount: float
    amount_remaining: float
    applications: Sequence[dict[str, Any]]
    conjoin_account_id: str
    conjoin_project_id: str
    credit_note_id: str
    currency: str
    customer_id: str
    cycle_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    entity_id: str
    invoice_id: str | None = None
    line_items: Sequence[dict[str, Any]]
    live_mode: bool
    reason: str
    reference_id: str
    status: str
    subscription_id: str | None = None


class BillingCreditNoteVoidResponse(ConjoinModel):
    amount: float
    amount_remaining: float
    applications: Sequence[dict[str, Any]]
    conjoin_account_id: str
    conjoin_project_id: str
    credit_note_id: str
    currency: str
    customer_id: str
    cycle_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    entity_id: str
    invoice_id: str | None = None
    line_items: Sequence[dict[str, Any]]
    live_mode: bool
    reason: str
    reference_id: str
    status: str
    subscription_id: str | None = None


class BillingCreditWalletCreateResponse(ConjoinModel):
    auto_topup: dict[str, Any]
    balance: float
    conjoin_account_id: str
    conjoin_project_id: str
    credit_value: float
    currency: str
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool
    label: str
    live_mode: bool
    wallet_id: str


class BillingCreditWalletGrantCreditsResponse(ConjoinModel):
    amount: float
    amount_remaining: float
    conjoin_account_id: str
    conjoin_project_id: str
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    expiration_date: str | None = None
    grant_id: str
    is_active: bool
    live_mode: bool
    source: str
    wallet_id: str


class BillingCreditWalletListCountResponse(ConjoinModel):
    count: int


class BillingCreditWalletListItem(ConjoinModel):
    auto_topup: dict[str, Any]
    balance: float
    conjoin_account_id: str
    conjoin_project_id: str
    credit_value: float
    currency: str
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool
    label: str
    live_mode: bool
    wallet_id: str


class BillingCreditWalletUpdateResponse(ConjoinModel):
    auto_topup: dict[str, Any]
    balance: float
    conjoin_account_id: str
    conjoin_project_id: str
    credit_value: float
    currency: str
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool
    label: str
    live_mode: bool
    wallet_id: str


class BillingCustomerArchiveResponse(ConjoinModel):
    address: dict[str, Any] | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str
    entity_id: str
    invoice_settings: dict[str, Any] | None = None
    name: str | None = None
    payment_settings: dict[str, Any] | None = None
    phone: str | None = None
    reference_id: str
    shipping_address: dict[str, Any] | None = None


class BillingCustomerCreateResponse(ConjoinModel):
    address: dict[str, Any] | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str
    entity_id: str
    invoice_settings: dict[str, Any] | None = None
    name: str | None = None
    payment_settings: dict[str, Any] | None = None
    phone: str | None = None
    reference_id: str
    shipping_address: dict[str, Any] | None = None


class BillingCustomerListCountResponse(ConjoinModel):
    count: int


class BillingCustomerListItem(ConjoinModel):
    address: dict[str, Any] | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str
    entity_id: str
    invoice_settings: dict[str, Any] | None = None
    name: str | None = None
    payment_settings: dict[str, Any] | None = None
    phone: str | None = None
    reference_id: str
    shipping_address: dict[str, Any] | None = None


class BillingCustomerReadResponse(ConjoinModel):
    address: dict[str, Any] | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str
    entity_id: str
    invoice_settings: dict[str, Any] | None = None
    name: str | None = None
    payment_settings: dict[str, Any] | None = None
    phone: str | None = None
    reference_id: str
    shipping_address: dict[str, Any] | None = None


class BillingCustomerRestoreResponse(ConjoinModel):
    address: dict[str, Any] | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str
    entity_id: str
    invoice_settings: dict[str, Any] | None = None
    name: str | None = None
    payment_settings: dict[str, Any] | None = None
    phone: str | None = None
    reference_id: str
    shipping_address: dict[str, Any] | None = None


class BillingCustomerUpdateResponse(ConjoinModel):
    address: dict[str, Any] | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str
    entity_id: str
    invoice_settings: dict[str, Any] | None = None
    name: str | None = None
    payment_settings: dict[str, Any] | None = None
    phone: str | None = None
    reference_id: str
    shipping_address: dict[str, Any] | None = None


class BillingDiscountCreateResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    coupon_id: str
    currency: str
    customer_id: str
    cycles_applied: float
    cycles_remaining: float | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    discount_amount: float
    discount_id: str
    end_date: str | None = None
    entity_id: str
    invoice_id: str | None = None
    is_active: bool
    live_mode: bool
    reference_id: str
    source_activation_id: str | None = None
    start_date: str
    subscription_id: str | None = None


class BillingDiscountDeleteResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    coupon_id: str
    currency: str
    customer_id: str
    cycles_applied: float
    cycles_remaining: float | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    discount_amount: float
    discount_id: str
    end_date: str | None = None
    entity_id: str
    invoice_id: str | None = None
    is_active: bool
    live_mode: bool
    reference_id: str
    source_activation_id: str | None = None
    start_date: str
    subscription_id: str | None = None


class BillingDiscountListCountResponse(ConjoinModel):
    count: int


class BillingDiscountListItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    coupon_id: str
    currency: str
    customer_id: str
    cycles_applied: float
    cycles_remaining: float | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    discount_amount: float
    discount_id: str
    end_date: str | None = None
    entity_id: str
    invoice_id: str | None = None
    is_active: bool
    live_mode: bool
    reference_id: str
    source_activation_id: str | None = None
    start_date: str
    subscription_id: str | None = None


class BillingDisputeGetResponse(ConjoinModel):
    accepted_amount: int | None = None
    amount: int
    charge_amount: int | None = None
    charge_id: str | None
    currency: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    dispute_fee: int | None = None
    dispute_id: str
    evidence_due_at: str | None = None
    funds_reinstated_amount: int | None = None
    funds_withdrawn_amount: int | None = None
    is_dispute_fee_reversed: bool | None = None
    opened_at: str | None = None
    outcome: str
    reason: str | None = None
    resolved_at: str | None = None


class BillingDisputeListCountResponse(ConjoinModel):
    count: int


class BillingDisputeListItem(ConjoinModel):
    accepted_amount: int | None = None
    amount: int
    charge_amount: int | None = None
    charge_id: str | None
    currency: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    dispute_fee: int | None = None
    dispute_id: str
    evidence_due_at: str | None = None
    funds_reinstated_amount: int | None = None
    funds_withdrawn_amount: int | None = None
    is_dispute_fee_reversed: bool | None = None
    opened_at: str | None = None
    outcome: str
    reason: str | None = None
    resolved_at: str | None = None


class BillingEntitlementFeatureArchiveResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    credit_config: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    feature_id: str
    is_active: bool
    key: str
    live_mode: bool
    metering_config: dict[str, Any] | None = None
    name: str
    type: str


class BillingEntitlementFeatureCreateResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    credit_config: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    feature_id: str
    is_active: bool
    key: str
    live_mode: bool
    metering_config: dict[str, Any] | None = None
    name: str
    type: str


class BillingEntitlementFeatureListCountResponse(ConjoinModel):
    count: int


class BillingEntitlementFeatureListItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    credit_config: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    feature_id: str
    is_active: bool
    key: str
    live_mode: bool
    metering_config: dict[str, Any] | None = None
    name: str
    type: str


class BillingEntitlementFeatureReadResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    credit_config: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    feature_id: str
    is_active: bool
    key: str
    live_mode: bool
    metering_config: dict[str, Any] | None = None
    name: str
    type: str


class BillingEntitlementFeatureUpdateResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    credit_config: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    feature_id: str
    is_active: bool
    key: str
    live_mode: bool
    metering_config: dict[str, Any] | None = None
    name: str
    type: str


class BillingEntitlementOverrideCreateResponse(ConjoinModel):
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


class BillingEntitlementOverrideDeleteResponse(ConjoinModel):
    response: Any | None = None


class BillingEntitlementOverrideListCountResponse(ConjoinModel):
    count: int


class BillingEntitlementOverrideListItem(ConjoinModel):
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


class BillingEntitlementOverrideUpdateResponse(ConjoinModel):
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


class BillingEntityCreateAccountLinkResponse(ConjoinModel):
    response: Any | None = None


class BillingEntityCreatePayoutBankAccountResponse(ConjoinModel):
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool


class BillingEntityCreatePaystackCredentialsResponse(ConjoinModel):
    response: Any | None = None


class BillingEntityCreateResponse(ConjoinModel):
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool


class BillingEntityListCountResponse(ConjoinModel):
    count: int


class BillingEntityListItem(ConjoinModel):
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool


class BillingEntityOnboardResponse(ConjoinModel):
    response: Any | None = None


class BillingEntityReadResponse(ConjoinModel):
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool


class BillingEntitySyncOnboardingResponse(ConjoinModel):
    response: Any | None = None


class BillingEntityUpdateResponse(ConjoinModel):
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool


class BillingFeatureAccessCheckEntitlementResponse(ConjoinModel):
    allowed: bool
    balance: float | None = None
    consumed: float | None = None
    feature_id: str
    feature_key: str
    feature_type: str
    granted_by: Sequence[str]
    limit: Any | None = None
    used: float | None = None


class BillingFeatureAccessTrackFeatureUsageResponse(ConjoinModel):
    customer_id: str
    feature_id: str
    tracked: bool
    value: float


class BillingInvoiceCreateResponse(ConjoinModel):
    amount_due: float
    amount_paid: float
    amount_remaining: float
    attempted_at: str | None = None
    automatic_finalisation: dict[str, Any] | None = None
    charge_id: str | None = None
    currency: str
    custom_fields: Sequence[dict[str, Any]] | None = None
    customer_id: str
    description: str | None = None
    display_settings: dict[str, Any] | None = None
    due_date: str | None = None
    footer_text: str | None = None
    invoice_id: str
    invoice_number: str
    invoice_url: str | None = None
    invoicing_option: str
    is_paid: bool
    is_paid_without_charge: bool
    line_items: Sequence[dict[str, Any]]
    payment_intent_id: str | None = None
    payment_method_id: str | None = None
    payment_settings: dict[str, Any] | None = None
    price_ids: Sequence[str]
    reference_id: str
    retry_count: float
    status: str
    subscription_id: str | None = None
    subtotal: float
    tax_amount: float


class BillingInvoiceExportPdfResponse(ConjoinModel):
    pdf_url: str


class BillingInvoiceFinalizeResponse(ConjoinModel):
    amount_due: float
    amount_paid: float
    amount_remaining: float
    attempted_at: str | None = None
    automatic_finalisation: dict[str, Any] | None = None
    charge_id: str | None = None
    currency: str
    custom_fields: Sequence[dict[str, Any]] | None = None
    customer_id: str
    description: str | None = None
    display_settings: dict[str, Any] | None = None
    due_date: str | None = None
    footer_text: str | None = None
    invoice_id: str
    invoice_number: str
    invoice_url: str | None = None
    invoicing_option: str
    is_paid: bool
    is_paid_without_charge: bool
    line_items: Sequence[dict[str, Any]]
    payment_intent_id: str | None = None
    payment_method_id: str | None = None
    payment_settings: dict[str, Any] | None = None
    price_ids: Sequence[str]
    reference_id: str
    retry_count: float
    status: str
    subscription_id: str | None = None
    subtotal: float
    tax_amount: float


class BillingInvoiceListCountResponse(ConjoinModel):
    count: int


class BillingInvoiceListItem(ConjoinModel):
    amount_due: float
    amount_paid: float
    amount_remaining: float
    attempted_at: str | None = None
    automatic_finalisation: dict[str, Any] | None = None
    charge_id: str | None = None
    currency: str
    custom_fields: Sequence[dict[str, Any]] | None = None
    customer_id: str
    description: str | None = None
    display_settings: dict[str, Any] | None = None
    due_date: str | None = None
    footer_text: str | None = None
    invoice_id: str
    invoice_number: str
    invoice_url: str | None = None
    invoicing_option: str
    is_paid: bool
    is_paid_without_charge: bool
    line_items: Sequence[dict[str, Any]]
    payment_intent_id: str | None = None
    payment_method_id: str | None = None
    payment_settings: dict[str, Any] | None = None
    price_ids: Sequence[str]
    reference_id: str
    retry_count: float
    status: str
    subscription_id: str | None = None
    subtotal: float
    tax_amount: float


class BillingInvoicePayOutOfBandResponse(ConjoinModel):
    amount_due: float
    amount_paid: float
    amount_remaining: float
    attempted_at: str | None = None
    automatic_finalisation: dict[str, Any] | None = None
    charge_id: str | None = None
    currency: str
    custom_fields: Sequence[dict[str, Any]] | None = None
    customer_id: str
    description: str | None = None
    display_settings: dict[str, Any] | None = None
    due_date: str | None = None
    footer_text: str | None = None
    invoice_id: str
    invoice_number: str
    invoice_url: str | None = None
    invoicing_option: str
    is_paid: bool
    is_paid_without_charge: bool
    line_items: Sequence[dict[str, Any]]
    payment_intent_id: str | None = None
    payment_method_id: str | None = None
    payment_settings: dict[str, Any] | None = None
    price_ids: Sequence[str]
    reference_id: str
    retry_count: float
    status: str
    subscription_id: str | None = None
    subtotal: float
    tax_amount: float


class BillingInvoicePayResponse(ConjoinModel):
    amount_due: float
    amount_paid: float
    amount_remaining: float
    attempted_at: str | None = None
    automatic_finalisation: dict[str, Any] | None = None
    charge_id: str | None = None
    currency: str
    custom_fields: Sequence[dict[str, Any]] | None = None
    customer_id: str
    description: str | None = None
    display_settings: dict[str, Any] | None = None
    due_date: str | None = None
    footer_text: str | None = None
    invoice_id: str
    invoice_number: str
    invoice_url: str | None = None
    invoicing_option: str
    is_paid: bool
    is_paid_without_charge: bool
    line_items: Sequence[dict[str, Any]]
    payment_intent_id: str | None = None
    payment_method_id: str | None = None
    payment_settings: dict[str, Any] | None = None
    price_ids: Sequence[str]
    reference_id: str
    retry_count: float
    status: str
    subscription_id: str | None = None
    subtotal: float
    tax_amount: float


class BillingInvoiceSendResponse(ConjoinModel):
    amount_due: float
    amount_paid: float
    amount_remaining: float
    attempted_at: str | None = None
    automatic_finalisation: dict[str, Any] | None = None
    charge_id: str | None = None
    currency: str
    custom_fields: Sequence[dict[str, Any]] | None = None
    customer_id: str
    description: str | None = None
    display_settings: dict[str, Any] | None = None
    due_date: str | None = None
    footer_text: str | None = None
    invoice_id: str
    invoice_number: str
    invoice_url: str | None = None
    invoicing_option: str
    is_paid: bool
    is_paid_without_charge: bool
    line_items: Sequence[dict[str, Any]]
    payment_intent_id: str | None = None
    payment_method_id: str | None = None
    payment_settings: dict[str, Any] | None = None
    price_ids: Sequence[str]
    reference_id: str
    retry_count: float
    status: str
    subscription_id: str | None = None
    subtotal: float
    tax_amount: float


class BillingInvoiceUpdateResponse(ConjoinModel):
    amount_due: float
    amount_paid: float
    amount_remaining: float
    attempted_at: str | None = None
    automatic_finalisation: dict[str, Any] | None = None
    charge_id: str | None = None
    currency: str
    custom_fields: Sequence[dict[str, Any]] | None = None
    customer_id: str
    description: str | None = None
    display_settings: dict[str, Any] | None = None
    due_date: str | None = None
    footer_text: str | None = None
    invoice_id: str
    invoice_number: str
    invoice_url: str | None = None
    invoicing_option: str
    is_paid: bool
    is_paid_without_charge: bool
    line_items: Sequence[dict[str, Any]]
    payment_intent_id: str | None = None
    payment_method_id: str | None = None
    payment_settings: dict[str, Any] | None = None
    price_ids: Sequence[str]
    reference_id: str
    retry_count: float
    status: str
    subscription_id: str | None = None
    subtotal: float
    tax_amount: float


class BillingInvoiceVoidResponse(ConjoinModel):
    amount_due: float
    amount_paid: float
    amount_remaining: float
    attempted_at: str | None = None
    automatic_finalisation: dict[str, Any] | None = None
    charge_id: str | None = None
    currency: str
    custom_fields: Sequence[dict[str, Any]] | None = None
    customer_id: str
    description: str | None = None
    display_settings: dict[str, Any] | None = None
    due_date: str | None = None
    footer_text: str | None = None
    invoice_id: str
    invoice_number: str
    invoice_url: str | None = None
    invoicing_option: str
    is_paid: bool
    is_paid_without_charge: bool
    line_items: Sequence[dict[str, Any]]
    payment_intent_id: str | None = None
    payment_method_id: str | None = None
    payment_settings: dict[str, Any] | None = None
    price_ids: Sequence[str]
    reference_id: str
    retry_count: float
    status: str
    subscription_id: str | None = None
    subtotal: float
    tax_amount: float


class BillingPaymentIntentListCountResponse(ConjoinModel):
    count: int


class BillingPaymentIntentListItem(ConjoinModel):
    amount: float
    currency: str
    customer_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    entity_id: str
    lookup_key: str | None = None
    payment_intent_id: str
    payment_method_id: str | None = None
    payment_method_types: Sequence[str] | None = None
    price_id: str | None = None
    receipt_email: str | None = None
    reference_id: str
    setup_future_usage: str | None = None
    status: str


class BillingPaymentIntentVerifyResponse(ConjoinModel):
    amount: float
    currency: str
    customer_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    entity_id: str
    lookup_key: str | None = None
    payment_intent_id: str
    payment_method_id: str | None = None
    payment_method_types: Sequence[str] | None = None
    price_id: str | None = None
    receipt_email: str | None = None
    reference_id: str
    setup_future_usage: str | None = None
    status: str


class BillingPaymentMethodDeleteResponse(ConjoinModel):
    brand: str | None = None
    country_of_issuance: str | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    exp_month: float | None = None
    exp_year: float | None = None
    is_active: bool
    is_default: bool
    last4: str | None = None
    name: str | None = None
    payment_method_id: str
    reference_id: str
    type: str | None = None


class BillingPaymentMethodListCountResponse(ConjoinModel):
    count: int


class BillingPaymentMethodListItem(ConjoinModel):
    brand: str | None = None
    country_of_issuance: str | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    exp_month: float | None = None
    exp_year: float | None = None
    is_active: bool
    is_default: bool
    last4: str | None = None
    name: str | None = None
    payment_method_id: str
    reference_id: str
    type: str | None = None


class BillingPriceArchiveResponse(ConjoinModel):
    amount: float
    billing_metadata: dict[str, Any] | None = None
    billing_scheme: str
    conjoin_account_id: str
    conjoin_project_id: str
    currency: str
    currency_options: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool
    live_mode: bool
    price_id: str
    product_id: str
    recurring: dict[str, Any] | None = None
    reference_id: str
    tax_behavior: str | None = None
    tiers: Sequence[dict[str, Any]] | None = None
    tiers_mode: str | None = None
    type: str


class BillingPriceBundleActivateResponse(ConjoinModel):
    activations: Sequence[dict[str, Any]]
    batch_id: str


class BillingPriceBundleArchiveResponse(ConjoinModel):
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


class BillingPriceBundleCreateResponse(ConjoinModel):
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


class BillingPriceBundleDeactivateResponse(ConjoinModel):
    activation_id: str
    batch_id: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    failure_reason: str | None = None
    invoice_id: str | None = None
    live_mode: bool
    previous_activation_id: str | None = None
    price_bundle_id: str
    resolved_items: Sequence[dict[str, Any]]
    status: str
    subscription_id: str | None = None
    tier_group: str | None = None
    tier_rank: float | None = None
    upgrade_strategy: str | None = None


class BillingPriceBundleListActivationsCountResponse(ConjoinModel):
    count: int


class BillingPriceBundleListActivationsItem(ConjoinModel):
    activation_id: str
    batch_id: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    failure_reason: str | None = None
    invoice_id: str | None = None
    live_mode: bool
    previous_activation_id: str | None = None
    price_bundle_id: str
    resolved_items: Sequence[dict[str, Any]]
    status: str
    subscription_id: str | None = None
    tier_group: str | None = None
    tier_rank: float | None = None
    upgrade_strategy: str | None = None


class BillingPriceBundleListCountResponse(ConjoinModel):
    count: int


class BillingPriceBundleListItem(ConjoinModel):
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


class BillingPriceBundlePublishResponse(ConjoinModel):
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


class BillingPriceBundleReadAvailableBundleTransitionsResponse(ConjoinModel):
    active_addons: dict[str, Any]
    available_addons: dict[str, Any]
    available_downgrades: dict[str, Any]
    available_upgrades: dict[str, Any]
    current_tier: dict[str, Any] | None
    customer_id: str
    entity_id: str
    pending_tier_change: dict[str, Any] | None


class BillingPriceBundleReadResponse(ConjoinModel):
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


class BillingPriceBundleRestoreResponse(ConjoinModel):
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


class BillingPriceBundleUpdateResponse(ConjoinModel):
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


class BillingPriceCreateResponse(ConjoinModel):
    amount: float
    billing_metadata: dict[str, Any] | None = None
    billing_scheme: str
    conjoin_account_id: str
    conjoin_project_id: str
    currency: str
    currency_options: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool
    live_mode: bool
    price_id: str
    product_id: str
    recurring: dict[str, Any] | None = None
    reference_id: str
    tax_behavior: str | None = None
    tiers: Sequence[dict[str, Any]] | None = None
    tiers_mode: str | None = None
    type: str


class BillingPriceDeleteResponse(ConjoinModel):
    response: Any | None = None


class BillingPriceListCountResponse(ConjoinModel):
    count: int


class BillingPriceListItem(ConjoinModel):
    amount: float
    billing_metadata: dict[str, Any] | None = None
    billing_scheme: str
    conjoin_account_id: str
    conjoin_project_id: str
    currency: str
    currency_options: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool
    live_mode: bool
    price_id: str
    product_id: str
    recurring: dict[str, Any] | None = None
    reference_id: str
    tax_behavior: str | None = None
    tiers: Sequence[dict[str, Any]] | None = None
    tiers_mode: str | None = None
    type: str


class BillingPriceReadResponse(ConjoinModel):
    amount: float
    billing_metadata: dict[str, Any] | None = None
    billing_scheme: str
    conjoin_account_id: str
    conjoin_project_id: str
    currency: str
    currency_options: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool
    live_mode: bool
    price_id: str
    product_id: str
    recurring: dict[str, Any] | None = None
    reference_id: str
    tax_behavior: str | None = None
    tiers: Sequence[dict[str, Any]] | None = None
    tiers_mode: str | None = None
    type: str


class BillingPriceRestoreResponse(ConjoinModel):
    amount: float
    billing_metadata: dict[str, Any] | None = None
    billing_scheme: str
    conjoin_account_id: str
    conjoin_project_id: str
    currency: str
    currency_options: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool
    live_mode: bool
    price_id: str
    product_id: str
    recurring: dict[str, Any] | None = None
    reference_id: str
    tax_behavior: str | None = None
    tiers: Sequence[dict[str, Any]] | None = None
    tiers_mode: str | None = None
    type: str


class BillingPriceUpdateResponse(ConjoinModel):
    amount: float
    billing_metadata: dict[str, Any] | None = None
    billing_scheme: str
    conjoin_account_id: str
    conjoin_project_id: str
    currency: str
    currency_options: dict[str, Any] | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    is_active: bool
    live_mode: bool
    price_id: str
    product_id: str
    recurring: dict[str, Any] | None = None
    reference_id: str
    tax_behavior: str | None = None
    tiers: Sequence[dict[str, Any]] | None = None
    tiers_mode: str | None = None
    type: str


class BillingProductArchiveResponse(ConjoinModel):
    billing_metadata: dict[str, Any] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    entity_id: str
    features: Sequence[dict[str, Any]] | None = None
    images: Sequence[str] | None = None
    is_active: bool
    live_mode: bool
    name: str
    product_id: str
    reference_id: str
    statement_descriptor: str | None = None
    unit_label: str


class BillingProductCreateResponse(ConjoinModel):
    billing_metadata: dict[str, Any] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    entity_id: str
    features: Sequence[dict[str, Any]] | None = None
    images: Sequence[str] | None = None
    is_active: bool
    live_mode: bool
    name: str
    product_id: str
    reference_id: str
    statement_descriptor: str | None = None
    unit_label: str


class BillingProductDeleteResponse(ConjoinModel):
    response: Any | None = None


class BillingProductListCountResponse(ConjoinModel):
    count: int


class BillingProductListItem(ConjoinModel):
    billing_metadata: dict[str, Any] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    entity_id: str
    features: Sequence[dict[str, Any]] | None = None
    images: Sequence[str] | None = None
    is_active: bool
    live_mode: bool
    name: str
    product_id: str
    reference_id: str
    statement_descriptor: str | None = None
    unit_label: str


class BillingProductReadResponse(ConjoinModel):
    billing_metadata: dict[str, Any] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    entity_id: str
    features: Sequence[dict[str, Any]] | None = None
    images: Sequence[str] | None = None
    is_active: bool
    live_mode: bool
    name: str
    product_id: str
    reference_id: str
    statement_descriptor: str | None = None
    unit_label: str


class BillingProductRestoreResponse(ConjoinModel):
    billing_metadata: dict[str, Any] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    entity_id: str
    features: Sequence[dict[str, Any]] | None = None
    images: Sequence[str] | None = None
    is_active: bool
    live_mode: bool
    name: str
    product_id: str
    reference_id: str
    statement_descriptor: str | None = None
    unit_label: str


class BillingProductUpdateResponse(ConjoinModel):
    billing_metadata: dict[str, Any] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    entity_id: str
    features: Sequence[dict[str, Any]] | None = None
    images: Sequence[str] | None = None
    is_active: bool
    live_mode: bool
    name: str
    product_id: str
    reference_id: str
    statement_descriptor: str | None = None
    unit_label: str


class BillingReceiptListCountResponse(ConjoinModel):
    count: int


class BillingReceiptListItem(ConjoinModel):
    amount: float
    charge_id: str
    currency: str
    customer_id: str | None
    date_created: str
    date_deleted: str | None
    date_updated: str | None
    entity_id: str
    error_reason: str | None
    pdf_url: str | None
    receipt_id: str
    status: str


class BillingReceiptReadResponse(ConjoinModel):
    amount: float
    charge_id: str
    currency: str
    customer_id: str | None
    date_created: str
    date_deleted: str | None
    date_updated: str | None
    entity_id: str
    error_reason: str | None
    pdf_url: str | None
    receipt_id: str
    status: str


class BillingRefundCreateResponse(ConjoinModel):
    amount: float
    charge_id: str
    currency: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    fulfilment_type: str
    reference_id: str
    refund_id: str
    status: str


class BillingRefundListCountResponse(ConjoinModel):
    count: int


class BillingRefundListItem(ConjoinModel):
    amount: float
    charge_id: str
    currency: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    fulfilment_type: str
    reference_id: str
    refund_id: str
    status: str


class BillingSettingsReadResponse(ConjoinModel):
    auto_receipt_generation: bool
    cancellation_fallback_behavior: str
    conjoin_account_id: str
    conjoin_project_id: str
    credit_auto_apply: bool
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    default_currency: str | None = None
    default_invoice_settings: dict[str, Any] | None = None
    incompatible_addon_behavior: str
    live_mode: bool
    settings_id: str
    tax_reporting_enabled: bool


class BillingSettingsUpdateResponse(ConjoinModel):
    auto_receipt_generation: bool
    cancellation_fallback_behavior: str
    conjoin_account_id: str
    conjoin_project_id: str
    credit_auto_apply: bool
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    default_currency: str | None = None
    default_invoice_settings: dict[str, Any] | None = None
    incompatible_addon_behavior: str
    live_mode: bool
    settings_id: str
    tax_reporting_enabled: bool


class BillingSubscriptionCancelResponse(ConjoinModel):
    auto_renew: bool | None = None
    cancellation: dict[str, Any] | None = None
    currency: str
    current_cycle: dict[str, Any] | None = None
    customer_id: str
    cycle_start_date: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    days_until_due: float | None = None
    end_date: str | None = None
    entity_id: str
    invoicing_option: str
    latest_state_transition: dict[str, Any] | None = None
    live_mode: bool
    payment_method: str | None = None
    payment_strategy: str
    plans: Sequence[dict[str, Any]]
    proration: dict[str, Any] | None = None
    reference_id: str
    renewal_notifications: dict[str, Any] | None = None
    start_date: str
    status: str
    subscription_id: str
    trial_end_date: str | None = None
    trial_start_date: str | None = None


class BillingSubscriptionCreatePlanChangeResponse(ConjoinModel):
    applied_proration_behavior: str
    subscription: dict[str, Any]


class BillingSubscriptionCreateResponse(ConjoinModel):
    auto_renew: bool | None = None
    cancellation: dict[str, Any] | None = None
    currency: str
    current_cycle: dict[str, Any] | None = None
    customer_id: str
    cycle_start_date: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    days_until_due: float | None = None
    end_date: str | None = None
    entity_id: str
    invoicing_option: str
    latest_state_transition: dict[str, Any] | None = None
    live_mode: bool
    payment_method: str | None = None
    payment_strategy: str
    plans: Sequence[dict[str, Any]]
    proration: dict[str, Any] | None = None
    reference_id: str
    renewal_notifications: dict[str, Any] | None = None
    start_date: str
    status: str
    subscription_id: str
    trial_end_date: str | None = None
    trial_start_date: str | None = None


class BillingSubscriptionListCountResponse(ConjoinModel):
    count: int


class BillingSubscriptionListCyclesCountResponse(ConjoinModel):
    count: int


class BillingSubscriptionListCyclesItem(ConjoinModel):
    amount: float
    billed_at: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    currency: str
    cycle_id: str
    cycle_sequence: float
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    entity_id: str
    invoice_id: str | None = None
    live_mode: bool
    period_end: str
    period_start: str
    status: str
    subscription_id: str
    usage_data: Sequence[dict[str, Any]] | None = None


class BillingSubscriptionListItem(ConjoinModel):
    auto_renew: bool | None = None
    cancellation: dict[str, Any] | None = None
    currency: str
    current_cycle: dict[str, Any] | None = None
    customer_id: str
    cycle_start_date: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    days_until_due: float | None = None
    end_date: str | None = None
    entity_id: str
    invoicing_option: str
    latest_state_transition: dict[str, Any] | None = None
    live_mode: bool
    payment_method: str | None = None
    payment_strategy: str
    plans: Sequence[dict[str, Any]]
    proration: dict[str, Any] | None = None
    reference_id: str
    renewal_notifications: dict[str, Any] | None = None
    start_date: str
    status: str
    subscription_id: str
    trial_end_date: str | None = None
    trial_start_date: str | None = None


class BillingSubscriptionPauseResponse(ConjoinModel):
    auto_renew: bool | None = None
    cancellation: dict[str, Any] | None = None
    currency: str
    current_cycle: dict[str, Any] | None = None
    customer_id: str
    cycle_start_date: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    days_until_due: float | None = None
    end_date: str | None = None
    entity_id: str
    invoicing_option: str
    latest_state_transition: dict[str, Any] | None = None
    live_mode: bool
    payment_method: str | None = None
    payment_strategy: str
    plans: Sequence[dict[str, Any]]
    proration: dict[str, Any] | None = None
    reference_id: str
    renewal_notifications: dict[str, Any] | None = None
    start_date: str
    status: str
    subscription_id: str
    trial_end_date: str | None = None
    trial_start_date: str | None = None


class BillingSubscriptionReadResponse(ConjoinModel):
    auto_renew: bool | None = None
    cancellation: dict[str, Any] | None = None
    currency: str
    current_cycle: dict[str, Any] | None = None
    customer_id: str
    cycle_start_date: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    days_until_due: float | None = None
    end_date: str | None = None
    entity_id: str
    invoicing_option: str
    latest_state_transition: dict[str, Any] | None = None
    live_mode: bool
    payment_method: str | None = None
    payment_strategy: str
    plans: Sequence[dict[str, Any]]
    proration: dict[str, Any] | None = None
    reference_id: str
    renewal_notifications: dict[str, Any] | None = None
    start_date: str
    status: str
    subscription_id: str
    trial_end_date: str | None = None
    trial_start_date: str | None = None


class BillingSubscriptionReadUsageSummaryItem(ConjoinModel):
    aggregate_usage: str | None
    currency: str
    plan_id: str
    plan_name: str
    usage_amount: float
    usage_quantity: float
    usage_type: str


class BillingSubscriptionResumeResponse(ConjoinModel):
    auto_renew: bool | None = None
    cancellation: dict[str, Any] | None = None
    currency: str
    current_cycle: dict[str, Any] | None = None
    customer_id: str
    cycle_start_date: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    days_until_due: float | None = None
    end_date: str | None = None
    entity_id: str
    invoicing_option: str
    latest_state_transition: dict[str, Any] | None = None
    live_mode: bool
    payment_method: str | None = None
    payment_strategy: str
    plans: Sequence[dict[str, Any]]
    proration: dict[str, Any] | None = None
    reference_id: str
    renewal_notifications: dict[str, Any] | None = None
    start_date: str
    status: str
    subscription_id: str
    trial_end_date: str | None = None
    trial_start_date: str | None = None


class BillingSubscriptionScheduleCancelResponse(ConjoinModel):
    canceled_date: str | None = None
    completed_date: str | None = None
    current_phase_index: float | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    end_behavior: str
    entity_id: str
    live_mode: bool
    phases: Sequence[dict[str, Any]]
    released_date: str | None = None
    schedule_id: str
    status: str
    subscription_id: str


class BillingSubscriptionScheduleCreateResponse(ConjoinModel):
    canceled_date: str | None = None
    completed_date: str | None = None
    current_phase_index: float | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    end_behavior: str
    entity_id: str
    live_mode: bool
    phases: Sequence[dict[str, Any]]
    released_date: str | None = None
    schedule_id: str
    status: str
    subscription_id: str


class BillingSubscriptionScheduleGetResponse(ConjoinModel):
    canceled_date: str | None = None
    completed_date: str | None = None
    current_phase_index: float | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    end_behavior: str
    entity_id: str
    live_mode: bool
    phases: Sequence[dict[str, Any]]
    released_date: str | None = None
    schedule_id: str
    status: str
    subscription_id: str


class BillingSubscriptionScheduleListCountResponse(ConjoinModel):
    count: int


class BillingSubscriptionScheduleListItem(ConjoinModel):
    canceled_date: str | None = None
    completed_date: str | None = None
    current_phase_index: float | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    end_behavior: str
    entity_id: str
    live_mode: bool
    phases: Sequence[dict[str, Any]]
    released_date: str | None = None
    schedule_id: str
    status: str
    subscription_id: str


class BillingSubscriptionScheduleReleaseResponse(ConjoinModel):
    canceled_date: str | None = None
    completed_date: str | None = None
    current_phase_index: float | None = None
    customer_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    end_behavior: str
    entity_id: str
    live_mode: bool
    phases: Sequence[dict[str, Any]]
    released_date: str | None = None
    schedule_id: str
    status: str
    subscription_id: str


class BillingSubscriptionUpdateResponse(ConjoinModel):
    auto_renew: bool | None = None
    cancellation: dict[str, Any] | None = None
    currency: str
    current_cycle: dict[str, Any] | None = None
    customer_id: str
    cycle_start_date: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    days_until_due: float | None = None
    end_date: str | None = None
    entity_id: str
    invoicing_option: str
    latest_state_transition: dict[str, Any] | None = None
    live_mode: bool
    payment_method: str | None = None
    payment_strategy: str
    plans: Sequence[dict[str, Any]]
    proration: dict[str, Any] | None = None
    reference_id: str
    renewal_notifications: dict[str, Any] | None = None
    start_date: str
    status: str
    subscription_id: str
    trial_end_date: str | None = None
    trial_start_date: str | None = None


class BillingTaxJurisdictionListCountResponse(ConjoinModel):
    count: int


class BillingTaxJurisdictionListItem(ConjoinModel):
    component_breakdown: Sequence[dict[str, Any]] | None = None
    country: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    effective_from: str
    effective_until: str | None = None
    exchange_rules: dict[str, Any] | None = None
    is_active: bool
    jurisdiction_id: str
    live_mode: bool
    rate: float
    state: str | None = None
    tax_type: str
    timezone: str


class BillingTaxJurisdictionQueryTaxRateResponse(ConjoinModel):
    component_breakdown: Sequence[dict[str, Any]] | None = None
    country: str
    rate: float
    state: str | None = None
    tax_type: str


class CloudAPIKeyReadApiKeysCountResponse(ConjoinModel):
    count: int


class CloudAPIKeyReadApiKeysItem(ConjoinModel):
    api_key_id: str
    date_created: str
    date_expired: str | None = None
    date_updated: str | None = None
    description: str | None = None
    entity_id: str
    has_expired: bool
    name: str
    project_id: str
    reference_id: str | None = None
    roles: Sequence[str]
    service_ids: Sequence[str] | None = None
    test_mode: bool


class CloudAPIKeyUpdateApiKeyResponse(ConjoinModel):
    api_key_id: str
    date_created: str
    date_expired: str | None = None
    date_updated: str | None = None
    description: str | None = None
    entity_id: str
    has_expired: bool
    name: str
    project_id: str
    reference_id: str | None = None
    roles: Sequence[str]
    service_ids: Sequence[str] | None = None
    test_mode: bool


class CloudAccountReadResponse(ConjoinModel):
    approved_services: Sequence[str]
    billing_customer_id: str | None
    billing_default_currency: str | None
    billing_subscription_id: str | None
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    entity_id: str
    inactivity_status: dict[str, Any]
    is_active: bool
    onboarding_status: dict[str, Any]
    plan_id: str | None
    region: str
    service_agreement: dict[str, Any]
    services_in_use: Sequence[str]


class CloudAccountUpdateResponse(ConjoinModel):
    approved_services: Sequence[str]
    billing_customer_id: str | None
    billing_default_currency: str | None
    billing_subscription_id: str | None
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    entity_id: str
    inactivity_status: dict[str, Any]
    is_active: bool
    onboarding_status: dict[str, Any]
    plan_id: str | None
    region: str
    service_agreement: dict[str, Any]
    services_in_use: Sequence[str]


class CloudAuditReadLogsCountResponse(ConjoinModel):
    count: int


class CloudAuditReadLogsItem(ConjoinModel):
    actor: dict[str, Any]
    audit_id: str
    categories: Sequence[str]
    cloud_account_id: str
    conjoin_request_id: str
    correlation_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    entity_id: str
    event_code: str
    expire_at: str | None = None
    idempotency_key: str
    occurred_at: str
    organization_id: str
    payload: dict[str, Any]
    payload_size: float
    producer_context: dict[str, Any] | None = None
    project_id: str
    recorded_at: str
    request_id: str | None = None
    resource: dict[str, Any] | None = None
    schema_version: float
    sensitive_fields_removed: Sequence[str] | None = None
    service: str
    severity: str | None = None
    trace_source: str | None = None


class CloudAuditReadStatsResponse(ConjoinModel):
    categories: dict[str, float]
    services: dict[str, float]
    total_events: float


class CloudBrandingGetOrgOverrideResponse(ConjoinModel):
    accessibility: dict[str, Any] | None = None
    animation: dict[str, Any] | None = None
    borders: dict[str, Any] | None = None
    colors: dict[str, Any] | None = None
    components: dict[str, Any] | None = None
    date_created: str
    date_updated: str | None = None
    general: dict[str, Any] | None = None
    layout: dict[str, Any] | None = None
    organization: dict[str, Any] | None = None
    organization_id: str
    override_id: str
    schema_version: float
    shadows: dict[str, Any] | None = None
    spacing: dict[str, Any] | None = None
    typography: dict[str, Any] | None = None


class CloudBrandingGetProjectResponse(ConjoinModel):
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


class CloudBrandingPatchOrgOverrideResponse(ConjoinModel):
    accessibility: dict[str, Any] | None = None
    animation: dict[str, Any] | None = None
    borders: dict[str, Any] | None = None
    colors: dict[str, Any] | None = None
    components: dict[str, Any] | None = None
    date_created: str
    date_updated: str | None = None
    general: dict[str, Any] | None = None
    layout: dict[str, Any] | None = None
    organization: dict[str, Any] | None = None
    organization_id: str
    override_id: str
    schema_version: float
    shadows: dict[str, Any] | None = None
    spacing: dict[str, Any] | None = None
    typography: dict[str, Any] | None = None


class CloudBrandingPatchProjectResponse(ConjoinModel):
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


class CloudOrganizationCreateResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_updated: str | None = None
    entity_id: str
    name: str
    organization_id: str
    reference_id: str | None = None
    tags: Sequence[str] | None = None


class CloudOrganizationListItem(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_updated: str | None = None
    entity_id: str
    name: str
    organization_id: str
    reference_id: str | None = None
    tags: Sequence[str] | None = None


class CloudOrganizationReadCountResponse(ConjoinModel):
    count: int


class CloudOrganizationReadResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_updated: str | None = None
    entity_id: str
    name: str
    organization_id: str
    reference_id: str | None = None
    tags: Sequence[str] | None = None


class CloudOrganizationUpdateResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_updated: str | None = None
    entity_id: str
    name: str
    organization_id: str
    reference_id: str | None = None
    tags: Sequence[str] | None = None


class CloudPlanListItem(ConjoinModel):
    billing_bundle_id: str | None
    cloud_plan_id: str
    currency: str
    date_created: str
    date_updated: str | None = None
    description: str | None = None
    effective_from: str | None = None
    name: str
    plan_items: Sequence[dict[str, Any]]
    replaces_plan_id: str | None = None
    slug: str
    spend_control_defaults: dict[str, Any] | None = None
    status: str


class CloudPlanReadCountResponse(ConjoinModel):
    count: int


class CloudPlanReadResponse(ConjoinModel):
    billing_bundle_id: str | None
    cloud_plan_id: str
    currency: str
    date_created: str
    date_updated: str | None = None
    description: str | None = None
    effective_from: str | None = None
    name: str
    plan_items: Sequence[dict[str, Any]]
    replaces_plan_id: str | None = None
    slug: str
    spend_control_defaults: dict[str, Any] | None = None
    status: str


class CloudProjectCreateResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    entity_id: str
    name: str | None = None
    organization_id: str
    project_id: str
    reference_id: str | None = None
    tags: Sequence[str]


class CloudProjectListItem(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    entity_id: str
    name: str | None = None
    organization_id: str
    project_id: str
    reference_id: str | None = None
    tags: Sequence[str]


class CloudProjectReadCountResponse(ConjoinModel):
    count: int


class CloudProjectReadResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    entity_id: str
    name: str | None = None
    organization_id: str
    project_id: str
    reference_id: str | None = None
    tags: Sequence[str]


class CloudProjectUpdateResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    entity_id: str
    name: str | None = None
    organization_id: str
    project_id: str
    reference_id: str | None = None
    tags: Sequence[str]


class CloudPublishableKeyListCountResponse(ConjoinModel):
    count: int


class CloudPublishableKeyListItem(ConjoinModel):
    allowed_domains: Sequence[str]
    date_created: str
    date_revoked: str | None = None
    date_updated: str | None = None
    is_active: bool
    project_id: str
    publishable_key_id: str
    test_mode: bool


class CloudPublishableKeyUpdateResponse(ConjoinModel):
    allowed_domains: Sequence[str]
    date_created: str
    date_revoked: str | None = None
    date_updated: str | None = None
    is_active: bool
    project_id: str
    publishable_key_id: str
    test_mode: bool


class CloudRoleCreateResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_updated: str | None = None
    description: str | None = None
    entity_id: str
    name: str
    reference_id: str | None = None
    role_id: str
    title: str
    total_permissions: float


class CloudRoleReadCountResponse(ConjoinModel):
    count: int


class CloudRoleReadItem(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_updated: str | None = None
    description: str | None = None
    entity_id: str
    name: str
    reference_id: str | None = None
    role_id: str
    title: str
    total_permissions: float


class CloudRoleUpdateResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_updated: str | None = None
    description: str | None = None
    entity_id: str
    name: str
    reference_id: str | None = None
    role_id: str
    title: str
    total_permissions: float


class CloudSKUCatalogReadSingleSkuCatalogResponse(ConjoinModel):
    category: str
    description: str
    meter_type: str
    name: str
    service: str
    sku_code: str
    sku_id: str
    unit_label: str


class CloudSKUCatalogReadSkuCatalogCountResponse(ConjoinModel):
    count: int


class CloudSKUCatalogReadSkuCatalogItem(ConjoinModel):
    category: str
    description: str
    meter_type: str
    name: str
    service: str
    sku_code: str
    sku_id: str
    unit_label: str


class CloudSpendControlReadResponse(ConjoinModel):
    ai_circuit_breaker_limits: Sequence[dict[str, Any]]
    alert_email_enabled: bool
    alert_sms_enabled: bool
    alert_thresholds: Sequence[float]
    alert_webhook_enabled: bool
    cloud_account_id: str
    currency: str
    date_created: str
    date_updated: str | None = None
    overage_budget_micros: float
    spend_control_id: str


class CloudSpendControlReadUsageResponse(ConjoinModel):
    ai_usage: Sequence[dict[str, Any]]
    billing_cycle_resets_at: str
    billing_period: str
    cloud_account_id: str
    currency: str
    overage_budget_micros: float
    overage_used_micros: float
    service_overage_breakdown: Sequence[dict[str, Any]]


class CloudSpendControlUpdateResponse(ConjoinModel):
    ai_circuit_breaker_limits: Sequence[dict[str, Any]]
    alert_email_enabled: bool
    alert_sms_enabled: bool
    alert_thresholds: Sequence[float]
    alert_webhook_enabled: bool
    cloud_account_id: str
    currency: str
    date_created: str
    date_updated: str | None = None
    overage_budget_micros: float
    spend_control_id: str


class CloudWebhookListItem(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    description: str | None = None
    entity_id: str
    events: Sequence[str]
    is_active: bool
    name: str | None = None
    project_id: str
    url: str
    webhook_id: str


class CloudWebhookReadCountResponse(ConjoinModel):
    count: int


class CloudWebhookReadEventsCountResponse(ConjoinModel):
    count: int


class CloudWebhookReadEventsItem(ConjoinModel):
    description: str
    event_id: str


class CloudWebhookReadResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    description: str | None = None
    entity_id: str
    events: Sequence[str]
    is_active: bool
    name: str | None = None
    project_id: str
    url: str
    webhook_id: str


class CloudWebhookRegisterResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    description: str | None = None
    entity_id: str
    events: Sequence[str]
    is_active: bool
    name: str | None = None
    project_id: str
    url: str
    webhook_id: str


class CloudWebhookUpdateResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    description: str | None = None
    entity_id: str
    events: Sequence[str]
    is_active: bool
    name: str | None = None
    project_id: str
    url: str
    webhook_id: str


class CloudZoneCreateResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    dkim_authority: str
    dns_records: Sequence[dict[str, Any]]
    domain: str
    entity_id: str
    external_dns_records: Sequence[dict[str, Any]]
    is_internal_zone: bool
    project_id: str
    provider_id: str
    reference_id: str | None = None
    status: str
    verification_record: dict[str, Any] | None
    zone_id: str


class CloudZoneListItem(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    dkim_authority: str
    dns_records: Sequence[dict[str, Any]]
    domain: str
    entity_id: str
    external_dns_records: Sequence[dict[str, Any]]
    is_internal_zone: bool
    project_id: str
    provider_id: str
    reference_id: str | None = None
    status: str
    verification_record: dict[str, Any] | None
    zone_id: str


class CloudZoneReadCountResponse(ConjoinModel):
    count: int


class CloudZoneReadResponse(ConjoinModel):
    cloud_account_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str | None = None
    dkim_authority: str
    dns_records: Sequence[dict[str, Any]]
    domain: str
    entity_id: str
    external_dns_records: Sequence[dict[str, Any]]
    is_internal_zone: bool
    project_id: str
    provider_id: str
    reference_id: str | None = None
    status: str
    verification_record: dict[str, Any] | None
    zone_id: str


class MessagingChannelAnalyticsCreateReportResponse(ConjoinModel):
    url: str


class MessagingChannelAnalyticsGenerateSummariesResponse(ConjoinModel):
    bounces: dict[str, Any]
    channel_id: str
    clicks: dict[str, Any]
    complaints: dict[str, Any]
    deliveries: dict[str, Any]
    duration: str
    failures: dict[str, Any]
    label: str
    opens: dict[str, Any]
    period_end: str
    period_start: str
    periods: Sequence[dict[str, Any]]
    rejections: dict[str, Any]
    subscribes: dict[str, Any]
    total_message_count: float
    unsubscribes: dict[str, Any]


class MessagingChannelAnalyticsIncrementClicksResponse(ConjoinModel):
    analytics_id: str
    bounces: dict[str, Any]
    channel_id: str
    clicks: dict[str, Any]
    complaints: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str | None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    deliveries: dict[str, Any]
    failures: dict[str, Any]
    live_mode: bool
    message_request_id: str
    opens: dict[str, Any]
    profile_id: str
    rejections: dict[str, Any]
    subscribes: dict[str, Any]
    total_message_count: float
    unsubscribes: dict[str, Any]


class MessagingChannelAnalyticsIncrementDeliveriesResponse(ConjoinModel):
    analytics_id: str
    bounces: dict[str, Any]
    channel_id: str
    clicks: dict[str, Any]
    complaints: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str | None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    deliveries: dict[str, Any]
    failures: dict[str, Any]
    live_mode: bool
    message_request_id: str
    opens: dict[str, Any]
    profile_id: str
    rejections: dict[str, Any]
    subscribes: dict[str, Any]
    total_message_count: float
    unsubscribes: dict[str, Any]


class MessagingChannelAnalyticsIncrementOpensResponse(ConjoinModel):
    analytics_id: str
    bounces: dict[str, Any]
    channel_id: str
    clicks: dict[str, Any]
    complaints: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str | None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    deliveries: dict[str, Any]
    failures: dict[str, Any]
    live_mode: bool
    message_request_id: str
    opens: dict[str, Any]
    profile_id: str
    rejections: dict[str, Any]
    subscribes: dict[str, Any]
    total_message_count: float
    unsubscribes: dict[str, Any]


class MessagingChannelAnalyticsIncrementSubscribesResponse(ConjoinModel):
    analytics_id: str
    bounces: dict[str, Any]
    channel_id: str
    clicks: dict[str, Any]
    complaints: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str | None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    deliveries: dict[str, Any]
    failures: dict[str, Any]
    live_mode: bool
    message_request_id: str
    opens: dict[str, Any]
    profile_id: str
    rejections: dict[str, Any]
    subscribes: dict[str, Any]
    total_message_count: float
    unsubscribes: dict[str, Any]


class MessagingChannelAnalyticsIncrementUnsubscribesResponse(ConjoinModel):
    analytics_id: str
    bounces: dict[str, Any]
    channel_id: str
    clicks: dict[str, Any]
    complaints: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str | None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    deliveries: dict[str, Any]
    failures: dict[str, Any]
    live_mode: bool
    message_request_id: str
    opens: dict[str, Any]
    profile_id: str
    rejections: dict[str, Any]
    subscribes: dict[str, Any]
    total_message_count: float
    unsubscribes: dict[str, Any]


class MessagingChannelAnalyticsListItem(ConjoinModel):
    analytics_id: str
    bounces: dict[str, Any]
    channel_id: str
    clicks: dict[str, Any]
    complaints: dict[str, Any]
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str | None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    deliveries: dict[str, Any]
    failures: dict[str, Any]
    live_mode: bool
    message_request_id: str
    opens: dict[str, Any]
    profile_id: str
    rejections: dict[str, Any]
    subscribes: dict[str, Any]
    total_message_count: float
    unsubscribes: dict[str, Any]


class MessagingContactAddPropertiesResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    live_mode: bool
    phone_number: Any | None = None
    preferred_channels: Sequence[str] | None = None
    profile_id: str
    properties: dict[str, Any] | None = None
    quiet_hours: dict[str, Any] | None = None
    reference_id: str | None = None
    timezone: str | None = None


class MessagingContactCreateResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    live_mode: bool
    phone_number: Any | None = None
    preferred_channels: Sequence[str] | None = None
    profile_id: str
    properties: dict[str, Any] | None = None
    quiet_hours: dict[str, Any] | None = None
    reference_id: str | None = None
    timezone: str | None = None


class MessagingContactDeletePropertiesResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    live_mode: bool
    phone_number: Any | None = None
    preferred_channels: Sequence[str] | None = None
    profile_id: str
    properties: dict[str, Any] | None = None
    quiet_hours: dict[str, Any] | None = None
    reference_id: str | None = None
    timezone: str | None = None


class MessagingContactDeleteResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    live_mode: bool
    phone_number: Any | None = None
    preferred_channels: Sequence[str] | None = None
    profile_id: str
    properties: dict[str, Any] | None = None
    quiet_hours: dict[str, Any] | None = None
    reference_id: str | None = None
    timezone: str | None = None


class MessagingContactListItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    live_mode: bool
    phone_number: Any | None = None
    preferred_channels: Sequence[str] | None = None
    profile_id: str
    properties: dict[str, Any] | None = None
    quiet_hours: dict[str, Any] | None = None
    reference_id: str | None = None
    timezone: str | None = None


class MessagingContactPropertiesCreateContactPropertyResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    default_value: Any
    key: str
    live_mode: bool
    profile_id: str
    property_id: str
    type: str


class MessagingContactPropertiesDeleteContactPropertyResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    default_value: Any
    key: str
    live_mode: bool
    profile_id: str
    property_id: str
    type: str


class MessagingContactPropertiesDeleteManyItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    default_value: Any
    key: str
    live_mode: bool
    profile_id: str
    property_id: str
    type: str


class MessagingContactPropertiesFetchOneContactPropertyResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    default_value: Any
    key: str
    live_mode: bool
    profile_id: str
    property_id: str
    type: str


class MessagingContactPropertiesListItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    default_value: Any
    key: str
    live_mode: bool
    profile_id: str
    property_id: str
    type: str


class MessagingContactSuppressMessagesResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    live_mode: bool
    phone_number: Any | None = None
    preferred_channels: Sequence[str] | None = None
    profile_id: str
    properties: dict[str, Any] | None = None
    quiet_hours: dict[str, Any] | None = None
    reference_id: str | None = None
    timezone: str | None = None


class MessagingContactUpdatePropertyResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    live_mode: bool
    phone_number: Any | None = None
    preferred_channels: Sequence[str] | None = None
    profile_id: str
    properties: dict[str, Any] | None = None
    quiet_hours: dict[str, Any] | None = None
    reference_id: str | None = None
    timezone: str | None = None


class MessagingContactUpdateResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    live_mode: bool
    phone_number: Any | None = None
    preferred_channels: Sequence[str] | None = None
    profile_id: str
    properties: dict[str, Any] | None = None
    quiet_hours: dict[str, Any] | None = None
    reference_id: str | None = None
    timezone: str | None = None


class MessagingConversationAddManyRecipientsItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    conversation_id: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    profile_id: str
    recipient_id: str
    reference_id: str | None = None


class MessagingConversationAddOneRecipientResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    conversation_id: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    profile_id: str
    recipient_id: str
    reference_id: str | None = None


class MessagingConversationArchiveResponse(ConjoinModel):
    accepts_replies: bool
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    message_channels: dict[str, Any]
    placeholders: dict[str, Any] | None = None
    profile_id: str
    reference_id: str | None = None
    senders: dict[str, Any] | None = None
    title: str
    total_recipients: float


class MessagingConversationCloneResponse(ConjoinModel):
    accepts_replies: bool
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    message_channels: dict[str, Any]
    placeholders: dict[str, Any] | None = None
    profile_id: str
    reference_id: str | None = None
    senders: dict[str, Any] | None = None
    title: str
    total_recipients: float


class MessagingConversationCreateResponse(ConjoinModel):
    accepts_replies: bool
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    message_channels: dict[str, Any]
    placeholders: dict[str, Any] | None = None
    profile_id: str
    reference_id: str | None = None
    senders: dict[str, Any] | None = None
    title: str
    total_recipients: float


class MessagingConversationDeleteRecipientsResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    conversation_id: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    profile_id: str
    recipient_id: str
    reference_id: str | None = None


class MessagingConversationDeleteResponse(ConjoinModel):
    accepts_replies: bool
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    message_channels: dict[str, Any]
    placeholders: dict[str, Any] | None = None
    profile_id: str
    reference_id: str | None = None
    senders: dict[str, Any] | None = None
    title: str
    total_recipients: float


class MessagingConversationListItem(ConjoinModel):
    accepts_replies: bool
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    message_channels: dict[str, Any]
    placeholders: dict[str, Any] | None = None
    profile_id: str
    reference_id: str | None = None
    senders: dict[str, Any] | None = None
    title: str
    total_recipients: float


class MessagingConversationReadManyRecipientsItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    conversation_id: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    profile_id: str
    recipient_id: str
    reference_id: str | None = None


class MessagingConversationReadOneRecipientResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    contact_id: str
    conversation_id: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    profile_id: str
    recipient_id: str
    reference_id: str | None = None


class MessagingConversationUpdateResponse(ConjoinModel):
    accepts_replies: bool
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    message_channels: dict[str, Any]
    placeholders: dict[str, Any] | None = None
    profile_id: str
    reference_id: str | None = None
    senders: dict[str, Any] | None = None
    title: str
    total_recipients: float


class MessagingEmailGenerateSummaryResponse(ConjoinModel):
    currency: str
    message_body: str
    price_per_part: float
    total_message_parts: float
    total_price: float
    total_recipients: float


class MessagingEmailReadMessagesItem(ConjoinModel):
    accepts_replies: bool
    attachments: Sequence[dict[str, Any]] | None = None
    bcc: Sequence[str] | None = None
    body: str
    cc: Sequence[str] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    from_: str = Field(..., alias='from')
    live_mode: bool
    message_id: str
    parent_message_id: str | None = None
    profile_id: str
    reference_id: str | None = None
    reply_to: str | None = None
    send_at: str | None = None
    sent_at: str
    status: str
    subject: str
    tracking: dict[str, Any] | None = None
    type: str


class MessagingEmailSendResponse(ConjoinModel):
    accepts_replies: bool
    attachments: Sequence[dict[str, Any]] | None = None
    bcc: Sequence[str] | None = None
    body: str
    cc: Sequence[str] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    from_: str = Field(..., alias='from')
    live_mode: bool
    message_id: str
    parent_message_id: str | None = None
    profile_id: str
    reference_id: str | None = None
    reply_to: str | None = None
    send_at: str | None = None
    sent_at: str
    status: str
    subject: str
    tracking: dict[str, Any] | None = None
    type: str


class MessagingEmailSenderCreateResponse(ConjoinModel):
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    dns_records: Sequence[dict[str, Any]] | None = None
    is_default_sender: bool | None = None
    is_test_sender: bool | None = None
    live_mode: bool
    message_quotas: dict[str, Any]
    profile_id: str
    provisioned_at: str | None = None
    queue_details: dict[str, Any] | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    sender_type: str
    status: str
    submitted_at: str
    tracking_details: dict[str, Any] | None = None


class MessagingEmailSenderDeleteResponse(ConjoinModel):
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    dns_records: Sequence[dict[str, Any]] | None = None
    is_default_sender: bool | None = None
    is_test_sender: bool | None = None
    live_mode: bool
    message_quotas: dict[str, Any]
    profile_id: str
    provisioned_at: str | None = None
    queue_details: dict[str, Any] | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    sender_type: str
    status: str
    submitted_at: str
    tracking_details: dict[str, Any] | None = None


class MessagingEmailSenderDisableResponse(ConjoinModel):
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    dns_records: Sequence[dict[str, Any]] | None = None
    is_default_sender: bool | None = None
    is_test_sender: bool | None = None
    live_mode: bool
    message_quotas: dict[str, Any]
    profile_id: str
    provisioned_at: str | None = None
    queue_details: dict[str, Any] | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    sender_type: str
    status: str
    submitted_at: str
    tracking_details: dict[str, Any] | None = None


class MessagingEmailSenderEnableResponse(ConjoinModel):
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    dns_records: Sequence[dict[str, Any]] | None = None
    is_default_sender: bool | None = None
    is_test_sender: bool | None = None
    live_mode: bool
    message_quotas: dict[str, Any]
    profile_id: str
    provisioned_at: str | None = None
    queue_details: dict[str, Any] | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    sender_type: str
    status: str
    submitted_at: str
    tracking_details: dict[str, Any] | None = None


class MessagingEmailSenderListManyItem(ConjoinModel):
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    dns_records: Sequence[dict[str, Any]] | None = None
    is_default_sender: bool | None = None
    is_test_sender: bool | None = None
    live_mode: bool
    message_quotas: dict[str, Any]
    profile_id: str
    provisioned_at: str | None = None
    queue_details: dict[str, Any] | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    sender_type: str
    status: str
    submitted_at: str
    tracking_details: dict[str, Any] | None = None


class MessagingEmailSenderListOneResponse(ConjoinModel):
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    dns_records: Sequence[dict[str, Any]] | None = None
    is_default_sender: bool | None = None
    is_test_sender: bool | None = None
    live_mode: bool
    message_quotas: dict[str, Any]
    profile_id: str
    provisioned_at: str | None = None
    queue_details: dict[str, Any] | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    sender_type: str
    status: str
    submitted_at: str
    tracking_details: dict[str, Any] | None = None


class MessagingEmailSenderPoolAddEmailSendersToPoolResponse(ConjoinModel):
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    pool_id: str
    profile_id: str
    senders: Sequence[str]
    title: str


class MessagingEmailSenderPoolCreateResponse(ConjoinModel):
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    pool_id: str
    profile_id: str
    senders: Sequence[str]
    title: str


class MessagingEmailSenderPoolDeleteResponse(ConjoinModel):
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    pool_id: str
    profile_id: str
    senders: Sequence[str]
    title: str


class MessagingEmailSenderPoolGetResponse(ConjoinModel):
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    pool_id: str
    profile_id: str
    senders: Sequence[str]
    title: str


class MessagingEmailSenderTransferResponse(ConjoinModel):
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    dns_records: Sequence[dict[str, Any]] | None = None
    is_default_sender: bool | None = None
    is_test_sender: bool | None = None
    live_mode: bool
    message_quotas: dict[str, Any]
    profile_id: str
    provisioned_at: str | None = None
    queue_details: dict[str, Any] | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    sender_type: str
    status: str
    submitted_at: str
    tracking_details: dict[str, Any] | None = None


class MessagingEmailSenderVerifyResponse(ConjoinModel):
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    dns_records: Sequence[dict[str, Any]] | None = None
    is_default_sender: bool | None = None
    is_test_sender: bool | None = None
    live_mode: bool
    message_quotas: dict[str, Any]
    profile_id: str
    provisioned_at: str | None = None
    queue_details: dict[str, Any] | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    sender_type: str
    status: str
    submitted_at: str
    tracking_details: dict[str, Any] | None = None


class MessagingMultisendCreateResponse(ConjoinModel):
    email: dict[str, Any] | None = None
    sms: dict[str, Any] | None = None


class MessagingMultisendReadResponse(ConjoinModel):
    broadcast_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    message_channels: Sequence[str]
    message_priority: str
    message_requests: dict[str, str]
    message_retry_statuses: Sequence[str]
    originator: str
    originator_primary_id: str
    originator_request_id: str
    profile_id: str
    reference_id: str | None = None
    send_at: str | None = None
    sent_at: str | None = None


class MessagingPhoneNumberListAvailableItem(ConjoinModel):
    capabilities: dict[str, Any]
    country_iso_code: str
    phone_number: str
    price: dict[str, Any]
    recurring_charge: dict[str, Any]
    requires_supporting_documents: bool
    type: str


class MessagingPhoneNumberListItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    country_iso_code: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    expires_at: str | None = None
    features: dict[str, Any] | None = None
    live_mode: bool
    phone_number: str
    phone_number_id: str
    price: dict[str, Any] | None = None
    profile_id: str
    provisioned_at: str | None = None
    recurring_charge: dict[str, Any] | None = None
    reference_id: str | None = None
    region_code: str
    status: str
    title: str
    type: str


class MessagingPhoneNumberPurchaseResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    country_iso_code: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    expires_at: str | None = None
    features: dict[str, Any] | None = None
    live_mode: bool
    phone_number: str
    phone_number_id: str
    price: dict[str, Any] | None = None
    profile_id: str
    provisioned_at: str | None = None
    recurring_charge: dict[str, Any] | None = None
    reference_id: str | None = None
    region_code: str
    status: str
    title: str
    type: str


class MessagingPhoneNumberReleaseResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    country_iso_code: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    expires_at: str | None = None
    features: dict[str, Any] | None = None
    live_mode: bool
    phone_number: str
    phone_number_id: str
    price: dict[str, Any] | None = None
    profile_id: str
    provisioned_at: str | None = None
    recurring_charge: dict[str, Any] | None = None
    reference_id: str | None = None
    region_code: str
    status: str
    title: str
    type: str


class MessagingPhoneNumberUpdateResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    country_iso_code: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    expires_at: str | None = None
    features: dict[str, Any] | None = None
    live_mode: bool
    phone_number: str
    phone_number_id: str
    price: dict[str, Any] | None = None
    profile_id: str
    provisioned_at: str | None = None
    recurring_charge: dict[str, Any] | None = None
    reference_id: str | None = None
    region_code: str
    status: str
    title: str
    type: str


class MessagingProfileCloseResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    email_config: dict[str, Any] | None = None
    features: dict[str, Any]
    is_system_profile: bool
    live_mode: bool
    message_retention_days: float
    multisend_config: dict[str, Any] | None = None
    name: str
    profile_id: str
    properties: dict[str, Any] | None = None
    reference_id: str | None = None
    resource_region: str
    sms_config: dict[str, Any] | None = None
    status: str
    verification_config: dict[str, Any] | None = None


class MessagingProfileCreateResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    email_config: dict[str, Any] | None = None
    features: dict[str, Any]
    is_system_profile: bool
    live_mode: bool
    message_retention_days: float
    multisend_config: dict[str, Any] | None = None
    name: str
    profile_id: str
    properties: dict[str, Any] | None = None
    reference_id: str | None = None
    resource_region: str
    sms_config: dict[str, Any] | None = None
    status: str
    verification_config: dict[str, Any] | None = None


class MessagingProfileDeleteResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    email_config: dict[str, Any] | None = None
    features: dict[str, Any]
    is_system_profile: bool
    live_mode: bool
    message_retention_days: float
    multisend_config: dict[str, Any] | None = None
    name: str
    profile_id: str
    properties: dict[str, Any] | None = None
    reference_id: str | None = None
    resource_region: str
    sms_config: dict[str, Any] | None = None
    status: str
    verification_config: dict[str, Any] | None = None


class MessagingProfileDisableResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    email_config: dict[str, Any] | None = None
    features: dict[str, Any]
    is_system_profile: bool
    live_mode: bool
    message_retention_days: float
    multisend_config: dict[str, Any] | None = None
    name: str
    profile_id: str
    properties: dict[str, Any] | None = None
    reference_id: str | None = None
    resource_region: str
    sms_config: dict[str, Any] | None = None
    status: str
    verification_config: dict[str, Any] | None = None


class MessagingProfileEnableResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    email_config: dict[str, Any] | None = None
    features: dict[str, Any]
    is_system_profile: bool
    live_mode: bool
    message_retention_days: float
    multisend_config: dict[str, Any] | None = None
    name: str
    profile_id: str
    properties: dict[str, Any] | None = None
    reference_id: str | None = None
    resource_region: str
    sms_config: dict[str, Any] | None = None
    status: str
    verification_config: dict[str, Any] | None = None


class MessagingProfileListItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    email_config: dict[str, Any] | None = None
    features: dict[str, Any]
    is_system_profile: bool
    live_mode: bool
    message_retention_days: float
    multisend_config: dict[str, Any] | None = None
    name: str
    profile_id: str
    properties: dict[str, Any] | None = None
    reference_id: str | None = None
    resource_region: str
    sms_config: dict[str, Any] | None = None
    status: str
    verification_config: dict[str, Any] | None = None


class MessagingProfileReadResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    email_config: dict[str, Any] | None = None
    features: dict[str, Any]
    is_system_profile: bool
    live_mode: bool
    message_retention_days: float
    multisend_config: dict[str, Any] | None = None
    name: str
    profile_id: str
    properties: dict[str, Any] | None = None
    reference_id: str | None = None
    resource_region: str
    sms_config: dict[str, Any] | None = None
    status: str
    verification_config: dict[str, Any] | None = None


class MessagingProfileUpdateEmailConfigResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    email_config: dict[str, Any] | None = None
    features: dict[str, Any]
    is_system_profile: bool
    live_mode: bool
    message_retention_days: float
    multisend_config: dict[str, Any] | None = None
    name: str
    profile_id: str
    properties: dict[str, Any] | None = None
    reference_id: str | None = None
    resource_region: str
    sms_config: dict[str, Any] | None = None
    status: str
    verification_config: dict[str, Any] | None = None


class MessagingProfileUpdateMultisendConfigResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    email_config: dict[str, Any] | None = None
    features: dict[str, Any]
    is_system_profile: bool
    live_mode: bool
    message_retention_days: float
    multisend_config: dict[str, Any] | None = None
    name: str
    profile_id: str
    properties: dict[str, Any] | None = None
    reference_id: str | None = None
    resource_region: str
    sms_config: dict[str, Any] | None = None
    status: str
    verification_config: dict[str, Any] | None = None


class MessagingProfileUpdateResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    email_config: dict[str, Any] | None = None
    features: dict[str, Any]
    is_system_profile: bool
    live_mode: bool
    message_retention_days: float
    multisend_config: dict[str, Any] | None = None
    name: str
    profile_id: str
    properties: dict[str, Any] | None = None
    reference_id: str | None = None
    resource_region: str
    sms_config: dict[str, Any] | None = None
    status: str
    verification_config: dict[str, Any] | None = None


class MessagingProfileUpdateVerificationsConfigResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    email_config: dict[str, Any] | None = None
    features: dict[str, Any]
    is_system_profile: bool
    live_mode: bool
    message_retention_days: float
    multisend_config: dict[str, Any] | None = None
    name: str
    profile_id: str
    properties: dict[str, Any] | None = None
    reference_id: str | None = None
    resource_region: str
    sms_config: dict[str, Any] | None = None
    status: str
    verification_config: dict[str, Any] | None = None


class MessagingSMSBrandCreateSmsBrandResponse(ConjoinModel):
    brand_id: str
    brand_registration_type: str
    brand_tcr_id: str | None = None
    business_details: dict[str, Any] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    display_name: str
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    sole_proprietor_details: dict[str, Any] | None = None
    status: str | None = None


class MessagingSMSBrandDeleteSmsBrandResponse(ConjoinModel):
    brand_id: str
    brand_registration_type: str
    brand_tcr_id: str | None = None
    business_details: dict[str, Any] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    display_name: str
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    sole_proprietor_details: dict[str, Any] | None = None
    status: str | None = None


class MessagingSMSBrandListSmsBrandsItem(ConjoinModel):
    brand_id: str
    brand_registration_type: str
    brand_tcr_id: str | None = None
    business_details: dict[str, Any] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    display_name: str
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    sole_proprietor_details: dict[str, Any] | None = None
    status: str | None = None


class MessagingSMSBrandReadSmsBrandResponse(ConjoinModel):
    brand_id: str
    brand_registration_type: str
    brand_tcr_id: str | None = None
    business_details: dict[str, Any] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    display_name: str
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    sole_proprietor_details: dict[str, Any] | None = None
    status: str | None = None


class MessagingSMSBrandUpdateSmsBrandResponse(ConjoinModel):
    brand_id: str
    brand_registration_type: str
    brand_tcr_id: str | None = None
    business_details: dict[str, Any] | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    display_name: str
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    sole_proprietor_details: dict[str, Any] | None = None
    status: str | None = None


class MessagingSMSCampaignCreateSmsCampaignResponse(ConjoinModel):
    brand_id: str
    campaign_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    status: str
    use_case: str | None = None


class MessagingSMSCampaignDeleteSmsCampaignResponse(ConjoinModel):
    brand_id: str
    campaign_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    status: str
    use_case: str | None = None


class MessagingSMSCampaignListSmsCampaignsItem(ConjoinModel):
    brand_id: str
    campaign_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    status: str
    use_case: str | None = None


class MessagingSMSCampaignReadSmsCampaignResponse(ConjoinModel):
    brand_id: str
    campaign_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    status: str
    use_case: str | None = None


class MessagingSMSCampaignUpdateSmsCampaignResponse(ConjoinModel):
    brand_id: str
    campaign_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    status: str
    use_case: str | None = None


class MessagingSMSGenerateSmsSummaryResponse(ConjoinModel):
    currency: str
    destinations: dict[str, dict[str, Any]]
    max_characters: float
    message_body: str
    price_per_part: float
    total_message_parts: float
    total_price: float


class MessagingSMSReadSmsMessagesItem(ConjoinModel):
    body: str
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    default_placeholders: dict[str, Any] | None = None
    live_mode: bool
    message_id: str
    parent_message_id: str | None = None
    profile_id: str
    reference_id: str | None = None
    reply_to: str | None = None
    send_at: str | None = None
    sent_at: str
    status: str
    truncate_message: bool
    type: str


class MessagingSMSSendSmsResponse(ConjoinModel):
    body: str
    conjoin_account_id: str
    conjoin_project_id: str
    conversation_id: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    default_placeholders: dict[str, Any] | None = None
    live_mode: bool
    message_id: str
    parent_message_id: str | None = None
    profile_id: str
    reference_id: str | None = None
    reply_to: str | None = None
    send_at: str | None = None
    sent_at: str
    status: str
    truncate_message: bool
    type: str


class MessagingSMSSenderCreateSmsSenderResponse(ConjoinModel):
    brand_id: str
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    destination_countries: dict[str, Any] | None = None
    is_default_sender: bool | None = None
    is_phone_number: bool
    is_test_sender: bool | None = None
    live_mode: bool
    profile_id: str
    provisioned_at: str | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    status: str
    submitted_at: str


class MessagingSMSSenderDeleteSmsSenderResponse(ConjoinModel):
    brand_id: str
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    destination_countries: dict[str, Any] | None = None
    is_default_sender: bool | None = None
    is_phone_number: bool
    is_test_sender: bool | None = None
    live_mode: bool
    profile_id: str
    provisioned_at: str | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    status: str
    submitted_at: str


class MessagingSMSSenderDisableSmsSenderResponse(ConjoinModel):
    brand_id: str
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    destination_countries: dict[str, Any] | None = None
    is_default_sender: bool | None = None
    is_phone_number: bool
    is_test_sender: bool | None = None
    live_mode: bool
    profile_id: str
    provisioned_at: str | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    status: str
    submitted_at: str


class MessagingSMSSenderEnableSmsSenderResponse(ConjoinModel):
    brand_id: str
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    destination_countries: dict[str, Any] | None = None
    is_default_sender: bool | None = None
    is_phone_number: bool
    is_test_sender: bool | None = None
    live_mode: bool
    profile_id: str
    provisioned_at: str | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    status: str
    submitted_at: str


class MessagingSMSSenderListSmsSenderResponse(ConjoinModel):
    brand_id: str
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    destination_countries: dict[str, Any] | None = None
    is_default_sender: bool | None = None
    is_phone_number: bool
    is_test_sender: bool | None = None
    live_mode: bool
    profile_id: str
    provisioned_at: str | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    status: str
    submitted_at: str


class MessagingSMSSenderPoolAddSmsSendersToPoolResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    pool_id: str
    profile_id: str
    senders: Sequence[str]


class MessagingSMSSenderPoolCreateSmsSenderPoolResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    pool_id: str
    profile_id: str
    senders: Sequence[str]


class MessagingSMSSenderPoolDeleteSmsSenderPoolResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    pool_id: str
    profile_id: str
    senders: Sequence[str]


class MessagingSMSSenderPoolGetSmsSenderPoolResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    live_mode: bool
    pool_id: str
    profile_id: str
    senders: Sequence[str]


class MessagingSMSSenderTransferSmsSenderResponse(ConjoinModel):
    brand_id: str
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    destination_countries: dict[str, Any] | None = None
    is_default_sender: bool | None = None
    is_phone_number: bool
    is_test_sender: bool | None = None
    live_mode: bool
    profile_id: str
    provisioned_at: str | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    status: str
    submitted_at: str


class MessagingSMSSenderUpdateOneSmsSenderResponse(ConjoinModel):
    brand_id: str
    capability: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    destination_countries: dict[str, Any] | None = None
    is_default_sender: bool | None = None
    is_phone_number: bool
    is_test_sender: bool | None = None
    live_mode: bool
    profile_id: str
    provisioned_at: str | None = None
    reference_id: str | None = None
    sender: str
    sender_id: str
    status: str
    submitted_at: str


class MessagingTemplateCreateMessageResponse(ConjoinModel):
    channel: str
    conjoin_account_id: str
    conjoin_project_id: str
    content: str
    content_limit: float | None = None
    content_type: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    is_default: bool
    is_favourite: bool
    is_otp_template: bool | None = None
    language: str
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    tags: Sequence[str] | None = None
    template_group_id: str | None = None
    template_id: str
    title: str


class MessagingTemplateDeleteMessageResponse(ConjoinModel):
    channel: str
    conjoin_account_id: str
    conjoin_project_id: str
    content: str
    content_limit: float | None = None
    content_type: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    is_default: bool
    is_favourite: bool
    is_otp_template: bool | None = None
    language: str
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    tags: Sequence[str] | None = None
    template_group_id: str | None = None
    template_id: str
    title: str


class MessagingTemplateDeleteMessagesResponse(ConjoinModel):
    response: Any | None = None


class MessagingTemplateListMessageItem(ConjoinModel):
    channel: str
    conjoin_account_id: str
    conjoin_project_id: str
    content: str
    content_limit: float | None = None
    content_type: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    is_default: bool
    is_favourite: bool
    is_otp_template: bool | None = None
    language: str
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    tags: Sequence[str] | None = None
    template_group_id: str | None = None
    template_id: str
    title: str


class MessagingTemplateReadMessageResponse(ConjoinModel):
    channel: str
    conjoin_account_id: str
    conjoin_project_id: str
    content: str
    content_limit: float | None = None
    content_type: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    is_default: bool
    is_favourite: bool
    is_otp_template: bool | None = None
    language: str
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    tags: Sequence[str] | None = None
    template_group_id: str | None = None
    template_id: str
    title: str


class MessagingTemplateUpdateMessageResponse(ConjoinModel):
    channel: str
    conjoin_account_id: str
    conjoin_project_id: str
    content: str
    content_limit: float | None = None
    content_type: str
    date_archived: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    is_default: bool
    is_favourite: bool
    is_otp_template: bool | None = None
    language: str
    live_mode: bool
    profile_id: str
    reference_id: str | None = None
    tags: Sequence[str] | None = None
    template_group_id: str | None = None
    template_id: str
    title: str


class MessagingVerificationCheckResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    current_verification_attempts: float
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    expires_at: str
    from_: str = Field(..., alias='from')
    live_mode: bool
    max_verification_attempts: float
    message_channel: str
    message_status: str
    message_subject: str | None = None
    profile_id: str
    recipient: dict[str, Any]
    reference_id: str | None = None
    sent_at: str
    token_type: str
    verification_id: str
    verification_status: str


class MessagingVerificationCreateResponse(ConjoinModel):
    channel: str
    expires_at: str
    message_id: str
    messages: Sequence[dict[str, Any]]
    status: str
    verification_id: str


class MessagingVerificationListMessagesItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    current_verification_attempts: float
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    expires_at: str
    from_: str = Field(..., alias='from')
    live_mode: bool
    max_verification_attempts: float
    message_channel: str
    message_status: str
    message_subject: str | None = None
    profile_id: str
    recipient: dict[str, Any]
    reference_id: str | None = None
    sent_at: str
    token_type: str
    verification_id: str
    verification_status: str


class MessagingVerificationResendResponse(ConjoinModel):
    channel: str
    expires_at: str
    message_id: str
    messages: Sequence[dict[str, Any]]
    status: str
    verification_id: str


class RelayBroadcastCreateChannelResponse(ConjoinModel):
    authorization_callback_url: str | None = None
    authorization_mode: str
    channel_id: str
    channel_type: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    history_size: float | None = None
    live_mode: bool
    max_connections: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    status: str


class RelayBroadcastDeleteChannelResponse(ConjoinModel):
    authorization_callback_url: str | None = None
    authorization_mode: str
    channel_id: str
    channel_type: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    history_size: float | None = None
    live_mode: bool
    max_connections: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    status: str


class RelayBroadcastGenerateAuthTokenResponse(ConjoinModel):
    expires_at: str
    token: str


class RelayBroadcastGenerateConnectionTokenResponse(ConjoinModel):
    expires_at: str
    token: str


class RelayBroadcastPublishToResponse(ConjoinModel):
    event_id: str
    published: bool


class RelayBroadcastReadChannelsCountResponse(ConjoinModel):
    count: int


class RelayBroadcastReadChannelsItem(ConjoinModel):
    authorization_callback_url: str | None = None
    authorization_mode: str
    channel_id: str
    channel_type: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    history_size: float | None = None
    live_mode: bool
    max_connections: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    status: str


class RelayBroadcastReadPresenceResponse(ConjoinModel):
    members: Sequence[str]


class RelayBroadcastUpdateChannelResponse(ConjoinModel):
    authorization_callback_url: str | None = None
    authorization_mode: str
    channel_id: str
    channel_type: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    history_size: float | None = None
    live_mode: bool
    max_connections: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    status: str


class RelayEventsCreateEventChannelResponse(ConjoinModel):
    channel_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    retention_hours: float | None = None
    status: str


class RelayEventsCreateEventSubscriptionResponse(ConjoinModel):
    channel_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    description: str | None = None
    endpoint_url: str
    filter_rules: dict[str, Any] | None = None
    headers: dict[str, str] | None = None
    live_mode: bool
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    paused_reason: str | None = None
    reference_id: str | None = None
    retry_policy: dict[str, Any] | None = None
    status: str
    subscription_id: str


class RelayEventsDeleteEventChannelResponse(ConjoinModel):
    channel_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    retention_hours: float | None = None
    status: str


class RelayEventsDeleteEventSubscriptionResponse(ConjoinModel):
    response: Any | None = None


class RelayEventsPauseEventSubscriptionResponse(ConjoinModel):
    channel_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    description: str | None = None
    endpoint_url: str
    filter_rules: dict[str, Any] | None = None
    headers: dict[str, str] | None = None
    live_mode: bool
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    paused_reason: str | None = None
    reference_id: str | None = None
    retry_policy: dict[str, Any] | None = None
    status: str
    subscription_id: str


class RelayEventsPublishEventResponse(ConjoinModel):
    channel_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    event_id: str
    event_type: str
    live_mode: bool
    payload: dict[str, Any] | None = None
    reference_id: str | None = None
    status: str


class RelayEventsReadCountResponse(ConjoinModel):
    count: int


class RelayEventsReadEventChannelsCountResponse(ConjoinModel):
    count: int


class RelayEventsReadEventChannelsItem(ConjoinModel):
    channel_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    retention_hours: float | None = None
    status: str


class RelayEventsReadEventSubscriptionsCountResponse(ConjoinModel):
    count: int


class RelayEventsReadEventSubscriptionsItem(ConjoinModel):
    channel_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    description: str | None = None
    endpoint_url: str
    filter_rules: dict[str, Any] | None = None
    headers: dict[str, str] | None = None
    live_mode: bool
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    paused_reason: str | None = None
    reference_id: str | None = None
    retry_policy: dict[str, Any] | None = None
    status: str
    subscription_id: str


class RelayEventsReadItem(ConjoinModel):
    channel_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    event_id: str
    event_type: str
    live_mode: bool
    payload: dict[str, Any] | None = None
    reference_id: str | None = None
    status: str


class RelayEventsReplayResponse(ConjoinModel):
    response: Any | None = None


class RelayEventsResumeEventSubscriptionResponse(ConjoinModel):
    channel_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    description: str | None = None
    endpoint_url: str
    filter_rules: dict[str, Any] | None = None
    headers: dict[str, str] | None = None
    live_mode: bool
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    paused_reason: str | None = None
    reference_id: str | None = None
    retry_policy: dict[str, Any] | None = None
    status: str
    subscription_id: str


class RelayEventsUpdateEventChannelResponse(ConjoinModel):
    channel_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    retention_hours: float | None = None
    status: str


class RelayEventsUpdateEventSubscriptionResponse(ConjoinModel):
    channel_id: str
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    description: str | None = None
    endpoint_url: str
    filter_rules: dict[str, Any] | None = None
    headers: dict[str, str] | None = None
    live_mode: bool
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    paused_reason: str | None = None
    reference_id: str | None = None
    retry_policy: dict[str, Any] | None = None
    status: str
    subscription_id: str


class RelayMemorystoreCreateClusterResponse(ConjoinModel):
    cluster_id: str
    cluster_type: str
    conjoin_account_id: str
    conjoin_project_id: str
    connection_uri: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    encryption_at_rest: bool | None = None
    gcp_instance_id: str | None = None
    gcp_instance_name: str | None = None
    live_mode: bool
    max_memory_mb: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    namespace_prefix: str | None = None
    reference_id: str | None = None
    region: str | None = None
    status: str
    tcp_access_enabled: bool | None = None


class RelayMemorystoreDeleteClusterResponse(ConjoinModel):
    cluster_id: str
    cluster_type: str
    conjoin_account_id: str
    conjoin_project_id: str
    connection_uri: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    encryption_at_rest: bool | None = None
    gcp_instance_id: str | None = None
    gcp_instance_name: str | None = None
    live_mode: bool
    max_memory_mb: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    namespace_prefix: str | None = None
    reference_id: str | None = None
    region: str | None = None
    status: str
    tcp_access_enabled: bool | None = None


class RelayMemorystoreExecuteCommandResponse(ConjoinModel):
    result: Any


class RelayMemorystoreReadClusterResponse(ConjoinModel):
    cluster_id: str
    cluster_type: str
    conjoin_account_id: str
    conjoin_project_id: str
    connection_uri: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    encryption_at_rest: bool | None = None
    gcp_instance_id: str | None = None
    gcp_instance_name: str | None = None
    live_mode: bool
    max_memory_mb: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    namespace_prefix: str | None = None
    reference_id: str | None = None
    region: str | None = None
    status: str
    tcp_access_enabled: bool | None = None


class RelayMemorystoreReadClustersCountResponse(ConjoinModel):
    count: int


class RelayMemorystoreReadClustersItem(ConjoinModel):
    cluster_id: str
    cluster_type: str
    conjoin_account_id: str
    conjoin_project_id: str
    connection_uri: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    encryption_at_rest: bool | None = None
    gcp_instance_id: str | None = None
    gcp_instance_name: str | None = None
    live_mode: bool
    max_memory_mb: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    namespace_prefix: str | None = None
    reference_id: str | None = None
    region: str | None = None
    status: str
    tcp_access_enabled: bool | None = None


class RelayMemorystoreSuspendClusterResponse(ConjoinModel):
    cluster_id: str
    cluster_type: str
    conjoin_account_id: str
    conjoin_project_id: str
    connection_uri: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    encryption_at_rest: bool | None = None
    gcp_instance_id: str | None = None
    gcp_instance_name: str | None = None
    live_mode: bool
    max_memory_mb: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    namespace_prefix: str | None = None
    reference_id: str | None = None
    region: str | None = None
    status: str
    tcp_access_enabled: bool | None = None


class RelayMemorystoreUpdateClusterResponse(ConjoinModel):
    cluster_id: str
    cluster_type: str
    conjoin_account_id: str
    conjoin_project_id: str
    connection_uri: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    encryption_at_rest: bool | None = None
    gcp_instance_id: str | None = None
    gcp_instance_name: str | None = None
    live_mode: bool
    max_memory_mb: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    namespace_prefix: str | None = None
    reference_id: str | None = None
    region: str | None = None
    status: str
    tcp_access_enabled: bool | None = None


class RelayPipelinesApprovePipelineGateResponse(ConjoinModel):
    attempt_count: float
    completed_at: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    error: str | None = None
    gate_metadata: dict[str, Any] | None = None
    input: Any | None = None
    live_mode: bool
    output: Any | None = None
    pipeline_id: str
    run_id: str
    started_at: str | None = None
    status: str
    step_id: str
    step_index: float
    step_name: str
    step_type: str


class RelayPipelinesCancelPipelineRunResponse(ConjoinModel):
    completed_at: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    date_created: str
    date_updated: str
    error: dict[str, Any] | None = None
    live_mode: bool
    payload: dict[str, Any] | None = None
    pipeline_id: str
    reference_id: str | None = None
    run_id: str
    started_at: str | None = None
    status: str
    steps: Sequence[dict[str, Any]] | None = None
    trace_source: str | None = None


class RelayPipelinesCreatePipelineDefinitionResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    endpoint_url: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    pipeline_id: str
    reference_id: str | None = None
    retry_policy: dict[str, Any] | None = None
    status: str
    timeout_seconds: float | None = None


class RelayPipelinesDeletePipelineDefinitionResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    endpoint_url: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    pipeline_id: str
    reference_id: str | None = None
    retry_policy: dict[str, Any] | None = None
    status: str
    timeout_seconds: float | None = None


class RelayPipelinesReadPipelineDefinitionsCountResponse(ConjoinModel):
    count: int


class RelayPipelinesReadPipelineDefinitionsItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    endpoint_url: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    pipeline_id: str
    reference_id: str | None = None
    retry_policy: dict[str, Any] | None = None
    status: str
    timeout_seconds: float | None = None


class RelayPipelinesReadPipelineRunResponse(ConjoinModel):
    completed_at: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    date_created: str
    date_updated: str
    error: dict[str, Any] | None = None
    live_mode: bool
    payload: dict[str, Any] | None = None
    pipeline_id: str
    reference_id: str | None = None
    run_id: str
    started_at: str | None = None
    status: str
    steps: Sequence[dict[str, Any]] | None = None
    trace_source: str | None = None


class RelayPipelinesReadPipelineRunsCountResponse(ConjoinModel):
    count: int


class RelayPipelinesReadPipelineRunsItem(ConjoinModel):
    completed_at: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    date_created: str
    date_updated: str
    error: dict[str, Any] | None = None
    live_mode: bool
    payload: dict[str, Any] | None = None
    pipeline_id: str
    reference_id: str | None = None
    run_id: str
    started_at: str | None = None
    status: str
    steps: Sequence[dict[str, Any]] | None = None
    trace_source: str | None = None


class RelayPipelinesRejectPipelineGateResponse(ConjoinModel):
    attempt_count: float
    completed_at: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str
    error: str | None = None
    gate_metadata: dict[str, Any] | None = None
    input: Any | None = None
    live_mode: bool
    output: Any | None = None
    pipeline_id: str
    run_id: str
    started_at: str | None = None
    status: str
    step_id: str
    step_index: float
    step_name: str
    step_type: str


class RelayPipelinesTriggerPipelineRunResponse(ConjoinModel):
    completed_at: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    date_created: str
    date_updated: str
    error: dict[str, Any] | None = None
    live_mode: bool
    payload: dict[str, Any] | None = None
    pipeline_id: str
    reference_id: str | None = None
    run_id: str
    started_at: str | None = None
    status: str
    steps: Sequence[dict[str, Any]] | None = None
    trace_source: str | None = None


class RelayPipelinesUpdatePipelineDefinitionResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    endpoint_url: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    pipeline_id: str
    reference_id: str | None = None
    retry_policy: dict[str, Any] | None = None
    status: str
    timeout_seconds: float | None = None


class RelayQueuesBatchEnqueueTasksResponse(ConjoinModel):
    tasks: Sequence[dict[str, Any]]
    tasks_created: float


class RelayQueuesCreateQueueDefinitionResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    default_delay_seconds: float | None = None
    description: str | None = None
    dlq_enabled: bool | None = None
    dlq_retention_days: float | None = None
    headers: dict[str, str] | None = None
    live_mode: bool
    max_concurrent_deliveries: float | None = None
    max_retries: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    priority: float | None = None
    queue_id: str
    rate_limit_per_minute: float | None = None
    reference_id: str | None = None
    response_forward_fields: Sequence[str] | None = None
    retry_backoff_base_seconds: float | None = None
    retry_backoff_strategy: str | None = None
    status: str
    status_batch_interval_seconds: float | None = None
    status_batch_max_size: float | None = None
    status_broadcast_channel_id: str | None = None
    status_broadcast_enabled: bool | None = None
    status_event_channel_id: str | None = None
    status_events_enabled: bool | None = None
    target_url: str
    task_retention_days: float | None = None
    timeout_seconds: float | None = None
    visibility_timeout_seconds: float | None = None


class RelayQueuesDeleteQueueDefinitionResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    default_delay_seconds: float | None = None
    description: str | None = None
    dlq_enabled: bool | None = None
    dlq_retention_days: float | None = None
    headers: dict[str, str] | None = None
    live_mode: bool
    max_concurrent_deliveries: float | None = None
    max_retries: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    priority: float | None = None
    queue_id: str
    rate_limit_per_minute: float | None = None
    reference_id: str | None = None
    response_forward_fields: Sequence[str] | None = None
    retry_backoff_base_seconds: float | None = None
    retry_backoff_strategy: str | None = None
    status: str
    status_batch_interval_seconds: float | None = None
    status_batch_max_size: float | None = None
    status_broadcast_channel_id: str | None = None
    status_broadcast_enabled: bool | None = None
    status_event_channel_id: str | None = None
    status_events_enabled: bool | None = None
    target_url: str
    task_retention_days: float | None = None
    timeout_seconds: float | None = None
    visibility_timeout_seconds: float | None = None


class RelayQueuesEnqueueTaskResponse(ConjoinModel):
    attempt_count: float | None = None
    completed_at: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    date_created: str
    date_updated: str
    live_mode: bool
    payload: dict[str, Any] | None = None
    queue_id: str
    reference_id: str | None = None
    response_body: str | None = None
    response_status_code: float | None = None
    scheduled_at: str | None = None
    status: str
    target_url: str | None = None
    task_id: str
    trace_source: str | None = None


class RelayQueuesPauseQueueResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    default_delay_seconds: float | None = None
    description: str | None = None
    dlq_enabled: bool | None = None
    dlq_retention_days: float | None = None
    headers: dict[str, str] | None = None
    live_mode: bool
    max_concurrent_deliveries: float | None = None
    max_retries: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    priority: float | None = None
    queue_id: str
    rate_limit_per_minute: float | None = None
    reference_id: str | None = None
    response_forward_fields: Sequence[str] | None = None
    retry_backoff_base_seconds: float | None = None
    retry_backoff_strategy: str | None = None
    status: str
    status_batch_interval_seconds: float | None = None
    status_batch_max_size: float | None = None
    status_broadcast_channel_id: str | None = None
    status_broadcast_enabled: bool | None = None
    status_event_channel_id: str | None = None
    status_events_enabled: bool | None = None
    target_url: str
    task_retention_days: float | None = None
    timeout_seconds: float | None = None
    visibility_timeout_seconds: float | None = None


class RelayQueuesPurgeQueueTasksResponse(ConjoinModel):
    dead_letters_deleted: float
    tasks_deleted: float


class RelayQueuesReadDeadLetterTasksCountResponse(ConjoinModel):
    count: int


class RelayQueuesReadDeadLetterTasksItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    date_created: str
    dlq_entry_id: str
    error: dict[str, Any] | None = None
    live_mode: bool
    original_attempt_count: float | None = None
    payload: dict[str, Any] | None = None
    queue_id: str
    reference_id: str | None = None
    response_body: str | None = None
    response_status_code: float | None = None
    task_id: str
    trace_source: str | None = None


class RelayQueuesReadQueueDefinitionsCountResponse(ConjoinModel):
    count: int


class RelayQueuesReadQueueDefinitionsItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    default_delay_seconds: float | None = None
    description: str | None = None
    dlq_enabled: bool | None = None
    dlq_retention_days: float | None = None
    headers: dict[str, str] | None = None
    live_mode: bool
    max_concurrent_deliveries: float | None = None
    max_retries: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    priority: float | None = None
    queue_id: str
    rate_limit_per_minute: float | None = None
    reference_id: str | None = None
    response_forward_fields: Sequence[str] | None = None
    retry_backoff_base_seconds: float | None = None
    retry_backoff_strategy: str | None = None
    status: str
    status_batch_interval_seconds: float | None = None
    status_batch_max_size: float | None = None
    status_broadcast_channel_id: str | None = None
    status_broadcast_enabled: bool | None = None
    status_event_channel_id: str | None = None
    status_events_enabled: bool | None = None
    target_url: str
    task_retention_days: float | None = None
    timeout_seconds: float | None = None
    visibility_timeout_seconds: float | None = None


class RelayQueuesReadQueueTasksCountResponse(ConjoinModel):
    count: int


class RelayQueuesReadQueueTasksItem(ConjoinModel):
    attempt_count: float | None = None
    completed_at: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    date_created: str
    date_updated: str
    live_mode: bool
    payload: dict[str, Any] | None = None
    queue_id: str
    reference_id: str | None = None
    response_body: str | None = None
    response_status_code: float | None = None
    scheduled_at: str | None = None
    status: str
    target_url: str | None = None
    task_id: str
    trace_source: str | None = None


class RelayQueuesReplayDeadLetterTaskResponse(ConjoinModel):
    attempt_count: float | None = None
    completed_at: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    date_created: str
    date_updated: str
    live_mode: bool
    payload: dict[str, Any] | None = None
    queue_id: str
    reference_id: str | None = None
    response_body: str | None = None
    response_status_code: float | None = None
    scheduled_at: str | None = None
    status: str
    target_url: str | None = None
    task_id: str
    trace_source: str | None = None


class RelayQueuesResumeQueueResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    default_delay_seconds: float | None = None
    description: str | None = None
    dlq_enabled: bool | None = None
    dlq_retention_days: float | None = None
    headers: dict[str, str] | None = None
    live_mode: bool
    max_concurrent_deliveries: float | None = None
    max_retries: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    priority: float | None = None
    queue_id: str
    rate_limit_per_minute: float | None = None
    reference_id: str | None = None
    response_forward_fields: Sequence[str] | None = None
    retry_backoff_base_seconds: float | None = None
    retry_backoff_strategy: str | None = None
    status: str
    status_batch_interval_seconds: float | None = None
    status_batch_max_size: float | None = None
    status_broadcast_channel_id: str | None = None
    status_broadcast_enabled: bool | None = None
    status_event_channel_id: str | None = None
    status_events_enabled: bool | None = None
    target_url: str
    task_retention_days: float | None = None
    timeout_seconds: float | None = None
    visibility_timeout_seconds: float | None = None


class RelayQueuesUpdateQueueDefinitionResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    default_delay_seconds: float | None = None
    description: str | None = None
    dlq_enabled: bool | None = None
    dlq_retention_days: float | None = None
    headers: dict[str, str] | None = None
    live_mode: bool
    max_concurrent_deliveries: float | None = None
    max_retries: float | None = None
    metadata: dict[str, Any] | None = None
    name: str
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    priority: float | None = None
    queue_id: str
    rate_limit_per_minute: float | None = None
    reference_id: str | None = None
    response_forward_fields: Sequence[str] | None = None
    retry_backoff_base_seconds: float | None = None
    retry_backoff_strategy: str | None = None
    status: str
    status_batch_interval_seconds: float | None = None
    status_batch_max_size: float | None = None
    status_broadcast_channel_id: str | None = None
    status_broadcast_enabled: bool | None = None
    status_event_channel_id: str | None = None
    status_events_enabled: bool | None = None
    target_url: str
    task_retention_days: float | None = None
    timeout_seconds: float | None = None
    visibility_timeout_seconds: float | None = None


class RelaySchedulerCancelResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    cron_expression: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    dlq_enabled: bool
    dlq_retention_days: float | None = None
    grace_window_seconds: float
    headers: dict[str, str] | None = None
    last_run_at: str | None = None
    live_mode: bool
    max_retries: float
    metadata: dict[str, Any] | None = None
    name: str
    next_run_at: str | None = None
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    one_time_at: str | None = None
    payload: dict[str, Any] | None = None
    reference_id: str | None = None
    retry_backoff_base_seconds: float
    retry_backoff_strategy: str
    schedule_id: str
    schedule_type: str
    status: str
    target_url: str
    timeout_seconds: float
    timezone: str | None = None


class RelaySchedulerCreateDefinitionResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    cron_expression: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    dlq_enabled: bool
    dlq_retention_days: float | None = None
    grace_window_seconds: float
    headers: dict[str, str] | None = None
    last_run_at: str | None = None
    live_mode: bool
    max_retries: float
    metadata: dict[str, Any] | None = None
    name: str
    next_run_at: str | None = None
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    one_time_at: str | None = None
    payload: dict[str, Any] | None = None
    reference_id: str | None = None
    retry_backoff_base_seconds: float
    retry_backoff_strategy: str
    schedule_id: str
    schedule_type: str
    status: str
    target_url: str
    timeout_seconds: float
    timezone: str | None = None


class RelaySchedulerPauseResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    cron_expression: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    dlq_enabled: bool
    dlq_retention_days: float | None = None
    grace_window_seconds: float
    headers: dict[str, str] | None = None
    last_run_at: str | None = None
    live_mode: bool
    max_retries: float
    metadata: dict[str, Any] | None = None
    name: str
    next_run_at: str | None = None
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    one_time_at: str | None = None
    payload: dict[str, Any] | None = None
    reference_id: str | None = None
    retry_backoff_base_seconds: float
    retry_backoff_strategy: str
    schedule_id: str
    schedule_type: str
    status: str
    target_url: str
    timeout_seconds: float
    timezone: str | None = None


class RelaySchedulerReadDeadLetterEntriesCountResponse(ConjoinModel):
    count: int


class RelaySchedulerReadDeadLetterEntriesItem(ConjoinModel):
    attempts: float
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    date_created: str
    dlq_entry_id: str
    execution_id: str
    failed_at: str
    failure_reason: str
    live_mode: bool
    payload: dict[str, Any]
    reference_id: str | None = None
    replayed: bool
    replayed_at: str | None = None
    schedule_id: str
    target_url: str
    trace_source: str | None = None


class RelaySchedulerReadDefinitionsCountResponse(ConjoinModel):
    count: int


class RelaySchedulerReadDefinitionsItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    cron_expression: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    dlq_enabled: bool
    dlq_retention_days: float | None = None
    grace_window_seconds: float
    headers: dict[str, str] | None = None
    last_run_at: str | None = None
    live_mode: bool
    max_retries: float
    metadata: dict[str, Any] | None = None
    name: str
    next_run_at: str | None = None
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    one_time_at: str | None = None
    payload: dict[str, Any] | None = None
    reference_id: str | None = None
    retry_backoff_base_seconds: float
    retry_backoff_strategy: str
    schedule_id: str
    schedule_type: str
    status: str
    target_url: str
    timeout_seconds: float
    timezone: str | None = None


class RelaySchedulerReadExecutionsCountResponse(ConjoinModel):
    count: int


class RelaySchedulerReadExecutionsItem(ConjoinModel):
    attempt_history: Sequence[dict[str, Any]] | None = None
    attempts: float
    completed_at: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    date_created: str
    duration_ms: float | None = None
    error: dict[str, Any] | None = None
    executed_at: str
    execution_id: str
    last_attempt_at: str | None = None
    live_mode: bool
    max_attempts: float
    next_attempt_at: str | None = None
    reference_id: str | None = None
    response_body: str | None = None
    response_code: float | None = None
    schedule_id: str
    scheduled_for: str
    status: str
    trace_source: str | None = None


class RelaySchedulerReplayDeadLetterEntryResponse(ConjoinModel):
    attempts: float
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    date_created: str
    dlq_entry_id: str
    execution_id: str
    failed_at: str
    failure_reason: str
    live_mode: bool
    payload: dict[str, Any]
    reference_id: str | None = None
    replayed: bool
    replayed_at: str | None = None
    schedule_id: str
    target_url: str
    trace_source: str | None = None


class RelaySchedulerResumeResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    cron_expression: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    dlq_enabled: bool
    dlq_retention_days: float | None = None
    grace_window_seconds: float
    headers: dict[str, str] | None = None
    last_run_at: str | None = None
    live_mode: bool
    max_retries: float
    metadata: dict[str, Any] | None = None
    name: str
    next_run_at: str | None = None
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    one_time_at: str | None = None
    payload: dict[str, Any] | None = None
    reference_id: str | None = None
    retry_backoff_base_seconds: float
    retry_backoff_strategy: str
    schedule_id: str
    schedule_type: str
    status: str
    target_url: str
    timeout_seconds: float
    timezone: str | None = None


class RelaySchedulerTriggerExecutionResponse(ConjoinModel):
    attempt_history: Sequence[dict[str, Any]] | None = None
    attempts: float
    completed_at: str | None = None
    conjoin_account_id: str
    conjoin_project_id: str
    conjoin_request_id: str
    date_created: str
    duration_ms: float | None = None
    error: dict[str, Any] | None = None
    executed_at: str
    execution_id: str
    last_attempt_at: str | None = None
    live_mode: bool
    max_attempts: float
    next_attempt_at: str | None = None
    reference_id: str | None = None
    response_body: str | None = None
    response_code: float | None = None
    schedule_id: str
    scheduled_for: str
    status: str
    trace_source: str | None = None


class RelaySchedulerUpdateDefinitionResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    cron_expression: str | None = None
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    dlq_enabled: bool
    dlq_retention_days: float | None = None
    grace_window_seconds: float
    headers: dict[str, str] | None = None
    last_run_at: str | None = None
    live_mode: bool
    max_retries: float
    metadata: dict[str, Any] | None = None
    name: str
    next_run_at: str | None = None
    on_failure: Sequence[dict[str, Any]] | None = None
    on_success: Sequence[dict[str, Any]] | None = None
    one_time_at: str | None = None
    payload: dict[str, Any] | None = None
    reference_id: str | None = None
    retry_backoff_base_seconds: float
    retry_backoff_strategy: str
    schedule_id: str
    schedule_type: str
    status: str
    target_url: str
    timeout_seconds: float
    timezone: str | None = None


class RelaySearchAutoSuggestResponse(ConjoinModel):
    suggestions: Sequence[str]


class RelaySearchCreateIndexResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    document_count: float | None = None
    index_id: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    schema_definition: dict[str, Any]
    settings: dict[str, Any] | None = None
    status: str


class RelaySearchDeleteIndexResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    document_count: float | None = None
    index_id: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    schema_definition: dict[str, Any]
    settings: dict[str, Any] | None = None
    status: str


class RelaySearchIndexDocumentBatchResponse(ConjoinModel):
    indexed_count: float


class RelaySearchIndexDocumentResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    content: dict[str, Any]
    date_created: str
    date_updated: str
    document_id: str
    index_id: str
    live_mode: bool
    reference_id: str | None = None
    search_metadata: dict[str, Any] | None = None


class RelaySearchReadIndexesItem(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_deleted: str | None = None
    date_updated: str
    description: str | None = None
    document_count: float | None = None
    index_id: str
    live_mode: bool
    metadata: dict[str, Any] | None = None
    name: str
    reference_id: str | None = None
    schema_definition: dict[str, Any]
    settings: dict[str, Any] | None = None
    status: str


class RelaySearchRemoveDocumentResponse(ConjoinModel):
    removed: bool


class RelaySearchSearchQueryResponse(ConjoinModel):
    hits: Sequence[dict[str, Any]]
    total: float


class RelaySettingsGetResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str | None = None
    events: dict[str, Any] | None = None
    live_mode: bool
    pipelines: dict[str, Any] | None = None
    queues: dict[str, Any] | None = None
    scheduler: dict[str, Any] | None = None
    settings_id: str
    signing_secret_masked: str
    signing_secret_rotated_at: str | None = None


class RelaySettingsRevealSigningSecretResponse(ConjoinModel):
    signing_secret: str


class RelaySettingsRotateSigningSecretResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str | None = None
    events: dict[str, Any] | None = None
    live_mode: bool
    pipelines: dict[str, Any] | None = None
    queues: dict[str, Any] | None = None
    scheduler: dict[str, Any] | None = None
    settings_id: str
    signing_secret_masked: str
    signing_secret_rotated_at: str | None = None


class RelaySettingsUpdateResponse(ConjoinModel):
    conjoin_account_id: str
    conjoin_project_id: str
    date_created: str
    date_updated: str | None = None
    events: dict[str, Any] | None = None
    live_mode: bool
    pipelines: dict[str, Any] | None = None
    queues: dict[str, Any] | None = None
    scheduler: dict[str, Any] | None = None
    settings_id: str
    signing_secret_masked: str
    signing_secret_rotated_at: str | None = None


class StorageContainerArchiveResponse(ConjoinModel):
    archived_date: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    date_created: str
    date_updated: str | None
    deletion_grace_period_days: float
    deletion_scheduled_at: str | None
    deletion_status: str
    is_public: bool
    lifecycle_policy: dict[str, Any]
    live_mode: bool
    metadata: dict[str, Any] | None = None
    migration_status: str
    name: str
    reference_id: str
    region: str
    settings: dict[str, Any]
    storage_class: str
    storage_class_transition_policy: dict[str, Any]
    versioning_enabled: bool
    versioning_policy: dict[str, Any]


class StorageContainerCancelDeletionResponse(ConjoinModel):
    archived_date: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    date_created: str
    date_updated: str | None
    deletion_grace_period_days: float
    deletion_scheduled_at: str | None
    deletion_status: str
    is_public: bool
    lifecycle_policy: dict[str, Any]
    live_mode: bool
    metadata: dict[str, Any] | None = None
    migration_status: str
    name: str
    reference_id: str
    region: str
    settings: dict[str, Any]
    storage_class: str
    storage_class_transition_policy: dict[str, Any]
    versioning_enabled: bool
    versioning_policy: dict[str, Any]


class StorageContainerChangeClassResponse(ConjoinModel):
    archived_date: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    date_created: str
    date_updated: str | None
    deletion_grace_period_days: float
    deletion_scheduled_at: str | None
    deletion_status: str
    is_public: bool
    lifecycle_policy: dict[str, Any]
    live_mode: bool
    metadata: dict[str, Any] | None = None
    migration_status: str
    name: str
    reference_id: str
    region: str
    settings: dict[str, Any]
    storage_class: str
    storage_class_transition_policy: dict[str, Any]
    versioning_enabled: bool
    versioning_policy: dict[str, Any]


class StorageContainerCreateResponse(ConjoinModel):
    archived_date: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    date_created: str
    date_updated: str | None
    deletion_grace_period_days: float
    deletion_scheduled_at: str | None
    deletion_status: str
    is_public: bool
    lifecycle_policy: dict[str, Any]
    live_mode: bool
    metadata: dict[str, Any] | None = None
    migration_status: str
    name: str
    reference_id: str
    region: str
    settings: dict[str, Any]
    storage_class: str
    storage_class_transition_policy: dict[str, Any]
    versioning_enabled: bool
    versioning_policy: dict[str, Any]


class StorageContainerListItem(ConjoinModel):
    archived_date: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    date_created: str
    date_updated: str | None
    deletion_grace_period_days: float
    deletion_scheduled_at: str | None
    deletion_status: str
    is_public: bool
    lifecycle_policy: dict[str, Any]
    live_mode: bool
    metadata: dict[str, Any] | None = None
    migration_status: str
    name: str
    reference_id: str
    region: str
    settings: dict[str, Any]
    storage_class: str
    storage_class_transition_policy: dict[str, Any]
    versioning_enabled: bool
    versioning_policy: dict[str, Any]


class StorageContainerReadResponse(ConjoinModel):
    archived_date: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    date_created: str
    date_updated: str | None
    deletion_grace_period_days: float
    deletion_scheduled_at: str | None
    deletion_status: str
    is_public: bool
    lifecycle_policy: dict[str, Any]
    live_mode: bool
    metadata: dict[str, Any] | None = None
    migration_status: str
    name: str
    reference_id: str
    region: str
    settings: dict[str, Any]
    storage_class: str
    storage_class_transition_policy: dict[str, Any]
    versioning_enabled: bool
    versioning_policy: dict[str, Any]


class StorageContainerRequestDeletionResponse(ConjoinModel):
    archived_date: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    date_created: str
    date_updated: str | None
    deletion_grace_period_days: float
    deletion_scheduled_at: str | None
    deletion_status: str
    is_public: bool
    lifecycle_policy: dict[str, Any]
    live_mode: bool
    metadata: dict[str, Any] | None = None
    migration_status: str
    name: str
    reference_id: str
    region: str
    settings: dict[str, Any]
    storage_class: str
    storage_class_transition_policy: dict[str, Any]
    versioning_enabled: bool
    versioning_policy: dict[str, Any]


class StorageContainerRestoreResponse(ConjoinModel):
    archived_date: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    date_created: str
    date_updated: str | None
    deletion_grace_period_days: float
    deletion_scheduled_at: str | None
    deletion_status: str
    is_public: bool
    lifecycle_policy: dict[str, Any]
    live_mode: bool
    metadata: dict[str, Any] | None = None
    migration_status: str
    name: str
    reference_id: str
    region: str
    settings: dict[str, Any]
    storage_class: str
    storage_class_transition_policy: dict[str, Any]
    versioning_enabled: bool
    versioning_policy: dict[str, Any]


class StorageContainerUpdateLifecyclePolicyResponse(ConjoinModel):
    archived_date: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    date_created: str
    date_updated: str | None
    deletion_grace_period_days: float
    deletion_scheduled_at: str | None
    deletion_status: str
    is_public: bool
    lifecycle_policy: dict[str, Any]
    live_mode: bool
    metadata: dict[str, Any] | None = None
    migration_status: str
    name: str
    reference_id: str
    region: str
    settings: dict[str, Any]
    storage_class: str
    storage_class_transition_policy: dict[str, Any]
    versioning_enabled: bool
    versioning_policy: dict[str, Any]


class StorageContainerUpdateSettingsResponse(ConjoinModel):
    archived_date: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    date_created: str
    date_updated: str | None
    deletion_grace_period_days: float
    deletion_scheduled_at: str | None
    deletion_status: str
    is_public: bool
    lifecycle_policy: dict[str, Any]
    live_mode: bool
    metadata: dict[str, Any] | None = None
    migration_status: str
    name: str
    reference_id: str
    region: str
    settings: dict[str, Any]
    storage_class: str
    storage_class_transition_policy: dict[str, Any]
    versioning_enabled: bool
    versioning_policy: dict[str, Any]


class StorageContainerUpdateTransitionPolicyResponse(ConjoinModel):
    archived_date: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    date_created: str
    date_updated: str | None
    deletion_grace_period_days: float
    deletion_scheduled_at: str | None
    deletion_status: str
    is_public: bool
    lifecycle_policy: dict[str, Any]
    live_mode: bool
    metadata: dict[str, Any] | None = None
    migration_status: str
    name: str
    reference_id: str
    region: str
    settings: dict[str, Any]
    storage_class: str
    storage_class_transition_policy: dict[str, Any]
    versioning_enabled: bool
    versioning_policy: dict[str, Any]


class StorageObjectACLGrantObjectAclResponse(ConjoinModel):
    entity_id: str
    entity_type: str
    role: str


class StorageObjectACLRevokeObjectAclResponse(ConjoinModel):
    entity_id: str
    entity_type: str
    role: str


class StorageObjectACLSetObjectPublicResponse(ConjoinModel):
    entity_id: str
    entity_type: str
    role: str


class StorageObjectArchiveResponse(ConjoinModel):
    archived_date: str | None
    checksum: str | None
    conjoin_account_id: str
    conjoin_auth_acl: Sequence[dict[str, Any]]
    conjoin_project_id: str
    container_id: str
    content_type: str | None
    date_created: str
    date_updated: str | None
    description: str | None
    duplicate_of: str | None
    generation_number: float
    is_public: bool
    labels: Sequence[str]
    lifecycle_expires_at: str | None
    live_mode: bool
    md5_hash: str | None
    metadata: dict[str, Any] | None = None
    name: str
    object_id: str
    object_metadata: dict[str, Any] | None = None
    reference_id: str | None
    size: float
    sync_status: str
    version_id: str | None


class StorageObjectCheckDuplicateResponse(ConjoinModel):
    archived_date: str | None
    checksum: str | None
    conjoin_account_id: str
    conjoin_auth_acl: Sequence[dict[str, Any]]
    conjoin_project_id: str
    container_id: str
    content_type: str | None
    date_created: str
    date_updated: str | None
    description: str | None
    duplicate_of: str | None
    generation_number: float
    is_public: bool
    labels: Sequence[str]
    lifecycle_expires_at: str | None
    live_mode: bool
    md5_hash: str | None
    metadata: dict[str, Any] | None = None
    name: str
    object_id: str
    object_metadata: dict[str, Any] | None = None
    reference_id: str | None
    size: float
    sync_status: str
    version_id: str | None


class StorageObjectCreateDownloadSignedUrlResponse(ConjoinModel):
    headers: dict[str, str] | None = None
    url: str


class StorageObjectCreateUploadSignedUrlResponse(ConjoinModel):
    required_fields: dict[str, Any]
    upload_mode: str
    upload_url: str


class StorageObjectDeleteResponse(ConjoinModel):
    archived_date: str | None
    checksum: str | None
    conjoin_account_id: str
    conjoin_auth_acl: Sequence[dict[str, Any]]
    conjoin_project_id: str
    container_id: str
    content_type: str | None
    date_created: str
    date_updated: str | None
    description: str | None
    duplicate_of: str | None
    generation_number: float
    is_public: bool
    labels: Sequence[str]
    lifecycle_expires_at: str | None
    live_mode: bool
    md5_hash: str | None
    metadata: dict[str, Any] | None = None
    name: str
    object_id: str
    object_metadata: dict[str, Any] | None = None
    reference_id: str | None
    size: float
    sync_status: str
    version_id: str | None


class StorageObjectListItem(ConjoinModel):
    archived_date: str | None
    checksum: str | None
    conjoin_account_id: str
    conjoin_auth_acl: Sequence[dict[str, Any]]
    conjoin_project_id: str
    container_id: str
    content_type: str | None
    date_created: str
    date_updated: str | None
    description: str | None
    duplicate_of: str | None
    generation_number: float
    is_public: bool
    labels: Sequence[str]
    lifecycle_expires_at: str | None
    live_mode: bool
    md5_hash: str | None
    metadata: dict[str, Any] | None = None
    name: str
    object_id: str
    object_metadata: dict[str, Any] | None = None
    reference_id: str | None
    size: float
    sync_status: str
    version_id: str | None


class StorageObjectListVersionsItem(ConjoinModel):
    checksum: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    content_type: str | None
    created_by: str
    date_created: str
    date_updated: str | None
    gcs_version_path: str
    live_mode: bool
    md5_hash: str | None
    metadata: dict[str, Any] | None = None
    name: str
    object_id: str
    size: float
    version_id: str


class StorageObjectReadResponse(ConjoinModel):
    archived_date: str | None
    checksum: str | None
    conjoin_account_id: str
    conjoin_auth_acl: Sequence[dict[str, Any]]
    conjoin_project_id: str
    container_id: str
    content_type: str | None
    date_created: str
    date_updated: str | None
    description: str | None
    duplicate_of: str | None
    generation_number: float
    is_public: bool
    labels: Sequence[str]
    lifecycle_expires_at: str | None
    live_mode: bool
    md5_hash: str | None
    metadata: dict[str, Any] | None = None
    name: str
    object_id: str
    object_metadata: dict[str, Any] | None = None
    reference_id: str | None
    size: float
    sync_status: str
    version_id: str | None


class StorageObjectRenameResponse(ConjoinModel):
    archived_date: str | None
    checksum: str | None
    conjoin_account_id: str
    conjoin_auth_acl: Sequence[dict[str, Any]]
    conjoin_project_id: str
    container_id: str
    content_type: str | None
    date_created: str
    date_updated: str | None
    description: str | None
    duplicate_of: str | None
    generation_number: float
    is_public: bool
    labels: Sequence[str]
    lifecycle_expires_at: str | None
    live_mode: bool
    md5_hash: str | None
    metadata: dict[str, Any] | None = None
    name: str
    object_id: str
    object_metadata: dict[str, Any] | None = None
    reference_id: str | None
    size: float
    sync_status: str
    version_id: str | None


class StorageObjectRestoreResponse(ConjoinModel):
    archived_date: str | None
    checksum: str | None
    conjoin_account_id: str
    conjoin_auth_acl: Sequence[dict[str, Any]]
    conjoin_project_id: str
    container_id: str
    content_type: str | None
    date_created: str
    date_updated: str | None
    description: str | None
    duplicate_of: str | None
    generation_number: float
    is_public: bool
    labels: Sequence[str]
    lifecycle_expires_at: str | None
    live_mode: bool
    md5_hash: str | None
    metadata: dict[str, Any] | None = None
    name: str
    object_id: str
    object_metadata: dict[str, Any] | None = None
    reference_id: str | None
    size: float
    sync_status: str
    version_id: str | None


class StorageObjectRestoreVersionResponse(ConjoinModel):
    checksum: str | None
    conjoin_account_id: str
    conjoin_project_id: str
    container_id: str
    content_type: str | None
    created_by: str
    date_created: str
    date_updated: str | None
    gcs_version_path: str
    live_mode: bool
    md5_hash: str | None
    metadata: dict[str, Any] | None = None
    name: str
    object_id: str
    size: float
    version_id: str


class _AiBYOKCreateByokConfigRequestRequired(TypedDict):
    api_key: str
    provider: str
    provider_name: str


class AiBYOKCreateByokConfigRequest(_AiBYOKCreateByokConfigRequestRequired, total=False):
    allowed_models: Sequence[str]
    description: str | None
    endpoint_url: str | None
    metadata: dict[str, Any]
    reference_id: str | None


class AiBYOKListByokConfigsCountQuery(TypedDict, total=False):
    provider: str
    status: str
    is_enabled: Any
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiBYOKListByokConfigsQuery(TypedDict, total=False):
    provider: str
    status: str
    is_enabled: Any
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiBYOKUpdateByokConfigRequest(TypedDict, total=False):
    allowed_models: Sequence[str]
    api_key: str
    description: str | None
    endpoint_url: str | None
    is_enabled: bool
    metadata: dict[str, Any]
    provider_name: str
    status: str


class _AiContextCreateIndexRequestRequired(TypedDict):
    name: str
    source_config: dict[str, Any]
    source_type: str


class AiContextCreateIndexRequest(_AiContextCreateIndexRequestRequired, total=False):
    description: str | None
    embedding_model: str
    metadata: dict[str, Any]
    reference_id: str | None


class _AiContextCreateQueryRequestRequired(TypedDict):
    index_ids: Sequence[str]
    query: str


class AiContextCreateQueryRequest(_AiContextCreateQueryRequestRequired, total=False):
    limit: int
    modes: Sequence[str]
    user_id: str


class AiContextListIndexesCountQuery(TypedDict, total=False):
    status: str
    sync_status: str
    source_type: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiContextListIndexesQuery(TypedDict, total=False):
    status: str
    sync_status: str
    source_type: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiContextListQueriesCountQuery(TypedDict, total=False):
    user_id: str
    queried_at: dict[str, Any]
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiContextListQueriesQuery(TypedDict, total=False):
    user_id: str
    queried_at: dict[str, Any]
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _AiInferenceCreateAiBestOfNRequestRequired(TypedDict):
    messages: Sequence[dict[str, Any]]
    model: str
    n: int


class AiInferenceCreateAiBestOfNRequest(_AiInferenceCreateAiBestOfNRequestRequired, total=False):
    max_tokens: int
    selection_criteria: str
    temperature: float


class _AiInferenceCreateAiMultiModelRequestRequired(TypedDict):
    messages: Sequence[dict[str, Any]]
    models: Sequence[str]


class AiInferenceCreateAiMultiModelRequest(
    _AiInferenceCreateAiMultiModelRequestRequired,
    total=False,
):
    judge_model: str
    max_tokens: int
    synthesize: bool
    temperature: float


class _AiInferenceCreateChatCompletionRequestRequired(TypedDict):
    messages: Sequence[dict[str, Any]]
    model: str


class AiInferenceCreateChatCompletionRequest(
    _AiInferenceCreateChatCompletionRequestRequired,
    total=False,
):
    context: dict[str, Any]
    max_tokens: int
    metadata: dict[str, Any]
    response_format: dict[str, Any]
    stop: Sequence[str]
    stream: bool
    temperature: float
    tools: Sequence[dict[str, Any]]
    top_p: float


class AiInferenceListRequestsCountQuery(TypedDict, total=False):
    model: str
    status: str
    request_type: str
    conjoin_request_id: str
    trace_source: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiInferenceListRequestsQuery(TypedDict, total=False):
    model: str
    status: str
    request_type: str
    conjoin_request_id: str
    trace_source: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiModelListCountQuery(TypedDict, total=False):
    vendor: str
    plan_availability: str
    text_input: Any
    image_input: Any
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiModelListQuery(TypedDict, total=False):
    vendor: str
    plan_availability: str
    text_input: Any
    image_input: Any
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _AiPolicyCreateCheckRequestRequired(TypedDict):
    content: str
    direction: str


class AiPolicyCreateCheckRequest(_AiPolicyCreateCheckRequestRequired, total=False):
    context: dict[str, Any]


class _AiPolicyCreateRuleRequestRequired(TypedDict):
    action: str
    config: dict[str, Any]
    direction: str
    name: str
    rule_type: str


class AiPolicyCreateRuleRequest(_AiPolicyCreateRuleRequestRequired, total=False):
    description: str | None
    metadata: dict[str, Any]
    priority: int
    reference_id: str | None


class AiPolicyListLogsCountQuery(TypedDict, total=False):
    rule_id: str
    rule_type: str
    action_taken: str
    severity: str
    direction: str
    logged_at: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiPolicyListLogsQuery(TypedDict, total=False):
    rule_id: str
    rule_type: str
    action_taken: str
    severity: str
    direction: str
    logged_at: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiPolicyListRulesCountQuery(TypedDict, total=False):
    rule_type: str
    status: str
    is_active: Any
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiPolicyListRulesQuery(TypedDict, total=False):
    rule_type: str
    status: str
    is_active: Any
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiPolicyUpdateRuleRequest(TypedDict, total=False):
    action: str
    config: dict[str, Any]
    description: str | None
    direction: str
    is_active: bool
    metadata: dict[str, Any]
    name: str
    priority: int
    status: str


class AiUsageListRecordsCountQuery(TypedDict, total=False):
    record_type: str
    model: str
    provider: str
    billing_period: str
    is_billable: Any
    conjoin_request_id: str
    trace_source: str
    recorded_at: dict[str, Any]
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiUsageListRecordsQuery(TypedDict, total=False):
    record_type: str
    model: str
    provider: str
    billing_period: str
    is_billable: Any
    conjoin_request_id: str
    trace_source: str
    recorded_at: dict[str, Any]
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AiUsageReadSummaryQuery(TypedDict, total=False):
    billing_period: str
    start_date: str
    end_date: str


class _AuthAccountAddEmailRequestRequired(TypedDict):
    email: str


class AuthAccountAddEmailRequest(_AuthAccountAddEmailRequestRequired, total=False):
    session_id: str
    set_as_primary: bool
    step_up_token: str


class _AuthAccountAddPhoneRequestRequired(TypedDict):
    phone: str


class AuthAccountAddPhoneRequest(_AuthAccountAddPhoneRequestRequired, total=False):
    session_id: str
    set_as_primary: bool
    step_up_token: str


class AuthAccountCreateRequest(TypedDict, total=False):
    image_url: str
    metadata: dict[str, Any]
    name: str
    primary_email: str
    primary_phone: str
    reference_id: str


class AuthAccountDeleteQuery(TypedDict, total=False):
    permanent: Any


class AuthAccountGrantGlobalRoleRequest(TypedDict):
    role_key: str


class AuthAccountImportPasswordHashesRequest(TypedDict):
    users: Sequence[dict[str, Any]]


class AuthAccountListCountQuery(TypedDict, total=False):
    account_id: str
    reference_id: str
    emails: Sequence[str]
    phones: Sequence[str]
    status: str
    dormant: Any
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthAccountListCredentialsCountQuery(TypedDict, total=False):
    credential_id: str
    credential_type: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthAccountListCredentialsQuery(TypedDict, total=False):
    credential_id: str
    credential_type: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthAccountListOrganizationMembershipsCountQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthAccountListOrganizationMembershipsQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthAccountListQuery(TypedDict, total=False):
    account_id: str
    reference_id: str
    emails: Sequence[str]
    phones: Sequence[str]
    status: str
    dormant: Any
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _AuthAccountMergeRequestRequired(TypedDict):
    source_account_id: str
    target_account_id: str


class AuthAccountMergeRequest(_AuthAccountMergeRequestRequired, total=False):
    strategy: str


class _AuthAccountRecoveryCompleteRecoveryRequestRequired(TypedDict):
    token: str


class AuthAccountRecoveryCompleteRecoveryRequest(
    _AuthAccountRecoveryCompleteRecoveryRequestRequired,
    total=False,
):
    credential_kinds_to_remove: Sequence[str]


class AuthAccountRecoveryVerifyRecoveryRequest(TypedDict):
    token: str


class _AuthAccountRemoveEmailRequestRequired(TypedDict):
    email: str


class AuthAccountRemoveEmailRequest(_AuthAccountRemoveEmailRequestRequired, total=False):
    primary_email: str
    session_id: str
    step_up_token: str


class _AuthAccountRemovePhoneRequestRequired(TypedDict):
    phone: str


class AuthAccountRemovePhoneRequest(_AuthAccountRemovePhoneRequestRequired, total=False):
    primary_phone: str
    session_id: str
    step_up_token: str


class AuthAccountRevokeGlobalRoleRequest(TypedDict):
    role_key: str


class AuthAccountUpdateRequest(TypedDict, total=False):
    custom_attributes: dict[str, Any | None]
    image_url: str | None
    metadata: dict[str, Any]
    name: str
    primary_email: str
    primary_phone: str
    status: str


class AuthAccountVerifyCredentialMfaTotpRequest(TypedDict):
    code: str


class AuthAccountVerifyCredentialRequest(TypedDict):
    credential_type: str
    credential_value: str


class _AuthAppCreateRequestRequired(TypedDict):
    name: str
    slug: str


class AuthAppCreateRequest(_AuthAppCreateRequestRequired, total=False):
    description: str | None
    metadata: dict[str, Any]
    reference_id: str
    support_email: str | None


class AuthAppListCountQuery(TypedDict, total=False):
    app_id: str
    reference_id: str
    slug: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthAppListQuery(TypedDict, total=False):
    app_id: str
    reference_id: str
    slug: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthAppUpdateRequest(TypedDict, total=False):
    description: str | None
    metadata: dict[str, Any]
    name: str
    support_email: str | None


class AuthAppUpdateSettingsRequest(TypedDict, total=False):
    authentication: dict[str, Any]
    billing_entity_id: str | None
    cloud_zone_id: str | None
    custom_attributes_schema: Sequence[dict[str, Any]]
    guard: dict[str, Any]
    messaging_options: dict[str, Any]
    sessions: dict[str, Any]


class _AuthAuthorizationAuthorizeActionRequestRequired(TypedDict):
    account_id: str
    permission_key: str


class AuthAuthorizationAuthorizeActionRequest(
    _AuthAuthorizationAuthorizeActionRequestRequired,
    total=False,
):
    context: dict[str, Any]
    resource_id: str
    resource_type: str


class AuthAuthorizationCheckRoleRequest(TypedDict):
    account_id: str
    role_key: str


class AuthAuthorizationReadEffectivePermissionsQuery(TypedDict):
    account_id: str


class AuthClientCreateRequest(TypedDict, total=False):
    metadata: dict[str, Any]
    reference_id: str


class AuthClientListCountQuery(TypedDict, total=False):
    client_id: str
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthClientListQuery(TypedDict, total=False):
    client_id: str
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthConnectionEnterpriseListEnterpriseConnectionsCountQuery(TypedDict, total=False):
    identity: str
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthConnectionEnterpriseListEnterpriseConnectionsQuery(TypedDict, total=False):
    identity: str
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthConnectionEnterpriseSyncEnterpriseSamlMetadataRequest(TypedDict):
    metadata_url: str


class AuthConnectionListFirstPartyQuery(TypedDict, total=False):
    identity: str


class _AuthConnectionUpsertFirstPartyRequestRequired(TypedDict):
    configuration: dict[str, Any]
    identity: str


class AuthConnectionUpsertFirstPartyRequest(
    _AuthConnectionUpsertFirstPartyRequestRequired,
    total=False,
):
    name: str | None
    status: str


class AuthCredentialActivateSmsMfaRequest(TypedDict):
    code: str


class AuthCredentialActivateTotpRequest(TypedDict):
    code: str


class AuthCredentialConsumeTotpRecoveryCodeRequest(TypedDict):
    code: str


class AuthCredentialCreatePasswordRequest(TypedDict):
    password: str


class _AuthCredentialEnrollSmsMfaRequestRequired(TypedDict):
    phone: str


class AuthCredentialEnrollSmsMfaRequest(_AuthCredentialEnrollSmsMfaRequestRequired, total=False):
    session_id: str
    step_up_token: str


class AuthCredentialEnrollTotpRequest(TypedDict, total=False):
    account_label: str
    issuer: str
    recovery_code_count: int
    recovery_code_length: int
    session_id: str
    step_up_token: str


class AuthCredentialIssueApiKeyRequest(TypedDict, total=False):
    allowed_ips: Sequence[str]
    environment: str | None
    expire_at: str
    label: str | None
    prefix: str
    rate_limit: dict[str, Any] | None
    scopes: Sequence[str]
    session_id: str
    step_up_token: str
    test_mode: bool
    token_metadata: dict[str, Any] | None


class AuthCredentialRevokeApiKeyRequest(TypedDict, total=False):
    session_id: str
    step_up_token: str


class AuthCredentialRotateApiKeyRequest(TypedDict, total=False):
    expire_at: str
    overlap_days: int
    prefix: str
    scopes: Sequence[str]
    session_id: str
    step_up_token: str
    test_mode: bool


class _AuthCredentialRotatePasswordRequestRequired(TypedDict):
    new_password: str


class AuthCredentialRotatePasswordRequest(
    _AuthCredentialRotatePasswordRequestRequired,
    total=False,
):
    current_password: str
    session_id: str
    step_up_token: str


class AuthCredentialRotateTotpRecoveryCodesRequest(TypedDict, total=False):
    recovery_code_count: int
    recovery_code_length: int
    session_id: str
    step_up_token: str


class _AuthCredentialStartPasskeyRegistrationRequestRequired(TypedDict):
    user_handle: str


class AuthCredentialStartPasskeyRegistrationRequest(
    _AuthCredentialStartPasskeyRegistrationRequestRequired,
    total=False,
):
    session_id: str
    step_up_token: str


class AuthCredentialUpdateApiKeyRequest(TypedDict, total=False):
    allowed_ips: Sequence[str]
    environment: str | None
    label: str | None
    rate_limit: dict[str, Any] | None
    token_metadata: dict[str, Any] | None


class _AuthCredentialVerifyPasskeyRegistrationRequestRequired(TypedDict):
    attestation_response: Any


class AuthCredentialVerifyPasskeyRegistrationRequest(
    _AuthCredentialVerifyPasskeyRegistrationRequestRequired,
    total=False,
):
    session_id: str
    step_up_token: str


class AuthCredentialVerifyPasskeyenticationRequest(TypedDict):
    assertion_response: Any


class AuthCredentialVerifySmsMfaRequest(TypedDict):
    code: str


class AuthDeprovisioningDeprovisionAccountRequest(TypedDict, total=False):
    policy: str
    revoke_sessions: bool


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


class AuthGuardAddAnonymousIpsRequest(TypedDict):
    ips: Sequence[str]


class AuthGuardAddTrustedDomainRequest(TypedDict):
    domain: str


class AuthGuardAddTrustedEmailRequest(TypedDict):
    email: str


class AuthGuardAddTrustedIpRequest(TypedDict):
    ip: str


class _AuthGuardCreateRuleRequestRequired(TypedDict):
    action: str
    name: str
    predicate: dict[str, Any]


class AuthGuardCreateRuleRequest(_AuthGuardCreateRuleRequestRequired, total=False):
    description: str | None
    expires_at: str | None
    is_enabled: bool


class AuthGuardListEventsCountQuery(TypedDict, total=False):
    event_type: str
    account_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthGuardListEventsQuery(TypedDict, total=False):
    event_type: str
    account_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthGuardListRulesCountQuery(TypedDict, total=False):
    action: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthGuardListRulesQuery(TypedDict, total=False):
    action: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthGuardRemoveAnonymousIpsRequest(TypedDict):
    ips: Sequence[str]


class AuthGuardRemoveTrustedDomainRequest(TypedDict):
    domain: str


class AuthGuardRemoveTrustedEmailRequest(TypedDict):
    email: str


class AuthGuardRemoveTrustedIpRequest(TypedDict):
    ip: str


class AuthGuardUpdateRuleRequest(TypedDict, total=False):
    action: str
    description: str | None
    expires_at: str | None
    is_enabled: bool
    name: str
    predicate: dict[str, Any]


class AuthIdentityDiscoverAccountRequest(TypedDict):
    identifiers: dict[str, Any]


class AuthIdentityLinkRequest(TypedDict):
    identity: dict[str, Any]


class AuthIdentityUnlinkRequest(TypedDict):
    identity: dict[str, Any]


class _AuthOrganizationCreateRequestRequired(TypedDict):
    name: str
    slug: str


class AuthOrganizationCreateRequest(_AuthOrganizationCreateRequestRequired, total=False):
    description: str | None
    image_url: str | None
    metadata: dict[str, Any]
    reference_id: str


class AuthOrganizationDeleteQuery(TypedDict, total=False):
    permanent: Any
    force: Any


class AuthOrganizationDomainCreateRequest(TypedDict):
    domain: str


class AuthOrganizationDomainListCountQuery(TypedDict, total=False):
    domain: str
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationDomainListQuery(TypedDict, total=False):
    domain: str
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationGroupAddGroupMemberRequest(TypedDict):
    account_id: str


class AuthOrganizationGroupBulkSyncGroupMembersRequest(TypedDict, total=False):
    add: Sequence[str]
    remove: Sequence[str]


class _AuthOrganizationGroupCreateGroupRequestRequired(TypedDict):
    name: str


class AuthOrganizationGroupCreateGroupRequest(
    _AuthOrganizationGroupCreateGroupRequestRequired,
    total=False,
):
    description: str
    image_url: str
    reference_id: str
    roles: Sequence[str]
    slug: str


class AuthOrganizationGroupListGroupMembersCountQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationGroupListGroupMembersQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationGroupListGroupsCountQuery(TypedDict, total=False):
    reference_id: str
    name: str
    slug: str
    provisioning_source: str
    external_id: str
    date_deleted: str | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationGroupListGroupsQuery(TypedDict, total=False):
    reference_id: str
    name: str
    slug: str
    provisioning_source: str
    external_id: str
    date_deleted: str | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationGroupRemoveGroupMemberRequest(TypedDict):
    account_id: str


class AuthOrganizationGroupUpdateGroupRequest(TypedDict, total=False):
    description: str
    image_url: str
    name: str
    roles: Sequence[str]
    slug: str


class _AuthOrganizationInvitationCreateInvitationRequestRequired(TypedDict):
    email: str


class AuthOrganizationInvitationCreateInvitationRequest(
    _AuthOrganizationInvitationCreateInvitationRequestRequired,
    total=False,
):
    expires_in_seconds: float
    metadata: dict[str, Any]
    name: str | None
    redirect_uri: str | None
    reference_id: str
    roles: Sequence[str]


class AuthOrganizationInvitationListInvitationsCountQuery(TypedDict, total=False):
    reference_id: str
    email: str
    status: str
    date_deleted: str | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationInvitationListInvitationsQuery(TypedDict, total=False):
    reference_id: str
    email: str
    status: str
    date_deleted: str | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationInvitationResendInvitationRequest(TypedDict, total=False):
    expires_in_seconds: float
    redirect_uri: str | None


class AuthOrganizationListCountQuery(TypedDict, total=False):
    organization_id: str
    account_id: str
    reference_id: str
    slug: str
    date_deleted: str | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationListQuery(TypedDict, total=False):
    organization_id: str
    account_id: str
    reference_id: str
    slug: str
    date_deleted: str | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _AuthOrganizationMembershipCreateMembershipRequestRequired(TypedDict):
    account_id: str
    roles: Sequence[str]


class AuthOrganizationMembershipCreateMembershipRequest(
    _AuthOrganizationMembershipCreateMembershipRequestRequired,
    total=False,
):
    joined_at: str
    metadata: dict[str, Any]
    status: str


class AuthOrganizationMembershipGrantOrgAccountRoleRequest(TypedDict):
    role_key: str


class AuthOrganizationMembershipListMembershipsCountQuery(TypedDict, total=False):
    account_id: str
    status: str
    date_deleted: str | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationMembershipListMembershipsQuery(TypedDict, total=False):
    account_id: str
    status: str
    date_deleted: str | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationMembershipRevokeOrgAccountRoleRequest(TypedDict):
    role_key: str


class AuthOrganizationMembershipUpdateMembershipRequest(TypedDict, total=False):
    joined_at: str
    metadata: dict[str, Any]
    roles: Sequence[str]
    status: str


class _AuthOrganizationPermissionCreateOrgPermissionRequestRequired(TypedDict):
    key: str
    name: str


class AuthOrganizationPermissionCreateOrgPermissionRequest(
    _AuthOrganizationPermissionCreateOrgPermissionRequestRequired,
    total=False,
):
    description: str | None
    metadata: dict[str, Any]
    reference_id: str


class AuthOrganizationPermissionListOrgPermissionsCountQuery(TypedDict, total=False):
    permission_id: str
    reference_id: str
    key: str
    date_deleted: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationPermissionListOrgPermissionsQuery(TypedDict, total=False):
    permission_id: str
    reference_id: str
    key: str
    date_deleted: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationPermissionUpdateOrgPermissionRequest(TypedDict, total=False):
    description: str | None
    key: str
    metadata: dict[str, Any]
    name: str


class _AuthOrganizationRoleCreateOrgRoleRequestRequired(TypedDict):
    key: str
    name: str


class AuthOrganizationRoleCreateOrgRoleRequest(
    _AuthOrganizationRoleCreateOrgRoleRequestRequired,
    total=False,
):
    description: str | None
    metadata: dict[str, Any]
    parent_role_id: str | None
    reference_id: str
    scope: str


class AuthOrganizationRoleListOrgRolesCountQuery(TypedDict, total=False):
    reference_id: str
    key: str
    date_deleted: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationRoleListOrgRolesQuery(TypedDict, total=False):
    reference_id: str
    key: str
    date_deleted: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationRolePermissionAssignOrgRolePermissionRequest(TypedDict):
    permission_keys: Sequence[str]


class AuthOrganizationRolePermissionListOrgRolePermissionsCountQuery(TypedDict, total=False):
    permission_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationRolePermissionListOrgRolePermissionsQuery(TypedDict, total=False):
    permission_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthOrganizationRolePermissionRemoveRolePermissionRequest(TypedDict):
    permission_keys: Sequence[str]


class AuthOrganizationRoleUpdateOrgRoleRequest(TypedDict, total=False):
    description: str | None
    key: str
    metadata: dict[str, Any]
    name: str
    parent_role_id: str | None


class AuthOrganizationUpdateRequest(TypedDict, total=False):
    description: str | None
    image_url: str | None
    metadata: dict[str, Any]
    name: str
    slug: str


class AuthOrganizationUpdateSettingsRequest(TypedDict, total=False):
    authentication: dict[str, Any]
    groups: dict[str, Any]
    membership: dict[str, Any]
    sessions: dict[str, Any]
    unset: Sequence[str]


class AuthPasskeyListCountQuery(TypedDict, total=False):
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthPasskeyListQuery(TypedDict, total=False):
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _AuthPolicyCreateRequestRequired(TypedDict):
    conditions: Sequence[dict[str, Any]]
    effect: Any
    name: str
    permission_keys: Sequence[str]


class AuthPolicyCreateRequest(_AuthPolicyCreateRequestRequired, total=False):
    description: str | None
    is_enabled: bool
    priority: float
    reference_id: str


class AuthPolicyListCountQuery(TypedDict, total=False):
    reference_id: str
    effect: str
    is_enabled: Any
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthPolicyListQuery(TypedDict, total=False):
    reference_id: str
    effect: str
    is_enabled: Any
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthPolicyUpdateRequest(TypedDict, total=False):
    conditions: Sequence[dict[str, Any]]
    description: str | None
    effect: Any
    is_enabled: bool
    name: str
    permission_keys: Sequence[str]
    priority: float


class AuthResourceGrantCheckResourcePermissionRequest(TypedDict):
    account_id: str
    permission_key: str
    resource_id: str
    resource_type: str


class AuthResourceGrantGrantResourcePermissionRequest(TypedDict):
    account_id: str
    permission_keys: Sequence[str]
    resource_id: str
    resource_type: str


class AuthResourceGrantListCountQuery(TypedDict, total=False):
    account_id: str
    resource_type: str
    resource_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthResourceGrantListQuery(TypedDict, total=False):
    account_id: str
    resource_type: str
    resource_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthResourceGrantRevokeResourcePermissionRequest(TypedDict, total=False):
    permission_keys: Sequence[str]


class AuthRoleAssignmentLogListCountQuery(TypedDict, total=False):
    account_id: str
    role_key: str
    action: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthRoleAssignmentLogListQuery(TypedDict, total=False):
    account_id: str
    role_key: str
    action: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthSCIMManagementReconcileScimGroupMembersRequest(TypedDict):
    changes: Sequence[dict[str, Any]]
    provider: str


class AuthSCIMManagementReconcileScimGroupsRequest(TypedDict):
    groups: Sequence[dict[str, Any]]


class AuthSCIMManagementReconcileScimUsersRequest(TypedDict):
    provider: str
    users: Sequence[dict[str, Any]]


class AuthSCIMManagementUpdateScimSettingsRequest(TypedDict, total=False):
    bearer_token: str
    config: dict[str, Any]
    provider: str


class _AuthSCIMScimBulkOperationsRequestRequired(TypedDict):
    operations: Sequence[dict[str, Any]]


class AuthSCIMScimBulkOperationsRequest(_AuthSCIMScimBulkOperationsRequestRequired, total=False):
    fail_on_errors: int
    schemas: Sequence[str]


class _AuthSCIMScimCreateGroupRequestRequired(TypedDict):
    display_name: str


class AuthSCIMScimCreateGroupRequest(_AuthSCIMScimCreateGroupRequestRequired, total=False):
    external_id: str
    members: Sequence[dict[str, Any]]


class AuthSCIMScimCreateUserRequest(TypedDict, total=False):
    active: bool
    emails: Sequence[dict[str, Any]]
    external_id: str
    name: dict[str, Any]
    phone_numbers: Sequence[dict[str, Any]]
    photos: Sequence[dict[str, Any]]
    user_name: str


class _AuthSCIMScimPatchGroupMembersRequestRequired(TypedDict):
    operations: Sequence[dict[str, Any]]


class AuthSCIMScimPatchGroupMembersRequest(
    _AuthSCIMScimPatchGroupMembersRequestRequired,
    total=False,
):
    schemas: Sequence[str]


class _AuthSCIMScimReplaceGroupRequestRequired(TypedDict):
    display_name: str


class AuthSCIMScimReplaceGroupRequest(_AuthSCIMScimReplaceGroupRequestRequired, total=False):
    external_id: str
    members: Sequence[dict[str, Any]]


class AuthSCIMScimReplaceUserRequest(TypedDict, total=False):
    active: bool
    emails: Sequence[dict[str, Any]]
    external_id: str
    name: dict[str, Any]
    phone_numbers: Sequence[dict[str, Any]]
    photos: Sequence[dict[str, Any]]
    user_name: str


class _AuthSLOOidcLogoutRequestRequired(TypedDict):
    end_session_endpoint: str


class AuthSLOOidcLogoutRequest(_AuthSLOOidcLogoutRequestRequired, total=False):
    id_token_hint: str
    post_logout_redirect_uri: str


class AuthSLOSamlIdpLogoutRequest(TypedDict):
    query_string: str


class _AuthSLOSamlSpLogoutRequestRequired(TypedDict):
    connection_id: str
    name_id: str


class AuthSLOSamlSpLogoutRequest(_AuthSLOSamlSpLogoutRequestRequired, total=False):
    relay_state: str
    session_index: str


class AuthSSOPortalUpdateSsoPortalSettingsRequest(TypedDict, total=False):
    allowed_providers: Sequence[str]
    require_domain_verification: bool
    setup_intents: Sequence[str]


class _AuthSessionBulkRevokeAccountRequestRequired(TypedDict):
    session_ids: Sequence[str]


class AuthSessionBulkRevokeAccountRequest(
    _AuthSessionBulkRevokeAccountRequestRequired,
    total=False,
):
    revoke_reason: str


class _AuthSessionBulkRevokeClientRequestRequired(TypedDict):
    session_ids: Sequence[str]


class AuthSessionBulkRevokeClientRequest(_AuthSessionBulkRevokeClientRequestRequired, total=False):
    revoke_reason: str


class _AuthSessionGetAnalyticsQueryRequired(TypedDict):
    start_date: str
    end_date: str


class AuthSessionGetAnalyticsQuery(_AuthSessionGetAnalyticsQueryRequired, total=False):
    group_by: str
    include_clients: Any
    client_ids: Sequence[str]


class AuthSessionListCountQuery(TypedDict, total=False):
    session_id: str
    account_id: str
    client_id: str
    status: str
    date_created: dict[str, Any]
    expires_at: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthSessionListQuery(TypedDict, total=False):
    session_id: str
    account_id: str
    client_id: str
    status: str
    date_created: dict[str, Any]
    expires_at: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthSessionReadStatsQuery(TypedDict, total=False):
    account_id: str
    client_id: str
    time_window_hours: Any


class AuthSessionUpdateRequest(TypedDict, total=False):
    extends_by_seconds: int
    metadata: dict[str, Any]
    status: str


class AuthSessionValidateRequest(TypedDict, total=False):
    check_expiry: bool
    ip_address: str
    update_last_activity: bool


class AuthStepUpRequestRequest(TypedDict):
    operation_id: str
    session_id: str


class AuthStepUpValidateRequest(TypedDict):
    operation_id: str
    session_id: str
    token: str


class _AuthStepUpVerifyRequestRequired(TypedDict):
    challenge_id: str
    method: str
    operation_id: str
    session_id: str


class AuthStepUpVerifyRequest(_AuthStepUpVerifyRequestRequired, total=False):
    assertion_response: Any
    code: str
    password: str


class AuthTrustedDeviceListCountQuery(TypedDict, total=False):
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class AuthTrustedDeviceListQuery(TypedDict, total=False):
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingChargeListCountQuery(TypedDict, total=False):
    transaction_id: str
    payment_type: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingChargeListQuery(TypedDict, total=False):
    transaction_id: str
    payment_type: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _BillingCouponCreateRequestRequired(TypedDict):
    coupon_code: str
    discount_type: str
    duration: str
    name: str
    reason_code: str


class BillingCouponCreateRequest(_BillingCouponCreateRequestRequired, total=False):
    amount_off: int
    applies_to: dict[str, Any]
    currency: str
    duration_in_cycles: int
    expiration_date: str
    max_redemptions: int
    percent_off: float
    reference_id: str


class BillingCouponListCountQuery(TypedDict, total=False):
    coupon_code: str
    reference_id: str
    is_active: Any
    reason_code: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingCouponListQuery(TypedDict, total=False):
    coupon_code: str
    reference_id: str
    is_active: Any
    reason_code: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingCouponUpdateRequest(TypedDict, total=False):
    applies_to: dict[str, Any]
    expiration_date: str | None
    is_active: bool
    max_redemptions: int
    name: str


class _BillingCreditNoteCreateRequestRequired(TypedDict):
    amount: int
    currency: str
    customer_id: str
    reason: str


class BillingCreditNoteCreateRequest(_BillingCreditNoteCreateRequestRequired, total=False):
    description: str
    invoice_id: str
    reference_id: str


class BillingCreditNoteListCountQuery(TypedDict, total=False):
    reference_id: str
    customer_id: str
    invoice_id: str
    status: str
    reason: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingCreditNoteListCustomerCreditBalancesCountQuery(TypedDict, total=False):
    currency: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingCreditNoteListCustomerCreditBalancesQuery(TypedDict, total=False):
    currency: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingCreditNoteListQuery(TypedDict, total=False):
    reference_id: str
    customer_id: str
    invoice_id: str
    status: str
    reason: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _BillingCreditWalletCreateRequestRequired(TypedDict):
    credit_value: float
    currency: str
    customer_id: str


class BillingCreditWalletCreateRequest(_BillingCreditWalletCreateRequestRequired, total=False):
    auto_topup: dict[str, Any]
    label: str


class _BillingCreditWalletGrantCreditsRequestRequired(TypedDict):
    amount: int
    source: str


class BillingCreditWalletGrantCreditsRequest(
    _BillingCreditWalletGrantCreditsRequestRequired,
    total=False,
):
    expiration_date: str


class BillingCreditWalletListCountQuery(TypedDict, total=False):
    customer_id: str
    label: str
    is_active: Any
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingCreditWalletListQuery(TypedDict, total=False):
    customer_id: str
    label: str
    is_active: Any
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingCreditWalletUpdateRequest(TypedDict, total=False):
    auto_topup: dict[str, Any]
    credit_value: float
    is_active: bool


class _BillingCustomerCreateRequestRequired(TypedDict):
    email: str


class BillingCustomerCreateRequest(_BillingCustomerCreateRequestRequired, total=False):
    address: dict[str, Any]
    invoice_settings: dict[str, Any]
    name: str
    payment_settings: dict[str, Any]
    phone: str
    reference_id: str
    shipping_address: dict[str, Any]


class BillingCustomerListCountQuery(TypedDict, total=False):
    customer_id: str
    reference_id: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingCustomerListQuery(TypedDict, total=False):
    customer_id: str
    reference_id: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingCustomerUpdateRequest(TypedDict, total=False):
    address: dict[str, Any]
    email: str
    invoice_settings: dict[str, Any]
    name: str
    payment_settings: dict[str, Any]
    phone: str
    shipping_address: dict[str, Any]


class _BillingDiscountCreateRequestRequired(TypedDict):
    coupon_id: str
    customer_id: str


class BillingDiscountCreateRequest(_BillingDiscountCreateRequestRequired, total=False):
    reference_id: str
    subscription_id: str


class BillingDiscountListCountQuery(TypedDict, total=False):
    customer_id: str
    coupon_id: str
    reference_id: str
    is_active: Any
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingDiscountListQuery(TypedDict, total=False):
    customer_id: str
    coupon_id: str
    reference_id: str
    is_active: Any
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingDisputeListCountQuery(TypedDict, total=False):
    charge_id: str
    outcome: str
    reason: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingDisputeListQuery(TypedDict, total=False):
    charge_id: str
    outcome: str
    reason: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _BillingEntitlementFeatureCreateRequestRequired(TypedDict):
    key: str
    name: str
    type: str


class BillingEntitlementFeatureCreateRequest(
    _BillingEntitlementFeatureCreateRequestRequired,
    total=False,
):
    credit_config: dict[str, Any]
    description: str
    metering_config: dict[str, Any]


class BillingEntitlementFeatureListCountQuery(TypedDict, total=False):
    type: str
    key: Any
    is_active: Any
    date_created: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingEntitlementFeatureListQuery(TypedDict, total=False):
    type: str
    key: Any
    is_active: Any
    date_created: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingEntitlementFeatureUpdateRequest(TypedDict, total=False):
    credit_config: dict[str, Any]
    description: str
    metering_config: dict[str, Any]
    name: str
    type: str


class _BillingEntitlementOverrideCreateRequestRequired(TypedDict):
    customer_id: str
    feature_id: str
    plan_id: str
    subscription_id: str
    value_type: str


class BillingEntitlementOverrideCreateRequest(
    _BillingEntitlementOverrideCreateRequestRequired,
    total=False,
):
    effective_from: str
    effective_to: str | None
    included_units: int
    reason: str
    soft_limit: bool


class BillingEntitlementOverrideListCountQuery(TypedDict, total=False):
    override_id: str
    customer_id: str
    subscription_id: str
    plan_id: str
    feature_id: str
    is_active: Any
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingEntitlementOverrideListQuery(TypedDict, total=False):
    override_id: str
    customer_id: str
    subscription_id: str
    plan_id: str
    feature_id: str
    is_active: Any
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingEntitlementOverrideUpdateRequest(TypedDict, total=False):
    effective_to: str | None
    included_units: int
    is_active: bool
    reason: str
    soft_limit: bool


class BillingEntityCreateAccountLinkRequest(TypedDict):
    refresh_url: str
    return_url: str


class BillingEntityCreatePayoutBankAccountRequest(TypedDict):
    data: dict[str, Any]


class BillingEntityCreatePaystackCredentialsRequest(TypedDict):
    public_key: str
    secret_key: str


class _BillingEntityCreateRequestRequired(TypedDict):
    account_data: dict[str, Any]


class BillingEntityCreateRequest(_BillingEntityCreateRequestRequired, total=False):
    invoicing: dict[str, Any]
    payments: dict[str, Any]
    subscriptions: dict[str, Any]
    tax_reporting: dict[str, Any]


class BillingEntityListCountQuery(TypedDict, total=False):
    expand: str
    is_active: Any
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingEntityListQuery(TypedDict, total=False):
    expand: str
    is_active: Any
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _BillingEntityOnboardRequestRequired(TypedDict):
    business_type: str
    company: dict[str, Any]
    country: str
    payment_markets: Sequence[dict[str, Any]]


class BillingEntityOnboardRequest(_BillingEntityOnboardRequestRequired, total=False):
    paystack_public_key: str
    paystack_secret_key: str
    stripe_refresh_url: str
    stripe_return_url: str


class BillingEntityReadQuery(TypedDict, total=False):
    expand: str


class BillingEntityUpdateRequest(TypedDict):
    data: dict[str, Any]


class _BillingFeatureAccessCheckEntitlementRequestRequired(TypedDict):
    feature_id: str


class BillingFeatureAccessCheckEntitlementRequest(
    _BillingFeatureAccessCheckEntitlementRequestRequired,
    total=False,
):
    consume: bool
    customer_id: str
    reference_id: str
    value: int


class _BillingFeatureAccessTrackFeatureUsageRequestRequired(TypedDict):
    feature_id: str
    value: int


class BillingFeatureAccessTrackFeatureUsageRequest(
    _BillingFeatureAccessTrackFeatureUsageRequestRequired,
    total=False,
):
    customer_id: str
    reference_id: str


class _BillingInvoiceCreateRequestRequired(TypedDict):
    customer_id: str
    invoicing_option: str


class BillingInvoiceCreateRequest(_BillingInvoiceCreateRequestRequired, total=False):
    currency: str
    custom_fields: Sequence[dict[str, Any]]
    description: str
    display_settings: dict[str, Any]
    email_settings: dict[str, Any]
    footer_text: str
    invoice_number: str
    line_items: Sequence[dict[str, Any]]
    payment_method_id: str
    payment_settings: dict[str, Any]
    reference_id: str
    subscription_id: str
    subtotal: int
    tax_amount: int


class BillingInvoiceListCountQuery(TypedDict, total=False):
    invoice_id: str
    reference_id: str
    customer_id: str
    subscription_id: str
    status: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingInvoiceListQuery(TypedDict, total=False):
    invoice_id: str
    reference_id: str
    customer_id: str
    subscription_id: str
    status: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingInvoicePayOutOfBandRequest(TypedDict, total=False):
    amount: int


class BillingInvoicePayRequest(TypedDict, total=False):
    allow_multiple_payment_methods: bool
    payment_method_id: str


class BillingInvoiceUpdateRequest(TypedDict, total=False):
    custom_fields: Sequence[dict[str, Any]]
    description: str
    display_settings: dict[str, Any]
    footer_text: str
    payment_method_id: str
    payment_settings: dict[str, Any]


class _BillingPaymentIntentCreateRequestRequired(TypedDict):
    currency: str
    customer_id: str


class BillingPaymentIntentCreateRequest(_BillingPaymentIntentCreateRequestRequired, total=False):
    amount: int
    customer_tax_id: str
    description: str
    disable_tax_reporting: bool
    payment_method_id: str
    payment_method_types: Sequence[str]
    price_id: str
    receipt_email: str
    reference_id: str
    setup_future_usage: str


class BillingPaymentIntentListCountQuery(TypedDict, total=False):
    payment_intent_id: str
    reference_id: str
    customer_id: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingPaymentIntentListQuery(TypedDict, total=False):
    payment_intent_id: str
    reference_id: str
    customer_id: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _BillingPaymentMethodCreateRequestRequired(TypedDict):
    customer_card_email: str
    customer_id: str


class BillingPaymentMethodCreateRequest(_BillingPaymentMethodCreateRequestRequired, total=False):
    is_default: bool
    name: str
    reference_id: str


class BillingPaymentMethodListCountQuery(TypedDict, total=False):
    reference_id: str
    customer_id: str
    type: str
    brand: str
    is_active: Any
    is_default: Any
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingPaymentMethodListQuery(TypedDict, total=False):
    reference_id: str
    customer_id: str
    type: str
    brand: str
    is_active: Any
    is_default: Any
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _BillingPriceBundleActivateRequestRequired(TypedDict):
    bundles: Sequence[dict[str, Any]]


class BillingPriceBundleActivateRequest(_BillingPriceBundleActivateRequestRequired, total=False):
    application_timing: str
    customer_id: str
    email: str
    incompatible_addon_behavior: str
    name: str
    payment_method_id: str
    payment_strategy: str
    proration_behavior: str
    reference_id: str
    subscription_strategy: str
    transition_timing: str


class _BillingPriceBundleCreateRequestRequired(TypedDict):
    items: Sequence[dict[str, Any]]
    name: str


class BillingPriceBundleCreateRequest(_BillingPriceBundleCreateRequestRequired, total=False):
    authoring_mode: str
    auto_activate: bool
    compatible_bundle_ids: Sequence[str] | None
    description: str
    discount_coupon_id: str
    is_default_tier: bool
    managed_catalog: dict[str, Any]
    metadata: dict[str, Any]
    min_tier_rank: int | None
    reference_id: str
    required_tier_group: str | None
    status: str
    tier_group: str | None
    tier_rank: int | None


class BillingPriceBundleDeactivateRequest(TypedDict, total=False):
    cancellation_fallback_behavior: str
    reason: str


class _BillingPriceBundleListActivationsCountQueryRequired(TypedDict):
    customer_id: str


class BillingPriceBundleListActivationsCountQuery(
    _BillingPriceBundleListActivationsCountQueryRequired,
    total=False,
):
    status: str
    price_bundle_id: str
    batch_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _BillingPriceBundleListActivationsQueryRequired(TypedDict):
    customer_id: str


class BillingPriceBundleListActivationsQuery(
    _BillingPriceBundleListActivationsQueryRequired,
    total=False,
):
    status: str
    price_bundle_id: str
    batch_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingPriceBundleListCountQuery(TypedDict, total=False):
    reference_id: str
    status: str
    auto_activate: Any
    date_created: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingPriceBundleListQuery(TypedDict, total=False):
    reference_id: str
    status: str
    auto_activate: Any
    date_created: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingPriceBundleReadAvailableBundleTransitionsQuery(TypedDict):
    customer_id: str


class BillingPriceBundleUpdateRequest(TypedDict, total=False):
    auto_activate: bool
    compatible_bundle_ids: Sequence[str] | None
    description: str
    discount_coupon_id: str
    is_default_tier: bool
    items: Sequence[dict[str, Any]]
    managed_catalog: dict[str, Any]
    metadata: dict[str, Any]
    min_tier_rank: int | None
    name: str
    required_tier_group: str | None
    status: str
    tier_group: str | None
    tier_rank: int | None


class _BillingPriceCreateRequestRequired(TypedDict):
    amount: int
    billing_scheme: str
    currency: str
    product_id: str
    type: str


class BillingPriceCreateRequest(_BillingPriceCreateRequestRequired, total=False):
    currency_options: dict[str, dict[str, Any]]
    is_active: bool
    metadata: dict[str, Any]
    recurring: dict[str, Any]
    reference_id: str
    tax_behavior: str
    tiers: Sequence[dict[str, Any]]
    tiers_mode: str


class BillingPriceListCountQuery(TypedDict, total=False):
    reference_id: str
    product_id: str
    currency: str
    type: str
    is_active: Any
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingPriceListQuery(TypedDict, total=False):
    reference_id: str
    product_id: str
    currency: str
    type: str
    is_active: Any
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingPriceUpdateRequest(TypedDict, total=False):
    billing_scheme: str
    is_active: bool
    metadata: dict[str, Any]
    recurring: dict[str, Any]
    tax_behavior: str
    tiers: Sequence[dict[str, Any]]
    tiers_mode: str
    type: str


class _BillingProductCreateRequestRequired(TypedDict):
    name: str
    unit_label: str


class BillingProductCreateRequest(_BillingProductCreateRequestRequired, total=False):
    description: str
    features: Sequence[dict[str, Any]]
    images: Sequence[str]
    is_active: bool
    metadata: dict[str, Any]
    reference_id: str
    statement_descriptor: str


class BillingProductListCountQuery(TypedDict, total=False):
    reference_id: str
    name: dict[str, Any]
    description: dict[str, Any]
    is_active: Any
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingProductListQuery(TypedDict, total=False):
    reference_id: str
    name: dict[str, Any]
    description: dict[str, Any]
    is_active: Any
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingProductUpdateRequest(TypedDict, total=False):
    description: str
    features: Sequence[dict[str, Any]]
    images: Sequence[str]
    is_active: bool
    metadata: dict[str, Any]
    name: str
    statement_descriptor: str
    unit_label: str


class BillingReceiptListCountQuery(TypedDict, total=False):
    status: str
    charge_id: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingReceiptListQuery(TypedDict, total=False):
    status: str
    charge_id: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _BillingRefundCreateRequestRequired(TypedDict):
    charge_id: str
    reference_id: str


class BillingRefundCreateRequest(_BillingRefundCreateRequestRequired, total=False):
    amount: int


class BillingRefundListCountQuery(TypedDict, total=False):
    refund_id: str
    reference_id: str
    charge_id: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingRefundListQuery(TypedDict, total=False):
    refund_id: str
    reference_id: str
    charge_id: str
    date_created: dict[str, Any]
    date_updated: dict[str, Any]
    date_deleted: dict[str, Any] | None
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingSettingsUpdateRequest(TypedDict, total=False):
    auto_receipt_generation: bool
    cancellation_fallback_behavior: str
    credit_auto_apply: bool
    default_currency: str
    default_invoice_settings: dict[str, Any]
    incompatible_addon_behavior: str
    tax_reporting_enabled: bool


class _BillingSubscriptionCancelRequestRequired(TypedDict):
    termination_behavior: str


class BillingSubscriptionCancelRequest(_BillingSubscriptionCancelRequestRequired, total=False):
    reason: str
    refund_policy: str


class _BillingSubscriptionCreatePlanChangeRequestRequired(TypedDict):
    items: Sequence[dict[str, Any]]


class BillingSubscriptionCreatePlanChangeRequest(
    _BillingSubscriptionCreatePlanChangeRequestRequired,
    total=False,
):
    application_timing: str
    proration_behavior: str


class _BillingSubscriptionCreateRequestRequired(TypedDict):
    customer_id: str


class BillingSubscriptionCreateRequest(_BillingSubscriptionCreateRequestRequired, total=False):
    auto_renew: bool
    cycle_start_date: str
    days_until_due: int
    invoicing_option: str
    payment_method: str
    payment_strategy: str
    plans: Sequence[dict[str, Any]]
    price_ids: Sequence[str]
    proration: dict[str, Any]
    reference_id: str
    renewal_notifications: dict[str, Any]
    trial_end_date: str


class BillingSubscriptionListCountQuery(TypedDict, total=False):
    reference_id: str
    customer_id: str
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingSubscriptionListCyclesCountQuery(TypedDict, total=False):
    cycle_id: str
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingSubscriptionListCyclesQuery(TypedDict, total=False):
    cycle_id: str
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingSubscriptionListQuery(TypedDict, total=False):
    reference_id: str
    customer_id: str
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingSubscriptionPauseRequest(TypedDict, total=False):
    reason: str


class BillingSubscriptionReadUsageSummaryQuery(TypedDict, total=False):
    cycle_id: str


class _BillingSubscriptionRecordUsageRequestRequired(TypedDict):
    plan_id: str
    records: Sequence[dict[str, Any]]


class BillingSubscriptionRecordUsageRequest(
    _BillingSubscriptionRecordUsageRequestRequired,
    total=False,
):
    cycle_id: str


class BillingSubscriptionScheduleCreateRequest(TypedDict):
    end_behavior: str
    phases: Sequence[dict[str, Any]]


class BillingSubscriptionScheduleListCountQuery(TypedDict, total=False):
    customer_id: str
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingSubscriptionScheduleListQuery(TypedDict, total=False):
    customer_id: str
    status: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingSubscriptionUpdateRequest(TypedDict, total=False):
    auto_renew: bool
    payment_method: str
    proration: dict[str, Any] | None
    renewal_notifications: dict[str, Any] | None


class BillingTaxJurisdictionListCountQuery(TypedDict, total=False):
    country: str
    state: str
    is_active: Any
    tax_type: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class BillingTaxJurisdictionListQuery(TypedDict, total=False):
    country: str
    state: str
    is_active: Any
    tax_type: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _BillingTaxJurisdictionQueryTaxRateQueryRequired(TypedDict):
    country: str


class BillingTaxJurisdictionQueryTaxRateQuery(
    _BillingTaxJurisdictionQueryTaxRateQueryRequired,
    total=False,
):
    state: str
    date: str


class _CloudAPIKeyCreateApiKeyRequestRequired(TypedDict):
    name: str


class CloudAPIKeyCreateApiKeyRequest(_CloudAPIKeyCreateApiKeyRequestRequired, total=False):
    description: str
    expire_at: str
    reference_id: str
    roles: Sequence[str]
    service_ids: Sequence[str]
    test_mode: bool


class CloudAPIKeyReadApiKeysCountQuery(TypedDict, total=False):
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudAPIKeyReadApiKeysQuery(TypedDict, total=False):
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _CloudAPIKeyRegenerateApiKeyRequestRequired(TypedDict):
    name: str
    test_mode: bool


class CloudAPIKeyRegenerateApiKeyRequest(_CloudAPIKeyRegenerateApiKeyRequestRequired, total=False):
    description: str
    expire_at: str
    roles: Sequence[str]
    service_ids: Sequence[str]


class _CloudAPIKeyUpdateApiKeyRequestRequired(TypedDict):
    name: str


class CloudAPIKeyUpdateApiKeyRequest(_CloudAPIKeyUpdateApiKeyRequestRequired, total=False):
    description: str


class CloudAccountUpdateRequest(TypedDict):
    has_accepted_terms: bool


class CloudAuditReadLogsCountQuery(TypedDict, total=False):
    event_code: str
    category: str
    actor_id: str
    resource_type: str
    resource_id: str
    severity: str
    conjoin_request_id: str
    from_: str
    to: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudAuditReadLogsQuery(TypedDict, total=False):
    event_code: str
    category: str
    actor_id: str
    resource_type: str
    resource_id: str
    severity: str
    conjoin_request_id: str
    from_: str
    to: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _CloudAuditReadStatsQueryRequired(TypedDict):
    by: str


class CloudAuditReadStatsQuery(_CloudAuditReadStatsQueryRequired, total=False):
    from_: str
    to: str


class CloudBrandingPatchOrgOverrideRequest(TypedDict, total=False):
    accessibility: dict[str, Any] | None
    animation: dict[str, Any] | None
    borders: dict[str, Any] | None
    colors: dict[str, Any] | None
    components: dict[str, Any] | None
    general: dict[str, Any] | None
    layout: dict[str, Any] | None
    organization: dict[str, Any] | None
    shadows: dict[str, Any] | None
    spacing: dict[str, Any] | None
    typography: dict[str, Any] | None


class CloudBrandingPatchProjectRequest(TypedDict, total=False):
    accessibility: dict[str, Any]
    animation: dict[str, Any]
    borders: dict[str, Any]
    colors: dict[str, Any]
    components: dict[str, Any]
    general: dict[str, Any]
    layout: dict[str, Any]
    organization: dict[str, Any] | None
    shadows: dict[str, Any]
    spacing: dict[str, Any]
    typography: dict[str, Any]


class _CloudOrganizationCreateRequestRequired(TypedDict):
    name: str


class CloudOrganizationCreateRequest(_CloudOrganizationCreateRequestRequired, total=False):
    reference_id: str
    tags: Sequence[str]


class CloudOrganizationListQuery(TypedDict, total=False):
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudOrganizationReadCountQuery(TypedDict, total=False):
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudOrganizationUpdateRequest(TypedDict, total=False):
    name: str
    tags: Sequence[str]


class CloudPlanListQuery(TypedDict, total=False):
    slug: str
    status: str
    currency: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudPlanReadCountQuery(TypedDict, total=False):
    slug: str
    status: str
    currency: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _CloudProjectCreateRequestRequired(TypedDict):
    name: str


class CloudProjectCreateRequest(_CloudProjectCreateRequestRequired, total=False):
    reference_id: str
    tags: Sequence[str]


class CloudProjectListQuery(TypedDict, total=False):
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudProjectReadCountQuery(TypedDict, total=False):
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudProjectUpdateRequest(TypedDict, total=False):
    name: str
    tags: Sequence[str]


class CloudPublishableKeyListCountQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudPublishableKeyListQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudPublishableKeyUpdateRequest(TypedDict):
    allowed_domains: Sequence[str]


class _CloudRoleCreateRequestRequired(TypedDict):
    name: str
    permissions: Sequence[str]
    project_id: str
    title: str


class CloudRoleCreateRequest(_CloudRoleCreateRequestRequired, total=False):
    description: str
    reference_id: str


class CloudRoleReadCountQuery(TypedDict, total=False):
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudRoleReadQuery(TypedDict, total=False):
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudRoleUpdateRequest(TypedDict, total=False):
    description: str
    permissions: Sequence[str]
    title: str


class CloudSKUCatalogReadSkuCatalogCountQuery(TypedDict, total=False):
    service: str
    category: str
    meter_type: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudSKUCatalogReadSkuCatalogQuery(TypedDict, total=False):
    service: str
    category: str
    meter_type: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudSpendControlUpdateRequest(TypedDict, total=False):
    ai_circuit_breaker_limits: Sequence[dict[str, Any]]
    alert_email_enabled: bool
    alert_sms_enabled: bool
    alert_thresholds: Sequence[int]
    alert_webhook_enabled: bool
    overage_budget_micros: int


class CloudWebhookListQuery(TypedDict, total=False):
    events: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudWebhookReadCountQuery(TypedDict, total=False):
    events: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudWebhookReadEventsCountQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudWebhookReadEventsQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _CloudWebhookRegisterRequestRequired(TypedDict):
    events: Sequence[str]
    url: str


class CloudWebhookRegisterRequest(_CloudWebhookRegisterRequestRequired, total=False):
    description: str
    is_active: bool
    name: str


class CloudWebhookUpdateRequest(TypedDict, total=False):
    description: str
    events: Sequence[str]
    is_active: bool
    name: str
    url: str


class _CloudZoneCreateRequestRequired(TypedDict):
    domain: str
    provider_id: str


class CloudZoneCreateRequest(_CloudZoneCreateRequestRequired, total=False):
    dkim_authority: str
    dns_records: Sequence[dict[str, Any]]


class CloudZoneListQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class CloudZoneReadCountQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _MessagingChannelAnalyticsCreateReportRequestRequired(TypedDict):
    duration: str


class MessagingChannelAnalyticsCreateReportRequest(
    _MessagingChannelAnalyticsCreateReportRequestRequired,
    total=False,
):
    document: dict[str, Any]


class MessagingChannelAnalyticsGenerateSummariesRequest(TypedDict):
    duration: str


class _MessagingChannelAnalyticsIncrementClicksRequestRequired(TypedDict):
    total_clicks: int


class MessagingChannelAnalyticsIncrementClicksRequest(
    _MessagingChannelAnalyticsIncrementClicksRequestRequired,
    total=False,
):
    unique_clicks: int


class MessagingChannelAnalyticsIncrementDeliveriesRequest(TypedDict):
    total_deliveries: int


class _MessagingChannelAnalyticsIncrementOpensRequestRequired(TypedDict):
    total_opens: int


class MessagingChannelAnalyticsIncrementOpensRequest(
    _MessagingChannelAnalyticsIncrementOpensRequestRequired,
    total=False,
):
    unique_opens: int


class MessagingChannelAnalyticsIncrementSubscribesRequest(TypedDict):
    total_subscribes: int


class MessagingChannelAnalyticsIncrementUnsubscribesRequest(TypedDict):
    total_unsubscribes: int


class MessagingChannelAnalyticsListRequest(TypedDict, total=False):
    cursor: dict[str, Any]
    filter: dict[str, Any]
    limit: Any
    query: dict[str, Any]
    sort: dict[str, str]


class MessagingContactAddPropertiesRequest(TypedDict):
    properties: dict[str, Any]


class MessagingContactCreateRequest(TypedDict, total=False):
    email: str
    first_name: str
    last_name: str
    phone_number: Any
    preferred_channels: Sequence[str]
    properties: dict[str, Any]
    quiet_hours: dict[str, Any]
    reference_id: str


class MessagingContactDeletePropertiesRequest(TypedDict):
    keys: Sequence[str]


class MessagingContactListRequest(TypedDict, total=False):
    cursor: dict[str, Any]
    filter: dict[str, Any]
    limit: Any
    query: dict[str, Any]
    search: dict[str, Any]
    sort: dict[str, str]


class MessagingContactPropertiesListRequest(TypedDict, total=False):
    cursor: dict[str, Any]
    limit: Any
    query: dict[str, Any]
    sort: dict[str, str]


class MessagingContactSuppressMessagesRequest(TypedDict):
    channels: Sequence[str]


class MessagingContactUpdatePropertyRequest(TypedDict):
    key: str
    value: Any


class MessagingContactUpdateRequest(TypedDict, total=False):
    email: str
    first_name: str
    last_name: str
    phone_number: Any
    preferred_channels: Sequence[str]
    quiet_hours: dict[str, Any]


class MessagingConversationAddManyRecipientsRequest(TypedDict):
    recipients: Sequence[dict[str, Any]]


class MessagingConversationAddOneRecipientRequest(TypedDict, total=False):
    email: str
    first_name: str
    last_name: str
    phone_number: Any
    preferred_channels: Sequence[str]
    properties: dict[str, Any]
    quiet_hours: dict[str, Any]
    reference_id: str


class MessagingConversationCloneRequest(TypedDict, total=False):
    accepts_replies: bool
    description: str
    title: str


class _MessagingConversationCreateRequestRequired(TypedDict):
    channels: Sequence[str]
    title: str


class MessagingConversationCreateRequest(_MessagingConversationCreateRequestRequired, total=False):
    accepts_replies: bool
    default_placeholders: dict[str, str]
    description: str
    recipients: Sequence[dict[str, Any]]
    reference_id: str
    senders: dict[str, Any]


class MessagingConversationListRequest(TypedDict, total=False):
    cursor: dict[str, Any]
    filter: dict[str, Any]
    limit: Any
    query: dict[str, Any]
    search: dict[str, Any]
    sort: dict[str, str]


class MessagingConversationReadManyRecipientsRequest(TypedDict, total=False):
    cursor: dict[str, Any]
    limit: Any
    sort: dict[str, str]


class _MessagingConversationReadMessagesRequestRequired(TypedDict):
    channel: str


class MessagingConversationReadMessagesRequest(
    _MessagingConversationReadMessagesRequestRequired,
    total=False,
):
    cursor: dict[str, Any]
    limit: Any
    search: dict[str, Any]
    sort: dict[str, str]


class _MessagingConversationSendMessageRequestRequired(TypedDict):
    messages: dict[str, Any]


class MessagingConversationSendMessageRequest(
    _MessagingConversationSendMessageRequestRequired,
    total=False,
):
    body: str
    default_placeholders: dict[str, Any]
    message_priority: str
    message_retry_statuses: Sequence[str]
    send_at: str
    to: Sequence[dict[str, Any]]


class MessagingConversationUpdateRequest(TypedDict, total=False):
    accepts_replies: bool
    description: str
    title: str


class _MessagingEmailGenerateSummaryRequestRequired(TypedDict):
    currency: str
    message: str


class MessagingEmailGenerateSummaryRequest(
    _MessagingEmailGenerateSummaryRequestRequired,
    total=False,
):
    default_placeholders: dict[str, str]
    to: Sequence[Any]


class MessagingEmailReadMessagesRequest(TypedDict, total=False):
    cursor: dict[str, Any]
    limit: Any
    query: dict[str, Any]
    search: dict[str, Any]
    sort: dict[str, str]


class _MessagingEmailSendRequestRequired(TypedDict):
    subject: str


class MessagingEmailSendRequest(_MessagingEmailSendRequestRequired, total=False):
    accepts_replies: bool
    attachments: Sequence[dict[str, Any]]
    bcc: Sequence[str]
    cc: Sequence[str]
    create_conversation: bool
    default_placeholders: dict[str, Any]
    from_: str
    html: str
    reference_id: str
    reply_to: str
    send_at: str
    sender_pool_id: str
    template_id: str
    text: str
    to: Sequence[Any]


class MessagingEmailSenderListManyRequest(TypedDict, total=False):
    cursor: dict[str, Any]
    filter: dict[str, Any]
    limit: Any
    query: dict[str, Any]
    search: dict[str, Any]
    sort: dict[str, str]


class MessagingEmailSenderPoolAddEmailSendersToPoolRequest(TypedDict):
    senders: Sequence[str]


class _MessagingEmailSenderPoolCreateRequestRequired(TypedDict):
    capability: str
    senders: Sequence[str]
    title: str


class MessagingEmailSenderPoolCreateRequest(
    _MessagingEmailSenderPoolCreateRequestRequired,
    total=False,
):
    description: str


class MessagingPhoneNumberListAvailableQuery(TypedDict, total=False):
    query: dict[str, Any]
    limit: Any


class MessagingPhoneNumberListQuery(TypedDict, total=False):
    filter: dict[str, Any]
    cursor: dict[str, Any]
    query: dict[str, Any]
    search: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _MessagingPhoneNumberPurchaseRequestRequired(TypedDict):
    country_iso_code: str
    title: str
    type: str


class MessagingPhoneNumberPurchaseRequest(
    _MessagingPhoneNumberPurchaseRequestRequired,
    total=False,
):
    callback_url: str
    config: dict[str, Any]
    description: str
    features: dict[str, Any]
    message_type: str


class _MessagingProfileCreateRequestRequired(TypedDict):
    email_config: dict[str, Any]
    name: str
    sms_config: dict[str, Any]


class MessagingProfileCreateRequest(_MessagingProfileCreateRequestRequired, total=False):
    description: str
    features: dict[str, Any]
    message_retention_days: float
    multisend_config: dict[str, Any]
    properties: dict[str, Any]
    resource_region: str
    verifications_config: dict[str, Any]


class MessagingProfileListRequest(TypedDict, total=False):
    cursor: dict[str, Any]
    filter: dict[str, Any]
    limit: Any
    query: dict[str, Any]
    sort: dict[str, str]


class MessagingProfileUpdateEmailConfigRequest(TypedDict):
    email_config: dict[str, Any]


class MessagingProfileUpdateMultisendConfigRequest(TypedDict):
    multisend_config: dict[str, Any]


class MessagingProfileUpdateRequest(TypedDict, total=False):
    features: dict[str, Any]
    message_retention_days: float
    name: str


class MessagingProfileUpdateVerificationsConfigRequest(TypedDict):
    verifications_config: dict[str, Any]


class MessagingSMSBrandListSmsBrandsRequest(TypedDict, total=False):
    cursor: dict[str, Any]
    filter: dict[str, Any]
    limit: Any
    query: dict[str, Any]
    sort: dict[str, str]


class MessagingSMSBrandUpdateSmsBrandRequest(TypedDict):
    display_name: str


class _MessagingSMSCampaignCreateSmsCampaignRequestRequired(TypedDict):
    brand_id: str
    description: str
    help_message: str
    message_flow: str
    message_samples: Sequence[str]
    opt_out_message: str
    privacy_policy_url: str
    terms_and_conditions_url: str
    title: str
    use_case: str


class MessagingSMSCampaignCreateSmsCampaignRequest(
    _MessagingSMSCampaignCreateSmsCampaignRequestRequired,
    total=False,
):
    age_gated: bool
    direct_lending: bool
    embeds_links: bool
    embeds_phone_numbers: bool
    help_keywords: Sequence[str]
    opt_in_keywords: Sequence[str]
    opt_in_message: str
    opt_out_keywords: Sequence[str]
    provision_number_pool: bool
    sub_use_cases: Sequence[str]
    subscriber_opt_in: bool


class MessagingSMSCampaignListSmsCampaignsRequest(TypedDict, total=False):
    cursor: dict[str, Any]
    filter: dict[str, Any]
    limit: Any
    query: dict[str, Any]
    sort: dict[str, str]


class MessagingSMSCampaignUpdateSmsCampaignRequest(TypedDict):
    title: str


class _MessagingSMSGenerateSmsSummaryRequestRequired(TypedDict):
    currency: str
    message: str


class MessagingSMSGenerateSmsSummaryRequest(
    _MessagingSMSGenerateSmsSummaryRequestRequired,
    total=False,
):
    default_placeholders: dict[str, str]
    to: Sequence[Any]
    truncate_message: bool


class MessagingSMSReadSmsMessagesRequest(TypedDict, total=False):
    cursor: dict[str, Any]
    limit: Any
    query: dict[str, Any]
    search: dict[str, Any]
    sort: dict[str, str]


class MessagingSMSSendSmsRequest(TypedDict, total=False):
    body: str
    create_conversation: bool
    default_placeholders: dict[str, Any]
    from_: str
    reference_id: str
    reply_to: str
    send_at: str
    sender_pool_id: str
    template_id: str
    to: Sequence[Any]
    truncate_message: bool


class MessagingSMSSenderPoolAddSmsSendersToPoolRequest(TypedDict):
    senders: Sequence[str]


class _MessagingSMSSenderPoolCreateSmsSenderPoolRequestRequired(TypedDict):
    capability: str
    senders: Sequence[str]
    title: str


class MessagingSMSSenderPoolCreateSmsSenderPoolRequest(
    _MessagingSMSSenderPoolCreateSmsSenderPoolRequestRequired,
    total=False,
):
    description: str


class MessagingSMSSenderUpdateOneSmsSenderRequest(TypedDict, total=False):
    is_default_sender: bool
    is_test_sender: bool
    properties: dict[str, Any]


class _MessagingTemplateCreateMessageRequestRequired(TypedDict):
    channel: str
    content: str
    content_type: str
    title: str


class MessagingTemplateCreateMessageRequest(
    _MessagingTemplateCreateMessageRequestRequired,
    total=False,
):
    content_limit: float | None
    description: str
    is_default: bool
    is_favourite: bool
    is_otp_template: bool
    language: str
    template_group_id: str


class MessagingTemplateDeleteMessagesRequest(TypedDict, total=False):
    query: dict[str, Any]


class MessagingTemplateListMessageRequest(TypedDict, total=False):
    cursor: dict[str, Any]
    filter: dict[str, Any]
    limit: Any
    query: dict[str, Any]
    search: dict[str, Any]
    sort: dict[str, str]


class MessagingTemplateUpdateMessageRequest(TypedDict, total=False):
    channel: str
    content: str
    content_limit: float | None
    content_type: str
    description: str
    is_default: bool
    is_favourite: bool
    is_otp_template: bool
    language: str
    template_group_id: str
    title: str


class MessagingVerificationCheckRequest(TypedDict):
    token: str


class _MessagingVerificationListMessagesRequestRequired(TypedDict):
    query: dict[str, Any]


class MessagingVerificationListMessagesRequest(
    _MessagingVerificationListMessagesRequestRequired,
    total=False,
):
    cursor: dict[str, Any]
    limit: Any
    sort: dict[str, str]


class _RelayBroadcastCreateChannelRequestRequired(TypedDict):
    name: str


class RelayBroadcastCreateChannelRequest(_RelayBroadcastCreateChannelRequestRequired, total=False):
    authorization_callback_url: str
    authorization_mode: str
    channel_type: str
    description: str
    history_size: int
    max_connections: int
    reference_id: str


class RelayBroadcastGenerateAuthTokenRequest(TypedDict, total=False):
    permissions: Sequence[str]
    user_id: str


class _RelayBroadcastPublishToRequestRequired(TypedDict):
    event: str


class RelayBroadcastPublishToRequest(_RelayBroadcastPublishToRequestRequired, total=False):
    data: dict[str, Any]


class RelayBroadcastReadChannelsCountQuery(TypedDict, total=False):
    status: str
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayBroadcastReadChannelsQuery(TypedDict, total=False):
    status: str
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayBroadcastUpdateChannelRequest(TypedDict, total=False):
    authorization_callback_url: str | None
    authorization_mode: str
    description: str | None
    history_size: int
    max_connections: int | None
    name: str


class _RelayEventsCreateEventChannelRequestRequired(TypedDict):
    name: str


class RelayEventsCreateEventChannelRequest(
    _RelayEventsCreateEventChannelRequestRequired,
    total=False,
):
    description: str
    reference_id: str
    retention_hours: int


class _RelayEventsCreateEventSubscriptionRequestRequired(TypedDict):
    endpoint_url: str


class RelayEventsCreateEventSubscriptionRequest(
    _RelayEventsCreateEventSubscriptionRequestRequired,
    total=False,
):
    description: str
    filter_rules: dict[str, Any]
    headers: dict[str, str] | None
    on_failure: Sequence[dict[str, Any]] | None
    on_success: Sequence[dict[str, Any]] | None
    reference_id: str
    retry_policy: dict[str, Any]


class _RelayEventsPublishEventRequestRequired(TypedDict):
    event_type: str


class RelayEventsPublishEventRequest(_RelayEventsPublishEventRequestRequired, total=False):
    payload: dict[str, Any]
    reference_id: str


class RelayEventsReadCountQuery(TypedDict, total=False):
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayEventsReadEventChannelsCountQuery(TypedDict, total=False):
    status: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayEventsReadEventChannelsQuery(TypedDict, total=False):
    status: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayEventsReadEventSubscriptionsCountQuery(TypedDict, total=False):
    status: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayEventsReadEventSubscriptionsQuery(TypedDict, total=False):
    status: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayEventsReadQuery(TypedDict, total=False):
    reference_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayEventsReplayRequest(TypedDict, total=False):
    from_timestamp: str
    subscription_id: str
    to_timestamp: str


class RelayEventsUpdateEventChannelRequest(TypedDict, total=False):
    description: str
    name: str
    retention_hours: int


class RelayEventsUpdateEventSubscriptionRequest(TypedDict, total=False):
    description: str
    endpoint_url: str
    filter_rules: dict[str, Any]
    headers: dict[str, str] | None
    on_failure: Sequence[dict[str, Any]] | None
    on_success: Sequence[dict[str, Any]] | None
    retry_policy: dict[str, Any]


class _RelayMemorystoreCreateClusterRequestRequired(TypedDict):
    name: str


class RelayMemorystoreCreateClusterRequest(
    _RelayMemorystoreCreateClusterRequestRequired,
    total=False,
):
    cluster_type: str
    description: str
    max_memory_mb: int
    reference_id: str
    region: str


class _RelayMemorystoreExecuteCommandRequestRequired(TypedDict):
    command: str


class RelayMemorystoreExecuteCommandRequest(
    _RelayMemorystoreExecuteCommandRequestRequired,
    total=False,
):
    args: Sequence[Any]


class RelayMemorystoreReadClustersCountQuery(TypedDict, total=False):
    status: str
    cluster_type: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayMemorystoreReadClustersQuery(TypedDict, total=False):
    status: str
    cluster_type: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayMemorystoreUpdateClusterRequest(TypedDict, total=False):
    description: str
    max_memory_mb: int
    name: str


class RelayPipelinesApprovePipelineGateRequest(TypedDict, total=False):
    approver_data: dict[str, Any]


class _RelayPipelinesCreatePipelineDefinitionRequestRequired(TypedDict):
    endpoint_url: str
    name: str


class RelayPipelinesCreatePipelineDefinitionRequest(
    _RelayPipelinesCreatePipelineDefinitionRequestRequired,
    total=False,
):
    description: str
    reference_id: str
    retry_policy: dict[str, Any]
    timeout_seconds: int


class RelayPipelinesReadPipelineDefinitionsCountQuery(TypedDict, total=False):
    status: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayPipelinesReadPipelineDefinitionsQuery(TypedDict, total=False):
    status: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayPipelinesReadPipelineRunsCountQuery(TypedDict, total=False):
    pipeline_id: str
    status: str
    reference_id: str
    conjoin_request_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayPipelinesReadPipelineRunsQuery(TypedDict, total=False):
    pipeline_id: str
    status: str
    reference_id: str
    conjoin_request_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayPipelinesRejectPipelineGateRequest(TypedDict, total=False):
    reason: str


class RelayPipelinesTriggerPipelineRunRequest(TypedDict, total=False):
    payload: dict[str, Any]
    reference_id: str


class RelayPipelinesUpdatePipelineDefinitionRequest(TypedDict, total=False):
    description: str
    endpoint_url: str
    name: str
    retry_policy: dict[str, Any]
    timeout_seconds: int


class _RelayQueuesBatchEnqueueTasksRequestRequired(TypedDict):
    tasks: Sequence[dict[str, Any]]


class RelayQueuesBatchEnqueueTasksRequest(
    _RelayQueuesBatchEnqueueTasksRequestRequired,
    total=False,
):
    defaults: dict[str, Any]


class _RelayQueuesCreateQueueDefinitionRequestRequired(TypedDict):
    name: str
    target_url: str


class RelayQueuesCreateQueueDefinitionRequest(
    _RelayQueuesCreateQueueDefinitionRequestRequired,
    total=False,
):
    default_delay_seconds: int
    description: str
    dlq_enabled: bool
    dlq_retention_days: int
    headers: dict[str, str] | None
    max_concurrent_deliveries: int | None
    max_retries: int
    on_failure: Sequence[dict[str, Any]] | None
    on_success: Sequence[dict[str, Any]] | None
    priority: int
    rate_limit_per_minute: int
    reference_id: str
    response_forward_fields: Sequence[str] | None
    retry_backoff_base_seconds: int
    retry_backoff_strategy: str
    status_batch_interval_seconds: int
    status_batch_max_size: int
    status_broadcast_channel_id: str | None
    status_broadcast_enabled: bool
    status_event_channel_id: str | None
    status_events_enabled: bool
    task_retention_days: int
    timeout_seconds: int
    visibility_timeout_seconds: int


class RelayQueuesEnqueueTaskRequest(TypedDict, total=False):
    delay_seconds: int
    headers: dict[str, str] | None
    payload: dict[str, Any]
    reference_id: str
    scheduled_for: dict[str, Any]
    target_url: str


class RelayQueuesPurgeQueueTasksRequest(TypedDict, total=False):
    status: str


class RelayQueuesReadDeadLetterTasksCountQuery(TypedDict, total=False):
    reference_id: str
    conjoin_request_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayQueuesReadDeadLetterTasksQuery(TypedDict, total=False):
    reference_id: str
    conjoin_request_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayQueuesReadQueueDefinitionsCountQuery(TypedDict, total=False):
    status: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayQueuesReadQueueDefinitionsQuery(TypedDict, total=False):
    status: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayQueuesReadQueueTasksCountQuery(TypedDict, total=False):
    status: str
    task_ids: str
    reference_id: str
    conjoin_request_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayQueuesReadQueueTasksQuery(TypedDict, total=False):
    status: str
    task_ids: str
    reference_id: str
    conjoin_request_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelayQueuesUpdateQueueDefinitionRequest(TypedDict, total=False):
    default_delay_seconds: int
    description: str
    dlq_enabled: bool
    dlq_retention_days: int
    headers: dict[str, str] | None
    max_concurrent_deliveries: int | None
    max_retries: int
    name: str
    on_failure: Sequence[dict[str, Any]] | None
    on_success: Sequence[dict[str, Any]] | None
    priority: int
    rate_limit_per_minute: int | None
    response_forward_fields: Sequence[str] | None
    retry_backoff_base_seconds: int
    retry_backoff_strategy: str
    status_batch_interval_seconds: int
    status_batch_max_size: int
    status_broadcast_channel_id: str | None
    status_broadcast_enabled: bool
    status_event_channel_id: str | None
    status_events_enabled: bool
    target_url: str
    task_retention_days: int
    timeout_seconds: int
    visibility_timeout_seconds: int


class _RelaySchedulerCreateDefinitionRequestRequired(TypedDict):
    name: str
    schedule_type: str
    target_url: str


class RelaySchedulerCreateDefinitionRequest(
    _RelaySchedulerCreateDefinitionRequestRequired,
    total=False,
):
    cron_expression: str
    description: str
    dlq_enabled: bool
    dlq_retention_days: int
    grace_window_seconds: int
    headers: dict[str, str] | None
    max_retries: int
    on_failure: Sequence[dict[str, Any]] | None
    on_success: Sequence[dict[str, Any]] | None
    one_time_at: str
    payload: dict[str, Any]
    reference_id: str
    retry_backoff_base_seconds: int
    retry_backoff_strategy: str
    timeout_seconds: int
    timezone: str


class RelaySchedulerReadDeadLetterEntriesCountQuery(TypedDict, total=False):
    replayed: Any
    reference_id: str
    conjoin_request_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelaySchedulerReadDeadLetterEntriesQuery(TypedDict, total=False):
    replayed: Any
    reference_id: str
    conjoin_request_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelaySchedulerReadDefinitionsCountQuery(TypedDict, total=False):
    status: str
    schedule_type: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelaySchedulerReadDefinitionsQuery(TypedDict, total=False):
    status: str
    schedule_type: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelaySchedulerReadExecutionsCountQuery(TypedDict, total=False):
    status: str
    reference_id: str
    conjoin_request_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelaySchedulerReadExecutionsQuery(TypedDict, total=False):
    status: str
    reference_id: str
    conjoin_request_id: str
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class RelaySchedulerUpdateDefinitionRequest(TypedDict, total=False):
    cron_expression: str
    description: str
    dlq_enabled: bool
    dlq_retention_days: int | None
    grace_window_seconds: int
    headers: dict[str, str] | None
    max_retries: int
    name: str
    on_failure: Sequence[dict[str, Any]] | None
    on_success: Sequence[dict[str, Any]] | None
    one_time_at: str
    payload: dict[str, Any]
    retry_backoff_base_seconds: int
    retry_backoff_strategy: str
    target_url: str
    timeout_seconds: int
    timezone: str


class _RelaySearchAutoSuggestRequestRequired(TypedDict):
    prefix: str


class RelaySearchAutoSuggestRequest(_RelaySearchAutoSuggestRequestRequired, total=False):
    field: str
    limit: int


class _RelaySearchCreateIndexRequestRequired(TypedDict):
    name: str
    schema_definition: dict[str, Any]


class RelaySearchCreateIndexRequest(_RelaySearchCreateIndexRequestRequired, total=False):
    description: str
    reference_id: str


class RelaySearchIndexDocumentBatchRequest(TypedDict):
    documents: Sequence[dict[str, Any]]


class _RelaySearchIndexDocumentRequestRequired(TypedDict):
    content: dict[str, Any]


class RelaySearchIndexDocumentRequest(_RelaySearchIndexDocumentRequestRequired, total=False):
    reference_id: str
    search_metadata: dict[str, Any]


class RelaySearchReadIndexesQuery(TypedDict, total=False):
    status: str
    reference_id: str
    date_created: dict[str, Any]
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class _RelaySearchSearchQueryRequestRequired(TypedDict):
    term: str


class RelaySearchSearchQueryRequest(_RelaySearchSearchQueryRequestRequired, total=False):
    filters: dict[str, Any]
    fuzzy: bool
    limit: int
    offset: int


class RelaySettingsUpdateRequest(TypedDict, total=False):
    events: dict[str, Any]
    pipelines: dict[str, Any]
    queues: dict[str, Any]
    scheduler: dict[str, Any]


class StorageContainerChangeClassRequest(TypedDict):
    storage_class: str


class _StorageContainerCreateRequestRequired(TypedDict):
    name: str
    region: str
    storage_class: str


class StorageContainerCreateRequest(_StorageContainerCreateRequestRequired, total=False):
    is_public: bool
    lifecycle_policy: dict[str, Any]


class StorageContainerListQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any
    is_archived: bool
    query: dict[str, Any]


class StorageContainerRequestDeletionQuery(TypedDict, total=False):
    grace_period_days: Any


class StorageContainerUpdateLifecyclePolicyRequest(TypedDict, total=False):
    delete_after_days: int


class StorageContainerUpdateSettingsRequest(TypedDict, total=False):
    acl: dict[str, Any]
    image_optimization: dict[str, Any]


class _StorageContainerUpdateTransitionPolicyRequestRequired(TypedDict):
    is_enabled: bool


class StorageContainerUpdateTransitionPolicyRequest(
    _StorageContainerUpdateTransitionPolicyRequestRequired,
    total=False,
):
    rules: Sequence[dict[str, Any]]


class StorageObjectACLGrantObjectAclRequest(TypedDict):
    entries: Sequence[dict[str, Any]]


class StorageObjectACLRevokeObjectAclRequest(TypedDict):
    entries: Sequence[dict[str, Any]]


class StorageObjectACLSetObjectPublicRequest(TypedDict):
    is_public: bool


class StorageObjectCheckDuplicateQuery(TypedDict):
    md5_hash: str


class StorageObjectCreateDownloadSignedUrlRequest(TypedDict):
    path: str


class _StorageObjectCreateUploadSignedUrlRequestRequired(TypedDict):
    content_type: str
    file_size: int
    path: str


class StorageObjectCreateUploadSignedUrlRequest(
    _StorageObjectCreateUploadSignedUrlRequestRequired,
    total=False,
):
    expires_in_minutes: int


class StorageObjectListQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    has_label: str
    has_metadata_key: str
    label: str
    name: str
    description: str
    container_id: str
    object_id: str
    is_archived: bool
    is_public: bool
    sync_status: Any
    limit: Any
    sort: dict[str, str]
    date_updated: str | None
    date_created: str | None


class StorageObjectListVersionsQuery(TypedDict, total=False):
    cursor: dict[str, Any]
    sort: dict[str, str]
    limit: Any


class StorageObjectRestoreVersionRequest(TypedDict):
    version_id: str
