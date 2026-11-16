package messaging

type CreateContactPropertyRequest struct {
	Key          string  `json:"key"`
	Type         *string `json:"type,omitzero"`
	DefaultValue any     `json:"default_value,omitzero"`
}

type CreateContactPropertyResponse struct {
	PropertyID       string `json:"property_id"`
	ProfileID        string `json:"profile_id"`
	ConjoinAccountID string `json:"conjoin_account_id"`
	ConjoinProjectID string `json:"conjoin_project_id"`
	LiveMode         bool   `json:"live_mode"`
	Key              string `json:"key"`
	Type             string `json:"type"`
	DefaultValue     any    `json:"default_value"`
	DateCreated      string `json:"date_created"`
	DateUpdated      string `json:"date_updated"`
}

type FetchOneContactPropertyResponse = CreateContactPropertyResponse

type DeleteContactPropertyResponse = CreateContactPropertyResponse

type ListContactPropertiesRequestQuery struct {
	PropertyID  any                                          `json:"property_id,omitzero"`
	Key         any                                          `json:"key,omitzero"`
	DateCreated *ListChannelAnalyticsRequestQueryDateCreated `json:"date_created,omitzero"`
}

type ListContactPropertiesRequest struct {
	Cursor *ListChannelAnalyticsRequestCursor `json:"cursor,omitzero"`
	Query  *ListContactPropertiesRequestQuery `json:"query,omitzero"`
	Sort   map[string]string                  `json:"sort,omitzero"`
	Limit  any                                `json:"limit,omitzero"`
}

type ListContactPropertiesItem = CreateContactPropertyResponse

type DeleteManyContactPropertiesRequest struct {
	Type        *string  `json:"type,omitzero"`
	Keys        []string `json:"keys,omitzero"`
	PropertyIDs []string `json:"property_ids,omitzero"`
}

type DeleteManyContactPropertiesItem = CreateContactPropertyResponse
