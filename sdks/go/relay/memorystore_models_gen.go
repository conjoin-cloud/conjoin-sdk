package relay

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadMemorystoreClustersQuery struct {
	Status      *string                            `json:"status,omitzero"`
	ClusterType *string                            `json:"cluster_type,omitzero"`
	ReferenceID *string                            `json:"reference_id,omitzero"`
	DateCreated *ReadEventChannelsQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ReadBroadcastChannelsQueryCursor  `json:"cursor,omitzero"`
	Sort        map[string]string                  `json:"sort,omitzero"`
	Limit       any                                `json:"limit,omitzero"`
}

type ReadMemorystoreClustersItem struct {
	ClusterID        string                    `json:"cluster_id"`
	ConjoinAccountID string                    `json:"conjoin_account_id"`
	ConjoinProjectID string                    `json:"conjoin_project_id"`
	ReferenceID      conjoin.Nullable[string]  `json:"reference_id,omitzero"`
	LiveMode         bool                      `json:"live_mode"`
	Name             string                    `json:"name"`
	ClusterType      string                    `json:"cluster_type"`
	NamespacePrefix  *string                   `json:"namespace_prefix,omitzero"`
	ConnectionURI    conjoin.Nullable[string]  `json:"connection_uri,omitzero"`
	Region           conjoin.Nullable[string]  `json:"region,omitzero"`
	MaxMemoryMb      conjoin.Nullable[float64] `json:"max_memory_mb,omitzero"`
	Status           string                    `json:"status"`
	GcpInstanceID    conjoin.Nullable[string]  `json:"gcp_instance_id,omitzero"`
	GcpInstanceName  conjoin.Nullable[string]  `json:"gcp_instance_name,omitzero"`
	EncryptionAtRest *bool                     `json:"encryption_at_rest,omitzero"`
	TcpAccessEnabled *bool                     `json:"tcp_access_enabled,omitzero"`
	Description      conjoin.Nullable[string]  `json:"description,omitzero"`
	Metadata         map[string]any            `json:"metadata,omitzero"`
	DateCreated      string                    `json:"date_created"`
	DateUpdated      string                    `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]  `json:"date_deleted,omitzero"`
}

type CreateMemorystoreClusterRequest struct {
	Name        string  `json:"name"`
	ClusterType *string `json:"cluster_type,omitzero"`
	Region      *string `json:"region,omitzero"`
	MaxMemoryMb *int64  `json:"max_memory_mb,omitzero"`
	ReferenceID *string `json:"reference_id,omitzero"`
	Description *string `json:"description,omitzero"`
}

type CreateMemorystoreClusterResponse = ReadMemorystoreClustersItem

type ReadMemorystoreClustersCountQuery = ReadMemorystoreClustersQuery

type ReadMemorystoreClustersCountResponse = ReadBroadcastChannelsCountResponse

type ReadMemorystoreClusterResponse = ReadMemorystoreClustersItem

type UpdateMemorystoreClusterRequest struct {
	Name        *string `json:"name,omitzero"`
	MaxMemoryMb *int64  `json:"max_memory_mb,omitzero"`
	Description *string `json:"description,omitzero"`
}

type UpdateMemorystoreClusterResponse = ReadMemorystoreClustersItem

type DeleteMemorystoreClusterResponse = ReadMemorystoreClustersItem

type SuspendMemorystoreClusterResponse = ReadMemorystoreClustersItem

type ExecuteMemorystoreCommandRequest struct {
	Command string `json:"command"`
	Args    []any  `json:"args,omitzero"`
}

type ExecuteMemorystoreCommandResponse struct {
	Result any `json:"result"`
}
