package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadAuditLogsQuery struct {
	EventCode        *string                 `json:"event_code,omitzero"`
	Category         *string                 `json:"category,omitzero"`
	ActorID          *string                 `json:"actor_id,omitzero"`
	ResourceType     *string                 `json:"resource_type,omitzero"`
	ResourceID       *string                 `json:"resource_id,omitzero"`
	Severity         *string                 `json:"severity,omitzero"`
	ConjoinRequestID *string                 `json:"conjoin_request_id,omitzero"`
	From             *string                 `json:"from,omitzero"`
	To               *string                 `json:"to,omitzero"`
	Cursor           *ReadApiKeysQueryCursor `json:"cursor,omitzero"`
	Sort             map[string]string       `json:"sort,omitzero"`
	Limit            any                     `json:"limit,omitzero"`
}

type ReadAuditLogsItemActor struct {
	Type string  `json:"type"`
	ID   string  `json:"id"`
	Role *string `json:"role,omitzero"`
}

type ReadAuditLogsItemResource struct {
	Type string `json:"type"`
	ID   string `json:"id"`
}

type ReadAuditLogsItemProducerContext struct {
	IP        *string `json:"ip,omitzero"`
	UserAgent *string `json:"user_agent,omitzero"`
}

type ReadAuditLogsItem struct {
	AuditID                string                            `json:"audit_id"`
	CloudAccountID         string                            `json:"cloud_account_id"`
	EntityID               string                            `json:"entity_id"`
	ProjectID              string                            `json:"project_id"`
	OrganizationID         string                            `json:"organization_id"`
	EventCode              string                            `json:"event_code"`
	SchemaVersion          float64                           `json:"schema_version"`
	Service                string                            `json:"service"`
	Categories             []string                          `json:"categories"`
	Actor                  ReadAuditLogsItemActor            `json:"actor"`
	Resource               *ReadAuditLogsItemResource        `json:"resource,omitzero"`
	Severity               *string                           `json:"severity,omitzero"`
	OccurredAt             string                            `json:"occurred_at"`
	RecordedAt             string                            `json:"recorded_at"`
	CorrelationID          *string                           `json:"correlation_id,omitzero"`
	RequestID              *string                           `json:"request_id,omitzero"`
	ConjoinRequestID       string                            `json:"conjoin_request_id"`
	TraceSource            conjoin.Nullable[string]          `json:"trace_source,omitzero"`
	IdempotencyKey         string                            `json:"idempotency_key"`
	Payload                map[string]any                    `json:"payload"`
	PayloadSize            float64                           `json:"payload_size"`
	ProducerContext        *ReadAuditLogsItemProducerContext `json:"producer_context,omitzero"`
	SensitiveFieldsRemoved []string                          `json:"sensitive_fields_removed,omitzero"`
	ExpireAt               conjoin.Nullable[string]          `json:"expire_at,omitzero"`
	DateCreated            string                            `json:"date_created"`
	DateUpdated            conjoin.Nullable[string]          `json:"date_updated,omitzero"`
	DateDeleted            conjoin.Nullable[string]          `json:"date_deleted,omitzero"`
}

type ReadAuditLogsCountQuery = ReadAuditLogsQuery

type ReadAuditLogsCountResponse = ReadApiKeysCountResponse

type ReadAuditStatsQuery struct {
	By   string  `json:"by"`
	From *string `json:"from,omitzero"`
	To   *string `json:"to,omitzero"`
}

type ReadAuditStatsResponse struct {
	TotalEvents float64            `json:"total_events"`
	Categories  map[string]float64 `json:"categories"`
	Services    map[string]float64 `json:"services"`
}
