package cloud

type ReadSkuCatalogQuery struct {
	Service   *string                 `json:"service,omitzero"`
	Category  *string                 `json:"category,omitzero"`
	MeterType *string                 `json:"meter_type,omitzero"`
	Cursor    *ReadApiKeysQueryCursor `json:"cursor,omitzero"`
	Sort      map[string]string       `json:"sort,omitzero"`
	Limit     any                     `json:"limit,omitzero"`
}

type ReadSkuCatalogItem struct {
	SkuID       string `json:"sku_id"`
	SkuCode     string `json:"sku_code"`
	Name        string `json:"name"`
	Description string `json:"description"`
	Service     string `json:"service"`
	Category    string `json:"category"`
	UnitLabel   string `json:"unit_label"`
	MeterType   string `json:"meter_type"`
}

type ReadSkuCatalogCountQuery = ReadSkuCatalogQuery

type ReadSkuCatalogCountResponse = ReadApiKeysCountResponse

type ReadSingleSkuCatalogResponse = ReadSkuCatalogItem
