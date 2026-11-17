package codegen

import (
	"fmt"
	"strings"
)

type responseKind int

const (
	responseEnvelope responseKind = iota
	responseList
	responseBody
	responseEmpty
)

type queryParameter struct {
	name     string
	schema   any
	required bool
}

type operation struct {
	id                    string
	method                string
	path                  string
	pathParams            []string
	body                  any
	bodyRequired          bool
	multipart             bool
	query                 []queryParameter
	kind                  responseKind
	result                any
	scopes                []string
	acceptsIdempotencyKey bool
	auth                  string
	headers               []declaredHeader
	methodName            string
}

type resourceGroup struct {
	service        string
	resource       string
	servicePascal  string
	resourcePascal string
	operations     []*operation
}

var httpMethods = map[string]bool{"get": true, "post": true, "put": true, "patch": true, "delete": true}

var scopeHeaders = map[string]string{
	"billing-entity-id":    "conjoin.ScopeBillingEntity",
	"messaging-profile-id": "conjoin.ScopeMessagingProfile",
	"auth-app-id":          "conjoin.ScopeAuthApp",
}

const (
	requestIDHeaderName      = "conjoin-request-id"
	idempotencyKeyHeaderName = "idempotency-key"
	multipartContentType     = "multipart/form-data"
	jsonContentType          = "application/json"
	noContentStatus          = "204"
)

func (d *document) readSecurity(op *object, built *operation) error {
	security, err := resolveSecurity(op, built.id)
	if err != nil {
		return err
	}
	built.auth = security.auth
	if security.sendsPortalKey {
		ticket, err := d.portalTicketHeader(built.id)
		if err != nil {
			return err
		}
		built.headers = append(built.headers, ticket)
	}
	return checkDeclaredHeaderFields(built.headers, built.id)
}

func (d *document) readParameters(op *object, built *operation) error {
	for _, raw := range op.list("parameters") {
		parameter, err := d.resolve(raw)
		if err != nil {
			return err
		}
		name := parameter.text("name")
		switch parameter.text("in") {
		case "path":
		case "query":
			built.query = append(built.query, queryParameter{name: name, schema: parameter.get("schema"), required: parameter.get("required") == true})
		case "header":
			lower := strings.ToLower(name)
			if scope, ok := scopeHeaders[lower]; ok {
				built.scopes = append(built.scopes, scope)
			} else if lower == idempotencyKeyHeaderName {
				built.acceptsIdempotencyKey = built.method == "POST"
			} else if lower != requestIDHeaderName {
				header, err := d.readDeclaredHeader(parameter, built.id)
				if err != nil {
					return err
				}
				built.headers = append(built.headers, header)
			}
		default:
			return fmt.Errorf("%s declares the parameter %s in %q, which the generator does not support", built.id, name, parameter.text("in"))
		}
	}
	return nil
}

func (d *document) readRequestBody(op *object, built *operation) error {
	if !op.has("requestBody") {
		return nil
	}
	if built.method == "GET" || built.method == "DELETE" {
		return fmt.Errorf("%s is a %s that declares a request body", built.id, built.method)
	}
	requestBody, err := d.resolve(op.get("requestBody"))
	if err != nil {
		return err
	}
	content := requestBody.object("content")
	if content == nil || len(content.keys) == 0 {
		return fmt.Errorf("%s declares a request body without content", built.id)
	}
	contentType := content.keys[0]
	if contentType != jsonContentType && contentType != multipartContentType {
		return fmt.Errorf("%s declares the request content type %s, which the generator does not support", built.id, contentType)
	}
	built.multipart = contentType == multipartContentType
	built.body = content.object(contentType).get("schema")
	built.bodyRequired = requestBody.get("required") == true
	return nil
}

func (d *document) readResponse(op *object, built *operation) error {
	responses := op.object("responses")
	successCode := ""
	for _, code := range responses.orderedKeys() {
		if strings.HasPrefix(code, "2") {
			successCode = code
			break
		}
	}
	if successCode == "" {
		return fmt.Errorf("%s declares no success response", built.id)
	}
	success, err := d.resolve(responses.get(successCode))
	if err != nil {
		return err
	}
	content := success.object("content")
	if successCode == noContentStatus || content == nil || len(content.keys) == 0 {
		built.kind = responseEmpty
		return nil
	}
	schema, err := d.resolve(content.object(content.keys[0]).get("schema"))
	if err != nil {
		return err
	}
	properties := schema.object("properties")
	if !properties.has("data") {
		built.kind = responseBody
		built.result = schema
		return nil
	}
	data, err := d.resolve(properties.get("data"))
	if err != nil {
		return err
	}
	if data.text("type") == "array" && properties.has("cursor") {
		built.kind = responseList
		built.result = data.get("items")
		return nil
	}
	built.kind = responseEnvelope
	built.result = data
	return nil
}

func (d *document) collectGroups() ([]*resourceGroup, error) {
	var groups []*resourceGroup
	byKey := map[string]*resourceGroup{}
	paths := d.root.object("paths")
	for _, path := range paths.orderedKeys() {
		item := paths.object(path)
		for _, method := range item.orderedKeys() {
			op := item.object(method)
			if !httpMethods[method] || op == nil {
				continue
			}
			tags := op.list("tags")
			tag, _ := firstString(tags)
			operationID := op.text("operationId")
			if tag == "" || operationID == "" {
				return nil, fmt.Errorf("%s %s has no tag or operationId", strings.ToUpper(method), path)
			}
			service, resource, _ := strings.Cut(tag, " - ")
			service = strings.ToLower(strings.TrimSpace(service))
			resource = strings.TrimSpace(resource)
			if service == "" || resource == "" {
				return nil, fmt.Errorf("%s %s has the tag %s without a service and a resource", strings.ToUpper(method), path, tag)
			}

			built := &operation{id: operationID, method: strings.ToUpper(method), path: path, pathParams: pathParameters(path)}
			if err := d.readParameters(op, built); err != nil {
				return nil, err
			}
			if err := d.readSecurity(op, built); err != nil {
				return nil, err
			}
			if err := d.readRequestBody(op, built); err != nil {
				return nil, err
			}
			if err := d.readResponse(op, built); err != nil {
				return nil, err
			}

			key := service + "/" + resource
			group, exists := byKey[key]
			if !exists {
				group = &resourceGroup{service: service, resource: resource, servicePascal: toPascalCase(service), resourcePascal: toPascalCase(resource)}
				byKey[key] = group
				groups = append(groups, group)
			}
			group.operations = append(group.operations, built)
		}
	}
	return groups, nil
}

func firstString(values []any) (string, bool) {
	if len(values) == 0 {
		return "", false
	}
	value, ok := values[0].(string)
	return value, ok
}
