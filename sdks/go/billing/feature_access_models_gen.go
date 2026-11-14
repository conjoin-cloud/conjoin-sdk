package billing

type CheckEntitlementRequest struct {
	CustomerID  *string `json:"customer_id,omitzero"`
	ReferenceID *string `json:"reference_id,omitzero"`
	FeatureID   string  `json:"feature_id"`
	Consume     *bool   `json:"consume,omitzero"`
	Value       *int64  `json:"value,omitzero"`
}

type CheckEntitlementResponse struct {
	Allowed     bool     `json:"allowed"`
	FeatureID   string   `json:"feature_id"`
	FeatureKey  string   `json:"feature_key"`
	FeatureType string   `json:"feature_type"`
	Balance     *float64 `json:"balance,omitzero"`
	Used        *float64 `json:"used,omitzero"`
	Limit       any      `json:"limit,omitzero"`
	Consumed    *float64 `json:"consumed,omitzero"`
	GrantedBy   []string `json:"granted_by"`
}

type TrackFeatureUsageRequest struct {
	CustomerID  *string `json:"customer_id,omitzero"`
	ReferenceID *string `json:"reference_id,omitzero"`
	FeatureID   string  `json:"feature_id"`
	Value       int64   `json:"value"`
}

type TrackFeatureUsageResponse struct {
	Tracked    bool    `json:"tracked"`
	FeatureID  string  `json:"feature_id"`
	CustomerID string  `json:"customer_id"`
	Value      float64 `json:"value"`
}
