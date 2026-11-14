package ai

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateContextIndexRequestSourceConfigOcr struct {
	Enabled          *bool    `json:"enabled,omitzero"`
	MaxFileSizeBytes *float64 `json:"max_file_size_bytes,omitzero"`
	MaxPages         *float64 `json:"max_pages,omitzero"`
	MaxImages        *float64 `json:"max_images,omitzero"`
	TimeoutMs        *float64 `json:"timeout_ms,omitzero"`
	MinConfidence    *float64 `json:"min_confidence,omitzero"`
}

type CreateContextIndexRequestSourceConfig struct {
	ContainerID    string                                    `json:"container_id"`
	PathPrefix     *string                                   `json:"path_prefix,omitzero"`
	FileExtensions []string                                  `json:"file_extensions,omitzero"`
	Ocr            *CreateContextIndexRequestSourceConfigOcr `json:"ocr,omitzero"`
}

type CreateContextIndexRequest struct {
	Name           string                                `json:"name"`
	SourceType     string                                `json:"source_type"`
	SourceConfig   CreateContextIndexRequestSourceConfig `json:"source_config"`
	EmbeddingModel *string                               `json:"embedding_model,omitzero"`
	Description    conjoin.Nullable[string]              `json:"description,omitzero"`
	ReferenceID    conjoin.Nullable[string]              `json:"reference_id,omitzero"`
	Metadata       map[string]any                        `json:"metadata,omitzero"`
}

type CreateContextIndexResponseSourceConfigOcr struct {
	Enabled          bool    `json:"enabled"`
	MaxFileSizeBytes float64 `json:"max_file_size_bytes"`
	MaxPages         float64 `json:"max_pages"`
	MaxImages        float64 `json:"max_images"`
	TimeoutMs        float64 `json:"timeout_ms"`
	MinConfidence    float64 `json:"min_confidence"`
}

type CreateContextIndexResponseSourceConfig struct {
	ContainerID    string                                     `json:"container_id"`
	PathPrefix     *string                                    `json:"path_prefix,omitzero"`
	FileExtensions []string                                   `json:"file_extensions,omitzero"`
	Ocr            *CreateContextIndexResponseSourceConfigOcr `json:"ocr,omitzero"`
}

type CreateContextIndexResponse struct {
	IndexID             string                                 `json:"index_id"`
	ConjoinAccountID    string                                 `json:"conjoin_account_id"`
	ConjoinProjectID    string                                 `json:"conjoin_project_id"`
	LiveMode            bool                                   `json:"live_mode"`
	ReferenceID         *string                                `json:"reference_id"`
	Name                string                                 `json:"name"`
	SourceType          string                                 `json:"source_type"`
	SourceConfig        CreateContextIndexResponseSourceConfig `json:"source_config"`
	EmbeddingModel      string                                 `json:"embedding_model"`
	EmbeddingDimensions float64                                `json:"embedding_dimensions"`
	DocumentCount       float64                                `json:"document_count"`
	TotalSizeBytes      float64                                `json:"total_size_bytes"`
	LastSyncedAt        conjoin.Nullable[string]               `json:"last_synced_at,omitzero"`
	SyncStatus          string                                 `json:"sync_status"`
	Status              string                                 `json:"status"`
	Description         conjoin.Nullable[string]               `json:"description,omitzero"`
	Metadata            map[string]any                         `json:"metadata"`
	DateCreated         string                                 `json:"date_created"`
	DateUpdated         string                                 `json:"date_updated"`
}

type ListContextIndexesQueryQuery struct {
	Status      *string                               `json:"status,omitzero"`
	SourceType  *string                               `json:"source_type,omitzero"`
	DateCreated *ListByokConfigsQueryQueryDateCreated `json:"date_created,omitzero"`
}

type ListContextIndexesQuery struct {
	Cursor *ListByokConfigsQueryCursor   `json:"cursor,omitzero"`
	Sort   map[string]string             `json:"sort,omitzero"`
	Limit  any                           `json:"limit,omitzero"`
	Query  *ListContextIndexesQueryQuery `json:"query,omitzero"`
}

type ListContextIndexesItem = CreateContextIndexResponse

type ReadContextIndexResponse = CreateContextIndexResponse

type DeleteContextIndexResponse = CreateContextIndexResponse

type SyncContextIndexResponse = CreateContextIndexResponse

type QueryContextRequest struct {
	IndexIDs []string       `json:"index_ids"`
	Query    string         `json:"query"`
	Modes    []string       `json:"modes,omitzero"`
	Limit    *int64         `json:"limit,omitzero"`
	Filters  map[string]any `json:"filters,omitzero"`
	UserID   *string        `json:"user_id,omitzero"`
}

type QueryContextResponseResultsItem struct {
	DocumentID  string  `json:"document_id"`
	Score       float64 `json:"score"`
	TextContent string  `json:"text_content"`
	SourcePath  string  `json:"source_path"`
	ChunkIndex  float64 `json:"chunk_index"`
}

type QueryContextResponse struct {
	QueryID      string                            `json:"query_id"`
	Results      []QueryContextResponseResultsItem `json:"results"`
	ModesUsed    []string                          `json:"modes_used"`
	TotalResults float64                           `json:"total_results"`
	LatencyMs    float64                           `json:"latency_ms"`
}

type ListContextQueryLogsQueryQuery struct {
	QueriedAt *ListByokConfigsQueryQueryDateCreated `json:"queried_at,omitzero"`
}

type ListContextQueryLogsQuery struct {
	Cursor *ListByokConfigsQueryCursor     `json:"cursor,omitzero"`
	Sort   map[string]string               `json:"sort,omitzero"`
	Limit  any                             `json:"limit,omitzero"`
	Query  *ListContextQueryLogsQueryQuery `json:"query,omitzero"`
}

type ListContextQueryLogsItem struct {
	QueryID              string   `json:"query_id"`
	ConjoinAccountID     string   `json:"conjoin_account_id"`
	ConjoinProjectID     string   `json:"conjoin_project_id"`
	LiveMode             bool     `json:"live_mode"`
	IndexIDs             []string `json:"index_ids"`
	ModesUsed            []string `json:"modes_used"`
	VectorResultsCount   float64  `json:"vector_results_count"`
	FulltextResultsCount float64  `json:"fulltext_results_count"`
	AgenticReadsCount    float64  `json:"agentic_reads_count"`
	TotalResultsReturned float64  `json:"total_results_returned"`
	LatencyMs            float64  `json:"latency_ms"`
	TokenCostUsd         float64  `json:"token_cost_usd"`
	QueriedAt            string   `json:"queried_at"`
	DateCreated          string   `json:"date_created"`
}
