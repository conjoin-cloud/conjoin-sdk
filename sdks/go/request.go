package conjoin

import (
	"context"
	"net/http"
	"net/url"
	"reflect"
	"regexp"
	"strings"
	"time"
)

var (
	absoluteURLPattern = regexp.MustCompile(`(?i)^[a-z][a-z0-9+.-]*:`)
	retryableMethods   = map[string]bool{http.MethodGet: true, http.MethodPut: true, http.MethodPatch: true, http.MethodDelete: true}
	sendableMethods    = map[string]bool{http.MethodGet: true, http.MethodPost: true, http.MethodPut: true, http.MethodPatch: true, http.MethodDelete: true}
)

type preparedRequest struct {
	method       string
	url          string
	header       http.Header
	body         []byte
	hasBody      bool
	requestID    string
	timeout      time.Duration
	maxRetries   int
	retryAllowed bool
}

func isNil(value any) bool {
	if value == nil {
		return true
	}
	v := reflect.ValueOf(value)
	switch v.Kind() {
	case reflect.Pointer, reflect.Map, reflect.Slice, reflect.Interface, reflect.Func, reflect.Chan:
		return v.IsNil()
	}
	return false
}

func readCallSettings(opts []CallOption) (callSettings, error) {
	var settings callSettings
	for _, opt := range opts {
		if opt == nil {
			return settings, configurationError("a call option must not be nil")
		}
		if err := opt.applyToCall(&settings); err != nil {
			return settings, err
		}
	}
	return settings, nil
}

func buildPath(template string, params []string) (string, error) {
	if absoluteURLPattern.MatchString(template) || strings.HasPrefix(template, "//") {
		return "", configurationError("the path must be relative to the Conjoin API")
	}
	rest := strings.TrimPrefix(strings.TrimLeft(template, "/"), "v1/")
	var path strings.Builder
	used := 0
	for {
		open := strings.IndexByte(rest, '{')
		if open < 0 {
			path.WriteString(rest)
			break
		}
		closing := strings.IndexByte(rest[open:], '}')
		if closing < 0 || used >= len(params) {
			return "", configurationError("the path %q does not match its path parameters", template)
		}
		value := params[used]
		if value == "" || value == "." || value == ".." {
			return "", configurationError("a path parameter must be a non-empty ID")
		}
		path.WriteString(rest[:open])
		path.WriteString(url.PathEscape(value))
		rest = rest[open+closing+1:]
		used++
	}
	if used != len(params) {
		return "", configurationError("the path %q does not match its path parameters", template)
	}
	return path.String(), nil
}

func (c *Client) resolveAuthorization(op Operation, settings callSettings) (string, error) {
	switch op.Auth {
	case AuthNone, AuthPublishableKey, AuthSession:
		if settings.hasBearerToken {
			return "", configurationError("this call sends only the credential that its operation declares, so it does not take WithBearerToken")
		}
	}
	switch op.Auth {
	case AuthNone:
		return "", nil
	case AuthPublishableKey:
		if c.publishableAuthorization == "" {
			return "", configurationError("this call needs a publishable key in the client settings; pass WithPublishableKey")
		}
		return c.publishableAuthorization, nil
	case AuthSession:
		if op.SessionToken == "" {
			return "", configurationError("this call needs a session token")
		}
		if !isHeaderToken(string(op.SessionToken)) {
			return "", configurationError("the session token must be a value without spaces or control characters")
		}
		return "Bearer " + string(op.SessionToken), nil
	}
	if settings.hasBearerToken {
		return "Bearer " + settings.bearerToken, nil
	}
	if op.Auth == AuthBearerToken {
		return "", configurationError("this call needs a bearer token; pass WithBearerToken")
	}
	return c.authorization, nil
}

func (c *Client) resolveRequestID(settings callSettings) string {
	for _, candidate := range []string{settings.requestID, c.requestID} {
		if isValidRequestID(candidate) {
			return candidate
		}
	}
	return newRequestID()
}

func resolveIdempotencyKey(op Operation, settings callSettings) (string, error) {
	if settings.hasIdempotency {
		if op.Method != http.MethodPost {
			return "", configurationError("only a POST takes an idempotency key")
		}
		return settings.idempotencyKey, nil
	}
	if op.Method == http.MethodPost && op.AcceptsIdempotencyKey {
		return newIdempotencyKey(), nil
	}
	return "", nil
}

func (c *Client) prepare(ctx context.Context, op Operation, query url.Values, opts []CallOption) (*preparedRequest, error) {
	if c == nil {
		return nil, configurationError("the client is nil")
	}
	if ctx == nil {
		return nil, configurationError("the context must not be nil")
	}
	if !sendableMethods[op.Method] {
		return nil, configurationError("the method %q is not one that the Conjoin API serves", op.Method)
	}
	settings, err := readCallSettings(opts)
	if err != nil {
		return nil, err
	}
	path, err := buildPath(op.Path, op.PathParams)
	if err != nil {
		return nil, err
	}
	if op.QueryRequired && isNil(op.Query) {
		return nil, configurationError("this call needs its query parameters")
	}
	if op.BodyRequired && isNil(op.Body) {
		return nil, configurationError("this call needs a request body")
	}

	target := c.baseURL + "/v1/" + path
	if encoded := query.Encode(); encoded != "" {
		target += "?" + encoded
	}
	if _, err := url.ParseRequestURI(target); err != nil {
		return nil, configurationError("the request URL is not valid")
	}

	body, contentType, err := encodeBody(op)
	if err != nil {
		return nil, err
	}
	authorization, err := c.resolveAuthorization(op, settings)
	if err != nil {
		return nil, err
	}
	idempotencyKey, err := resolveIdempotencyKey(op, settings)
	if err != nil {
		return nil, err
	}

	header := settings.headers.Clone()
	if header == nil {
		header = http.Header{}
	}
	if err := applyDeclaredHeaders(header, op.Headers); err != nil {
		return nil, err
	}
	if authorization != "" {
		header.Set(authorizationHeader, authorization)
	}
	if contentType != "" {
		header.Set(contentTypeHeader, contentType)
	}
	header.Set(userAgentHeader, userAgentValue)
	header.Set(sdkVersionHeader, Version)
	header.Set(apiVersionHeader, c.apiVersion)
	for _, name := range op.Scopes {
		headerName, value, known := c.scope.header(name)
		if !known {
			return nil, configurationError("the call declares an unknown scope")
		}
		if value == "" {
			return nil, configurationError("this call needs %s in the client settings", headerName)
		}
		header.Set(headerName, value)
	}

	requestID := c.resolveRequestID(settings)
	header.Set(requestIDHeader, requestID)
	if idempotencyKey != "" {
		header.Set(idempotencyKeyHeader, idempotencyKey)
	}

	timeout := c.timeout
	if settings.timeout > 0 {
		timeout = settings.timeout
	}
	maxRetries := c.maxRetries
	if settings.hasMaxRetries {
		maxRetries = settings.maxRetries
	}

	return &preparedRequest{
		method:       op.Method,
		url:          target,
		header:       header,
		body:         body,
		hasBody:      body != nil,
		requestID:    requestID,
		timeout:      timeout,
		maxRetries:   maxRetries,
		retryAllowed: retryableMethods[op.Method] || (op.Method == http.MethodPost && op.AcceptsIdempotencyKey && idempotencyKey != ""),
	}, nil
}
