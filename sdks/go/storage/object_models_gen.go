package storage

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateUploadSignedUrlRequest struct {
	Path             string `json:"path"`
	ContentType      string `json:"content_type"`
	FileSize         int64  `json:"file_size"`
	ExpiresInMinutes *int64 `json:"expires_in_minutes,omitzero"`
}

type CreateUploadSignedUrlResponseRequiredFields struct {
	Method  string            `json:"method"`
	Headers map[string]string `json:"headers"`
}

type CreateUploadSignedUrlResponse struct {
	UploadURL      string                                      `json:"upload_url"`
	RequiredFields CreateUploadSignedUrlResponseRequiredFields `json:"required_fields"`
	UploadMode     string                                      `json:"upload_mode"`
}

type CreateDownloadSignedUrlRequest struct {
	Path string `json:"path"`
}

type CreateDownloadSignedUrlResponse struct {
	URL     string            `json:"url"`
	Headers map[string]string `json:"headers,omitzero"`
}

type RenameObjectResponse struct {
	ObjectID           string                             `json:"object_id"`
	ReferenceID        *string                            `json:"reference_id"`
	ContainerID        string                             `json:"container_id"`
	ConjoinAccountID   string                             `json:"conjoin_account_id"`
	ConjoinProjectID   string                             `json:"conjoin_project_id"`
	LiveMode           bool                               `json:"live_mode"`
	Name               string                             `json:"name"`
	Description        *string                            `json:"description"`
	Size               float64                            `json:"size"`
	ContentType        *string                            `json:"content_type"`
	ObjectMetadata     map[string]any                     `json:"object_metadata,omitzero"`
	Checksum           *string                            `json:"checksum"`
	VersionID          *string                            `json:"version_id"`
	Labels             []string                           `json:"labels"`
	ConjoinAuthACL     []GrantObjectAclRequestEntriesItem `json:"conjoin_auth_acl"`
	IsPublic           bool                               `json:"is_public"`
	ArchivedDate       *string                            `json:"archived_date"`
	GenerationNumber   float64                            `json:"generation_number"`
	Md5Hash            *string                            `json:"md5_hash"`
	SyncStatus         string                             `json:"sync_status"`
	LifecycleExpiresAt *string                            `json:"lifecycle_expires_at"`
	DuplicateOf        *string                            `json:"duplicate_of"`
	Metadata           map[string]any                     `json:"metadata,omitzero"`
	DateCreated        string                             `json:"date_created"`
	DateUpdated        *string                            `json:"date_updated"`
}

type ArchiveObjectResponse = RenameObjectResponse

type RestoreObjectResponse = RenameObjectResponse

type DeleteObjectResponse = RenameObjectResponse

type ListObjectVersionsQuery struct {
	Cursor *ListContainersQueryCursor `json:"cursor,omitzero"`
	Sort   map[string]string          `json:"sort,omitzero"`
	Limit  any                        `json:"limit,omitzero"`
}

type ListObjectVersionsItem struct {
	VersionID        string         `json:"version_id"`
	ObjectID         string         `json:"object_id"`
	ContainerID      string         `json:"container_id"`
	ConjoinAccountID string         `json:"conjoin_account_id"`
	ConjoinProjectID string         `json:"conjoin_project_id"`
	LiveMode         bool           `json:"live_mode"`
	Name             string         `json:"name"`
	ContentType      *string        `json:"content_type"`
	Size             float64        `json:"size"`
	Md5Hash          *string        `json:"md5_hash"`
	Checksum         *string        `json:"checksum"`
	GcsVersionPath   string         `json:"gcs_version_path"`
	CreatedBy        string         `json:"created_by"`
	Metadata         map[string]any `json:"metadata,omitzero"`
	DateCreated      string         `json:"date_created"`
	DateUpdated      *string        `json:"date_updated"`
}

type RestoreObjectVersionRequest struct {
	VersionID string `json:"version_id"`
}

type RestoreObjectVersionResponse = ListObjectVersionsItem

type CheckObjectDuplicateQuery struct {
	Md5Hash string `json:"md5_hash"`
}

type CheckObjectDuplicateResponse = RenameObjectResponse

type ReadObjectResponse = RenameObjectResponse

type ListObjectsQuery struct {
	Cursor         *ListContainersQueryCursor `json:"cursor,omitzero"`
	HasLabel       *string                    `json:"has_label,omitzero"`
	HasMetadataKey *string                    `json:"has_metadata_key,omitzero"`
	Label          *string                    `json:"label,omitzero"`
	Name           *string                    `json:"name,omitzero"`
	Description    *string                    `json:"description,omitzero"`
	ContainerID    *string                    `json:"container_id,omitzero"`
	ObjectID       *string                    `json:"object_id,omitzero"`
	IsArchived     *bool                      `json:"is_archived,omitzero"`
	IsPublic       *bool                      `json:"is_public,omitzero"`
	SyncStatus     any                        `json:"sync_status,omitzero"`
	Limit          any                        `json:"limit,omitzero"`
	Sort           map[string]string          `json:"sort,omitzero"`
	DateUpdated    conjoin.Nullable[string]   `json:"date_updated,omitzero"`
	DateCreated    conjoin.Nullable[string]   `json:"date_created,omitzero"`
}

type ListObjectsItem = RenameObjectResponse
