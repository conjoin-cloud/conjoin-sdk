package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListFirstPartyConnectionsQuery struct {
	Identity *string `json:"identity,omitzero"`
}

type ListFirstPartyConnectionsResponseConnectionsItem struct {
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

type ListFirstPartyConnectionsResponse struct {
	Connections []ListFirstPartyConnectionsResponseConnectionsItem `json:"connections"`
}

type UpsertFirstPartyConnectionRequestConfigurationVerificationCode struct {
	IsEnabled bool `json:"is_enabled"`
}

type UpsertFirstPartyConnectionRequestConfigurationMagicLink struct {
	IsEnabled       bool `json:"is_enabled"`
	ForceSameDevice bool `json:"force_same_device"`
}

type UpsertFirstPartyConnectionRequestConfigurationRules struct {
	RequireUppercase bool  `json:"require_uppercase"`
	RequireLowercase bool  `json:"require_lowercase"`
	RequireNumbers   bool  `json:"require_numbers"`
	RequireSymbols   bool  `json:"require_symbols"`
	MinLength        int64 `json:"min_length"`
	MaxLength        int64 `json:"max_length"`
}

type UpsertFirstPartyConnectionRequestConfigurationOauth2Endpoints struct {
	Authorization string `json:"authorization"`
	Token         string `json:"token"`
	JWKSURI       string `json:"jwks_uri"`
}

type UpsertFirstPartyConnectionRequestConfigurationOauth2 struct {
	ClientSecret string                                                        `json:"client_secret"`
	Endpoints    UpsertFirstPartyConnectionRequestConfigurationOauth2Endpoints `json:"endpoints"`
	Pkce         *bool                                                         `json:"pkce"`
}

type UpsertFirstPartyConnectionRequestConfigurationOIDC struct {
	Issuer string `json:"issuer"`
}

type UpsertFirstPartyConnectionRequestConfiguration struct {
	IsEnabled        *bool                                                           `json:"is_enabled,omitzero"`
	VerificationCode *UpsertFirstPartyConnectionRequestConfigurationVerificationCode `json:"verification_code,omitzero"`
	MagicLink        *UpsertFirstPartyConnectionRequestConfigurationMagicLink        `json:"magic_link,omitzero"`
	Rules            *UpsertFirstPartyConnectionRequestConfigurationRules            `json:"rules,omitzero"`
	EnhancedSecurity *UpsertFirstPartyConnectionRequestConfigurationVerificationCode `json:"enhanced_security,omitzero"`
	ClientID         *string                                                         `json:"client_id,omitzero"`
	Scopes           []string                                                        `json:"scopes,omitzero"`
	Oauth2           *UpsertFirstPartyConnectionRequestConfigurationOauth2           `json:"oauth2,omitzero"`
	OIDC             *UpsertFirstPartyConnectionRequestConfigurationOIDC             `json:"oidc,omitzero"`
	ClientSecret     *string                                                         `json:"client_secret,omitzero"`
	Endpoints        *UpsertFirstPartyConnectionRequestConfigurationOauth2Endpoints  `json:"endpoints,omitzero"`
	Pkce             conjoin.Nullable[bool]                                          `json:"pkce,omitzero"`
	Issuer           *string                                                         `json:"issuer,omitzero"`
}

type UpsertFirstPartyConnectionRequest struct {
	Identity      string                                         `json:"identity"`
	Status        *string                                        `json:"status,omitzero"`
	Name          conjoin.Nullable[string]                       `json:"name,omitzero"`
	Configuration UpsertFirstPartyConnectionRequestConfiguration `json:"configuration"`
}

type UpsertFirstPartyConnectionResponse = ListFirstPartyConnectionsResponseConnectionsItem
