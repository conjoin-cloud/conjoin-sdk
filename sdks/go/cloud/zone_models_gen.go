package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadZonesQuery = ListPublishableKeysQuery

type ReadZonesItemVerificationRecord struct {
	Type  string `json:"type"`
	Name  string `json:"name"`
	Value string `json:"value"`
}

type ReadZonesItemDNSRecordsItem struct {
	ID           string   `json:"id"`
	Type         string   `json:"type"`
	Value        string   `json:"value"`
	TTL          *float64 `json:"ttl,omitzero"`
	MxPriority   *string  `json:"mx_priority,omitzero"`
	DkimSelector *string  `json:"dkim_selector,omitzero"`
	Name         *string  `json:"name,omitzero"`
	MailPolicy   *string  `json:"mail_policy,omitzero"`
	LastVerified *string  `json:"last_verified"`
}

type ReadZonesItemExternalDNSRecordsItem struct {
	ID           string   `json:"id"`
	Type         string   `json:"type"`
	Value        string   `json:"value"`
	TTL          *float64 `json:"ttl,omitzero"`
	MxPriority   *string  `json:"mx_priority,omitzero"`
	DkimSelector *string  `json:"dkim_selector,omitzero"`
	Name         *string  `json:"name,omitzero"`
	MailPolicy   *string  `json:"mail_policy,omitzero"`
}

type ReadZonesItem struct {
	CloudAccountID     string                                `json:"cloud_account_id"`
	EntityID           string                                `json:"entity_id"`
	ProjectID          string                                `json:"project_id"`
	ZoneID             string                                `json:"zone_id"`
	ReferenceID        *string                               `json:"reference_id,omitzero"`
	ProviderID         string                                `json:"provider_id"`
	DkimAuthority      string                                `json:"dkim_authority"`
	Domain             string                                `json:"domain"`
	Status             string                                `json:"status"`
	VerificationRecord *ReadZonesItemVerificationRecord      `json:"verification_record"`
	DNSRecords         []ReadZonesItemDNSRecordsItem         `json:"dns_records"`
	ExternalDNSRecords []ReadZonesItemExternalDNSRecordsItem `json:"external_dns_records"`
	IsInternalZone     bool                                  `json:"is_internal_zone"`
	DateCreated        string                                `json:"date_created"`
	DateUpdated        conjoin.Nullable[string]              `json:"date_updated,omitzero"`
	DateDeleted        conjoin.Nullable[string]              `json:"date_deleted,omitzero"`
}

type CreateZoneRequestDNSRecordsItem struct {
	Type         string                   `json:"type"`
	Value        string                   `json:"value"`
	TTL          conjoin.Nullable[int64]  `json:"ttl,omitzero"`
	MxPriority   conjoin.Nullable[int64]  `json:"mx_priority,omitzero"`
	DkimSelector conjoin.Nullable[string] `json:"dkim_selector,omitzero"`
	Name         conjoin.Nullable[string] `json:"name,omitzero"`
	MailPolicy   conjoin.Nullable[string] `json:"mail_policy,omitzero"`
}

type CreateZoneRequest struct {
	ProviderID    string                            `json:"provider_id"`
	Domain        string                            `json:"domain"`
	DkimAuthority *string                           `json:"dkim_authority,omitzero"`
	DNSRecords    []CreateZoneRequestDNSRecordsItem `json:"dns_records,omitzero"`
}

type CreateZoneResponse = ReadZonesItem

type ReadZonesCountQuery = ListPublishableKeysQuery

type ReadZonesCountResponse = ReadApiKeysCountResponse

type ReadZoneResponse = ReadZonesItem
