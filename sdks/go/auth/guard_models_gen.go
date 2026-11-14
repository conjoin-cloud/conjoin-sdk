package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListGuardRulesQuery struct {
	Action *string                     `json:"action,omitzero"`
	Cursor *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort   map[string]string           `json:"sort,omitzero"`
	Limit  any                         `json:"limit,omitzero"`
}

type ListGuardRulesItem struct {
	RuleID           string                   `json:"rule_id"`
	AppID            string                   `json:"app_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	Name             string                   `json:"name"`
	Description      conjoin.Nullable[string] `json:"description,omitzero"`
	Action           string                   `json:"action"`
	Predicate        map[string]any           `json:"predicate"`
	IsEnabled        *bool                    `json:"is_enabled,omitzero"`
	ExpiresAt        conjoin.Nullable[string] `json:"expires_at,omitzero"`
	Metadata         map[string]any           `json:"metadata,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      *string                  `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateGuardRuleRequestPredicateAllItemAllItemAllItem struct {
	Kind       *string  `json:"kind,omitzero"`
	Detection  *string  `json:"detection,omitzero"`
	EventTypes []string `json:"event_types,omitzero"`
	Countries  []string `json:"countries,omitzero"`
	Ranges     []string `json:"ranges,omitzero"`
	Domains    []string `json:"domains,omitzero"`
	Value      any      `json:"value,omitzero"`
}

type CreateGuardRuleRequestPredicateAllItemAllItem struct {
	Kind       *string                                                `json:"kind,omitzero"`
	Detection  *string                                                `json:"detection,omitzero"`
	EventTypes []string                                               `json:"event_types,omitzero"`
	Countries  []string                                               `json:"countries,omitzero"`
	Ranges     []string                                               `json:"ranges,omitzero"`
	Domains    []string                                               `json:"domains,omitzero"`
	Value      any                                                    `json:"value,omitzero"`
	All        []CreateGuardRuleRequestPredicateAllItemAllItemAllItem `json:"all,omitzero"`
	Any        []CreateGuardRuleRequestPredicateAllItemAllItemAllItem `json:"any,omitzero"`
	Not        *CreateGuardRuleRequestPredicateAllItemAllItemAllItem  `json:"not,omitzero"`
}

type CreateGuardRuleRequestPredicateAllItem struct {
	Kind       *string                                         `json:"kind,omitzero"`
	Detection  *string                                         `json:"detection,omitzero"`
	EventTypes []string                                        `json:"event_types,omitzero"`
	Countries  []string                                        `json:"countries,omitzero"`
	Ranges     []string                                        `json:"ranges,omitzero"`
	Domains    []string                                        `json:"domains,omitzero"`
	Value      any                                             `json:"value,omitzero"`
	All        []CreateGuardRuleRequestPredicateAllItemAllItem `json:"all,omitzero"`
	Any        []CreateGuardRuleRequestPredicateAllItemAllItem `json:"any,omitzero"`
	Not        *CreateGuardRuleRequestPredicateAllItemAllItem  `json:"not,omitzero"`
}

type CreateGuardRuleRequestPredicate struct {
	Kind       *string                                  `json:"kind,omitzero"`
	Detection  *string                                  `json:"detection,omitzero"`
	EventTypes []string                                 `json:"event_types,omitzero"`
	Countries  []string                                 `json:"countries,omitzero"`
	Ranges     []string                                 `json:"ranges,omitzero"`
	Domains    []string                                 `json:"domains,omitzero"`
	Value      any                                      `json:"value,omitzero"`
	All        []CreateGuardRuleRequestPredicateAllItem `json:"all,omitzero"`
	Any        []CreateGuardRuleRequestPredicateAllItem `json:"any,omitzero"`
	Not        *CreateGuardRuleRequestPredicateAllItem  `json:"not,omitzero"`
}

type CreateGuardRuleRequest struct {
	Name        string                          `json:"name"`
	Description conjoin.Nullable[string]        `json:"description,omitzero"`
	Action      string                          `json:"action"`
	Predicate   CreateGuardRuleRequestPredicate `json:"predicate"`
	IsEnabled   *bool                           `json:"is_enabled,omitzero"`
	ExpiresAt   conjoin.Nullable[string]        `json:"expires_at,omitzero"`
}

type CreateGuardRuleResponse = ListGuardRulesItem

type ListGuardRulesCountQuery = ListGuardRulesQuery

type ListGuardRulesCountResponse = ListCredentialsCountResponse

type ReadGuardRuleResponse = ListGuardRulesItem

type UpdateGuardRuleRequest struct {
	Name        *string                          `json:"name,omitzero"`
	Description conjoin.Nullable[string]         `json:"description,omitzero"`
	Action      *string                          `json:"action,omitzero"`
	Predicate   *CreateGuardRuleRequestPredicate `json:"predicate,omitzero"`
	IsEnabled   *bool                            `json:"is_enabled,omitzero"`
	ExpiresAt   conjoin.Nullable[string]         `json:"expires_at,omitzero"`
}

type UpdateGuardRuleResponse = ListGuardRulesItem

type DeleteGuardRuleResponse = DeleteEnterpriseConnectionResponse

type ListGuardEventsQuery struct {
	EventType *string                     `json:"event_type,omitzero"`
	AccountID *string                     `json:"account_id,omitzero"`
	Cursor    *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort      map[string]string           `json:"sort,omitzero"`
	Limit     any                         `json:"limit,omitzero"`
}

type ListGuardEventsItemDetailsDetectionsItem struct {
	Detection string  `json:"detection"`
	Triggered bool    `json:"triggered"`
	Reason    *string `json:"reason"`
}

type ListGuardEventsItemDetailsMatchedRulesItem struct {
	RuleID string `json:"rule_id"`
	Name   string `json:"name"`
	Action string `json:"action"`
}

type ListGuardEventsItemDetails struct {
	Reasons      []string                                     `json:"reasons"`
	Detections   []ListGuardEventsItemDetailsDetectionsItem   `json:"detections"`
	MatchedRules []ListGuardEventsItemDetailsMatchedRulesItem `json:"matched_rules,omitzero"`
}

type ListGuardEventsItem struct {
	EventID          string                      `json:"event_id"`
	AppID            string                      `json:"app_id"`
	ConjoinAccountID string                      `json:"conjoin_account_id"`
	ConjoinProjectID string                      `json:"conjoin_project_id"`
	LiveMode         bool                        `json:"live_mode"`
	EventType        string                      `json:"event_type"`
	ActionTaken      string                      `json:"action_taken"`
	IPAddress        conjoin.Nullable[string]    `json:"ip_address,omitzero"`
	UserAgent        conjoin.Nullable[string]    `json:"user_agent,omitzero"`
	AccountID        conjoin.Nullable[string]    `json:"account_id,omitzero"`
	Details          *ListGuardEventsItemDetails `json:"details,omitzero"`
	Metadata         map[string]any              `json:"metadata,omitzero"`
	DateCreated      string                      `json:"date_created"`
	DateUpdated      string                      `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]    `json:"date_deleted,omitzero"`
}

type ListGuardEventsCountQuery = ListGuardEventsQuery

type ListGuardEventsCountResponse = ListCredentialsCountResponse

type AddGuardTrustedIpRequest struct {
	IP string `json:"ip"`
}

type AddGuardTrustedIpResponse struct {
	IP      string  `json:"ip"`
	AddedAt *string `json:"added_at,omitzero"`
}

type RemoveGuardTrustedIpRequest = AddGuardTrustedIpRequest

type RemoveGuardTrustedIpResponse = AddGuardTrustedIpResponse

type AddGuardTrustedEmailRequest struct {
	Email string `json:"email"`
}

type AddGuardTrustedEmailResponse = AddGuardTrustedEmailRequest

type RemoveGuardTrustedEmailRequest = AddGuardTrustedEmailRequest

type RemoveGuardTrustedEmailResponse = AddGuardTrustedEmailRequest

type AddGuardTrustedDomainRequest struct {
	Domain string `json:"domain"`
}

type AddGuardTrustedDomainResponse = AddGuardTrustedDomainRequest

type RemoveGuardTrustedDomainRequest = AddGuardTrustedDomainRequest

type RemoveGuardTrustedDomainResponse = AddGuardTrustedDomainRequest

type ListGuardAnonymousIpsResponse struct {
	Ips []string `json:"ips"`
}

type AddGuardAnonymousIpsRequest = ListGuardAnonymousIpsResponse

type AddGuardAnonymousIpsResponse = ListGuardAnonymousIpsResponse

type RemoveGuardAnonymousIpsRequest = ListGuardAnonymousIpsResponse

type RemoveGuardAnonymousIpsResponse = ListGuardAnonymousIpsResponse
