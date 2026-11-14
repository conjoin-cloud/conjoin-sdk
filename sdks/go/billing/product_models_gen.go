package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListProductsQueryName struct {
	NotEquals *string  `json:"not_equals,omitzero"`
	HasLength *float64 `json:"has_length,omitzero"`
	HasAny    []string `json:"has_any,omitzero"`
	HasNone   []string `json:"has_none,omitzero"`
	Gt        *string  `json:"gt,omitzero"`
	Lt        *string  `json:"lt,omitzero"`
	Gte       *string  `json:"gte,omitzero"`
	Lte       *string  `json:"lte,omitzero"`
}

type ListProductsQuery struct {
	ReferenceID *string                                       `json:"reference_id,omitzero"`
	Name        *ListProductsQueryName                        `json:"name,omitzero"`
	Description *ListProductsQueryName                        `json:"description,omitzero"`
	IsActive    any                                           `json:"is_active,omitzero"`
	DateCreated *ListChargesQueryDateCreated                  `json:"date_created,omitzero"`
	DateUpdated *ListChargesQueryDateCreated                  `json:"date_updated,omitzero"`
	DateDeleted conjoin.Nullable[ListChargesQueryDateCreated] `json:"date_deleted,omitzero"`
	Cursor      *ListChargesQueryCursor                       `json:"cursor,omitzero"`
	Sort        map[string]string                             `json:"sort,omitzero"`
	Limit       any                                           `json:"limit,omitzero"`
}

type ListProductsItem struct {
	ConjoinAccountID    string                                                  `json:"conjoin_account_id"`
	ConjoinProjectID    string                                                  `json:"conjoin_project_id"`
	EntityID            string                                                  `json:"entity_id"`
	ProductID           string                                                  `json:"product_id"`
	ReferenceID         string                                                  `json:"reference_id"`
	Name                string                                                  `json:"name"`
	Description         conjoin.Nullable[string]                                `json:"description,omitzero"`
	StatementDescriptor conjoin.Nullable[string]                                `json:"statement_descriptor,omitzero"`
	UnitLabel           string                                                  `json:"unit_label"`
	IsActive            bool                                                    `json:"is_active"`
	Images              []string                                                `json:"images,omitzero"`
	Features            []ListPriceBundlesItemManagedCatalogProductFeaturesItem `json:"features,omitzero"`
	BillingMetadata     map[string]any                                          `json:"billing_metadata,omitzero"`
	DateCreated         string                                                  `json:"date_created"`
	DateUpdated         string                                                  `json:"date_updated"`
	DateDeleted         conjoin.Nullable[string]                                `json:"date_deleted,omitzero"`
	LiveMode            bool                                                    `json:"live_mode"`
}

type CreateProductRequest struct {
	Name                string                                                  `json:"name"`
	ReferenceID         *string                                                 `json:"reference_id,omitzero"`
	Description         *string                                                 `json:"description,omitzero"`
	StatementDescriptor *string                                                 `json:"statement_descriptor,omitzero"`
	UnitLabel           string                                                  `json:"unit_label"`
	IsActive            *bool                                                   `json:"is_active,omitzero"`
	Images              []string                                                `json:"images,omitzero"`
	Features            []ListPriceBundlesItemManagedCatalogProductFeaturesItem `json:"features,omitzero"`
	Metadata            map[string]any                                          `json:"metadata,omitzero"`
}

type CreateProductResponse = ListProductsItem

type ListProductsCountQuery = ListProductsQuery

type ListProductsCountResponse = ListChargesCountResponse

type ReadProductResponse = ListProductsItem

type UpdateProductRequest struct {
	Name                *string                                                 `json:"name,omitzero"`
	Description         *string                                                 `json:"description,omitzero"`
	StatementDescriptor *string                                                 `json:"statement_descriptor,omitzero"`
	UnitLabel           *string                                                 `json:"unit_label,omitzero"`
	IsActive            *bool                                                   `json:"is_active,omitzero"`
	Images              []string                                                `json:"images,omitzero"`
	Features            []ListPriceBundlesItemManagedCatalogProductFeaturesItem `json:"features,omitzero"`
	Metadata            map[string]any                                          `json:"metadata,omitzero"`
}

type UpdateProductResponse = ListProductsItem

type DeleteProductResponse = DeleteEntitlementOverrideResponse

type ArchiveProductResponse = ListProductsItem

type RestoreProductResponse = ListProductsItem
