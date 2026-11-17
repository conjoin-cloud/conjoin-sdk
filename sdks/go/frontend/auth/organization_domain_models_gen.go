package auth

type VerifySsoPortalDomainRequest struct {
	Domain string `json:"domain"`
}

type VerifySsoPortalDomainResponseVerification struct {
	Status     string  `json:"status"`
	VerifiedAt *string `json:"verified_at"`
	ExpiresAt  *string `json:"expires_at"`
}

type VerifySsoPortalDomainResponseRecheck struct {
	GraceStartedAt  string  `json:"grace_started_at"`
	FailureWarnedAt *string `json:"failure_warned_at"`
	ReminderSentAt  *string `json:"reminder_sent_at"`
}

type VerifySsoPortalDomainResponse struct {
	OrganizationDomainID    string                                    `json:"organization_domain_id"`
	ConjoinAccountID        string                                    `json:"conjoin_account_id"`
	ConjoinProjectID        string                                    `json:"conjoin_project_id"`
	AppID                   string                                    `json:"app_id"`
	LiveMode                bool                                      `json:"live_mode"`
	OrganizationID          string                                    `json:"organization_id"`
	Domain                  string                                    `json:"domain"`
	VerificationHostname    string                                    `json:"verification_hostname"`
	VerificationToken       string                                    `json:"verification_token"`
	VerificationRecordValue string                                    `json:"verification_record_value"`
	Verification            VerifySsoPortalDomainResponseVerification `json:"verification"`
	LastCheckedAt           *string                                   `json:"last_checked_at"`
	Recheck                 *VerifySsoPortalDomainResponseRecheck     `json:"recheck"`
	DateCreated             string                                    `json:"date_created"`
	DateUpdated             string                                    `json:"date_updated"`
}
