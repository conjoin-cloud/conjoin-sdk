package conjoin

import (
	"net/http"
	"net/url"
	"strings"
	"time"
)

type Client struct {
	authorization            string
	publishableAuthorization string
	baseURL                  string
	httpClient               *http.Client
	apiVersion               string
	timeout                  time.Duration
	maxRetries               int
	retryBackoff             time.Duration
	maxRetryDelay            time.Duration
	requestID                string
	scope                    Scope
}

func NewClient(opts ...ClientOption) (*Client, error) {
	settings := clientSettings{
		apiVersion:    DefaultAPIVersion,
		timeout:       DefaultTimeout,
		maxRetries:    DefaultMaxRetries,
		retryBackoff:  DefaultRetryBackoff,
		maxRetryDelay: DefaultMaxRetryDelay,
	}
	for _, opt := range opts {
		if opt == nil {
			return nil, configurationError("a client option must not be nil")
		}
		if err := opt.applyToClient(&settings); err != nil {
			return nil, err
		}
	}

	key, err := resolveKey(settings.apiKey, settings.publishableKey)
	if err != nil {
		return nil, err
	}
	baseURL, err := resolveBaseURL(settings.baseURL, key)
	if err != nil {
		return nil, err
	}
	if err := settings.scope.validate(); err != nil {
		return nil, err
	}

	httpClient := settings.httpClient
	if httpClient == nil {
		httpClient = &http.Client{}
	}

	publishableAuthorization := ""
	if settings.publishableKey != "" {
		publishableAuthorization = "Bearer " + key
	}

	return &Client{
		authorization:            "Bearer " + key,
		publishableAuthorization: publishableAuthorization,
		baseURL:                  baseURL,
		httpClient:               httpClient,
		apiVersion:               settings.apiVersion,
		timeout:                  settings.timeout,
		maxRetries:               settings.maxRetries,
		retryBackoff:             settings.retryBackoff,
		maxRetryDelay:            settings.maxRetryDelay,
		requestID:                settings.requestID,
		scope:                    settings.scope,
	}, nil
}

func (c *Client) WithScope(scope Scope) (*Client, error) {
	if c == nil {
		return nil, configurationError("the client is nil")
	}
	merged := c.scope.merge(scope)
	if err := merged.validate(); err != nil {
		return nil, err
	}
	scoped := *c
	scoped.scope = merged
	return &scoped, nil
}

func (c *Client) BaseURL() string {
	if c == nil {
		return ""
	}
	return c.baseURL
}

func (c Client) String() string {
	return "conjoin.Client{baseURL: " + c.baseURL + ", key: [redacted]}"
}

func (c Client) GoString() string {
	return c.String()
}

func resolveKey(apiKey, publishableKey string) (string, error) {
	if apiKey != "" && publishableKey != "" {
		return "", configurationError("provide exactly one of an API key or a publishable key")
	}
	key := apiKey
	if key == "" {
		key = publishableKey
	}
	if key == "" {
		return "", configurationError("an API key or a publishable key must be provided")
	}
	if !isHeaderToken(key) {
		return "", configurationError("the key must be a value without spaces or control characters")
	}
	return key, nil
}

func resolveBaseURL(baseURL, key string) (string, error) {
	if baseURL == "" {
		return regionBaseURL(keyRegion(key)), nil
	}
	parsed, err := url.Parse(baseURL)
	if err != nil || (parsed.Scheme != "https" && parsed.Scheme != "http") || parsed.Host == "" {
		return "", configurationError("the base URL must be an absolute http or https URL")
	}
	if parsed.RawQuery != "" || parsed.Fragment != "" || parsed.User != nil {
		return "", configurationError("the base URL must not carry a query, a fragment, or credentials")
	}
	return strings.TrimRight(baseURL, "/"), nil
}
