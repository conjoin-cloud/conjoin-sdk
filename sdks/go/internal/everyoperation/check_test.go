package everyoperation

import (
	"encoding/json"
	"reflect"
	"strings"
	"testing"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

func requiredQuery(sampler *sampler, operation *documentOperation) any {
	query := jsonObject{}
	for _, parameter := range operation.queryParams {
		if required, _ := parameter["required"].(bool); required {
			name, _ := parameter["name"].(string)
			query[name] = sampler.sample(parameter["schema"])
		}
	}
	if len(query) == 0 {
		return nil
	}
	return query
}

func checkOperation(t *testing.T, server *contractServer, sampler *sampler, method generatedMethod, operation *documentOperation) {
	pathValues := make([]string, 0, len(operation.paramNames))
	for _, name := range operation.paramNames {
		pathValues = append(pathValues, pathValue(name))
	}
	if got := pathArgumentCount(method); got != len(pathValues) {
		t.Fatalf("the method takes %d path parameters and %s declares %d", got, operation.key, len(pathValues))
	}

	var structArgs []any
	var body any
	if operation.hasBody {
		body = sampler.sample(operation.bodySchema)
		structArgs = append(structArgs, body)
	}
	if len(operation.queryParams) > 0 {
		structArgs = append(structArgs, requiredQuery(sampler, operation))
	}
	if want := method.value.Type().NumIn() - 2 - len(pathValues); want != len(structArgs) {
		t.Fatalf("the method takes %d body and query arguments and %s declares %d", want, operation.key, len(structArgs))
	}

	var opts []conjoin.CallOption
	if operation.security == "scimBearer" {
		opts = append(opts, conjoin.WithBearerToken(contractSCIM))
	}
	results := callMethod(method, pathValues, structArgs, opts)
	if err, _ := results[len(results)-1].Interface().(error); err != nil {
		t.Fatalf("the call failed: %v", err)
	}

	requests, unmatched := server.take()
	if len(requests) != 1 || len(unmatched) != 0 || requests[0].operation != operation {
		t.Fatalf("the call reached %d requests and %v undocumented routes", len(requests), unmatched)
	}
	request := requests[0]
	for index, name := range operation.paramNames {
		if request.pathParams[name] != pathValues[index] {
			t.Fatalf("the path parameter %s arrived as %q", name, request.pathParams[name])
		}
	}
	checkHeaders(t, request, operation)
	checkRequestBody(t, request, operation, body)
	if query, _ := requiredQuery(sampler, operation).(jsonObject); query != nil {
		for name := range query {
			if !hasQueryKey(request, name) {
				t.Fatalf("the required query parameter %s did not arrive", name)
			}
		}
	}
	if len(results) == 2 {
		checkResult(t, results[0].Interface(), operation)
	}
}

func hasQueryKey(request recordedRequest, name string) bool {
	for key := range request.query {
		if key == name || strings.HasPrefix(key, name+"[") {
			return true
		}
	}
	return false
}

func checkHeaders(t *testing.T, request recordedRequest, operation *documentOperation) {
	t.Helper()
	if id := request.header.Get("Conjoin-Request-Id"); !operation.requestIDRef.MatchString(id) {
		t.Fatalf("the request ID %q does not match the documented pattern", id)
	}
	for header, value := range scopeHeaders {
		want := ""
		if operation.headers[header] {
			want = value
		}
		if got := request.header.Get(header); got != want {
			t.Fatalf("the %s header arrived as %q, want %q", header, got, want)
		}
	}
	if key := request.header.Get("Idempotency-Key"); (key != "") != (operation.method == "POST" && operation.headers["idempotency-key"]) {
		t.Fatalf("the Idempotency-Key header arrived as %q", key)
	}
	wantAuthorization := map[string]string{"conjoinApiKey": "Bearer " + contractAPIKey, "scimBearer": "Bearer " + contractSCIM}[operation.security]
	if got := request.header.Get("Authorization"); got != wantAuthorization {
		t.Fatalf("the Authorization header arrived as %q, want %q", got, wantAuthorization)
	}
}

func checkRequestBody(t *testing.T, request recordedRequest, operation *documentOperation, body any) {
	t.Helper()
	if !operation.hasBody {
		if len(request.body) != 0 {
			t.Fatalf("a call without a documented body sent %q", request.body)
		}
		return
	}
	if operation.bodyType == "multipart/form-data" {
		if !strings.HasPrefix(request.header.Get("Content-Type"), "multipart/form-data; boundary=") {
			t.Fatalf("a form call sent the content type %q", request.header.Get("Content-Type"))
		}
		object, _ := body.(jsonObject)
		for name, value := range object {
			if _, isScalar := value.(string); isScalar && !strings.Contains(string(request.body), `name="`+name+`"`) {
				t.Fatalf("the form field %s did not arrive", name)
			}
		}
		return
	}
	var received any
	if err := json.Unmarshal(request.body, &received); err != nil {
		t.Fatalf("the body %q is not JSON: %v", request.body, err)
	}
	if !jsonEqual(t, received, body) {
		t.Fatalf("the server received the body %s, want %s", request.body, mustJSON(t, body))
	}
}

func checkResult(t *testing.T, result any, operation *documentOperation) {
	t.Helper()
	sample, _ := operation.successBody.(jsonObject)
	if sample == nil {
		return
	}
	data, hasData := sample["data"]
	if _, isList := sample["cursor"]; isList && hasData {
		page := reflect.ValueOf(result).Elem()
		cursor := page.FieldByName("Cursor").Interface().(conjoin.Cursor)
		wantCursor, _ := sample["cursor"].(jsonObject)
		if !jsonEqual(t, page.FieldByName("Data").Interface(), data) || cursor.Next != wantCursor["next"] || cursor.Prev != wantCursor["prev"] {
			t.Fatalf("the page returned %s with %+v, want %s", mustJSON(t, page.FieldByName("Data").Interface()), cursor, mustJSON(t, sample))
		}
		return
	}
	want := any(sample)
	if hasData {
		want = data
	}
	if !jsonEqual(t, result, want) {
		t.Fatalf("the call returned %s, want %s", mustJSON(t, result), mustJSON(t, want))
	}
}

func mustJSON(t *testing.T, value any) string {
	t.Helper()
	raw, err := json.Marshal(value)
	if err != nil {
		t.Fatalf("a value could not be encoded: %v", err)
	}
	return string(raw)
}
