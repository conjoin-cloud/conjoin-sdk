package everyoperation

import (
	"encoding/json"
	"os"
	"path/filepath"
	"regexp"
	"strconv"
	"strings"
	"testing"
)

type jsonObject = map[string]any

var httpMethods = []string{"get", "post", "put", "patch", "delete"}

type documentOperation struct {
	key          string
	method       string
	template     string
	route        *regexp.Regexp
	paramNames   []string
	operation    jsonObject
	headers      map[string]bool
	security     string
	successCode  int
	successBody  any
	hasBody      bool
	bodyType     string
	bodySchema   any
	queryParams  []jsonObject
	headerParams []jsonObject
	requestIDRef *regexp.Regexp
}

var sdkManagedHeaderNames = map[string]bool{
	"billing-entity-id":    true,
	"messaging-profile-id": true,
	"auth-app-id":          true,
	"idempotency-key":      true,
	"conjoin-request-id":   true,
}

type openAPIDocument struct {
	root       jsonObject
	operations []*documentOperation
}

func loadDocument(t *testing.T, file string) *openAPIDocument {
	t.Helper()
	raw, err := os.ReadFile(filepath.Join("..", "..", "..", "..", "spec", file))
	if err != nil {
		t.Fatalf("the document %s did not load: %v", file, err)
	}
	var root jsonObject
	if err := json.Unmarshal(raw, &root); err != nil {
		t.Fatalf("the document %s is not JSON: %v", file, err)
	}
	doc := &openAPIDocument{root: root}
	paths, _ := root["paths"].(jsonObject)
	for template, rawItem := range paths {
		item, _ := rawItem.(jsonObject)
		for _, method := range httpMethods {
			operation, ok := item[method].(jsonObject)
			if ok {
				doc.operations = append(doc.operations, doc.describe(t, strings.ToUpper(method), template, operation))
			}
		}
	}
	return doc
}

func (d *openAPIDocument) resolve(value any) jsonObject {
	node, _ := value.(jsonObject)
	for hop := 0; node != nil && hop < 32; hop++ {
		ref, isRef := node["$ref"].(string)
		if !isRef {
			return node
		}
		var target any = d.root
		for _, segment := range strings.Split(strings.TrimPrefix(ref, "#/"), "/") {
			parent, _ := target.(jsonObject)
			target = parent[segment]
		}
		node, _ = target.(jsonObject)
	}
	return node
}

var templateParam = regexp.MustCompile(`\{([^{}]+)\}`)

func (d *openAPIDocument) describe(t *testing.T, method, template string, operation jsonObject) *documentOperation {
	t.Helper()
	described := &documentOperation{key: method + " " + template, method: method, template: template, operation: operation, headers: map[string]bool{}}

	var pattern strings.Builder
	pattern.WriteString("^")
	last := 0
	for _, match := range templateParam.FindAllStringSubmatchIndex(template, -1) {
		pattern.WriteString(regexp.QuoteMeta(template[last:match[0]]))
		pattern.WriteString("([^/]+)")
		described.paramNames = append(described.paramNames, template[match[2]:match[3]])
		last = match[1]
	}
	pattern.WriteString(regexp.QuoteMeta(template[last:]) + "$")
	described.route = regexp.MustCompile(pattern.String())

	parameters, _ := operation["parameters"].([]any)
	for _, raw := range parameters {
		parameter := d.resolve(raw)
		name, _ := parameter["name"].(string)
		switch parameter["in"] {
		case "header":
			described.headers[strings.ToLower(name)] = true
			if !sdkManagedHeaderNames[strings.ToLower(name)] {
				described.headerParams = append(described.headerParams, parameter)
			}
			if strings.EqualFold(name, "Conjoin-Request-Id") {
				schema := d.resolve(parameter["schema"])
				expression, _ := schema["pattern"].(string)
				described.requestIDRef = regexp.MustCompile(expression)
			}
		case "query":
			described.queryParams = append(described.queryParams, parameter)
		}
	}
	if described.requestIDRef == nil {
		t.Fatalf("%s declares no Conjoin-Request-Id pattern", described.key)
	}

	if security, ok := operation["security"].([]any); ok && len(security) > 0 {
		if requirement, ok := security[0].(jsonObject); ok {
			for scheme := range requirement {
				described.security = scheme
			}
		}
	}

	if requestBody := d.resolve(operation["requestBody"]); requestBody != nil {
		content, _ := requestBody["content"].(jsonObject)
		for contentType, media := range content {
			described.hasBody, described.bodyType, described.bodySchema = true, contentType, d.resolve(media)["schema"]
		}
	}

	responses, _ := operation["responses"].(jsonObject)
	for code := 200; code < 300; code++ {
		response := d.resolve(responses[strconv.Itoa(code)])
		if response == nil {
			continue
		}
		described.successCode = code
		content, _ := response["content"].(jsonObject)
		if media := d.resolve(content["application/json"]); media != nil && code != 204 {
			described.successBody = newSampler(d).sample(media["schema"])
		}
		break
	}
	if described.successCode == 0 {
		t.Fatalf("%s declares no success response", described.key)
	}
	return described
}
