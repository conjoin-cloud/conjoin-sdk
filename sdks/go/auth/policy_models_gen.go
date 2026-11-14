package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListPoliciesQuery struct {
	ReferenceID *string                     `json:"reference_id,omitzero"`
	Effect      *string                     `json:"effect,omitzero"`
	IsEnabled   any                         `json:"is_enabled,omitzero"`
	Cursor      *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort        map[string]string           `json:"sort,omitzero"`
	Limit       any                         `json:"limit,omitzero"`
}

type ListPoliciesItem struct {
	PolicyID         string                   `json:"policy_id"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	OrganizationID   string                   `json:"organization_id"`
	AppID            string                   `json:"app_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	Name             string                   `json:"name"`
	Description      conjoin.Nullable[string] `json:"description,omitzero"`
	Conditions       []map[string]any         `json:"conditions,omitzero"`
	PermissionKeys   []string                 `json:"permission_keys,omitzero"`
	Effect           string                   `json:"effect"`
	Priority         *float64                 `json:"priority,omitzero"`
	IsEnabled        *bool                    `json:"is_enabled,omitzero"`
	Metadata         map[string]any           `json:"metadata,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreatePolicyRequestConditionsItem struct {
	Type         *string                  `json:"type,omitzero"`
	StartTime    conjoin.Nullable[string] `json:"start_time,omitzero"`
	EndTime      conjoin.Nullable[string] `json:"end_time,omitzero"`
	DaysOfWeek   []float64                `json:"days_of_week,omitzero"`
	Timezone     *string                  `json:"timezone,omitzero"`
	AllowedCidrs []string                 `json:"allowed_cidrs,omitzero"`
	Key          *string                  `json:"key,omitzero"`
	Operator     *string                  `json:"operator,omitzero"`
	Value        any                      `json:"value,omitzero"`
}

type CreatePolicyRequest struct {
	ReferenceID    *string                             `json:"reference_id,omitzero"`
	Name           string                              `json:"name"`
	Description    conjoin.Nullable[string]            `json:"description,omitzero"`
	Conditions     []CreatePolicyRequestConditionsItem `json:"conditions"`
	PermissionKeys []string                            `json:"permission_keys"`
	Effect         string                              `json:"effect"`
	Priority       *float64                            `json:"priority,omitzero"`
	IsEnabled      *bool                               `json:"is_enabled,omitzero"`
}

type CreatePolicyResponse = ListPoliciesItem

type ListPoliciesCountQuery = ListPoliciesQuery

type ListPoliciesCountResponse = ListCredentialsCountResponse

type ReadPolicyResponse = ListPoliciesItem

type UpdatePolicyRequest struct {
	Name           *string                             `json:"name,omitzero"`
	Description    conjoin.Nullable[string]            `json:"description,omitzero"`
	Conditions     []CreatePolicyRequestConditionsItem `json:"conditions,omitzero"`
	PermissionKeys []string                            `json:"permission_keys,omitzero"`
	Effect         *string                             `json:"effect,omitzero"`
	Priority       *float64                            `json:"priority,omitzero"`
	IsEnabled      *bool                               `json:"is_enabled,omitzero"`
}

type UpdatePolicyResponse = ListPoliciesItem

type DeletePolicyResponse = ListPoliciesItem
