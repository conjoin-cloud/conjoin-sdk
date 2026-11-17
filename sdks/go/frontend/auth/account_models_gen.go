package auth

type BatchLookupAccountsRequest struct {
	AccountIDs []string `json:"account_ids"`
}

type BatchLookupAccountsResponseItem struct {
	AccountID string  `json:"account_id"`
	Name      *string `json:"name"`
	ImageURL  *string `json:"image_url"`
}
