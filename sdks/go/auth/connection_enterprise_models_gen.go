package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListEnterpriseConnectionsQuery struct {
	Identity *string                     `json:"identity,omitzero"`
	Status   *string                     `json:"status,omitzero"`
	Cursor   *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort     map[string]string           `json:"sort,omitzero"`
	Limit    any                         `json:"limit,omitzero"`
}

type ListEnterpriseConnectionsItem = ListFirstPartyConnectionsResponseConnectionsItem

type CreateEnterpriseConnectionRequestConfigurationDomainRouting struct {
	Enabled              bool     `json:"enabled"`
	Domains              []string `json:"domains"`
	AllowExternalDomains bool     `json:"allow_external_domains"`
}

type CreateEnterpriseConnectionRequestConfigurationJitProvisioningAttributeMappings struct {
	FirstName        string            `json:"first_name"`
	LastName         string            `json:"last_name"`
	Email            string            `json:"email"`
	Picture          *string           `json:"picture,omitzero"`
	CustomAttributes map[string]string `json:"custom_attributes"`
}

type CreateEnterpriseConnectionRequestConfigurationJitProvisioning struct {
	Enabled           bool                                                                           `json:"enabled"`
	UpdateOnLogin     bool                                                                           `json:"update_on_login"`
	AttributeMappings CreateEnterpriseConnectionRequestConfigurationJitProvisioningAttributeMappings `json:"attribute_mappings"`
}

type CreateEnterpriseConnectionRequestConfigurationRoleMapping struct {
	Enabled       bool              `json:"enabled"`
	RoleMappings  map[string]string `json:"role_mappings"`
	DefaultRole   *string           `json:"default_role"`
	RoleAttribute string            `json:"role_attribute"`
}

type CreateEnterpriseConnectionRequestConfigurationSAMLConfig struct {
	EntityID                   string  `json:"entity_id"`
	SSOURL                     string  `json:"sso_url"`
	SLOURL                     *string `json:"slo_url,omitzero"`
	Certificate                string  `json:"certificate"`
	RequestBinding             string  `json:"request_binding"`
	ResponseBinding            string  `json:"response_binding"`
	SignRequests               bool    `json:"sign_requests"`
	RequireEncryptedAssertions bool    `json:"require_encrypted_assertions"`
	NameIDFormat               string  `json:"name_id_format"`
}

type CreateEnterpriseConnectionRequestConfigurationOIDCConfig struct {
	Issuer               string            `json:"issuer"`
	ClientID             string            `json:"client_id"`
	ClientSecret         string            `json:"client_secret"`
	Scopes               []string          `json:"scopes"`
	DiscoveryEndpoint    *string           `json:"discovery_endpoint,omitzero"`
	UsePkce              bool              `json:"use_pkce"`
	AdditionalParameters map[string]string `json:"additional_parameters"`
}

type CreateEnterpriseConnectionRequestConfigurationCustomConfig struct {
	AuthEndpoint     string            `json:"auth_endpoint"`
	TokenEndpoint    string            `json:"token_endpoint"`
	UserinfoEndpoint string            `json:"userinfo_endpoint"`
	ClientSecret     *string           `json:"client_secret,omitzero"`
	AuthMethod       string            `json:"auth_method"`
	CustomHeaders    map[string]string `json:"custom_headers"`
	CustomParameters map[string]string `json:"custom_parameters"`
	ResponseFormat   string            `json:"response_format"`
}

type CreateEnterpriseConnectionRequestConfiguration struct {
	Name                                *string                                                        `json:"name,omitzero"`
	Description                         *string                                                        `json:"description,omitzero"`
	DomainRouting                       *CreateEnterpriseConnectionRequestConfigurationDomainRouting   `json:"domain_routing,omitzero"`
	JitProvisioning                     *CreateEnterpriseConnectionRequestConfigurationJitProvisioning `json:"jit_provisioning,omitzero"`
	RoleMapping                         *CreateEnterpriseConnectionRequestConfigurationRoleMapping     `json:"role_mapping,omitzero"`
	SessionTimeout                      conjoin.Nullable[int64]                                        `json:"session_timeout,omitzero"`
	RequireReauthForSensitiveOperations *bool                                                          `json:"require_reauth_for_sensitive_operations,omitzero"`
	SAMLConfig                          *CreateEnterpriseConnectionRequestConfigurationSAMLConfig      `json:"saml_config,omitzero"`
	OIDCConfig                          *CreateEnterpriseConnectionRequestConfigurationOIDCConfig      `json:"oidc_config,omitzero"`
	CustomConfig                        *CreateEnterpriseConnectionRequestConfigurationCustomConfig    `json:"custom_config,omitzero"`
}

type CreateEnterpriseConnectionRequest struct {
	Protocol      *string                                         `json:"protocol,omitzero"`
	Name          *string                                         `json:"name,omitzero"`
	Configuration *CreateEnterpriseConnectionRequestConfiguration `json:"configuration,omitzero"`
}

type CreateEnterpriseConnectionResponse = ListFirstPartyConnectionsResponseConnectionsItem

type ListEnterpriseConnectionsCountQuery = ListEnterpriseConnectionsQuery

type ListEnterpriseConnectionsCountResponse = ListCredentialsCountResponse

type ReadEnterpriseConnectionResponse = ListFirstPartyConnectionsResponseConnectionsItem

type UpdateEnterpriseConnectionRequest struct {
	Protocol      any                                             `json:"protocol,omitzero"`
	Name          conjoin.Nullable[string]                        `json:"name,omitzero"`
	Configuration *CreateEnterpriseConnectionRequestConfiguration `json:"configuration,omitzero"`
}

type UpdateEnterpriseConnectionResponse = ListFirstPartyConnectionsResponseConnectionsItem

type DeleteEnterpriseConnectionResponse struct {
	Deleted bool `json:"deleted"`
}

type EnableEnterpriseConnectionResponse = ListFirstPartyConnectionsResponseConnectionsItem

type DisableEnterpriseConnectionResponse = ListFirstPartyConnectionsResponseConnectionsItem

type RotateEnterpriseConnectionSigningKeyResponseSigningKeysItem struct {
	CertificateID  string `json:"certificate_id"`
	Status         string `json:"status"`
	CertificatePem string `json:"certificate_pem"`
	Fingerprint    string `json:"fingerprint"`
	ExpiresAt      string `json:"expires_at"`
	DateCreated    string `json:"date_created"`
}

type RotateEnterpriseConnectionSigningKeyResponse struct {
	SigningKeys []RotateEnterpriseConnectionSigningKeyResponseSigningKeysItem `json:"signing_keys"`
}

type ActivateEnterpriseConnectionSigningKeyResponse = RotateEnterpriseConnectionSigningKeyResponse

type CancelEnterpriseConnectionSigningKeyResponse = RotateEnterpriseConnectionSigningKeyResponse

type RevokeEnterpriseConnectionSigningKeyResponse = RotateEnterpriseConnectionSigningKeyResponse

type ReadEnterpriseProviderSettingsResponse struct {
	Protocol            *string                                                       `json:"protocol,omitzero"`
	AcsURL              *string                                                       `json:"acs_url,omitzero"`
	SpEntityID          *string                                                       `json:"sp_entity_id,omitzero"`
	SlsURL              *string                                                       `json:"sls_url,omitzero"`
	SpMetadataXML       *string                                                       `json:"sp_metadata_xml,omitzero"`
	SigningKeys         []RotateEnterpriseConnectionSigningKeyResponseSigningKeysItem `json:"signing_keys,omitzero"`
	RedirectURIGuidance *string                                                       `json:"redirect_uri_guidance,omitzero"`
}

type ImportEnterpriseSamlMetadataRequest struct {
	Source      *string                                                   `json:"source,omitzero"`
	MetadataURL *string                                                   `json:"metadata_url,omitzero"`
	SAMLConfig  *CreateEnterpriseConnectionRequestConfigurationSAMLConfig `json:"saml_config,omitzero"`
}

type ImportEnterpriseSamlMetadataResponse = ListFirstPartyConnectionsResponseConnectionsItem

type SyncEnterpriseSamlMetadataRequest struct {
	MetadataURL string `json:"metadata_url"`
}

type SyncEnterpriseSamlMetadataResponse = ListFirstPartyConnectionsResponseConnectionsItem
