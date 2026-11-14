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
	ContactID         string                   `json:"contact_id"`
	ProfileID         string                   `json:"profile_id"`
	ConjoinAccountID  string                   `json:"conjoin_account_id"`
	ConjoinProjectID  string                   `json:"conjoin_project_id"`
	LiveMode          bool                     `json:"live_mode"`
	ReferenceID       conjoin.Nullable[string] `json:"reference_id,omitzero"`
	Name              conjoin.Nullable[string] `json:"name,omitzero"`
	Email             conjoin.Nullable[string] `json:"email,omitzero"`
	PhoneNumber       any                      `json:"phone_number,omitzero"`
	PreferredChannels []string                 `json:"preferred_channels,omitzero"`
	Properties        map[string]any           `json:"properties,omitzero"`
	DateCreated       string                   `json:"date_created"`
	DateUpdated       string                   `json:"date_updated"`
	DateDeleted       conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type SuppressContactMessagesRequest struct {
	Channels []string `json:"channels"`
}

type SuppressContactMessagesResponse = CreateContactResponse

type UpdateContactRequestUpdates struct {
	Name              *string  `json:"name,omitzero"`
	Email             *string  `json:"email,omitzero"`
	PhoneNumber       *string  `json:"phone_number,omitzero"`
	PreferredChannels []string `json:"preferred_channels,omitzero"`
}

type UpdateContactRequest struct {
	Updates UpdateContactRequestUpdates `json:"updates"`
}

type UpdateContactResponse = CreateContactResponse

type DeleteContactResponse = CreateContactResponse

type ListContactsRequestCursor struct {
	Prev *string `json:"prev,omitzero"`
	Next *string `json:"next,omitzero"`
}

type ListContactsRequestQueryDateCreated struct {
	Equals    *string `json:"equals,omitzero"`
	NotEquals *string `json:"not_equals,omitzero"`
	Gt        *string `json:"gt,omitzero"`
	Lt        *string `json:"lt,omitzero"`
	Gte       *string `json:"gte,omitzero"`
	Lte       *string `json:"lte,omitzero"`
}

type ListContactsRequestQuery struct {
	ContactID   any                                  `json:"contact_id,omitzero"`
	ReferenceID any                                  `json:"reference_id,omitzero"`
	FirstName   any                                  `json:"first_name,omitzero"`
	LastName    any                                  `json:"last_name,omitzero"`
	Email       any                                  `json:"email,omitzero"`
	PhoneNumber any                                  `json:"phone_number,omitzero"`
	DateCreated *ListContactsRequestQueryDateCreated `json:"date_created,omitzero"`
	DateDeleted *ListContactsRequestQueryDateCreated `json:"date_deleted,omitzero"`
}

type ListContactsRequestSearch struct {
	Keyword string `json:"keyword"`
}

type ListContactsRequest struct {
	Cursor *ListContactsRequestCursor `json:"cursor,omitzero"`
	Filter map[string]bool            `json:"filter,omitzero"`
	Query  *ListContactsRequestQuery  `json:"query,omitzero"`
	Search *ListContactsRequestSearch `json:"search,omitzero"`
	Sort   map[string]string          `json:"sort,omitzero"`
	Limit  any                        `json:"limit,omitzero"`
}

type ListContactsItem = CreateContactResponse

type AddContactPropertiesResponse = CreateContactResponse

type UpdateContactPropertyResponse = CreateContactResponse

type DeleteContactPropertiesResponse = CreateContactResponse
