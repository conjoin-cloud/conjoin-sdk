package codegen

import (
	"go/token"
	"regexp"
	"strings"
	"unicode"
)

var (
	tagSeparatorPattern = regexp.MustCompile(`[\s\-_]+`)
	camelBoundary       = regexp.MustCompile(`([a-z0-9])([A-Z])`)
	acronymBoundary     = regexp.MustCompile(`([A-Z]+)([A-Z][a-z])`)
	nonAlphanumeric     = regexp.MustCompile(`[^A-Za-z0-9]+`)
	pathParamPattern    = regexp.MustCompile(`\{([^{}]+)\}`)
)

var initialisms = map[string]string{
	"acl": "ACL", "api": "API", "cidr": "CIDR", "cpu": "CPU", "css": "CSS", "dns": "DNS", "html": "HTML",
	"http": "HTTP", "https": "HTTPS", "id": "ID", "ids": "IDs", "ip": "IP", "json": "JSON", "jwks": "JWKS",
	"mfa": "MFA", "oidc": "OIDC", "otp": "OTP", "saml": "SAML", "scim": "SCIM", "sdk": "SDK", "slo": "SLO",
	"sms": "SMS", "smtp": "SMTP", "sql": "SQL", "ssh": "SSH", "sso": "SSO", "tls": "TLS", "ttl": "TTL",
	"ui": "UI", "uri": "URI", "url": "URL", "urls": "URLs", "uuid": "UUID", "xml": "XML",
}

var reservedParameterNames = map[string]bool{
	"ctx": true, "body": true, "query": true, "headers": true, "sessionToken": true, "opts": true, "out": true,
	"err": true, "s": true, "conjoin": true, "context": true,
}

func toPascalCase(value string) string {
	var builder strings.Builder
	for _, word := range tagSeparatorPattern.Split(value, -1) {
		if word == "" {
			continue
		}
		builder.WriteString(strings.ToUpper(word[:1]))
		builder.WriteString(word[1:])
	}
	return builder.String()
}

func lowerFirst(value string) string {
	if value == "" {
		return value
	}
	return strings.ToLower(value[:1]) + value[1:]
}

func upperFirst(value string) string {
	if value == "" {
		return value
	}
	return strings.ToUpper(value[:1]) + value[1:]
}

func identifierWords(value string) []string {
	spaced := acronymBoundary.ReplaceAllString(value, "${1} ${2}")
	spaced = camelBoundary.ReplaceAllString(spaced, "${1} ${2}")
	spaced = nonAlphanumeric.ReplaceAllString(spaced, " ")
	return strings.Fields(spaced)
}

func goIdentifier(value string) string {
	var builder strings.Builder
	for _, word := range identifierWords(value) {
		lower := strings.ToLower(word)
		if initialism, ok := initialisms[lower]; ok {
			builder.WriteString(initialism)
			continue
		}
		builder.WriteString(strings.ToUpper(lower[:1]))
		builder.WriteString(lower[1:])
	}
	name := builder.String()
	if name == "" {
		return "Value"
	}
	if unicode.IsDigit(rune(name[0])) {
		return "Value" + name
	}
	return name
}

func goParameterName(value string) string {
	words := identifierWords(value)
	if len(words) == 0 {
		return "param"
	}
	name := strings.ToLower(words[0])
	if len(words) > 1 {
		name += goIdentifier(strings.Join(words[1:], " "))
	}
	if unicode.IsDigit(rune(name[0])) || token.IsKeyword(name) || reservedParameterNames[name] {
		return name + "Param"
	}
	return name
}

func snakeCase(value string) string {
	words := identifierWords(value)
	for index, word := range words {
		words[index] = strings.ToLower(word)
	}
	return strings.Join(words, "_")
}

func operationMethodName(operationID, servicePascal, resourcePascal string) string {
	serviceResource := servicePascal + resourcePascal
	candidates := []string{pluralize(serviceResource), serviceResource, pluralize(resourcePascal), resourcePascal, servicePascal}
	for _, candidate := range candidates {
		index := strings.Index(operationID, candidate)
		if index < 0 {
			continue
		}
		if stripped := operationID[:index] + operationID[index+len(candidate):]; stripped != "" {
			return lowerFirst(stripped)
		}
	}
	return operationID
}

func operationTypeBase(operationID, servicePascal string) string {
	if index := strings.Index(operationID, servicePascal); index >= 0 && servicePascal != "" {
		if stripped := operationID[:index] + operationID[index+len(servicePascal):]; stripped != "" {
			return upperFirst(stripped)
		}
	}
	return upperFirst(operationID)
}

func pathParameters(path string) []string {
	matches := pathParamPattern.FindAllStringSubmatch(path, -1)
	names := make([]string, 0, len(matches))
	for _, match := range matches {
		names = append(names, match[1])
	}
	return names
}
