package conjoin

import (
	"net/http"
	"time"
)

type ClientOption interface {
	applyToClient(*clientSettings) error
}

type CallOption interface {
	applyToCall(*callSettings) error
}

type Option interface {
	ClientOption
	CallOption
}

type clientOptionFunc func(*clientSettings) error

func (f clientOptionFunc) applyToClient(s *clientSettings) error { return f(s) }

type callOptionFunc func(*callSettings) error

func (f callOptionFunc) applyToCall(s *callSettings) error { return f(s) }

type clientAndCallOption struct {
	client clientOptionFunc
	call   callOptionFunc
}

func (o clientAndCallOption) applyToClient(s *clientSettings) error { return o.client(s) }

func (o clientAndCallOption) applyToCall(s *callSettings) error { return o.call(s) }

type clientSettings struct {
	apiKey         string
	publishableKey string
	baseURL        string
	httpClient     *http.Client
	apiVersion     string
	timeout        time.Duration
	maxRetries     int
	retryBackoff   time.Duration
	maxRetryDelay  time.Duration
	requestID      string
	scope          Scope
}

type callSettings struct {
	timeout        time.Duration
	maxRetries     int
	hasMaxRetries  bool
	requestID      string
	idempotencyKey string
	hasIdempotency bool
	bearerToken    string
	hasBearerToken bool
	headers        http.Header
}

func WithAPIKey(key string) ClientOption {
	return clientOptionFunc(func(s *clientSettings) error {
		s.apiKey = key
		return nil
	})
}

func WithPublishableKey(key string) ClientOption {
	return clientOptionFunc(func(s *clientSettings) error {
		s.publishableKey = key
		return nil
	})
}

func WithBaseURL(baseURL string) ClientOption {
	return clientOptionFunc(func(s *clientSettings) error {
		s.baseURL = baseURL
		return nil
	})
}

func WithHTTPClient(client *http.Client) ClientOption {
	return clientOptionFunc(func(s *clientSettings) error {
		if client == nil {
			return configurationError("the HTTP client must not be nil")
		}
		s.httpClient = client
		return nil
	})
}

func WithAPIVersion(version string) ClientOption {
	return clientOptionFunc(func(s *clientSettings) error {
		if !isHeaderToken(version) {
			return configurationError("the API version must be a non-empty value without spaces or control characters")
		}
		s.apiVersion = version
		return nil
	})
}

func WithRetryBackoff(base time.Duration) ClientOption {
	return clientOptionFunc(func(s *clientSettings) error {
		if base < 0 {
			return configurationError("the retry backoff must be 0 or more")
		}
		s.retryBackoff = base
		return nil
	})
}

func WithMaxRetryDelay(limit time.Duration) ClientOption {
	return clientOptionFunc(func(s *clientSettings) error {
		if limit < 0 {
			return configurationError("the maximum retry delay must be 0 or more")
		}
		s.maxRetryDelay = limit
		return nil
	})
}

func WithBillingEntityID(id string) ClientOption {
	return clientOptionFunc(func(s *clientSettings) error {
		s.scope.BillingEntityID = id
		return nil
	})
}

func WithMessagingProfileID(id string) ClientOption {
	return clientOptionFunc(func(s *clientSettings) error {
		s.scope.MessagingProfileID = id
		return nil
	})
}

func WithAuthAppID(id string) ClientOption {
	return clientOptionFunc(func(s *clientSettings) error {
		s.scope.AuthAppID = id
		return nil
	})
}

func WithTimeout(timeout time.Duration) Option {
	check := func() error {
		if timeout <= 0 {
			return configurationError("the timeout must be greater than 0")
		}
		return nil
	}
	return clientAndCallOption{
		client: func(s *clientSettings) error {
			s.timeout = timeout
			return check()
		},
		call: func(s *callSettings) error {
			s.timeout = timeout
			return check()
		},
	}
}

func WithMaxRetries(retries int) Option {
	check := func() error {
		if retries < 0 {
			return configurationError("the maximum number of retries must be 0 or more")
		}
		return nil
	}
	return clientAndCallOption{
		client: func(s *clientSettings) error {
			s.maxRetries = retries
			return check()
		},
		call: func(s *callSettings) error {
			s.maxRetries = retries
			s.hasMaxRetries = true
			return check()
		},
	}
}

func WithRequestID(requestID string) Option {
	return clientAndCallOption{
		client: func(s *clientSettings) error {
			s.requestID = requestID
			return nil
		},
		call: func(s *callSettings) error {
			s.requestID = requestID
			return nil
		},
	}
}

func WithIdempotencyKey(key string) CallOption {
	return callOptionFunc(func(s *callSettings) error {
		if err := validateIdempotencyKey(key); err != nil {
			return err
		}
		s.idempotencyKey = key
		s.hasIdempotency = true
		return nil
	})
}

func WithBearerToken(token string) CallOption {
	return callOptionFunc(func(s *callSettings) error {
		if !isHeaderToken(token) {
			return configurationError("the bearer token must be a non-empty value without spaces or control characters")
		}
		s.bearerToken = token
		s.hasBearerToken = true
		return nil
	})
}

func WithHeader(name, value string) CallOption {
	return callOptionFunc(func(s *callSettings) error {
		if !isHeaderName(name) || !isHeaderValue(value) {
			return configurationError("a request header has a name or value that HTTP does not allow")
		}
		if isManagedHeader(name) {
			return nil
		}
		if s.headers == nil {
			s.headers = http.Header{}
		}
		s.headers.Add(name, value)
		return nil
	})
}
