package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListContactsQuery struct {
	ContactID   any                                   `json:"contact_id,omitzero"`
	ReferenceID any                                   `json:"reference_id,omitzero"`
	FirstName   any                                   `json:"first_name,omitzero"`
	LastName    any                                   `json:"last_name,omitzero"`
	Email       any                                   `json:"email,omitzero"`
	PhoneNumber any                                   `json:"phone_number,omitzero"`
	DateCreated *ListChannelAnalyticsQueryDateCreated `json:"date_created,omitzero"`
	DateDeleted *ListChannelAnalyticsQueryDateCreated `json:"date_deleted,omitzero"`
	Search      *string                               `json:"search,omitzero"`
	Cursor      *ListChannelAnalyticsQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string                     `json:"sort,omitzero"`
	Limit       any                                   `json:"limit,omitzero"`
}

type ListContactsItemQuietHours struct {
	StartsAt string `json:"starts_at"`
	EndsAt   string `json:"ends_at"`
}

type ListContactsItem struct {
	ContactID         string                                       `json:"contact_id"`
	ProfileID         string                                       `json:"profile_id"`
	ConjoinAccountID  string                                       `json:"conjoin_account_id"`
	ConjoinProjectID  string                                       `json:"conjoin_project_id"`
	LiveMode          bool                                         `json:"live_mode"`
	ReferenceID       conjoin.Nullable[string]                     `json:"reference_id,omitzero"`
	FirstName         conjoin.Nullable[string]                     `json:"first_name,omitzero"`
	LastName          conjoin.Nullable[string]                     `json:"last_name,omitzero"`
	Email             conjoin.Nullable[string]                     `json:"email,omitzero"`
	PhoneNumber       any                                          `json:"phone_number,omitzero"`
	PreferredChannels []string                                     `json:"preferred_channels,omitzero"`
	QuietHours        conjoin.Nullable[ListContactsItemQuietHours] `json:"quiet_hours,omitzero"`
	Timezone          conjoin.Nullable[string]                     `json:"timezone,omitzero"`
	Properties        map[string]any                               `json:"properties,omitzero"`
	DateCreated       string                                       `json:"date_created"`
	DateUpdated       string                                       `json:"date_updated"`
	DateDeleted       conjoin.Nullable[string]                     `json:"date_deleted,omitzero"`
}

type CreateContactRequest struct {
	ReferenceID       *string                     `json:"reference_id,omitzero"`
	FirstName         *string                     `json:"first_name,omitzero"`
	LastName          *string                     `json:"last_name,omitzero"`
	Email             *string                     `json:"email,omitzero"`
	PhoneNumber       any                         `json:"phone_number,omitzero"`
	PreferredChannels []string                    `json:"preferred_channels,omitzero"`
	QuietHours        *ListContactsItemQuietHours `json:"quiet_hours,omitzero"`
	Properties        map[string]any              `json:"properties,omitzero"`
}

type CreateContactResponse = ListContactsItem

type ListContactsCountQuery = ListContactsQuery

type ListContactsCountResponse = ListChannelAnalyticsCountResponse

type SuppressContactMessagesRequest struct {
	Channels []string `json:"channels"`
}

type SuppressContactMessagesResponse = ListContactsItem

type UpdateContactRequest struct {
	FirstName         *string                     `json:"first_name,omitzero"`
	LastName          *string                     `json:"last_name,omitzero"`
	Email             *string                     `json:"email,omitzero"`
	PhoneNumber       any                         `json:"phone_number,omitzero"`
	PreferredChannels []string                    `json:"preferred_channels,omitzero"`
	QuietHours        *ListContactsItemQuietHours `json:"quiet_hours,omitzero"`
}

type UpdateContactResponse = ListContactsItem

type DeleteContactResponse = ListContactsItem

type AddContactPropertiesRequest struct {
	Properties map[string]any `json:"properties"`
}

type AddContactPropertiesResponse = ListContactsItem

type UpdateContactPropertyRequest struct {
	Value any `json:"value"`
}

type UpdateContactPropertyResponse = ListContactsItem

type DeleteContactPropertyValueResponse = ListContactsItem
