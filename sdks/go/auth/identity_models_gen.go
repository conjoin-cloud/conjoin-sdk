package auth

type DiscoverAccountRequestIdentifiersConnectedIdentity struct {
	Type   string `json:"type"`
	UserID string `json:"user_id"`
}

type DiscoverAccountRequestIdentifiers struct {
	Email             *string                                             `json:"email,omitzero"`
	Phone             *string                                             `json:"phone,omitzero"`
	ConnectedIdentity *DiscoverAccountRequestIdentifiersConnectedIdentity `json:"connected_identity,omitzero"`
	OrgDomain         *string                                             `json:"org_domain,omitzero"`
}

type DiscoverAccountRequest struct {
	Identifiers DiscoverAccountRequestIdentifiers `json:"identifiers"`
}

type DiscoverAccountResponse struct {
	AccountID *string `json:"account_id"`
	Reason    *string `json:"reason,omitzero"`
}

type LinkIdentityRequestIdentity struct {
	Type   string   `json:"type"`
	UserID string   `json:"user_id"`
	Email  *string  `json:"email,omitzero"`
	Phone  *string  `json:"phone,omitzero"`
	Scopes []string `json:"scopes,omitzero"`
}

type LinkIdentityRequest struct {
	Identity LinkIdentityRequestIdentity `json:"identity"`
}

type LinkIdentityResponse struct {
	ResolvedAccountID string `json:"resolved_account_id"`
}

type UnlinkIdentityRequest struct {
	Identity DiscoverAccountRequestIdentifiersConnectedIdentity `json:"identity"`
}
