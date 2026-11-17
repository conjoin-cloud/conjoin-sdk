package conjoin

import "time"

const (
	Version              = "0.1.0"
	DefaultAPIVersion    = "2026-06-01"
	DefaultTimeout       = 30 * time.Second
	DefaultMaxRetries    = 3
	DefaultRetryBackoff  = 500 * time.Millisecond
	DefaultMaxRetryDelay = 60 * time.Second
)

const (
	sdkVersionHeader     = "X-Conjoin-SDK-Version"
	apiVersionHeader     = "X-Conjoin-API-Version"
	requestIDHeader      = "Conjoin-Request-Id"
	idempotencyKeyHeader = "Idempotency-Key"
	retryAfterHeader     = "Retry-After"
	userAgentValue       = "conjoin-sdk-go/" + Version
)
