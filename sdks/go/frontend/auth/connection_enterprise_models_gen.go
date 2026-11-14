package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ConfigureSsoPortalConnectionRequestConfigurationDomainRouting struct {
	Enabled              bool     `json:"enabled"`
	Domains              []string `json:"domains"`
	AllowExternalDomains bool     `json:"allow_external_domains"`
}

type ConfigureSsoPortalConnectionRequestConfigurationJitProvisioningAttributeMappings struct {
	FirstName        string            `json:"first_name"`
	LastName         string            `json:"last_name"`
	Email            string            `json:"email"`
	Picture          *string           `json:"picture,omitzero"`
	CustomAttributes map[string]string `json:"custom_attributes"`
}

type ConfigureSsoPortalConnectionRequestConfigurationJitProvisioning struct {
	Enabled           bool                                                                             `json:"enabled"`
	UpdateOnLogin     bool                                                                             `json:"update_on_login"`
	AttributeMappings ConfigureSsoPortalConnectionRequestConfigurationJitProvisioningAttributeMappings `json:"attribute_mappings"`
}

type ConfigureSsoPortalConnectionRequestConfigurationRoleMapping struct {
	Enabled       bool              `json:"enabled"`
	RoleMappings  map[string]string `json:"role_mappings"`
	DefaultRole   *string           `json:"default_role"`
	RoleAttribute string            `json:"role_attribute"`
}

type ConfigureSsoPortalConnectionRequestConfigurationSAMLConfig struct {
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

type ConfigureSsoPortalConnectionRequestConfigurationOIDCConfig struct {
	Issuer               string            `json:"issuer"`
	ClientID             string            `json:"client_id"`
	ClientSecret         string            `json:"client_secret"`
	Scopes               []string          `json:"scopes"`
	DiscoveryEndpoint    *string           `json:"discovery_endpoint,omitzero"`
	UsePkce              bool              `json:"use_pkce"`
	AdditionalParameters map[string]string `json:"additional_parameters"`
}

type ConfigureSsoPortalConnectionRequestConfigurationCustomConfig struct {
	AuthEndpoint     string            `json:"auth_endpoint"`
	TokenEndpoint    string            `json:"token_endpoint"`
	UserinfoEndpoint string            `json:"userinfo_endpoint"`
	ClientSecret     *string           `json:"client_secret,omitzero"`
	AuthMethod       string            `json:"auth_method"`
	CustomHeaders    map[string]string `json:"custom_headers"`
	CustomParameters map[string]string `json:"custom_parameters"`
	ResponseFormat   string            `json:"response_format"`
}

type ConfigureSsoPortalConnectionRequestConfiguration struct {
	Name                                *string                                                          `json:"name,omitzero"`
	Description                         *string                                                          `json:"description,omitzero"`
	DomainRouting                       *ConfigureSsoPortalConnectionRequestConfigurationDomainRouting   `json:"domain_routing,omitzero"`
	JitProvisioning                     *ConfigureSsoPortalConnectionRequestConfigurationJitProvisioning `json:"jit_provisioning,omitzero"`
	RoleMapping                         *ConfigureSsoPortalConnectionRequestConfigurationRoleMapping     `json:"role_mapping,omitzero"`
	SessionTimeout                      conjoin.Nullable[int64]                                          `json:"session_timeout,omitzero"`
	RequireReauthForSensitiveOperations *bool                                                            `json:"require_reauth_for_sensitive_operations,omitzero"`
	SAMLConfig                          *ConfigureSsoPortalConnectionRequestConfigurationSAMLConfig      `json:"saml_config,omitzero"`
	OIDCConfig                          *ConfigureSsoPortalConnectionRequestConfigurationOIDCConfig      `json:"oidc_config,omitzero"`
	CustomConfig                        *ConfigureSsoPortalConnectionRequestConfigurationCustomConfig    `json:"custom_config,omitzero"`
}

type ConfigureSsoPortalConnectionRequest struct {
	Protocol      *string                                           `json:"protocol,omitzero"`
	Name          *string                                           `json:"name,omitzero"`
	Configuration *ConfigureSsoPortalConnectionRequestConfiguration `json:"configuration,omitzero"`
}

type ConfigureSsoPortalConnectionResponse struct {
	ConnectionID     string         `json:"connection_id"`
	ConjoinAccountID string         `json:"conjoin_account_id"`
	ConjoinProjectID string         `json:"conjoin_project_id"`
	AppID            string         `json:"app_id"`
	LiveMode         bool           `json:"live_mode"`
	OrganizationID   *string        `json:"organization_id"`
	Identity         string         `json:"identity"`
	Status           string         `json:"status"`
	Name             *string        `json:"name"`
	IsEnterprise     bool           `json:"is_enterprise"`
	Configuration    map[string]any `json:"configuration"`
	DateCreated      string         `json:"date_created"`
	DateUpdated      string         `json:"date_updated"`
}

type UpdateSsoPortalConnectionRequest struct {
	Protocol      any                                               `json:"protocol,omitzero"`
	Name          conjoin.Nullable[string]                          `json:"name,omitzero"`
	Configuration *ConfigureSsoPortalConnectionRequestConfiguration `json:"configuration,omitzero"`
}

type UpdateSsoPortalConnectionResponse = ConfigureSsoPortalConnectionResponse

type ImportSsoPortalMetadataRequest struct {
	Source      *string                                                     `json:"source,omitzero"`
	MetadataURL *string                                                     `json:"metadata_url,omitzero"`
	SAMLConfig  *ConfigureSsoPortalConnectionRequestConfigurationSAMLConfig `json:"saml_config,omitzero"`
}

type ImportSsoPortalMetadataResponse = ConfigureSsoPortalConnectionResponse

type ReadSsoPortalProviderConfigResponseSigningKeysItem struct {
	CertificateID  string `json:"certificate_id"`
	Status         string `json:"status"`
	CertificatePem string `json:"certificate_pem"`
	Fingerprint    string `json:"fingerprint"`
	ExpiresAt      string `json:"expires_at"`
	DateCreated    string `json:"date_created"`
}

type ReadSsoPortalProviderConfigResponse struct {
	Protocol            *string                                              `json:"protocol,omitzero"`
	AcsURL              *string                                              `json:"acs_url,omitzero"`
	SpEntityID          *string                                              `json:"sp_entity_id,omitzero"`
	SlsURL              *string                                              `json:"sls_url,omitzero"`
	SpMetadataXML       *string                                              `json:"sp_metadata_xml,omitzero"`
	SigningKeys         []ReadSsoPortalProviderConfigResponseSigningKeysItem `json:"signing_keys,omitzero"`
	RedirectURIGuidance *string                                              `json:"redirect_uri_guidance,omitzero"`
}
