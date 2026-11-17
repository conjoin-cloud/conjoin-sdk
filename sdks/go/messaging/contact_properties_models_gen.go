package messaging

type ListContactPropertiesQuery struct {
	ReferenceID any                                   `json:"reference_id,omitzero"`
	PropertyID  any                                   `json:"property_id,omitzero"`
	Key         any                                   `json:"key,omitzero"`
	DateCreated *ListChannelAnalyticsQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListChannelAnalyticsQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string                     `json:"sort,omitzero"`
	Limit       any                                   `json:"limit,omitzero"`
}

type ListContactPropertiesItem struct {
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

type CreateContactPropertyRequest struct {
	Key          string  `json:"key"`
	Type         *string `json:"type,omitzero"`
	DefaultValue any     `json:"default_value,omitzero"`
}

type CreateContactPropertyResponse = ListContactPropertiesItem

type ListContactPropertiesCountQuery = ListContactPropertiesQuery

type ListContactPropertiesCountResponse = ListChannelAnalyticsCountResponse

type FetchOneContactPropertyResponse = ListContactPropertiesItem

type DeleteContactPropertyResponse = ListContactPropertiesItem
