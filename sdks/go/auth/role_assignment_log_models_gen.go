package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListRoleAssignmentLogsQuery struct {
	AccountID *string                     `json:"account_id,omitzero"`
	RoleKey   *string                     `json:"role_key,omitzero"`
	Action    *string                     `json:"action,omitzero"`
	Cursor    *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort      map[string]string           `json:"sort,omitzero"`
	Limit     any                         `json:"limit,omitzero"`
}

type ListRoleAssignmentLogsItem struct {
	AssignmentLogID      string                   `json:"assignment_log_id"`
	OrganizationID       string                   `json:"organization_id"`
	AccountID            string                   `json:"account_id"`
	AppID                string                   `json:"app_id"`
	ConjoinAccountID     string                   `json:"conjoin_account_id"`
	ConjoinProjectID     string                   `json:"conjoin_project_id"`
	LiveMode             bool                     `json:"live_mode"`
	RoleKey              string                   `json:"role_key"`
	Action               string                   `json:"action"`
	PerformedByAccountID conjoin.Nullable[string] `json:"performed_by_account_id,omitzero"`
	PerformedAt          *string                  `json:"performed_at,omitzero"`
	Context              map[string]any           `json:"context,omitzero"`
	Metadata             map[string]any           `json:"metadata,omitzero"`
	DateCreated          string                   `json:"date_created"`
	DateUpdated          string                   `json:"date_updated"`
	DateDeleted          conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ListRoleAssignmentLogsCountQuery = ListRoleAssignmentLogsQuery

type ListRoleAssignmentLogsCountResponse = ListCredentialsCountResponse
