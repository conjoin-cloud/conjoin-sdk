package auth

type ReadScimSettingsResponseUserAttributeMapping struct {
	UserNameToPrimaryEmail bool   `json:"userNameToPrimaryEmail"`
	GivenNamePath          string `json:"givenNamePath"`
	FamilyNamePath         string `json:"familyNamePath"`
	EmailsPath             string `json:"emailsPath"`
	PhonesPath             string `json:"phonesPath"`
	PhotoPath              string `json:"photoPath"`
}

type ReadScimSettingsResponseGroupAttributeMapping struct {
	DisplayNamePath string  `json:"displayNamePath"`
	ExternalIDPath  string  `json:"externalIdPath"`
	DescriptionPath *string `json:"descriptionPath,omitzero"`
	ImagePath       *string `json:"imagePath,omitzero"`
}

type ReadScimSettingsResponseRoleMappingRulesItem struct {
	MatchBy string   `json:"matchBy"`
	Pattern string   `json:"pattern"`
	Roles   []string `json:"roles"`
}

type ReadScimSettingsResponseRateLimits struct {
	WritesPerSecond *float64 `json:"writesPerSecond,omitzero"`
	ReadsPerSecond  *float64 `json:"readsPerSecond,omitzero"`
}

type ReadScimSettingsResponseLimits struct {
	MaxGroupMembersApplyBatch *float64 `json:"maxGroupMembersApplyBatch,omitzero"`
}

type ReadScimSettingsResponse struct {
	DeprovisionPolicy     string                                         `json:"deprovisionPolicy"`
	UserAttributeMapping  ReadScimSettingsResponseUserAttributeMapping   `json:"userAttributeMapping"`
	GroupAttributeMapping ReadScimSettingsResponseGroupAttributeMapping  `json:"groupAttributeMapping"`
	RoleMappingRules      []ReadScimSettingsResponseRoleMappingRulesItem `json:"roleMappingRules"`
	RateLimits            *ReadScimSettingsResponseRateLimits            `json:"rateLimits,omitzero"`
	Limits                *ReadScimSettingsResponseLimits                `json:"limits,omitzero"`
	BearerTokenConfigured bool                                           `json:"bearer_token_configured"`
}

type UpdateScimSettingsRequestConfigRateLimits struct {
	WritesPerSecond *int64 `json:"writesPerSecond,omitzero"`
	ReadsPerSecond  *int64 `json:"readsPerSecond,omitzero"`
}

type UpdateScimSettingsRequestConfigLimits struct {
	MaxGroupMembersApplyBatch *int64 `json:"maxGroupMembersApplyBatch,omitzero"`
}

type UpdateScimSettingsRequestConfig struct {
	DeprovisionPolicy     string                                         `json:"deprovisionPolicy"`
	UserAttributeMapping  ReadScimSettingsResponseUserAttributeMapping   `json:"userAttributeMapping"`
	GroupAttributeMapping ReadScimSettingsResponseGroupAttributeMapping  `json:"groupAttributeMapping"`
	RoleMappingRules      []ReadScimSettingsResponseRoleMappingRulesItem `json:"roleMappingRules"`
	RateLimits            *UpdateScimSettingsRequestConfigRateLimits     `json:"rateLimits,omitzero"`
	Limits                *UpdateScimSettingsRequestConfigLimits         `json:"limits,omitzero"`
}

type UpdateScimSettingsRequest struct {
	BearerToken *string                          `json:"bearer_token,omitzero"`
	Config      *UpdateScimSettingsRequestConfig `json:"config,omitzero"`
	Provider    *string                          `json:"provider,omitzero"`
}

type UpdateScimSettingsResponse struct {
	Status string `json:"status"`
}

type SyncScimRolesForMemberResponse = UpdateScimSettingsResponse

type SyncScimRolesForGroupResponse = UpdateScimSettingsResponse

type ReconcileScimUsersRequestUsersItemUserName struct {
	GivenName  *string `json:"givenName,omitzero"`
	FamilyName *string `json:"familyName,omitzero"`
}

type ReconcileScimUsersRequestUsersItemUserEmailsItem struct {
	Value   string  `json:"value"`
	Type    *string `json:"type,omitzero"`
	Primary *bool   `json:"primary,omitzero"`
}

type ReconcileScimUsersRequestUsersItemUser struct {
	ExternalID   *string                                            `json:"externalId,omitzero"`
	UserName     *string                                            `json:"userName,omitzero"`
	Name         *ReconcileScimUsersRequestUsersItemUserName        `json:"name,omitzero"`
	Emails       []ReconcileScimUsersRequestUsersItemUserEmailsItem `json:"emails,omitzero"`
	PhoneNumbers []ReconcileScimUsersRequestUsersItemUserEmailsItem `json:"phoneNumbers,omitzero"`
	Active       *bool                                              `json:"active,omitzero"`
	Photos       []ReconcileScimUsersRequestUsersItemUserEmailsItem `json:"photos,omitzero"`
}

type ReconcileScimUsersRequestUsersItem struct {
	ExternalUserID string                                 `json:"external_user_id"`
	User           ReconcileScimUsersRequestUsersItemUser `json:"user"`
}

type ReconcileScimUsersRequest struct {
	Provider string                               `json:"provider"`
	Users    []ReconcileScimUsersRequestUsersItem `json:"users"`
}

type ReconcileScimUsersResponse = UpdateScimSettingsResponse

type ReconcileScimGroupsRequestGroupsItemMembersItem struct {
	Value string  `json:"value"`
	Type  *string `json:"type,omitzero"`
}

type ReconcileScimGroupsRequestGroupsItem struct {
	ExternalID  *string                                           `json:"externalId,omitzero"`
	DisplayName string                                            `json:"displayName"`
	Members     []ReconcileScimGroupsRequestGroupsItemMembersItem `json:"members,omitzero"`
}

type ReconcileScimGroupsRequest struct {
	Groups []ReconcileScimGroupsRequestGroupsItem `json:"groups"`
}

type ReconcileScimGroupsResponse = UpdateScimSettingsResponse

type ReconcileScimGroupMembersRequestChangesItem struct {
	ExternalGroupID string   `json:"external_group_id"`
	Added           []string `json:"added"`
	Removed         []string `json:"removed"`
}

type ReconcileScimGroupMembersRequest struct {
	Provider string                                        `json:"provider"`
	Changes  []ReconcileScimGroupMembersRequestChangesItem `json:"changes"`
}

type ReconcileScimGroupMembersResponse = UpdateScimSettingsResponse
