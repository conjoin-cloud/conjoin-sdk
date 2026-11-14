package auth

type DeprovisionAccountRequest struct {
	Policy         *string `json:"policy,omitzero"`
	RevokeSessions *bool   `json:"revoke_sessions,omitzero"`
}

type DeprovisionAccountResponse struct {
	ActionTaken string `json:"action_taken"`
}
