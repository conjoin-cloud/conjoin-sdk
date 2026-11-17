package ai

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListContextIndexesQuery struct {
	Status      *string                          `json:"status,omitzero"`
	SyncStatus  *string                          `json:"sync_status,omitzero"`
	SourceType  *string                          `json:"source_type,omitzero"`
	ReferenceID *string                          `json:"reference_id,omitzero"`
	DateCreated *ListByokConfigsQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListByokConfigsQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string                `json:"sort,omitzero"`
	Limit       any                              `json:"limit,omitzero"`
}

type ListContextIndexesItemSourceConfigOcr struct {
	Enabled          bool    `json:"enabled"`
	MaxFileSizeBytes float64 `json:"max_file_size_bytes"`
	MaxPages         float64 `json:"max_pages"`
	MaxImages        float64 `json:"max_images"`
	TimeoutMs        float64 `json:"timeout_ms"`
	MinConfidence    float64 `json:"min_confidence"`
}

type ListContextIndexesItemSourceConfig struct {
	ContainerID    string                                 `json:"container_id"`
	PathPrefix     *string                                `json:"path_prefix,omitzero"`
	FileExtensions []string                               `json:"file_extensions,omitzero"`
	Ocr            *ListContextIndexesItemSourceConfigOcr `json:"ocr,omitzero"`
}

type ListContextIndexesItem struct {
	IndexID             string                             `json:"index_id"`
	ConjoinAccountID    string                             `json:"conjoin_account_id"`
	ConjoinProjectID    string                             `json:"conjoin_project_id"`
	LiveMode            bool                               `json:"live_mode"`
	ReferenceID         *string                            `json:"reference_id"`
	Name                string                             `json:"name"`
	SourceType          string                             `json:"source_type"`
	SourceConfig        ListContextIndexesItemSourceConfig `json:"source_config"`
	EmbeddingModel      string                             `json:"embedding_model"`
	EmbeddingDimensions float64                            `json:"embedding_dimensions"`
	DocumentCount       float64                            `json:"document_count"`
	TotalSizeBytes      float64                            `json:"total_size_bytes"`
	LastSyncedAt        conjoin.Nullable[string]           `json:"last_synced_at,omitzero"`
	SyncStatus          string                             `json:"sync_status"`
	Status              string                             `json:"status"`
	Description         conjoin.Nullable[string]           `json:"description,omitzero"`
	Metadata            map[string]any                     `json:"metadata"`
	DateCreated         string                             `json:"date_created"`
	DateUpdated         string                             `json:"date_updated"`
	DateDeleted         conjoin.Nullable[string]           `json:"date_deleted,omitzero"`
}

type CreateContextIndexRequestSourceConfigOcr struct {
	Enabled          *bool    `json:"enabled,omitzero"`
	MaxFileSizeBytes *int64   `json:"max_file_size_bytes,omitzero"`
	MaxPages         *int64   `json:"max_pages,omitzero"`
	MaxImages        *int64   `json:"max_images,omitzero"`
	TimeoutMs        *int64   `json:"timeout_ms,omitzero"`
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

type CreateContextIndexResponse = ListContextIndexesItem

type ListContextIndexesCountQuery = ListContextIndexesQuery

type ListContextIndexesCountResponse = ListByokConfigsCountResponse

type ReadContextIndexResponse = ListContextIndexesItem

type DeleteContextIndexResponse = ListContextIndexesItem

type SyncContextIndexResponse = ListContextIndexesItem

type ListContextQueriesQuery struct {
	UserID      *string                          `json:"user_id,omitzero"`
	QueriedAt   *ListByokConfigsQueryDateCreated `json:"queried_at,omitzero"`
	DateCreated *ListByokConfigsQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListByokConfigsQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string                `json:"sort,omitzero"`
	Limit       any                              `json:"limit,omitzero"`
}

type ListContextQueriesItem struct {
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

type CreateContextQueryRequest struct {
	IndexIDs []string `json:"index_ids"`
	Query    string   `json:"query"`
	Modes    []string `json:"modes,omitzero"`
	Limit    *int64   `json:"limit,omitzero"`
	UserID   *string  `json:"user_id,omitzero"`
}

type CreateContextQueryResponseResultsItem struct {
	DocumentID  string  `json:"document_id"`
	Score       float64 `json:"score"`
	TextContent string  `json:"text_content"`
	SourcePath  string  `json:"source_path"`
	ChunkIndex  float64 `json:"chunk_index"`
}

type CreateContextQueryResponse struct {
	QueryID      string                                  `json:"query_id"`
	Results      []CreateContextQueryResponseResultsItem `json:"results"`
	ModesUsed    []string                                `json:"modes_used"`
	TotalResults float64                                 `json:"total_results"`
	LatencyMs    float64                                 `json:"latency_ms"`
}

type ListContextQueriesCountQuery = ListContextQueriesQuery

type ListContextQueriesCountResponse = ListByokConfigsCountResponse
