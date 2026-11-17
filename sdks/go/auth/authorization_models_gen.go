package auth

type AuthorizeActionRequestContext struct {
	IPAddress        *string        `json:"ip_address,omitzero"`
	CustomAttributes map[string]any `json:"custom_attributes,omitzero"`
}

type AuthorizeActionRequest struct {
	AccountID     string                         `json:"account_id"`
	PermissionKey string                         `json:"permission_key"`
	ResourceType  *string                        `json:"resource_type,omitzero"`
	ResourceID    *string                        `json:"resource_id,omitzero"`
	Context       *AuthorizeActionRequestContext `json:"context,omitzero"`
}

type AuthorizeActionResponse struct {
	Allowed              bool     `json:"allowed"`
	Missing              []string `json:"missing"`
	EvaluatedPermissions []string `json:"evaluated_permissions"`
}

type CheckRoleRequest struct {
	AccountID string `json:"account_id"`
	RoleKey   string `json:"role_key"`
}

type CheckRoleResponse struct {
	HasRole bool `json:"has_role"`
}

type ReadEffectivePermissionsQuery struct {
	AccountID string `json:"account_id"`
}

type ReadEffectivePermissionsResponse struct {
	Roles       []string `json:"roles"`
	Permissions []string `json:"permissions"`
}
