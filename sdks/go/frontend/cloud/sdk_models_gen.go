package cloud

type ReadSdkSettingsResponseAuth struct {
	Domain        string   `json:"domain"`
	SignInMethods []string `json:"sign_in_methods"`
	MFAEnabled    bool     `json:"mfa_enabled"`
	SignUpEnabled bool     `json:"sign_up_enabled"`
}

type ReadSdkSettingsResponseRelay struct {
	URL string `json:"url"`
}

type ReadSdkSettingsResponse struct {
	ProjectID   string                       `json:"project_id"`
	Environment string                       `json:"environment"`
	APIURL      string                       `json:"api_url"`
	Branding    map[string]any               `json:"branding"`
	Auth        *ReadSdkSettingsResponseAuth `json:"auth"`
	Relay       ReadSdkSettingsResponseRelay `json:"relay"`
}
