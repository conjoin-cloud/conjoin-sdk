package ai

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreatePolicyCheckRequestContext struct {
	Model     *string `json:"model,omitzero"`
	RequestID *string `json:"request_id,omitzero"`
}

type CreatePolicyCheckRequest struct {
	Content   string                           `json:"content"`
	Direction string                           `json:"direction"`
	Context   *CreatePolicyCheckRequestContext `json:"context,omitzero"`
}

type CreatePolicyCheckResponseMatchedRulesItemDetectionsItemPosition struct {
	Start float64 `json:"start"`
	End   float64 `json:"end"`
}

type CreatePolicyCheckResponseMatchedRulesItemDetectionsItem struct {
	Type       string                                                          `json:"type"`
	Value      string                                                          `json:"value"`
	Position   CreatePolicyCheckResponseMatchedRulesItemDetectionsItemPosition `json:"position"`
	Confidence float64                                                         `json:"confidence"`
}

type CreatePolicyCheckResponseMatchedRulesItem struct {
	RuleID     string                                                    `json:"rule_id"`
	RuleType   string                                                    `json:"rule_type"`
	Action     string                                                    `json:"action"`
	Detections []CreatePolicyCheckResponseMatchedRulesItemDetectionsItem `json:"detections"`
}

type CreatePolicyCheckResponse struct {
	Allowed            bool                                        `json:"allowed"`
	ActionTaken        string                                      `json:"action_taken"`
	MatchedRules       []CreatePolicyCheckResponseMatchedRulesItem `json:"matched_rules"`
	TransformedContent conjoin.Nullable[string]                    `json:"transformed_content,omitzero"`
}

type ListPolicyLogsQuery struct {
	RuleID      *string                          `json:"rule_id,omitzero"`
	RuleType    *string                          `json:"rule_type,omitzero"`
	ActionTaken *string                          `json:"action_taken,omitzero"`
	Severity    *string                          `json:"severity,omitzero"`
	Direction   *string                          `json:"direction,omitzero"`
	LoggedAt    *ListByokConfigsQueryDateCreated `json:"logged_at,omitzero"`
	Cursor      *ListByokConfigsQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string                `json:"sort,omitzero"`
	Limit       any                              `json:"limit,omitzero"`
}

type ListPolicyLogsItem struct {
	LogID            string                                                    `json:"log_id"`
	ConjoinAccountID string                                                    `json:"conjoin_account_id"`
	ConjoinProjectID string                                                    `json:"conjoin_project_id"`
	LiveMode         bool                                                      `json:"live_mode"`
	RequestID        string                                                    `json:"request_id"`
	RuleID           string                                                    `json:"rule_id"`
	RuleType         string                                                    `json:"rule_type"`
	ActionTaken      string                                                    `json:"action_taken"`
	Direction        string                                                    `json:"direction"`
	Detections       []CreatePolicyCheckResponseMatchedRulesItemDetectionsItem `json:"detections"`
	Severity         string                                                    `json:"severity"`
	LoggedAt         string                                                    `json:"logged_at"`
	DateCreated      string                                                    `json:"date_created"`
}

type ListPolicyLogsCountQuery = ListPolicyLogsQuery

type ListPolicyLogsCountResponse = ListByokConfigsCountResponse

type ListPolicyRulesQuery struct {
	RuleType    *string                          `json:"rule_type,omitzero"`
	Status      *string                          `json:"status,omitzero"`
	IsActive    any                              `json:"is_active,omitzero"`
	ReferenceID *string                          `json:"reference_id,omitzero"`
	DateCreated *ListByokConfigsQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListByokConfigsQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string                `json:"sort,omitzero"`
	Limit       any                              `json:"limit,omitzero"`
}

type ListPolicyRulesItemConfig struct {
	Patterns            []string `json:"patterns"`
	PiiTypes            []string `json:"pii_types"`
	Topics              []string `json:"topics"`
	Regex               []string `json:"regex"`
	ReplacementTemplate string   `json:"replacement_template"`
}

type ListPolicyRulesItem struct {
	RuleID           string                    `json:"rule_id"`
	ConjoinAccountID string                    `json:"conjoin_account_id"`
	ConjoinProjectID string                    `json:"conjoin_project_id"`
	LiveMode         bool                      `json:"live_mode"`
	ReferenceID      *string                   `json:"reference_id"`
	Name             string                    `json:"name"`
	RuleType         string                    `json:"rule_type"`
	Direction        string                    `json:"direction"`
	Action           string                    `json:"action"`
	Priority         float64                   `json:"priority"`
	Config           ListPolicyRulesItemConfig `json:"config"`
	IsActive         bool                      `json:"is_active"`
	Status           string                    `json:"status"`
	Description      conjoin.Nullable[string]  `json:"description,omitzero"`
	Metadata         map[string]any            `json:"metadata"`
	DateCreated      string                    `json:"date_created"`
	DateUpdated      *string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]  `json:"date_deleted,omitzero"`
}

type CreatePolicyRuleRequestConfig struct {
	Patterns            []string `json:"patterns,omitzero"`
	PiiTypes            []string `json:"pii_types,omitzero"`
	Topics              []string `json:"topics,omitzero"`
	Regex               *string  `json:"regex,omitzero"`
	ReplacementTemplate *string  `json:"replacement_template,omitzero"`
}

type CreatePolicyRuleRequest struct {
	Name        string                        `json:"name"`
	RuleType    string                        `json:"rule_type"`
	Direction   string                        `json:"direction"`
	Action      string                        `json:"action"`
	Priority    *int64                        `json:"priority,omitzero"`
	Config      CreatePolicyRuleRequestConfig `json:"config"`
	Description conjoin.Nullable[string]      `json:"description,omitzero"`
	ReferenceID conjoin.Nullable[string]      `json:"reference_id,omitzero"`
	Metadata    map[string]any                `json:"metadata,omitzero"`
}

type CreatePolicyRuleResponse = ListPolicyRulesItem

type ListPolicyRulesCountQuery = ListPolicyRulesQuery

type ListPolicyRulesCountResponse = ListByokConfigsCountResponse

type ReadPolicyRuleResponse = ListPolicyRulesItem

type UpdatePolicyRuleRequest struct {
	Name        *string                        `json:"name,omitzero"`
	Direction   *string                        `json:"direction,omitzero"`
	Action      *string                        `json:"action,omitzero"`
	Priority    *int64                         `json:"priority,omitzero"`
	Config      *CreatePolicyRuleRequestConfig `json:"config,omitzero"`
	IsActive    *bool                          `json:"is_active,omitzero"`
	Status      *string                        `json:"status,omitzero"`
	Description conjoin.Nullable[string]       `json:"description,omitzero"`
	Metadata    map[string]any                 `json:"metadata,omitzero"`
}

type UpdatePolicyRuleResponse = ListPolicyRulesItem

type DeletePolicyRuleResponse = ListPolicyRulesItem
