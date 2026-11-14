package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ScimBulkOperationsRequestOperationsItem struct {
	Method  string  `json:"method"`
	Path    *string `json:"path,omitzero"`
	BulkID  *string `json:"bulkId,omitzero"`
	Version *string `json:"version,omitzero"`
	Data    any     `json:"data,omitzero"`
}

type ScimBulkOperationsRequest struct {
	Schemas      []string                                  `json:"schemas,omitzero"`
	FailOnErrors *int64                                    `json:"failOnErrors,omitzero"`
	Operations   []ScimBulkOperationsRequestOperationsItem `json:"Operations"`
}

type ScimBulkOperationsResponse struct {
	Schemas    []string         `json:"schemas"`
	Operations []map[string]any `json:"Operations,omitzero"`
}

type ScimListGroupsResponse struct {
	Schemas      []string         `json:"schemas"`
	TotalResults float64          `json:"totalResults"`
	StartIndex   *float64         `json:"startIndex,omitzero"`
	ItemsPerPage *float64         `json:"itemsPerPage,omitzero"`
	Resources    []map[string]any `json:"Resources,omitzero"`
}

type ScimCreateGroupRequest = ReconcileScimGroupsRequestGroupsItem

type ScimCreateGroupResponseMembersItem struct {
	Value   string  `json:"value"`
	Display *string `json:"display,omitzero"`
	Type    *string `json:"type,omitzero"`
}

type ScimCreateGroupResponseMeta struct {
	ResourceType *string `json:"resourceType,omitzero"`
	Created      *string `json:"created,omitzero"`
	LastModified *string `json:"lastModified,omitzero"`
	Location     *string `json:"location,omitzero"`
}

type ScimCreateGroupResponse struct {
	Schemas     []string                             `json:"schemas"`
	ID          *string                              `json:"id,omitzero"`
	ExternalID  conjoin.Nullable[string]             `json:"externalId,omitzero"`
	DisplayName string                               `json:"displayName"`
	Members     []ScimCreateGroupResponseMembersItem `json:"members,omitzero"`
	Meta        *ScimCreateGroupResponseMeta         `json:"meta,omitzero"`
}

type ScimGetGroupResponse = ScimCreateGroupResponse

type ScimReplaceGroupRequest = ReconcileScimGroupsRequestGroupsItem

type ScimReplaceGroupResponse = ScimCreateGroupResponse

type ScimPatchGroupMembersRequestOperationsItem struct {
	Op    string  `json:"op"`
	Path  *string `json:"path,omitzero"`
	Value any     `json:"value,omitzero"`
}

type ScimPatchGroupMembersRequest struct {
	Schemas    []string                                     `json:"schemas,omitzero"`
	Operations []ScimPatchGroupMembersRequestOperationsItem `json:"Operations"`
}

type ScimPatchGroupMembersResponse = ScimCreateGroupResponse

type ScimGetServiceProviderConfigResponsePatch struct {
	Supported bool `json:"supported"`
}

type ScimGetServiceProviderConfigResponseBulk struct {
	Supported      bool     `json:"supported"`
	MaxOperations  *float64 `json:"maxOperations,omitzero"`
	MaxPayloadSize *float64 `json:"maxPayloadSize,omitzero"`
}

type ScimGetServiceProviderConfigResponseFilter struct {
	Supported  bool     `json:"supported"`
	MaxResults *float64 `json:"maxResults,omitzero"`
}

type ScimGetServiceProviderConfigResponse struct {
	Schemas               []string                                    `json:"schemas"`
	DocumentationURI      *string                                     `json:"documentationUri,omitzero"`
	Patch                 *ScimGetServiceProviderConfigResponsePatch  `json:"patch,omitzero"`
	Bulk                  *ScimGetServiceProviderConfigResponseBulk   `json:"bulk,omitzero"`
	Filter                *ScimGetServiceProviderConfigResponseFilter `json:"filter,omitzero"`
	ChangePassword        *ScimGetServiceProviderConfigResponsePatch  `json:"changePassword,omitzero"`
	Sort                  *ScimGetServiceProviderConfigResponsePatch  `json:"sort,omitzero"`
	Etag                  *ScimGetServiceProviderConfigResponsePatch  `json:"etag,omitzero"`
	AuthenticationSchemes []map[string]any                            `json:"authenticationSchemes,omitzero"`
}

type ScimGetSchemasResponse struct {
	Schemas      []string         `json:"schemas"`
	TotalResults *float64         `json:"totalResults,omitzero"`
	Resources    []map[string]any `json:"Resources,omitzero"`
}

type ScimGetResourceTypesResponse = ScimGetSchemasResponse

type ScimListUsersResponse = ScimListGroupsResponse

type ScimCreateUserRequest = ReconcileScimUsersRequestUsersItemUser

type ScimCreateUserResponse struct {
	Schemas      []string                                           `json:"schemas"`
	ID           *string                                            `json:"id,omitzero"`
	ExternalID   conjoin.Nullable[string]                           `json:"externalId,omitzero"`
	UserName     *string                                            `json:"userName,omitzero"`
	Name         *ReconcileScimUsersRequestUsersItemUserName        `json:"name,omitzero"`
	Emails       []ReconcileScimUsersRequestUsersItemUserEmailsItem `json:"emails,omitzero"`
	PhoneNumbers []ReconcileScimUsersRequestUsersItemUserEmailsItem `json:"phoneNumbers,omitzero"`
	Active       *bool                                              `json:"active,omitzero"`
	Photos       []ReconcileScimUsersRequestUsersItemUserEmailsItem `json:"photos,omitzero"`
	Meta         *ScimCreateGroupResponseMeta                       `json:"meta,omitzero"`
}

type ScimGetUserResponse = ScimCreateUserResponse

type ScimReplaceUserRequest = ReconcileScimUsersRequestUsersItemUser

type ScimReplaceUserResponse = ScimCreateUserResponse

type ScimPatchUserResponse = ScimCreateUserResponse
