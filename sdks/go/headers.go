package conjoin

import (
	"net/http"
	"strings"
)

const (
	authorizationHeader = "Authorization"
	contentTypeHeader   = "Content-Type"
	userAgentHeader     = "User-Agent"
)

var managedHeaders = map[string]bool{
	http.CanonicalHeaderKey(authorizationHeader):      true,
	http.CanonicalHeaderKey(contentTypeHeader):        true,
	http.CanonicalHeaderKey(requestIDHeader):          true,
	http.CanonicalHeaderKey(idempotencyKeyHeader):     true,
	http.CanonicalHeaderKey(scopeBillingEntityHeader): true,
	http.CanonicalHeaderKey(scopeMessagingHeader):     true,
	http.CanonicalHeaderKey(scopeAuthAppHeader):       true,
}

func isManagedHeader(name string) bool {
	return managedHeaders[http.CanonicalHeaderKey(name)]
}

func isHeaderToken(value string) bool {
	if value == "" {
		return false
	}
	for i := 0; i < len(value); i++ {
		if value[i] < 0x21 || value[i] > 0x7e {
			return false
		}
	}
	return true
}

func isHeaderName(name string) bool {
	if name == "" {
		return false
	}
	for i := 0; i < len(name); i++ {
		c := name[i]
		isAlphanumeric := c >= '0' && c <= '9' || c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z'
		if !isAlphanumeric && !strings.ContainsRune("!#$%&'*+-.^_`|~", rune(c)) {
			return false
		}
	}
	return true
}

func isHeaderValue(value string) bool {
	for i := 0; i < len(value); i++ {
		c := value[i]
		if c == 0x7f || c < 0x20 && c != '\t' {
			return false
		}
	}
	return true
}
