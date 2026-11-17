package auth

type ReadSsoPortalContextResponseProvidersItemRequiredFieldsItem struct {
	Key        string `json:"key"`
	Label      string `json:"label"`
	IsRequired bool   `json:"is_required"`
	IsSecret   bool   `json:"is_secret"`
}

type ReadSsoPortalContextResponseProvidersItem struct {
	ProviderKey    string                                                        `json:"provider_key"`
	Label          string                                                        `json:"label"`
	DisplayName    string                                                        `json:"display_name"`
	Protocol       string                                                        `json:"protocol"`
	LogoReference  string                                                        `json:"logo_reference"`
	SetupGuideSlug string                                                        `json:"setup_guide_slug"`
	RequiredFields []ReadSsoPortalContextResponseProvidersItemRequiredFieldsItem `json:"required_fields"`
}

type ReadSsoPortalContextResponse struct {
	OrganizationID            string                                      `json:"organization_id"`
	AllowedProviders          []string                                    `json:"allowed_providers"`
	SetupIntents              []string                                    `json:"setup_intents"`
	RequireDomainVerification bool                                        `json:"require_domain_verification"`
	Providers                 []ReadSsoPortalContextResponseProvidersItem `json:"providers"`
}

type ReadSsoPortalCatalogResponse struct {
	Providers []ReadSsoPortalContextResponseProvidersItem `json:"providers"`
}

type StartSsoPortalTestRequest struct {
	ConnectionID string `json:"connection_id"`
}

type StartSsoPortalTestResponse struct {
	RedirectURL string `json:"redirect_url"`
}
