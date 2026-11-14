package conjoin

import (
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"time"
)

var (
	ErrValidation       = errors.New("conjoin: the request failed validation")
	ErrAuthentication   = errors.New("conjoin: authentication failed")
	ErrPermissionDenied = errors.New("conjoin: permission denied")
	ErrNotFound         = errors.New("conjoin: not found")
	ErrConflict         = errors.New("conjoin: conflict")
	ErrRateLimited      = errors.New("conjoin: rate limited")
	ErrServer           = errors.New("conjoin: server error")
	ErrNetwork          = errors.New("conjoin: network failure")
	ErrTimeout          = errors.New("conjoin: request timed out")
	ErrCanceled         = errors.New("conjoin: request canceled")
	ErrInvalidResponse  = errors.New("conjoin: invalid response")
	ErrConfiguration    = errors.New("conjoin: invalid configuration")
	ErrNoNextPage       = errors.New("conjoin: the list has no next page")
)

type FieldError struct {
	Message string `json:"message"`
	Path    string `json:"path"`
}

type APIError struct {
	Status      int
	Code        string
	Message     string
	Param       string
	Details     json.RawMessage
	FieldErrors []FieldError
	RetryAfter  time.Duration
	RequestID   string
}

func (e *APIError) Error() string {
	return fmt.Sprintf("conjoin: %d %s: %s (request %s)", e.Status, e.Code, e.Message, e.RequestID)
}

func (e *APIError) Is(target error) bool {
	switch target {
	case ErrValidation:
		return e.Status == http.StatusBadRequest || e.Status == http.StatusUnprocessableEntity
	case ErrAuthentication:
		return e.Status == http.StatusUnauthorized
	case ErrPermissionDenied:
		return e.Status == http.StatusForbidden
	case ErrNotFound:
		return e.Status == http.StatusNotFound
	case ErrConflict:
		return e.Status == http.StatusConflict
	case ErrRateLimited:
		return e.Status == http.StatusTooManyRequests
	case ErrServer:
		return e.Status >= http.StatusInternalServerError
	}
	return false
}

type NetworkError struct {
	RequestID string
	Err       error
}

func (e *NetworkError) Error() string {
	return fmt.Sprintf("conjoin: network request failed: %v (request %s)", e.Err, e.RequestID)
}

func (e *NetworkError) Unwrap() error { return e.Err }

func (e *NetworkError) Is(target error) bool { return target == ErrNetwork }

type TimeoutError struct {
	RequestID string
	Timeout   time.Duration
}

func (e *TimeoutError) Error() string {
	return fmt.Sprintf("conjoin: request timed out after %s (request %s)", e.Timeout, e.RequestID)
}

func (e *TimeoutError) Is(target error) bool { return target == ErrTimeout }

type CanceledError struct {
	RequestID string
	Err       error
}

func (e *CanceledError) Error() string {
	return fmt.Sprintf("conjoin: the caller canceled the request: %v (request %s)", e.Err, e.RequestID)
}

func (e *CanceledError) Unwrap() error { return e.Err }

func (e *CanceledError) Is(target error) bool { return target == ErrCanceled }

type ResponseError struct {
	Status    int
	RequestID string
	Reason    string
}

func (e *ResponseError) Error() string {
	return fmt.Sprintf("conjoin: %s (status %d, request %s)", e.Reason, e.Status, e.RequestID)
}

func (e *ResponseError) Is(target error) bool { return target == ErrInvalidResponse }

type ConfigurationError struct {
	Reason string
}

func (e *ConfigurationError) Error() string {
	return "conjoin: " + e.Reason
}

func (e *ConfigurationError) Is(target error) bool { return target == ErrConfiguration }

func configurationError(format string, args ...any) error {
	return &ConfigurationError{Reason: fmt.Sprintf(format, args...)}
}
