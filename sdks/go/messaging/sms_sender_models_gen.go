package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListManySmsSendersQuery struct {
	SenderID        any                                   `json:"sender_id,omitzero"`
	ReferenceID     any                                   `json:"reference_id,omitzero"`
	Sender          *string                               `json:"sender,omitzero"`
	Capability      any                                   `json:"capability,omitzero"`
	Status          any                                   `json:"status,omitzero"`
	IsDefaultSender any                                   `json:"is_default_sender,omitzero"`
	IsTestSender    any                                   `json:"is_test_sender,omitzero"`
	DateCreated     *ListChannelAnalyticsQueryDateCreated `json:"date_created,omitzero"`
	Cursor          *ListChannelAnalyticsQueryCursor      `json:"cursor,omitzero"`
	Sort            map[string]string                     `json:"sort,omitzero"`
	Limit           any                                   `json:"limit,omitzero"`
}

type ListManySmsSendersItem struct {
	SenderID             string                   `json:"sender_id"`
	ProfileID            string                   `json:"profile_id"`
	ConjoinAccountID     string                   `json:"conjoin_account_id"`
	ConjoinProjectID     string                   `json:"conjoin_project_id"`
	LiveMode             bool                     `json:"live_mode"`
	ReferenceID          conjoin.Nullable[string] `json:"reference_id,omitzero"`
	BrandID              string                   `json:"brand_id"`
	Sender               string                   `json:"sender"`
	Capability           string                   `json:"capability"`
	DestinationCountries map[string]any           `json:"destination_countries,omitzero"`
	IsPhoneNumber        bool                     `json:"is_phone_number"`
	IsDefaultSender      *bool                    `json:"is_default_sender,omitzero"`
	IsTestSender         *bool                    `json:"is_test_sender,omitzero"`
	SubmittedAt          string                   `json:"submitted_at"`
	ProvisionedAt        conjoin.Nullable[string] `json:"provisioned_at,omitzero"`
	Status               string                   `json:"status"`
	DateCreated          string                   `json:"date_created"`
	DateUpdated          string                   `json:"date_updated"`
	DateDeleted          conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateSmsSenderRequest struct {
	SenderType         *string  `json:"sender_type,omitzero"`
	Sender             *string  `json:"sender,omitzero"`
	SupportedCountries []string `json:"supported_countries,omitzero"`
	ReferenceID        *string  `json:"reference_id,omitzero"`
	Capability         string   `json:"capability"`
	IsDefaultSender    *bool    `json:"is_default_sender,omitzero"`
	IsTestSender       *bool    `json:"is_test_sender,omitzero"`
}

type CreateSmsSenderResponse = ListManySmsSendersItem

type ListManySmsSendersCountQuery = ListManySmsSendersQuery

type ListManySmsSendersCountResponse = ListChannelAnalyticsCountResponse

type ReadSmsSenderResponse = ListManySmsSendersItem

type UpdateOneSmsSenderRequestProperties struct {
	IndiaTemplateID *string `json:"india_template_id,omitzero"`
	IndiaSenderID   *string `json:"india_sender_id,omitzero"`
}

type UpdateOneSmsSenderRequest struct {
	IsDefaultSender *bool                                `json:"is_default_sender,omitzero"`
	IsTestSender    *bool                                `json:"is_test_sender,omitzero"`
	Properties      *UpdateOneSmsSenderRequestProperties `json:"properties,omitzero"`
}

type UpdateOneSmsSenderResponse = ListManySmsSendersItem

type DeleteSmsSenderResponse = ListManySmsSendersItem

type EnableSmsSenderResponse = ListManySmsSendersItem

type DisableSmsSenderResponse = ListManySmsSendersItem

type TransferSmsSenderRequest = TransferEmailSenderRequest

type TransferSmsSenderResponse = ListManySmsSendersItem
