package auth

type StartRecoveryResponse struct {
	Status        string  `json:"status"`
	RecoveryToken *string `json:"recovery_token,omitzero"`
	ExpiresAt     *string `json:"expires_at,omitzero"`
	AccountID     *string `json:"account_id,omitzero"`
}

type VerifyRecoveryRequest struct {
	Token string `json:"token"`
}

type VerifyRecoveryResponse = StartRecoveryResponse

type CompleteRecoveryRequest struct {
	Token                   string   `json:"token"`
	CredentialKindsToRemove []string `json:"credential_kinds_to_remove,omitzero"`
}

type CompleteRecoveryResponse = StartRecoveryResponse

type AdminResetAccountResponse struct {
	RemovedCredentialCount float64 `json:"removed_credential_count"`
}
