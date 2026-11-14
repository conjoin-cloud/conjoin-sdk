package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type GetProjectBrandingResponse struct {
	BrandingID    string                           `json:"branding_id"`
	ProjectID     string                           `json:"project_id"`
	SchemaVersion float64                          `json:"schema_version"`
	General       map[string]any                   `json:"general,omitzero"`
	Colors        map[string]any                   `json:"colors,omitzero"`
	Typography    map[string]any                   `json:"typography,omitzero"`
	Borders       map[string]any                   `json:"borders,omitzero"`
	Spacing       map[string]any                   `json:"spacing,omitzero"`
	Shadows       map[string]any                   `json:"shadows,omitzero"`
	Components    map[string]any                   `json:"components,omitzero"`
	Layout        map[string]any                   `json:"layout,omitzero"`
	Animation     map[string]any                   `json:"animation,omitzero"`
	Accessibility map[string]any                   `json:"accessibility,omitzero"`
	Organization  conjoin.Nullable[map[string]any] `json:"organization,omitzero"`
	DateCreated   string                           `json:"date_created"`
	DateUpdated   conjoin.Nullable[string]         `json:"date_updated,omitzero"`
}

type PatchProjectBrandingRequestGeneral struct {
	LogoURL                conjoin.Nullable[string] `json:"logo_url,omitzero"`
	LogoDarkURL            conjoin.Nullable[string] `json:"logo_dark_url,omitzero"`
	FaviconURL             conjoin.Nullable[string] `json:"favicon_url,omitzero"`
	AppName                conjoin.Nullable[string] `json:"app_name,omitzero"`
	SupportEmail           conjoin.Nullable[string] `json:"support_email,omitzero"`
	SupportURL             conjoin.Nullable[string] `json:"support_url,omitzero"`
	PrivacyPolicyURL       conjoin.Nullable[string] `json:"privacy_policy_url,omitzero"`
	TermsOfServiceURL      conjoin.Nullable[string] `json:"terms_of_service_url,omitzero"`
	DisableConjoinBranding *bool                    `json:"disable_conjoin_branding,omitzero"`
}

type PatchProjectBrandingRequestColorsLight struct {
	Primary           conjoin.Nullable[string] `json:"primary,omitzero"`
	PrimaryContrast   conjoin.Nullable[string] `json:"primary_contrast,omitzero"`
	Secondary         conjoin.Nullable[string] `json:"secondary,omitzero"`
	SecondaryContrast conjoin.Nullable[string] `json:"secondary_contrast,omitzero"`
	Accent            conjoin.Nullable[string] `json:"accent,omitzero"`
	AccentContrast    conjoin.Nullable[string] `json:"accent_contrast,omitzero"`
	Background        conjoin.Nullable[string] `json:"background,omitzero"`
	Text              conjoin.Nullable[string] `json:"text,omitzero"`
	Subtle            conjoin.Nullable[string] `json:"subtle,omitzero"`
	SubtleText        conjoin.Nullable[string] `json:"subtle_text,omitzero"`
	Panel             conjoin.Nullable[string] `json:"panel,omitzero"`
	PanelText         conjoin.Nullable[string] `json:"panel_text,omitzero"`
	Border            conjoin.Nullable[string] `json:"border,omitzero"`
	Input             conjoin.Nullable[string] `json:"input,omitzero"`
	FocusRing         conjoin.Nullable[string] `json:"focus_ring,omitzero"`
	Danger            conjoin.Nullable[string] `json:"danger,omitzero"`
	DangerContrast    conjoin.Nullable[string] `json:"danger_contrast,omitzero"`
	Success           conjoin.Nullable[string] `json:"success,omitzero"`
	SuccessContrast   conjoin.Nullable[string] `json:"success_contrast,omitzero"`
	Warning           conjoin.Nullable[string] `json:"warning,omitzero"`
	WarningContrast   conjoin.Nullable[string] `json:"warning_contrast,omitzero"`
	Info              conjoin.Nullable[string] `json:"info,omitzero"`
	InfoContrast      conjoin.Nullable[string] `json:"info_contrast,omitzero"`
	Overlay           conjoin.Nullable[string] `json:"overlay,omitzero"`
}

type PatchProjectBrandingRequestColors struct {
	Light *PatchProjectBrandingRequestColorsLight `json:"light,omitzero"`
	Dark  *PatchProjectBrandingRequestColorsLight `json:"dark,omitzero"`
}

type PatchProjectBrandingRequestTypography struct {
	FontFamilyHeading    conjoin.Nullable[string] `json:"font_family_heading,omitzero"`
	FontFamilyBody       conjoin.Nullable[string] `json:"font_family_body,omitzero"`
	FontFamilyMono       conjoin.Nullable[string] `json:"font_family_mono,omitzero"`
	FontSizeBase         conjoin.Nullable[string] `json:"font_size_base,omitzero"`
	FontWeightHeading    conjoin.Nullable[string] `json:"font_weight_heading,omitzero"`
	FontWeightBody       conjoin.Nullable[string] `json:"font_weight_body,omitzero"`
	LineHeightBase       conjoin.Nullable[string] `json:"line_height_base,omitzero"`
	LetterSpacingHeading conjoin.Nullable[string] `json:"letter_spacing_heading,omitzero"`
	LetterSpacingBody    conjoin.Nullable[string] `json:"letter_spacing_body,omitzero"`
}

type PatchProjectBrandingRequestBorders struct {
	RadiusSm     conjoin.Nullable[string] `json:"radius_sm,omitzero"`
	RadiusMd     conjoin.Nullable[string] `json:"radius_md,omitzero"`
	RadiusLg     conjoin.Nullable[string] `json:"radius_lg,omitzero"`
	RadiusFull   conjoin.Nullable[string] `json:"radius_full,omitzero"`
	WidthDefault conjoin.Nullable[string] `json:"width_default,omitzero"`
	ColorDefault conjoin.Nullable[string] `json:"color_default,omitzero"`
}

type PatchProjectBrandingRequestSpacing struct {
	Unit        conjoin.Nullable[string]  `json:"unit,omitzero"`
	ScaleFactor conjoin.Nullable[float64] `json:"scale_factor,omitzero"`
}

type PatchProjectBrandingRequestShadows struct {
	Sm    conjoin.Nullable[string] `json:"sm,omitzero"`
	Md    conjoin.Nullable[string] `json:"md,omitzero"`
	Lg    conjoin.Nullable[string] `json:"lg,omitzero"`
	Xl    conjoin.Nullable[string] `json:"xl,omitzero"`
	Inner conjoin.Nullable[string] `json:"inner,omitzero"`
	None  conjoin.Nullable[string] `json:"none,omitzero"`
}

type PatchProjectBrandingRequestComponentsButton struct {
	BorderRadius  conjoin.Nullable[string] `json:"border_radius,omitzero"`
	FontWeight    conjoin.Nullable[string] `json:"font_weight,omitzero"`
	TextTransform conjoin.Nullable[string] `json:"text_transform,omitzero"`
	PaddingX      conjoin.Nullable[string] `json:"padding_x,omitzero"`
	PaddingY      conjoin.Nullable[string] `json:"padding_y,omitzero"`
}

type PatchProjectBrandingRequestComponentsInput struct {
	BorderRadius conjoin.Nullable[string] `json:"border_radius,omitzero"`
	BorderWidth  conjoin.Nullable[string] `json:"border_width,omitzero"`
	PaddingX     conjoin.Nullable[string] `json:"padding_x,omitzero"`
	PaddingY     conjoin.Nullable[string] `json:"padding_y,omitzero"`
}

type PatchProjectBrandingRequestComponentsCard struct {
	BorderRadius conjoin.Nullable[string] `json:"border_radius,omitzero"`
	Padding      conjoin.Nullable[string] `json:"padding,omitzero"`
	Shadow       conjoin.Nullable[string] `json:"shadow,omitzero"`
}

type PatchProjectBrandingRequestComponentsSocialButton struct {
	BorderRadius conjoin.Nullable[string] `json:"border_radius,omitzero"`
	Style        conjoin.Nullable[string] `json:"style,omitzero"`
}

type PatchProjectBrandingRequestComponentsPricingCard struct {
	BorderRadius   conjoin.Nullable[string] `json:"border_radius,omitzero"`
	HighlightColor conjoin.Nullable[string] `json:"highlight_color,omitzero"`
}

type PatchProjectBrandingRequestComponentsPeriodToggle struct {
	Style conjoin.Nullable[string] `json:"style,omitzero"`
}

type PatchProjectBrandingRequestComponentsFileUploader struct {
	BorderStyle  conjoin.Nullable[string] `json:"border_style,omitzero"`
	BorderRadius conjoin.Nullable[string] `json:"border_radius,omitzero"`
}

type PatchProjectBrandingRequestComponentsChatWidget struct {
	BorderRadius conjoin.Nullable[string] `json:"border_radius,omitzero"`
	Position     conjoin.Nullable[string] `json:"position,omitzero"`
}

type PatchProjectBrandingRequestComponents struct {
	Button       *PatchProjectBrandingRequestComponentsButton       `json:"button,omitzero"`
	Input        *PatchProjectBrandingRequestComponentsInput        `json:"input,omitzero"`
	Card         *PatchProjectBrandingRequestComponentsCard         `json:"card,omitzero"`
	SocialButton *PatchProjectBrandingRequestComponentsSocialButton `json:"social_button,omitzero"`
	PricingCard  *PatchProjectBrandingRequestComponentsPricingCard  `json:"pricing_card,omitzero"`
	PeriodToggle *PatchProjectBrandingRequestComponentsPeriodToggle `json:"period_toggle,omitzero"`
	FileUploader *PatchProjectBrandingRequestComponentsFileUploader `json:"file_uploader,omitzero"`
	ChatWidget   *PatchProjectBrandingRequestComponentsChatWidget   `json:"chat_widget,omitzero"`
}

type PatchProjectBrandingRequestLayout struct {
	ContainerMaxWidth conjoin.Nullable[string] `json:"container_max_width,omitzero"`
	ContentMaxWidth   conjoin.Nullable[string] `json:"content_max_width,omitzero"`
	SidebarWidth      conjoin.Nullable[string] `json:"sidebar_width,omitzero"`
}

type PatchProjectBrandingRequestAnimation struct {
	Enabled               *bool                    `json:"enabled,omitzero"`
	DurationFast          conjoin.Nullable[string] `json:"duration_fast,omitzero"`
	DurationNormal        conjoin.Nullable[string] `json:"duration_normal,omitzero"`
	DurationSlow          conjoin.Nullable[string] `json:"duration_slow,omitzero"`
	EasingDefault         conjoin.Nullable[string] `json:"easing_default,omitzero"`
	ReducedMotionBehavior *string                  `json:"reduced_motion_behavior,omitzero"`
}

type PatchProjectBrandingRequestAccessibility struct {
	FocusRingStyle  conjoin.Nullable[string] `json:"focus_ring_style,omitzero"`
	FocusRingColor  conjoin.Nullable[string] `json:"focus_ring_color,omitzero"`
	FocusRingOffset conjoin.Nullable[string] `json:"focus_ring_offset,omitzero"`
}

type PatchProjectBrandingRequestOrganization struct {
	LogoURL      conjoin.Nullable[string] `json:"logo_url,omitzero"`
	LogoDarkURL  conjoin.Nullable[string] `json:"logo_dark_url,omitzero"`
	Name         conjoin.Nullable[string] `json:"name,omitzero"`
	SupportEmail conjoin.Nullable[string] `json:"support_email,omitzero"`
}

type PatchProjectBrandingRequest struct {
	General       *PatchProjectBrandingRequestGeneral                       `json:"general,omitzero"`
	Colors        *PatchProjectBrandingRequestColors                        `json:"colors,omitzero"`
	Typography    *PatchProjectBrandingRequestTypography                    `json:"typography,omitzero"`
	Borders       *PatchProjectBrandingRequestBorders                       `json:"borders,omitzero"`
	Spacing       *PatchProjectBrandingRequestSpacing                       `json:"spacing,omitzero"`
	Shadows       *PatchProjectBrandingRequestShadows                       `json:"shadows,omitzero"`
	Components    *PatchProjectBrandingRequestComponents                    `json:"components,omitzero"`
	Layout        *PatchProjectBrandingRequestLayout                        `json:"layout,omitzero"`
	Animation     *PatchProjectBrandingRequestAnimation                     `json:"animation,omitzero"`
	Accessibility *PatchProjectBrandingRequestAccessibility                 `json:"accessibility,omitzero"`
	Organization  conjoin.Nullable[PatchProjectBrandingRequestOrganization] `json:"organization,omitzero"`
}

type PatchProjectBrandingResponse = GetProjectBrandingResponse

type GetOrgBrandingOverrideResponse struct {
	OverrideID     string                           `json:"override_id"`
	OrganizationID string                           `json:"organization_id"`
	SchemaVersion  float64                          `json:"schema_version"`
	General        conjoin.Nullable[map[string]any] `json:"general,omitzero"`
	Colors         conjoin.Nullable[map[string]any] `json:"colors,omitzero"`
	Typography     conjoin.Nullable[map[string]any] `json:"typography,omitzero"`
	Borders        conjoin.Nullable[map[string]any] `json:"borders,omitzero"`
	Spacing        conjoin.Nullable[map[string]any] `json:"spacing,omitzero"`
	Shadows        conjoin.Nullable[map[string]any] `json:"shadows,omitzero"`
	Components     conjoin.Nullable[map[string]any] `json:"components,omitzero"`
	Layout         conjoin.Nullable[map[string]any] `json:"layout,omitzero"`
	Animation      conjoin.Nullable[map[string]any] `json:"animation,omitzero"`
	Accessibility  conjoin.Nullable[map[string]any] `json:"accessibility,omitzero"`
	Organization   conjoin.Nullable[map[string]any] `json:"organization,omitzero"`
	DateCreated    string                           `json:"date_created"`
	DateUpdated    conjoin.Nullable[string]         `json:"date_updated,omitzero"`
}

type PatchOrgBrandingOverrideRequest struct {
	General       conjoin.Nullable[PatchProjectBrandingRequestGeneral]       `json:"general,omitzero"`
	Colors        conjoin.Nullable[PatchProjectBrandingRequestColors]        `json:"colors,omitzero"`
	Typography    conjoin.Nullable[PatchProjectBrandingRequestTypography]    `json:"typography,omitzero"`
	Borders       conjoin.Nullable[PatchProjectBrandingRequestBorders]       `json:"borders,omitzero"`
	Spacing       conjoin.Nullable[PatchProjectBrandingRequestSpacing]       `json:"spacing,omitzero"`
	Shadows       conjoin.Nullable[PatchProjectBrandingRequestShadows]       `json:"shadows,omitzero"`
	Components    conjoin.Nullable[PatchProjectBrandingRequestComponents]    `json:"components,omitzero"`
	Layout        conjoin.Nullable[PatchProjectBrandingRequestLayout]        `json:"layout,omitzero"`
	Animation     conjoin.Nullable[PatchProjectBrandingRequestAnimation]     `json:"animation,omitzero"`
	Accessibility conjoin.Nullable[PatchProjectBrandingRequestAccessibility] `json:"accessibility,omitzero"`
	Organization  conjoin.Nullable[PatchProjectBrandingRequestOrganization]  `json:"organization,omitzero"`
}

type PatchOrgBrandingOverrideResponse = GetOrgBrandingOverrideResponse
