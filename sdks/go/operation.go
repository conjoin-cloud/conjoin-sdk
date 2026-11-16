package conjoin

type ScopeName int

const (
	ScopeBillingEntity ScopeName = iota + 1
	ScopeMessagingProfile
	ScopeAuthApp
)

const (
	scopeBillingEntityHeader = "Billing-Entity-ID"
	scopeMessagingHeader     = "Messaging-Profile-ID"
	scopeAuthAppHeader       = "Auth-App-ID"
)

type Scope struct {
	BillingEntityID    string
	MessagingProfileID string
	AuthAppID          string
}

type AuthMode int

const (
	AuthDefault AuthMode = iota
	AuthNone
	AuthBearerToken
	AuthPublishableKey
	AuthSession
)

type ResponseShape int

const (
	ResponseEnvelope ResponseShape = iota
	ResponseBody
	ResponseEmpty
)

type CursorLocation int

const (
	CursorInQuery CursorLocation = iota
	CursorInBody
	CursorNotAccepted
)

type Operation struct {
	Method                string
	Path                  string
	PathParams            []string
	Query                 any
	QueryRequired         bool
	Body                  any
	BodyRequired          bool
	Multipart             bool
	Headers               []DeclaredHeader
	SessionToken          Credential
	Scopes                []ScopeName
	AcceptsIdempotencyKey bool
	Auth                  AuthMode
	Response              ResponseShape
	Cursor                CursorLocation
}

func (s Scope) header(name ScopeName) (string, string, bool) {
	switch name {
	case ScopeBillingEntity:
		return scopeBillingEntityHeader, s.BillingEntityID, true
	case ScopeMessagingProfile:
		return scopeMessagingHeader, s.MessagingProfileID, true
	case ScopeAuthApp:
		return scopeAuthAppHeader, s.AuthAppID, true
	}
	return "", "", false
}

func (s Scope) merge(override Scope) Scope {
	if override.BillingEntityID != "" {
		s.BillingEntityID = override.BillingEntityID
	}
	if override.MessagingProfileID != "" {
		s.MessagingProfileID = override.MessagingProfileID
	}
	if override.AuthAppID != "" {
		s.AuthAppID = override.AuthAppID
	}
	return s
}

func (s Scope) validate() error {
	for _, name := range []ScopeName{ScopeBillingEntity, ScopeMessagingProfile, ScopeAuthApp} {
		header, value, _ := s.header(name)
		if value != "" && !isHeaderToken(value) {
			return configurationError("the %s must be a value without spaces or control characters", header)
		}
	}
	return nil
}
