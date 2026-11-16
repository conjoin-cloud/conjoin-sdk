package conjoin

import (
	"net/http"
	"regexp"
	"sync"
)

type DeclaredHeader struct {
	Name      string
	Argument  string
	Value     Credential
	Required  bool
	MinLength int
	MaxLength int
	Pattern   string
}

var declaredHeaderPatterns sync.Map

func compileDeclaredHeaderPattern(pattern string) (*regexp.Regexp, error) {
	if cached, found := declaredHeaderPatterns.Load(pattern); found {
		if compiled, isCompiled := cached.(*regexp.Regexp); isCompiled {
			return compiled, nil
		}
	}
	compiled, err := regexp.Compile(pattern)
	if err != nil {
		return nil, err
	}
	declaredHeaderPatterns.Store(pattern, compiled)
	return compiled, nil
}

func (h DeclaredHeader) check(value string) error {
	isTooShort := len(value) < h.MinLength
	isTooLong := h.MaxLength > 0 && len(value) > h.MaxLength
	if !isHeaderToken(value) || isTooShort || isTooLong {
		return configurationError("%s does not meet the documented length or format", h.Argument)
	}
	if h.Pattern == "" {
		return nil
	}
	compiled, err := compileDeclaredHeaderPattern(h.Pattern)
	if err != nil {
		return configurationError("the documented format of %s cannot be checked", h.Argument)
	}
	if !compiled.MatchString(value) {
		return configurationError("%s does not meet the documented length or format", h.Argument)
	}
	return nil
}

func applyDeclaredHeaders(header http.Header, declared []DeclaredHeader) error {
	for _, rule := range declared {
		header.Del(rule.Name)
	}
	for _, rule := range declared {
		value := string(rule.Value)
		if value == "" {
			if rule.Required {
				return configurationError("this call needs %s", rule.Argument)
			}
			continue
		}
		if err := rule.check(value); err != nil {
			return err
		}
		header.Set(rule.Name, value)
	}
	return nil
}
