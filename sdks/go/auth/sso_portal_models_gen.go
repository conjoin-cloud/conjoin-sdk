package auth

type ReadSsoPortalSettingsResponse struct {
	AllowedProviders          []string `json:"allowed_providers"`
	SetupIntents              []string `json:"setup_intents"`
	RequireDomainVerification bool     `json:"require_domain_verification"`
}

type UpdateSsoPortalSettingsRequest struct {
	AllowedProviders          []string `json:"allowed_providers,omitzero"`
	SetupIntents              []string `json:"setup_intents,omitzero"`
	RequireDomainVerification *bool    `json:"require_domain_verification,omitzero"`
}

type UpdateSsoPortalSettingsResponse = ReadSsoPortalSettingsResponse

type MintSsoPortalTicketResponseTicket struct {
	TicketID                  string   `json:"ticket_id"`
	ConjoinAccountID          string   `json:"conjoin_account_id"`
	ConjoinProjectID          string   `json:"conjoin_project_id"`
	AppID                     string   `json:"app_id"`
	LiveMode                  bool     `json:"live_mode"`
	OrganizationID            string   `json:"organization_id"`
	Status                    string   `json:"status"`
	AllowedProviders          []string `json:"allowed_providers"`
	SetupIntents              []string `json:"setup_intents"`
	RequireDomainVerification bool     `json:"require_domain_verification"`
	MaxOpens                  float64  `json:"max_opens"`
	OpenCount                 float64  `json:"open_count"`
	ExpiresAt                 string   `json:"expires_at"`
	FirstOpenedAt             *string  `json:"first_opened_at"`
	OpenDeadlineAt            *string  `json:"open_deadline_at"`
	DateCreated               string   `json:"date_created"`
	DateUpdated               string   `json:"date_updated"`
}

type MintSsoPortalTicketResponse struct {
	Ticket    MintSsoPortalTicketResponseTicket `json:"ticket"`
	PortalURL string                            `json:"portal_url"`
	Secret    string                            `json:"secret"`
}

type RevokeSsoPortalTicketResponse struct {
	Revoked bool `json:"revoked"`
}
