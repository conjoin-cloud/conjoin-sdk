package auth

type RequestStepUpRequest struct {
	SessionID   string `json:"session_id"`
	OperationID string `json:"operation_id"`
}

type RequestStepUpResponse = StartSignupResponseStepUp

type VerifyStepUpRequest struct {
	SessionID         string  `json:"session_id"`
	OperationID       string  `json:"operation_id"`
	ChallengeID       string  `json:"challenge_id"`
	Method            string  `json:"method"`
	Code              *string `json:"code,omitzero"`
	Password          *string `json:"password,omitzero"`
	AssertionResponse any     `json:"assertion_response,omitzero"`
}

type VerifyStepUpResponse struct {
	StepUpToken string `json:"step_up_token"`
	ExpiresIn   int64  `json:"expires_in"`
}

type ValidateStepUpRequest struct {
	SessionID   string `json:"session_id"`
	OperationID string `json:"operation_id"`
	Token       string `json:"token"`
}

type ValidateStepUpResponse struct {
	Valid bool `json:"valid"`
}
