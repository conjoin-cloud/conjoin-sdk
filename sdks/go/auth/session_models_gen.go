package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListSessionsQueryDateCreated struct {
	Equals    *string `json:"equals,omitzero"`
	NotEquals *string `json:"not_equals,omitzero"`
	Gt        *string `json:"gt,omitzero"`
	Lt        *string `json:"lt,omitzero"`
	Gte       *string `json:"gte,omitzero"`
	Lte       *string `json:"lte,omitzero"`
}

type ListSessionsQuery struct {
	SessionID   *string                       `json:"session_id,omitzero"`
	AccountID   *string                       `json:"account_id,omitzero"`
	ClientID    *string                       `json:"client_id,omitzero"`
	Status      *string                       `json:"status,omitzero"`
	DateCreated *ListSessionsQueryDateCreated `json:"date_created,omitzero"`
	ExpiresAt   *ListSessionsQueryDateCreated `json:"expires_at,omitzero"`
	Cursor      *ListCredentialsQueryCursor   `json:"cursor,omitzero"`
	Sort        map[string]string             `json:"sort,omitzero"`
	Limit       any                           `json:"limit,omitzero"`
}

type ListSessionsItemLastActivity struct {
	IP          conjoin.Nullable[string]  `json:"ip,omitzero"`
	InitiatedAt conjoin.Nullable[string]  `json:"initiated_at,omitzero"`
	CountryCode conjoin.Nullable[string]  `json:"country_code,omitzero"`
	Latitude    conjoin.Nullable[float64] `json:"latitude,omitzero"`
	Longitude   conjoin.Nullable[float64] `json:"longitude,omitzero"`
}

type ListSessionsItem struct {
	SessionID        string                        `json:"session_id"`
	AccountID        string                        `json:"account_id"`
	ClientID         string                        `json:"client_id"`
	AppID            string                        `json:"app_id"`
	ConjoinAccountID string                        `json:"conjoin_account_id"`
	ConjoinProjectID string                        `json:"conjoin_project_id"`
	LiveMode         bool                          `json:"live_mode"`
	ExpiresAt        conjoin.Nullable[string]      `json:"expires_at,omitzero"`
	LastActivity     *ListSessionsItemLastActivity `json:"last_activity,omitzero"`
	Status           string                        `json:"status"`
	RevokedAt        conjoin.Nullable[string]      `json:"revoked_at,omitzero"`
	RevokedReason    conjoin.Nullable[string]      `json:"revoked_reason,omitzero"`
	Metadata         map[string]any                `json:"metadata,omitzero"`
	DateCreated      string                        `json:"date_created"`
	DateUpdated      string                        `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]      `json:"date_deleted,omitzero"`
}

type ListSessionsCountQuery = ListSessionsQuery

type ListSessionsCountResponse = ListCredentialsCountResponse

type ReadSessionStatsQuery struct {
	AccountID       *string `json:"account_id,omitzero"`
	ClientID        *string `json:"client_id,omitzero"`
	TimeWindowHours any     `json:"time_window_hours,omitzero"`
}

type ReadSessionStatsResponse struct {
	ActiveSessionCount float64 `json:"active_session_count"`
	ActiveClientCount  float64 `json:"active_client_count"`
}

type GetSessionAnalyticsQuery struct {
	StartDate      string   `json:"start_date"`
	EndDate        string   `json:"end_date"`
	GroupBy        *string  `json:"group_by,omitzero"`
	IncludeClients any      `json:"include_clients,omitzero"`
	ClientIDs      []string `json:"client_ids,omitzero"`
}

type GetSessionAnalyticsResponse struct {
	Data []map[string]any `json:"data"`
}

type ReadSessionResponse = ListSessionsItem

type UpdateSessionRequest struct {
	Status           *string        `json:"status,omitzero"`
	ExtendsBySeconds *int64         `json:"extends_by_seconds,omitzero"`
	Metadata         map[string]any `json:"metadata,omitzero"`
}

type UpdateSessionResponse = ListSessionsItem

type ValidateSessionRequest struct {
	CheckExpiry        *bool   `json:"check_expiry,omitzero"`
	UpdateLastActivity *bool   `json:"update_last_activity,omitzero"`
	IPAddress          *string `json:"ip_address,omitzero"`
}

type ValidateSessionResponse struct {
	Valid     bool     `json:"valid"`
	SessionID *string  `json:"session_id,omitzero"`
	AccountID *string  `json:"account_id,omitzero"`
	Errors    []string `json:"errors,omitzero"`
}

type RevokeSessionResponse = ListSessionsItem

type RevokeAllSessionsForAccountResponse struct {
	RevokedCount float64  `json:"revoked_count"`
	SessionIDs   []string `json:"session_ids,omitzero"`
}

type BulkRevokeAccountSessionsRequest struct {
	SessionIDs   []string `json:"session_ids"`
	RevokeReason *string  `json:"revoke_reason,omitzero"`
}

type BulkRevokeAccountSessionsResponse = RevokeAllSessionsForAccountResponse

type BulkRevokeClientSessionsRequest = BulkRevokeAccountSessionsRequest

type BulkRevokeClientSessionsResponse = RevokeAllSessionsForAccountResponse
