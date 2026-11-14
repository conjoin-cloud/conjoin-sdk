package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type AccountsService struct {
	client *conjoin.Client
}

func (s *AccountsService) ListCredentials(ctx context.Context, accountID string, query *ListCredentialsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListCredentialsItem], error) {
	return conjoin.List[ListCredentialsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/accounts/{account_id}/credentials",
		PathParams: []string{accountID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *AccountsService) VerifyCredential(ctx context.Context, accountID string, body *VerifyCredentialRequest, opts ...conjoin.CallOption) (*VerifyCredentialResponse, error) {
	var out VerifyCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/credentials/verify",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) VerifyCredentialMfaTotp(ctx context.Context, accountID string, body *VerifyCredentialMfaTotpRequest, opts ...conjoin.CallOption) (*VerifyCredentialMfaTotpResponse, error) {
	var out VerifyCredentialMfaTotpResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/totp-credentials/verify",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) ListCredentialsCount(ctx context.Context, accountID string, query *ListCredentialsCountQuery, opts ...conjoin.CallOption) (*ListCredentialsCountResponse, error) {
	var out ListCredentialsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/accounts/{account_id}/credentials/count",
		PathParams: []string{accountID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) ReadCredential(ctx context.Context, accountID string, credentialID string, opts ...conjoin.CallOption) (*ReadCredentialResponse, error) {
	var out ReadCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/accounts/{account_id}/credentials/{credential_id}",
		PathParams: []string{accountID, credentialID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) RemoveCredential(ctx context.Context, accountID string, credentialID string, opts ...conjoin.CallOption) (*RemoveCredentialResponse, error) {
	var out RemoveCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/accounts/{account_id}/credentials/{credential_id}/remove",
		PathParams: []string{accountID, credentialID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) List(ctx context.Context, query *ListAccountsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListAccountsItem], error) {
	return conjoin.List[ListAccountsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "auth/accounts/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *AccountsService) Create(ctx context.Context, body *CreateAccountRequest, opts ...conjoin.CallOption) (*CreateAccountResponse, error) {
	var out CreateAccountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) ListOrganizationMemberships(ctx context.Context, accountID string, query *ListAccountOrganizationMembershipsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListAccountOrganizationMembershipsItem], error) {
	return conjoin.List[ListAccountOrganizationMembershipsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/accounts/{account_id}/organizations",
		PathParams: []string{accountID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *AccountsService) ListCount(ctx context.Context, query *ListAccountsCountQuery, opts ...conjoin.CallOption) (*ListAccountsCountResponse, error) {
	var out ListAccountsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/accounts/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) Merge(ctx context.Context, body *MergeAccountsRequest, opts ...conjoin.CallOption) (*MergeAccountsResponse, error) {
	var out MergeAccountsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/merge",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) Read(ctx context.Context, accountID string, opts ...conjoin.CallOption) (*ReadAccountResponse, error) {
	var out ReadAccountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/accounts/{account_id}",
		PathParams: []string{accountID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) Update(ctx context.Context, accountID string, body *UpdateAccountRequest, opts ...conjoin.CallOption) (*UpdateAccountResponse, error) {
	var out UpdateAccountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/accounts/{account_id}",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) Delete(ctx context.Context, accountID string, opts ...conjoin.CallOption) (*DeleteAccountResponse, error) {
	var out DeleteAccountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/accounts/{account_id}",
		PathParams: []string{accountID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) AddEmail(ctx context.Context, accountID string, body *AddAccountEmailRequest, opts ...conjoin.CallOption) (*AddAccountEmailResponse, error) {
	var out AddAccountEmailResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/emails/add",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) RemoveEmail(ctx context.Context, accountID string, body *RemoveAccountEmailRequest, opts ...conjoin.CallOption) (*RemoveAccountEmailResponse, error) {
	var out RemoveAccountEmailResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/emails/remove",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) AddPhone(ctx context.Context, accountID string, body *AddAccountPhoneRequest, opts ...conjoin.CallOption) (*AddAccountPhoneResponse, error) {
	var out AddAccountPhoneResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/phones/add",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) RemovePhone(ctx context.Context, accountID string, body *RemoveAccountPhoneRequest, opts ...conjoin.CallOption) (*RemoveAccountPhoneResponse, error) {
	var out RemoveAccountPhoneResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/phones/remove",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) GrantGlobalRole(ctx context.Context, accountID string, body *GrantGlobalRoleRequest, opts ...conjoin.CallOption) (*GrantGlobalRoleResponse, error) {
	var out GrantGlobalRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/global-roles/grant",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) RevokeGlobalRole(ctx context.Context, accountID string, body *RevokeGlobalRoleRequest, opts ...conjoin.CallOption) (*RevokeGlobalRoleResponse, error) {
	var out RevokeGlobalRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/global-roles/revoke",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) ListOrganizationMembershipsCount(ctx context.Context, accountID string, query *ListAccountOrganizationMembershipsCountQuery, opts ...conjoin.CallOption) (*ListAccountOrganizationMembershipsCountResponse, error) {
	var out ListAccountOrganizationMembershipsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/accounts/{account_id}/organizations/count",
		PathParams: []string{accountID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) Export(ctx context.Context, accountID string, opts ...conjoin.CallOption) (*ExportAccountResponse, error) {
	var out ExportAccountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/accounts/{account_id}/export",
		PathParams: []string{accountID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountsService) ImportPasswordHashes(ctx context.Context, body *ImportPasswordHashesRequest, opts ...conjoin.CallOption) (*ImportPasswordHashesResponse, error) {
	var out ImportPasswordHashesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/import-password-hashes",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
