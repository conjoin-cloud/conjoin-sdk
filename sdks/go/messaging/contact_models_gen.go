package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateContactRequestQuietHours struct {
	StartsAt string `json:"starts_at"`
	EndsAt   string `json:"ends_at"`
}

type CreateContactRequest struct {
	ReferenceID       *string                         `json:"reference_id,omitzero"`
	FirstName         *string                         `json:"first_name,omitzero"`
	LastName          *string                         `json:"last_name,omitzero"`
	Email             *string                         `json:"email,omitzero"`
	PhoneNumber       any                             `json:"phone_number,omitzero"`
	PreferredChannels []string                        `json:"preferred_channels,omitzero"`
	QuietHours        *CreateContactRequestQuietHours `json:"quiet_hours,omitzero"`
	Properties        map[string]any                  `json:"properties,omitzero"`
}

type CreateContactResponse struct {
	ContactID         string                                           `json:"contact_id"`
	ProfileID         string                                           `json:"profile_id"`
	ConjoinAccountID  string                                           `json:"conjoin_account_id"`
	ConjoinProjectID  string                                           `json:"conjoin_project_id"`
	LiveMode          bool                                             `json:"live_mode"`
	ReferenceID       conjoin.Nullable[string]                         `json:"reference_id,omitzero"`
	FirstName         conjoin.Nullable[string]                         `json:"first_name,omitzero"`
	LastName          conjoin.Nullable[string]                         `json:"last_name,omitzero"`
	Email             conjoin.Nullable[string]                         `json:"email,omitzero"`
	PhoneNumber       any                                              `json:"phone_number,omitzero"`
	PreferredChannels []string                                         `json:"preferred_channels,omitzero"`
	QuietHours        conjoin.Nullable[CreateContactRequestQuietHours] `json:"quiet_hours,omitzero"`
	Timezone          conjoin.Nullable[string]                         `json:"timezone,omitzero"`
	Properties        map[string]any                                   `json:"properties,omitzero"`
	DateCreated       string                                           `json:"date_created"`
	DateUpdated       string                                           `json:"date_updated"`
	DateDeleted       conjoin.Nullable[string]                         `json:"date_deleted,omitzero"`
}

type SuppressContactMessagesRequest struct {
	Channels []string `json:"channels"`
}

type SuppressContactMessagesResponse = CreateContactResponse

type UpdateContactRequest struct {
	FirstName         *string                         `json:"first_name,omitzero"`
	LastName          *string                         `json:"last_name,omitzero"`
	Email             *string                         `json:"email,omitzero"`
	PhoneNumber       any                             `json:"phone_number,omitzero"`
	PreferredChannels []string                        `json:"preferred_channels,omitzero"`
	QuietHours        *CreateContactRequestQuietHours `json:"quiet_hours,omitzero"`
}

type UpdateContactResponse = CreateContactResponse

type DeleteContactResponse = CreateContactResponse

type ListContactsRequestQuery struct {
	ContactID   any                                          `json:"contact_id,omitzero"`
	ReferenceID any                                          `json:"reference_id,omitzero"`
	FirstName   any                                          `json:"first_name,omitzero"`
	LastName    any                                          `json:"last_name,omitzero"`
	Email       any                                          `json:"email,omitzero"`
	PhoneNumber any                                          `json:"phone_number,omitzero"`
	DateCreated *ListChannelAnalyticsRequestQueryDateCreated `json:"date_created,omitzero"`
	DateDeleted *ListChannelAnalyticsRequestQueryDateCreated `json:"date_deleted,omitzero"`
}

type ListContactsRequestSearch struct {
	Keyword string `json:"keyword"`
}

type ListContactsRequest struct {
	Cursor *ListChannelAnalyticsRequestCursor `json:"cursor,omitzero"`
	Filter map[string]bool                    `json:"filter,omitzero"`
	Query  *ListContactsRequestQuery          `json:"query,omitzero"`
	Search *ListContactsRequestSearch         `json:"search,omitzero"`
	Sort   map[string]string                  `json:"sort,omitzero"`
	Limit  any                                `json:"limit,omitzero"`
}

type ListContactsItem = CreateContactResponse

type AddContactPropertiesRequest struct {
	Properties map[string]any `json:"properties"`
}

type AddContactPropertiesResponse = CreateContactResponse

type UpdateContactPropertyRequest struct {
	Key   string `json:"key"`
	Value any    `json:"value"`
}

type UpdateContactPropertyResponse = CreateContactResponse

type DeleteContactPropertiesRequest struct {
	Keys []string `json:"keys"`
}

type DeleteContactPropertiesResponse = CreateContactResponse
