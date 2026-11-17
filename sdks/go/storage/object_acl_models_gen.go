package storage

type GrantObjectAclRequestEntriesItem struct {
	EntityType string `json:"entity_type"`
	EntityID   string `json:"entity_id"`
	Role       string `json:"role"`
}

type GrantObjectAclRequest struct {
	Entries []GrantObjectAclRequestEntriesItem `json:"entries"`
}

type GrantObjectAclResponse = GrantObjectAclRequestEntriesItem

type RevokeObjectAclRequestEntriesItem struct {
	EntityType string `json:"entity_type"`
	EntityID   string `json:"entity_id"`
}

type RevokeObjectAclRequest struct {
	Entries []RevokeObjectAclRequestEntriesItem `json:"entries"`
}

type RevokeObjectAclResponse = GrantObjectAclRequestEntriesItem

type SetObjectPublicRequest struct {
	IsPublic bool `json:"is_public"`
}

type SetObjectPublicResponse = GrantObjectAclRequestEntriesItem
