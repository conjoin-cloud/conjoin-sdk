package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListCredentialsQueryCursor struct {
	Prev *string `json:"prev,omitzero"`
	Next *string `json:"next,omitzero"`
}

type ListCredentialsQuery struct {
	CredentialID   *string                     `json:"credential_id,omitzero"`
	CredentialType *string                     `json:"credential_type,omitzero"`
	Cursor         *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort           map[string]string           `json:"sort,omitzero"`
	Limit          any                         `json:"limit,omitzero"`
}

type ListCredentialsItem struct {
	CredentialID     string                   `json:"credential_id"`
	AccountID        string                   `json:"account_id"`
	Kind             string                   `json:"kind"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	AppID            string                   `json:"app_id"`
	LiveMode         bool                     `json:"live_mode"`
	Metadata         map[string]any           `json:"metadata,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type VerifyCredentialRequest struct {
	CredentialType  string `json:"credential_type"`
	CredentialValue string `json:"credential_value"`
}

type VerifyCredentialResponse = ListCredentialsItem

type VerifyCredentialMfaTotpRequest struct {
	Code string `json:"code"`
}

type VerifyCredentialMfaTotpResponse = ListCredentialsItem

type ListCredentialsCountQuery = ListCredentialsQuery

type ListCredentialsCountResponse struct {
	Count int64 `json:"count"`
}

type ReadCredentialResponse = ListCredentialsItem

type RemoveCredentialResponse = ListCredentialsItem

type ListAccountsQuery struct {
	AccountID   *string                     `json:"account_id,omitzero"`
	ReferenceID *string                     `json:"reference_id,omitzero"`
	Emails      []string                    `json:"emails,omitzero"`
	Phones      []string                    `json:"phones,omitzero"`
	Status      *string                     `json:"status,omitzero"`
	Dormant     any                         `json:"dormant,omitzero"`
	Cursor      *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort        map[string]string           `json:"sort,omitzero"`
	Limit       any                         `json:"limit,omitzero"`
}

type ListAccountsItemEmailsItemVerification struct {
	Status     string  `json:"status"`
	VerifiedAt *string `json:"verified_at"`
}

type ListAccountsItemEmailsItem struct {
	Email        string                                 `json:"email"`
	IsPrimary    bool                                   `json:"is_primary"`
	Verification ListAccountsItemEmailsItemVerification `json:"verification"`
}

type ListAccountsItemPhonesItem struct {
	Phone        string                                 `json:"phone"`
	IsPrimary    bool                                   `json:"is_primary"`
	Verification ListAccountsItemEmailsItemVerification `json:"verification"`
}

type ListAccountsItem struct {
	AccountID        string                       `json:"account_id"`
	AppID            string                       `json:"app_id"`
	ConjoinAccountID string                       `json:"conjoin_account_id"`
	ConjoinProjectID string                       `json:"conjoin_project_id"`
	LiveMode         bool                         `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string]     `json:"reference_id,omitzero"`
	Emails           []ListAccountsItemEmailsItem `json:"emails,omitzero"`
	Phones           []ListAccountsItemPhonesItem `json:"phones,omitzero"`
	Name             conjoin.Nullable[string]     `json:"name,omitzero"`
	ImageURL         conjoin.Nullable[string]     `json:"image_url,omitzero"`
	Status           string                       `json:"status"`
	LastActiveAt     conjoin.Nullable[string]     `json:"last_active_at,omitzero"`
	DormantAt        conjoin.Nullable[string]     `json:"dormant_at,omitzero"`
	CustomAttributes map[string]any               `json:"custom_attributes,omitzero"`
	GlobalRoles      []string                     `json:"global_roles,omitzero"`
	Metadata         map[string]any               `json:"metadata,omitzero"`
	DateCreated      string                       `json:"date_created"`
	DateUpdated      string                       `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]     `json:"date_deleted,omitzero"`
}

type CreateAccountRequest struct {
	ReferenceID  *string        `json:"reference_id,omitzero"`
	PrimaryEmail *string        `json:"primary_email,omitzero"`
	PrimaryPhone *string        `json:"primary_phone,omitzero"`
	Name         *string        `json:"name,omitzero"`
	ImageURL     *string        `json:"image_url,omitzero"`
	Metadata     map[string]any `json:"metadata,omitzero"`
}

type CreateAccountResponse = ListAccountsItem

type ListAccountOrganizationMembershipsQuery struct {
	Cursor *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort   map[string]string           `json:"sort,omitzero"`
	Limit  any                         `json:"limit,omitzero"`
}

type ListAccountOrganizationMembershipsItem struct {
	AccountOrganizationID string                   `json:"account_organization_id"`
	AccountID             string                   `json:"account_id"`
	OrganizationID        string                   `json:"organization_id"`
	JoinedAt              conjoin.Nullable[string] `json:"joined_at,omitzero"`
	Roles                 []string                 `json:"roles,omitzero"`
	Status                string                   `json:"status"`
	ConjoinAccountID      string                   `json:"conjoin_account_id"`
	ConjoinProjectID      string                   `json:"conjoin_project_id"`
	AppID                 string                   `json:"app_id"`
	LiveMode              bool                     `json:"live_mode"`
	Metadata              map[string]any           `json:"metadata,omitzero"`
	DateCreated           string                   `json:"date_created"`
	DateUpdated           string                   `json:"date_updated"`
	DateDeleted           conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ListAccountsCountQuery = ListAccountsQuery

type ListAccountsCountResponse = ListCredentialsCountResponse

type MergeAccountsRequest struct {
	SourceAccountID string  `json:"source_account_id"`
	TargetAccountID string  `json:"target_account_id"`
	Strategy        *string `json:"strategy,omitzero"`
}

type MergeAccountsResponse struct {
	MergedInto string `json:"merged_into"`
}

type ReadAccountResponse = ListAccountsItem

type UpdateAccountRequest struct {
	Name             *string                  `json:"name,omitzero"`
	PrimaryEmail     *string                  `json:"primary_email,omitzero"`
	PrimaryPhone     *string                  `json:"primary_phone,omitzero"`
	ImageURL         conjoin.Nullable[string] `json:"image_url,omitzero"`
	Status           *string                  `json:"status,omitzero"`
	Metadata         map[string]any           `json:"metadata,omitzero"`
	CustomAttributes map[string]any           `json:"custom_attributes,omitzero"`
}

type UpdateAccountResponse = ListAccountsItem

type DeleteAccountQuery struct {
	Permanent any `json:"permanent,omitzero"`
}

type DeleteAccountResponse = ListAccountsItem

type AddAccountEmailRequest struct {
	Email        string  `json:"email"`
	SetAsPrimary *bool   `json:"set_as_primary,omitzero"`
	SessionID    *string `json:"session_id,omitzero"`
	StepUpToken  *string `json:"step_up_token,omitzero"`
}

type AddAccountEmailResponse = ListAccountsItem

type RemoveAccountEmailRequest struct {
	Email        string  `json:"email"`
	PrimaryEmail *string `json:"primary_email,omitzero"`
	SessionID    *string `json:"session_id,omitzero"`
	StepUpToken  *string `json:"step_up_token,omitzero"`
}

type RemoveAccountEmailResponse = ListAccountsItem

type AddAccountPhoneRequest struct {
	Phone        string  `json:"phone"`
	SetAsPrimary *bool   `json:"set_as_primary,omitzero"`
	SessionID    *string `json:"session_id,omitzero"`
	StepUpToken  *string `json:"step_up_token,omitzero"`
}

type AddAccountPhoneResponse = ListAccountsItem

type RemoveAccountPhoneRequest struct {
	Phone        string  `json:"phone"`
	PrimaryPhone *string `json:"primary_phone,omitzero"`
	SessionID    *string `json:"session_id,omitzero"`
	StepUpToken  *string `json:"step_up_token,omitzero"`
}

type RemoveAccountPhoneResponse = ListAccountsItem

type GrantGlobalRoleRequest struct {
	RoleKey string `json:"role_key"`
}

type GrantGlobalRoleResponse = ListAccountsItem

type RevokeGlobalRoleRequest = GrantGlobalRoleRequest

type RevokeGlobalRoleResponse = ListAccountsItem

type ListAccountOrganizationMembershipsCountQuery = ListAccountOrganizationMembershipsQuery

type ListAccountOrganizationMembershipsCountResponse = ListCredentialsCountResponse

type ExportAccountResponse = ListAccountsItem

type ImportPasswordHashesRequestUsersItemParams struct {
	Salt              *string `json:"salt,omitzero"`
	SaltEncoding      *string `json:"salt_encoding,omitzero"`
	HashEncoding      *string `json:"hash_encoding,omitzero"`
	SaltPosition      *string `json:"salt_position,omitzero"`
	Digest            *string `json:"digest,omitzero"`
	Iterations        *int64  `json:"iterations,omitzero"`
	KeyLength         *int64  `json:"key_length,omitzero"`
	ScryptCost        *int64  `json:"scrypt_cost,omitzero"`
	ScryptBlockSize   *int64  `json:"scrypt_block_size,omitzero"`
	ScryptParallelism *int64  `json:"scrypt_parallelism,omitzero"`
	SignerKey         *string `json:"signer_key,omitzero"`
	SaltSeparator     *string `json:"salt_separator,omitzero"`
	Rounds            *int64  `json:"rounds,omitzero"`
	MemCost           *int64  `json:"mem_cost,omitzero"`
}

type ImportPasswordHashesRequestUsersItem struct {
	ReferenceID  *string                                     `json:"reference_id,omitzero"`
	PrimaryEmail *string                                     `json:"primary_email,omitzero"`
	PrimaryPhone *string                                     `json:"primary_phone,omitzero"`
	Name         *string                                     `json:"name,omitzero"`
	ImageURL     *string                                     `json:"image_url,omitzero"`
	Metadata     map[string]any                              `json:"metadata,omitzero"`
	Hash         string                                      `json:"hash"`
	Format       string                                      `json:"format"`
	Params       *ImportPasswordHashesRequestUsersItemParams `json:"params,omitzero"`
}

type ImportPasswordHashesRequest struct {
	Users []ImportPasswordHashesRequestUsersItem `json:"users"`
}

type ImportPasswordHashesResponseResultsItem struct {
	Index       float64                  `json:"index"`
	ReferenceID *string                  `json:"reference_id"`
	Status      string                   `json:"status"`
	AccountID   conjoin.Nullable[string] `json:"account_id,omitzero"`
	Code        *string                  `json:"code,omitzero"`
	Message     *string                  `json:"message,omitzero"`
}

type ImportPasswordHashesResponse struct {
	Total   float64                                   `json:"total"`
	Created float64                                   `json:"created"`
	Failed  float64                                   `json:"failed"`
	Results []ImportPasswordHashesResponseResultsItem `json:"results"`
}
