package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateSmsSenderRequest struct {
	SenderType         *string  `json:"sender_type,omitzero"`
	Sender             *string  `json:"sender,omitzero"`
	SupportedCountries []string `json:"supported_countries,omitzero"`
	Capability         string   `json:"capability"`
	IsDefaultSender    *bool    `json:"is_default_sender,omitzero"`
	IsTestSender       *bool    `json:"is_test_sender,omitzero"`
}

type CreateSmsSenderResponse struct {
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

type EnableSmsSenderResponse = CreateSmsSenderResponse

type DisableSmsSenderResponse = CreateSmsSenderResponse

type ListSmsSenderResponse = CreateSmsSenderResponse

type DeleteSmsSenderResponse = CreateSmsSenderResponse

type UpdateOneSmsSenderResponse = CreateSmsSenderResponse

type TransferSmsSenderResponse = CreateSmsSenderResponse
