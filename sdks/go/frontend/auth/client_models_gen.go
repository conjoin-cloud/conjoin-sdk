package auth

type GetOidcDiscoveryResponse struct {
	Issuer                           string   `json:"issuer"`
	AuthorizationEndpoint            string   `json:"authorization_endpoint"`
	TokenEndpoint                    string   `json:"token_endpoint"`
	UserinfoEndpoint                 string   `json:"userinfo_endpoint"`
	EndSessionEndpoint               string   `json:"end_session_endpoint"`
	JWKSURI                          string   `json:"jwks_uri"`
	ResponseTypesSupported           []string `json:"response_types_supported"`
	SubjectTypesSupported            []string `json:"subject_types_supported"`
	IDTokenSigningAlgValuesSupported []string `json:"id_token_signing_alg_values_supported"`
	ScopesSupported                  []string `json:"scopes_supported"`
	ClaimsSupported                  []string `json:"claims_supported"`
}

type ProcessHandshakeResponse struct {
	SessionID             string  `json:"session_id"`
	AccountID             string  `json:"account_id"`
	Iat                   float64 `json:"iat"`
	Exp                   float64 `json:"exp"`
	AccessTokenTTLSeconds float64 `json:"access_token_ttl_seconds"`
}

type ProcessLogoutResponse struct {
	Success bool `json:"success"`
}

type GetJwksResponseKeysItem struct {
	Kty string  `json:"kty"`
	Use *string `json:"use,omitzero"`
	Kid *string `json:"kid,omitzero"`
	Alg *string `json:"alg,omitzero"`
	N   *string `json:"n,omitzero"`
	E   *string `json:"e,omitzero"`
}

type GetJwksResponse struct {
	Keys []GetJwksResponseKeysItem `json:"keys"`
}
