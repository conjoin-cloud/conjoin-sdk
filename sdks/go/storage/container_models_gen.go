package storage

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateContainerRequestLifecyclePolicy struct {
	DeleteAfterDays *int64 `json:"delete_after_days,omitzero"`
}

type CreateContainerRequest struct {
	Name            string                                 `json:"name"`
	Region          string                                 `json:"region"`
	StorageClass    string                                 `json:"storage_class"`
	LifecyclePolicy *CreateContainerRequestLifecyclePolicy `json:"lifecycle_policy,omitzero"`
	IsPublic        *bool                                  `json:"is_public,omitzero"`
}

type CreateContainerResponseLifecyclePolicy struct {
	DeleteAfterDays float64 `json:"delete_after_days"`
}

type CreateContainerResponseVersioningPolicy struct {
	MaxVersionsToKeep    float64 `json:"max_versions_to_keep"`
	VersionRetentionDays float64 `json:"version_retention_days"`
}

type CreateContainerResponseStorageClassTransitionPolicyRulesItem struct {
	FromClass string  `json:"from_class"`
	ToClass   string  `json:"to_class"`
	AfterDays float64 `json:"after_days"`
}

type CreateContainerResponseStorageClassTransitionPolicy struct {
	IsEnabled bool                                                           `json:"is_enabled"`
	Rules     []CreateContainerResponseStorageClassTransitionPolicyRulesItem `json:"rules"`
}

type CreateContainerResponseSettingsACL struct {
	ConjoinAuthEnabled bool `json:"conjoin_auth_enabled"`
}

type CreateContainerResponseSettingsImageOptimizationWidthSettings struct {
	Default float64 `json:"default"`
	Max     float64 `json:"max"`
	Min     float64 `json:"min"`
}

type CreateContainerResponseSettingsImageOptimizationQualitySettings struct {
	DefaultPerFormat map[string]float64 `json:"defaultPerFormat"`
	Max              float64            `json:"max"`
}

type CreateContainerResponseSettingsImageOptimizationDprSettings struct {
	Default float64 `json:"default"`
	Max     float64 `json:"max"`
}

type CreateContainerResponseSettingsImageOptimization struct {
	IsEnabled                   bool                                                            `json:"is_enabled"`
	WidthSettings               CreateContainerResponseSettingsImageOptimizationWidthSettings   `json:"width_settings"`
	HeightSettings              CreateContainerResponseSettingsImageOptimizationWidthSettings   `json:"height_settings"`
	QualitySettings             CreateContainerResponseSettingsImageOptimizationQualitySettings `json:"quality_settings"`
	DprSettings                 CreateContainerResponseSettingsImageOptimizationDprSettings     `json:"dpr_settings"`
	AllowedFits                 []string                                                        `json:"allowed_fits"`
	AllowedFormats              []string                                                        `json:"allowed_formats"`
	FaceDetectionEnabled        bool                                                            `json:"face_detection_enabled"`
	BlurEnabled                 bool                                                            `json:"blur_enabled"`
	SharpenEnabled              bool                                                            `json:"sharpen_enabled"`
	RotationEnabled             bool                                                            `json:"rotation_enabled"`
	FlipEnabled                 bool                                                            `json:"flip_enabled"`
	GrayscaleEnabled            bool                                                            `json:"grayscale_enabled"`
	TrimEnabled                 bool                                                            `json:"trim_enabled"`
	ProgressiveJpegEnabled      bool                                                            `json:"progressive_jpeg_enabled"`
	StillFrameExtractionEnabled bool                                                            `json:"still_frame_extraction_enabled"`
	ColorAdjustmentsEnabled     bool                                                            `json:"color_adjustments_enabled"`
	NegateEnabled               bool                                                            `json:"negate_enabled"`
	BorderRadiusEnabled         bool                                                            `json:"border_radius_enabled"`
	WatermarkEnabled            bool                                                            `json:"watermark_enabled"`
	FaceBlurEnabled             bool                                                            `json:"face_blur_enabled"`
	SaveDataQualityEnabled      bool                                                            `json:"save_data_quality_enabled"`
	MetadataMode                string                                                          `json:"metadata_mode"`
	AllowedGravityAnchors       []string                                                        `json:"allowed_gravity_anchors"`
}

type CreateContainerResponseSettings struct {
	ACL               CreateContainerResponseSettingsACL               `json:"acl"`
	ImageOptimization CreateContainerResponseSettingsImageOptimization `json:"image_optimization"`
}

type CreateContainerResponse struct {
	ContainerID                  string                                              `json:"container_id"`
	ReferenceID                  string                                              `json:"reference_id"`
	ConjoinAccountID             string                                              `json:"conjoin_account_id"`
	ConjoinProjectID             string                                              `json:"conjoin_project_id"`
	LiveMode                     bool                                                `json:"live_mode"`
	Name                         string                                              `json:"name"`
	Region                       string                                              `json:"region"`
	StorageClass                 string                                              `json:"storage_class"`
	LifecyclePolicy              CreateContainerResponseLifecyclePolicy              `json:"lifecycle_policy"`
	ArchivedDate                 *string                                             `json:"archived_date"`
	IsPublic                     bool                                                `json:"is_public"`
	DeletionStatus               string                                              `json:"deletion_status"`
	DeletionScheduledAt          *string                                             `json:"deletion_scheduled_at"`
	DeletionGracePeriodDays      float64                                             `json:"deletion_grace_period_days"`
	MigrationStatus              string                                              `json:"migration_status"`
	VersioningEnabled            bool                                                `json:"versioning_enabled"`
	VersioningPolicy             CreateContainerResponseVersioningPolicy             `json:"versioning_policy"`
	StorageClassTransitionPolicy CreateContainerResponseStorageClassTransitionPolicy `json:"storage_class_transition_policy"`
	Settings                     CreateContainerResponseSettings                     `json:"settings"`
	Metadata                     map[string]any                                      `json:"metadata,omitzero"`
	DateCreated                  string                                              `json:"date_created"`
	DateUpdated                  *string                                             `json:"date_updated"`
}

type ListContainersQueryCursor struct {
	Prev *string `json:"prev,omitzero"`
	Next *string `json:"next,omitzero"`
}

type ListContainersQueryQuery struct {
	ContainerID *string                  `json:"container_id,omitzero"`
	Name        *string                  `json:"name,omitzero"`
	DateDeleted conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ListContainersQuery struct {
	Cursor     *ListContainersQueryCursor `json:"cursor,omitzero"`
	Sort       map[string]string          `json:"sort,omitzero"`
	Limit      any                        `json:"limit,omitzero"`
	IsArchived *bool                      `json:"is_archived,omitzero"`
	Query      *ListContainersQueryQuery  `json:"query,omitzero"`
}

type ListContainersItem = CreateContainerResponse

type ReadContainerResponse = CreateContainerResponse

type RequestContainerDeletionQuery struct {
	GracePeriodDays any `json:"grace_period_days,omitzero"`
}

type RequestContainerDeletionResponse = CreateContainerResponse

type ArchiveContainerResponse = CreateContainerResponse

type RestoreContainerResponse = CreateContainerResponse

type UpdateContainerLifecyclePolicyRequest = CreateContainerRequestLifecyclePolicy

type UpdateContainerLifecyclePolicyResponse = CreateContainerResponse

type UpdateContainerSettingsRequestACL struct {
	ConjoinAuthEnabled *bool `json:"conjoin_auth_enabled,omitzero"`
}

type UpdateContainerSettingsRequestImageOptimizationWidthSettings struct {
	Default *int64 `json:"default,omitzero"`
	Max     *int64 `json:"max,omitzero"`
	Min     *int64 `json:"min,omitzero"`
}

type UpdateContainerSettingsRequestImageOptimizationQualitySettingsDefaultPerFormat struct {
	Jpeg *int64 `json:"jpeg,omitzero"`
	Png  *int64 `json:"png,omitzero"`
	Webp *int64 `json:"webp,omitzero"`
	Avif *int64 `json:"avif,omitzero"`
}

type UpdateContainerSettingsRequestImageOptimizationQualitySettings struct {
	DefaultPerFormat *UpdateContainerSettingsRequestImageOptimizationQualitySettingsDefaultPerFormat `json:"defaultPerFormat,omitzero"`
	Max              *int64                                                                          `json:"max,omitzero"`
}

type UpdateContainerSettingsRequestImageOptimizationDprSettings struct {
	Default *float64 `json:"default,omitzero"`
	Max     *float64 `json:"max,omitzero"`
}

type UpdateContainerSettingsRequestImageOptimization struct {
	IsEnabled                   *bool                                                           `json:"is_enabled,omitzero"`
	WidthSettings               *UpdateContainerSettingsRequestImageOptimizationWidthSettings   `json:"width_settings,omitzero"`
	HeightSettings              *UpdateContainerSettingsRequestImageOptimizationWidthSettings   `json:"height_settings,omitzero"`
	QualitySettings             *UpdateContainerSettingsRequestImageOptimizationQualitySettings `json:"quality_settings,omitzero"`
	DprSettings                 *UpdateContainerSettingsRequestImageOptimizationDprSettings     `json:"dpr_settings,omitzero"`
	AllowedFits                 []string                                                        `json:"allowed_fits,omitzero"`
	AllowedFormats              []string                                                        `json:"allowed_formats,omitzero"`
	FaceDetectionEnabled        *bool                                                           `json:"face_detection_enabled,omitzero"`
	BlurEnabled                 *bool                                                           `json:"blur_enabled,omitzero"`
	SharpenEnabled              *bool                                                           `json:"sharpen_enabled,omitzero"`
	RotationEnabled             *bool                                                           `json:"rotation_enabled,omitzero"`
	FlipEnabled                 *bool                                                           `json:"flip_enabled,omitzero"`
	GrayscaleEnabled            *bool                                                           `json:"grayscale_enabled,omitzero"`
	TrimEnabled                 *bool                                                           `json:"trim_enabled,omitzero"`
	ProgressiveJpegEnabled      *bool                                                           `json:"progressive_jpeg_enabled,omitzero"`
	StillFrameExtractionEnabled *bool                                                           `json:"still_frame_extraction_enabled,omitzero"`
	ColorAdjustmentsEnabled     *bool                                                           `json:"color_adjustments_enabled,omitzero"`
	NegateEnabled               *bool                                                           `json:"negate_enabled,omitzero"`
	BorderRadiusEnabled         *bool                                                           `json:"border_radius_enabled,omitzero"`
	WatermarkEnabled            *bool                                                           `json:"watermark_enabled,omitzero"`
	FaceBlurEnabled             *bool                                                           `json:"face_blur_enabled,omitzero"`
	SaveDataQualityEnabled      *bool                                                           `json:"save_data_quality_enabled,omitzero"`
	MetadataMode                *string                                                         `json:"metadata_mode,omitzero"`
	AllowedGravityAnchors       []string                                                        `json:"allowed_gravity_anchors,omitzero"`
}

type UpdateContainerSettingsRequest struct {
	ACL               *UpdateContainerSettingsRequestACL               `json:"acl,omitzero"`
	ImageOptimization *UpdateContainerSettingsRequestImageOptimization `json:"image_optimization,omitzero"`
}

type UpdateContainerSettingsResponse = CreateContainerResponse

type CancelContainerDeletionResponse = CreateContainerResponse

type ChangeContainerClassRequest struct {
	StorageClass string `json:"storage_class"`
}

type ChangeContainerClassResponse = CreateContainerResponse

type UpdateContainerTransitionPolicyRequestRulesItem struct {
	FromClass string `json:"from_class"`
	ToClass   string `json:"to_class"`
	AfterDays int64  `json:"after_days"`
}

type UpdateContainerTransitionPolicyRequest struct {
	IsEnabled bool                                              `json:"is_enabled"`
	Rules     []UpdateContainerTransitionPolicyRequestRulesItem `json:"rules,omitzero"`
}

type UpdateContainerTransitionPolicyResponse = CreateContainerResponse
