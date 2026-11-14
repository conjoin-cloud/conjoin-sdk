package relay

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateSearchIndexRequestSchemaDefinitionFieldsValue struct {
	Type     string `json:"type"`
	Tokenize *bool  `json:"tokenize,omitzero"`
	Stem     *bool  `json:"stem,omitzero"`
}

type CreateSearchIndexRequestSchemaDefinitionTypoTolerance struct {
	Enabled  bool   `json:"enabled"`
	Distance *int64 `json:"distance,omitzero"`
}

type CreateSearchIndexRequestSchemaDefinition struct {
	Fields        map[string]CreateSearchIndexRequestSchemaDefinitionFieldsValue `json:"fields"`
	Language      *string                                                        `json:"language,omitzero"`
	TypoTolerance *CreateSearchIndexRequestSchemaDefinitionTypoTolerance         `json:"typo_tolerance,omitzero"`
}

type CreateSearchIndexRequest struct {
	Name             string                                   `json:"name"`
	ReferenceID      *string                                  `json:"reference_id,omitzero"`
	SchemaDefinition CreateSearchIndexRequestSchemaDefinition `json:"schema_definition"`
	Description      *string                                  `json:"description,omitzero"`
}

type CreateSearchIndexResponseSchemaDefinitionTypoTolerance struct {
	Enabled  bool     `json:"enabled"`
	Distance *float64 `json:"distance,omitzero"`
}

type CreateSearchIndexResponseSchemaDefinition struct {
	Fields        map[string]CreateSearchIndexRequestSchemaDefinitionFieldsValue `json:"fields"`
	Language      conjoin.Nullable[string]                                       `json:"language,omitzero"`
	TypoTolerance *CreateSearchIndexResponseSchemaDefinitionTypoTolerance        `json:"typo_tolerance,omitzero"`
}

type CreateSearchIndexResponse struct {
	IndexID          string                                    `json:"index_id"`
	ConjoinAccountID string                                    `json:"conjoin_account_id"`
	ConjoinProjectID string                                    `json:"conjoin_project_id"`
	ReferenceID      conjoin.Nullable[string]                  `json:"reference_id,omitzero"`
	LiveMode         bool                                      `json:"live_mode"`
	Name             string                                    `json:"name"`
	SchemaDefinition CreateSearchIndexResponseSchemaDefinition `json:"schema_definition"`
	Settings         map[string]any                            `json:"settings,omitzero"`
	DocumentCount    *float64                                  `json:"document_count,omitzero"`
	Status           string                                    `json:"status"`
	Description      conjoin.Nullable[string]                  `json:"description,omitzero"`
	Metadata         map[string]any                            `json:"metadata,omitzero"`
	DateCreated      string                                    `json:"date_created"`
	DateUpdated      string                                    `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]                  `json:"date_deleted,omitzero"`
}

type ReadSearchIndexesQuery = ReadEventChannelsQuery

type ReadSearchIndexesItem = CreateSearchIndexResponse

type DeleteSearchIndexResponse = CreateSearchIndexResponse

type IndexSearchDocumentRequest struct {
	ReferenceID    *string        `json:"reference_id,omitzero"`
	Content        map[string]any `json:"content"`
	SearchMetadata map[string]any `json:"search_metadata,omitzero"`
}

type IndexSearchDocumentResponse struct {
	DocumentID       string                   `json:"document_id"`
	IndexID          string                   `json:"index_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	LiveMode         bool                     `json:"live_mode"`
	Content          map[string]any           `json:"content"`
	SearchMetadata   map[string]any           `json:"search_metadata,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
}

type IndexSearchDocumentBatchRequest struct {
	Documents []IndexSearchDocumentRequest `json:"documents"`
}

type IndexSearchDocumentBatchResponse struct {
	IndexedCount float64 `json:"indexed_count"`
}

type RemoveSearchDocumentResponse struct {
	Removed bool `json:"removed"`
}

type SearchQueryRequest struct {
	Term    string         `json:"term"`
	Filters map[string]any `json:"filters,omitzero"`
	Fuzzy   *bool          `json:"fuzzy,omitzero"`
	Limit   *int64         `json:"limit,omitzero"`
	Offset  *int64         `json:"offset,omitzero"`
}

type SearchQueryResponseHitsItem struct {
	DocumentID string         `json:"document_id"`
	Score      float64        `json:"score"`
	Content    map[string]any `json:"content"`
}

type SearchQueryResponse struct {
	Hits  []SearchQueryResponseHitsItem `json:"hits"`
	Total float64                       `json:"total"`
}

type AutoSuggestSearchRequest struct {
	Prefix string  `json:"prefix"`
	Field  *string `json:"field,omitzero"`
	Limit  *int64  `json:"limit,omitzero"`
}

type AutoSuggestSearchResponse struct {
	Suggestions []string `json:"suggestions"`
}
