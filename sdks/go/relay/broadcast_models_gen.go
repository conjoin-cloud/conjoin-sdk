package relay

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type GenerateBroadcastConnectionTokenResponse struct {
	Token     string `json:"token"`
	ExpiresAt string `json:"expires_at"`
}

type ReadBroadcastChannelsQueryCursor struct {
	Prev *string `json:"prev,omitzero"`
	Next *string `json:"next,omitzero"`
}

type ReadBroadcastChannelsQuery struct {
	Status      *string                           `json:"status,omitzero"`
	ReferenceID *string                           `json:"reference_id,omitzero"`
	Cursor      *ReadBroadcastChannelsQueryCursor `json:"cursor,omitzero"`
	Sort        map[string]string                 `json:"sort,omitzero"`
	Limit       any                               `json:"limit,omitzero"`
}

type ReadBroadcastChannelsItem struct {
	ChannelID                string                    `json:"channel_id"`
	ConjoinAccountID         string                    `json:"conjoin_account_id"`
	ConjoinProjectID         string                    `json:"conjoin_project_id"`
	ReferenceID              conjoin.Nullable[string]  `json:"reference_id,omitzero"`
	LiveMode                 bool                      `json:"live_mode"`
	Name                     string                    `json:"name"`
	ChannelType              string                    `json:"channel_type"`
	AuthorizationMode        string                    `json:"authorization_mode"`
	AuthorizationCallbackURL conjoin.Nullable[string]  `json:"authorization_callback_url,omitzero"`
	MaxConnections           conjoin.Nullable[float64] `json:"max_connections,omitzero"`
	HistorySize              *float64                  `json:"history_size,omitzero"`
	Status                   string                    `json:"status"`
	Description              conjoin.Nullable[string]  `json:"description,omitzero"`
	Metadata                 map[string]any            `json:"metadata,omitzero"`
	DateCreated              string                    `json:"date_created"`
	DateUpdated              string                    `json:"date_updated"`
	DateDeleted              conjoin.Nullable[string]  `json:"date_deleted,omitzero"`
}

type CreateBroadcastChannelRequest struct {
	Name                     string  `json:"name"`
	ReferenceID              *string `json:"reference_id,omitzero"`
	ChannelType              *string `json:"channel_type,omitzero"`
	AuthorizationMode        *string `json:"authorization_mode,omitzero"`
	AuthorizationCallbackURL *string `json:"authorization_callback_url,omitzero"`
	MaxConnections           *int64  `json:"max_connections,omitzero"`
	HistorySize              *int64  `json:"history_size,omitzero"`
	Description              *string `json:"description,omitzero"`
}

type CreateBroadcastChannelResponse = ReadBroadcastChannelsItem

type ReadBroadcastChannelsCountQuery = ReadBroadcastChannelsQuery

type ReadBroadcastChannelsCountResponse struct {
	Count int64 `json:"count"`
}

type UpdateBroadcastChannelRequest struct {
	Name                     *string                  `json:"name,omitzero"`
	AuthorizationMode        *string                  `json:"authorization_mode,omitzero"`
	AuthorizationCallbackURL conjoin.Nullable[string] `json:"authorization_callback_url,omitzero"`
	MaxConnections           conjoin.Nullable[int64]  `json:"max_connections,omitzero"`
	HistorySize              *int64                   `json:"history_size,omitzero"`
	Description              conjoin.Nullable[string] `json:"description,omitzero"`
}

type UpdateBroadcastChannelResponse = ReadBroadcastChannelsItem

type DeleteBroadcastChannelResponse = ReadBroadcastChannelsItem

type GenerateBroadcastAuthTokenRequest struct {
	UserID      *string  `json:"user_id,omitzero"`
	Permissions []string `json:"permissions,omitzero"`
}

type GenerateBroadcastAuthTokenResponse = GenerateBroadcastConnectionTokenResponse

type PublishToBroadcastRequest struct {
	Event string         `json:"event"`
	Data  map[string]any `json:"data,omitzero"`
}

type PublishToBroadcastResponse struct {
	Published bool   `json:"published"`
	EventID   string `json:"event_id"`
}

type ReadBroadcastPresenceResponse struct {
	Members []string `json:"members"`
}
