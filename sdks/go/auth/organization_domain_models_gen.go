package auth

type ListOrganizationDomainsQuery struct {
	Domain *string                     `json:"domain,omitzero"`
	Status *string                     `json:"status,omitzero"`
	Cursor *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort   map[string]string           `json:"sort,omitzero"`
	Limit  any                         `json:"limit,omitzero"`
}

type ListOrganizationDomainsItemVerification struct {
	Status     string  `json:"status"`
	VerifiedAt *string `json:"verified_at"`
	ExpiresAt  *string `json:"expires_at"`
}

type ListOrganizationDomainsItemRecheck struct {
	GraceStartedAt  string  `json:"grace_started_at"`
	FailureWarnedAt *string `json:"failure_warned_at"`
	ReminderSentAt  *string `json:"reminder_sent_at"`
}

type ListOrganizationDomainsItem struct {
	OrganizationDomainID    string                                  `json:"organization_domain_id"`
	ConjoinAccountID        string                                  `json:"conjoin_account_id"`
	ConjoinProjectID        string                                  `json:"conjoin_project_id"`
	AppID                   string                                  `json:"app_id"`
	LiveMode                bool                                    `json:"live_mode"`
	OrganizationID          string                                  `json:"organization_id"`
	Domain                  string                                  `json:"domain"`
	VerificationHostname    string                                  `json:"verification_hostname"`
	VerificationToken       string                                  `json:"verification_token"`
	VerificationRecordValue string                                  `json:"verification_record_value"`
	Verification            ListOrganizationDomainsItemVerification `json:"verification"`
	LastCheckedAt           *string                                 `json:"last_checked_at"`
	Recheck                 *ListOrganizationDomainsItemRecheck     `json:"recheck"`
	DateCreated             string                                  `json:"date_created"`
	DateUpdated             string                                  `json:"date_updated"`
}

type CreateOrganizationDomainRequest = AddGuardTrustedDomainRequest

type CreateOrganizationDomainResponse = ListOrganizationDomainsItem

type ListOrganizationDomainsCountQuery = ListOrganizationDomainsQuery

type ListOrganizationDomainsCountResponse = ListCredentialsCountResponse

type VerifyOrganizationDomainResponse = ListOrganizationDomainsItem

type DeleteOrganizationDomainResponse = DeleteEnterpriseConnectionResponse
