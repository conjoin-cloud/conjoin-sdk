package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type OidcLogoutRequest struct {
	EndSessionEndpoint    string  `json:"end_session_endpoint"`
	IDTokenHint           *string `json:"id_token_hint,omitzero"`
	PostLogoutRedirectURI *string `json:"post_logout_redirect_uri,omitzero"`
}

type OidcLogoutResponse struct {
	LogoutURL         conjoin.Nullable[string] `json:"logout_url,omitzero"`
	LogoutRequestXML  *string                  `json:"logout_request_xml,omitzero"`
	LogoutResponseXML *string                  `json:"logout_response_xml,omitzero"`
	Status            *string                  `json:"status,omitzero"`
}

type SamlSpLogoutRequest struct {
	ConnectionID string  `json:"connection_id"`
	NameID       string  `json:"name_id"`
	SessionIndex *string `json:"session_index,omitzero"`
	RelayState   *string `json:"relay_state,omitzero"`
}

type SamlSpLogoutResponse = OidcLogoutResponse

type SamlIdpLogoutRequest struct {
	QueryString string `json:"query_string"`
}

type SamlIdpLogoutResponse = OidcLogoutResponse
