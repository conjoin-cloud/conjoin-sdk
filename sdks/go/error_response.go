package conjoin

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
	"time"
)

const maxErrorBodyBytes = 64 << 10

var fallbackErrorCodes = map[int]string{
	http.StatusBadRequest:          "invalid_request",
	http.StatusUnauthorized:        "authentication_failed",
	http.StatusForbidden:           "permission_denied",
	http.StatusNotFound:            "not_found",
	http.StatusConflict:            "conflict",
	http.StatusUnprocessableEntity: "invalid_request",
	http.StatusTooManyRequests:     "rate_limited",
}

func fallbackErrorCode(status int) string {
	if code, ok := fallbackErrorCodes[status]; ok {
		return code
	}
	if status >= http.StatusInternalServerError {
		return "server_error"
	}
	return "api_error"
}

func fallbackErrorMessage(status int) string {
	if text := http.StatusText(status); text != "" {
		return text
	}
	return fmt.Sprintf("HTTP %d", status)
}

func readJSONObject(raw json.RawMessage) map[string]json.RawMessage {
	var object map[string]json.RawMessage
	if json.Unmarshal(raw, &object) != nil {
		return nil
	}
	return object
}

func readNonBlankString(raw json.RawMessage) string {
	var value string
	if json.Unmarshal(raw, &value) != nil || strings.TrimSpace(value) == "" {
		return ""
	}
	return value
}

func isJSONNull(raw json.RawMessage) bool {
	trimmed := bytes.TrimSpace(raw)
	return len(trimmed) == 0 || bytes.Equal(trimmed, []byte("null"))
}

func readFieldErrors(details json.RawMessage) []FieldError {
	var items []json.RawMessage
	if json.Unmarshal(details, &items) != nil {
		return nil
	}
	fieldErrors := make([]FieldError, 0, len(items))
	for _, item := range items {
		object := readJSONObject(item)
		var message, path string
		if json.Unmarshal(object["message"], &message) != nil || json.Unmarshal(object["path"], &path) != nil {
			continue
		}
		fieldErrors = append(fieldErrors, FieldError{Message: message, Path: path})
	}
	return fieldErrors
}

func buildAPIError(status int, header http.Header, body []byte, requestID string, now time.Time) *APIError {
	apiError := &APIError{
		Status:    status,
		Code:      fallbackErrorCode(status),
		Message:   fallbackErrorMessage(status),
		RequestID: requestID,
	}

	if status == http.StatusTooManyRequests {
		if delay, ok := parseRetryAfter(header.Get(retryAfterHeader), now); ok {
			apiError.RetryAfter = delay
		}
	}

	payload := readJSONObject(body)
	if payload == nil {
		return apiError
	}

	response := readJSONObject(payload["response"])
	detail := readJSONObject(payload["error"])

	if message := readNonBlankString(response["message"]); message != "" {
		apiError.Message = message
	} else if message := readNonBlankString(payload["message"]); message != "" {
		apiError.Message = message
	}
	if code := readNonBlankString(detail["code"]); code != "" {
		apiError.Code = code
	}
	apiError.Param = readNonBlankString(detail["param"])

	details := detail["details"]
	if legacy := bytes.TrimSpace(payload["errors"]); isJSONNull(details) && bytes.HasPrefix(legacy, []byte("[")) {
		details = legacy
	}
	if !isJSONNull(details) {
		apiError.Details = append(json.RawMessage(nil), bytes.TrimSpace(details)...)
	}

	if status == http.StatusBadRequest || status == http.StatusUnprocessableEntity {
		apiError.FieldErrors = readFieldErrors(apiError.Details)
	}
	return apiError
}
