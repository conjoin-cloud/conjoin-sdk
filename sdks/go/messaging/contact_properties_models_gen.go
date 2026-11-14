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

type DeleteManyContactPropertiesResponse = CreateContactPropertyResponse

type FetchOneContactPropertyResponse = CreateContactPropertyResponse

type DeleteContactPropertyResponse = CreateContactPropertyResponse

type ListContactPropertiesItem = CreateContactPropertyResponse
