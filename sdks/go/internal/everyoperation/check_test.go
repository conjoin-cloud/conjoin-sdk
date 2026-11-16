package everyoperation

import (
	"bytes"
	"context"
	"encoding/json"
	"net/url"
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
	if got := countArguments(method, isSampledArgument); got != len(structArgs) {
		t.Fatalf("the method takes %d body and query arguments and %s declares %d", got, operation.key, len(structArgs))
	}

	headerValues := declaredHeaderSamples(sampler, operation)
	if got, want := countArguments(method, isHeadersArgument), min(len(headerValues), 1); got != want {
		t.Fatalf("the method takes %d header arguments and %s declares %d headers", got, operation.key, len(headerValues))
	}
	wantSessionArguments := 0
	if operation.security == "conjoinSessionBearer" {
		wantSessionArguments = 1
	}
	if got := countArguments(method, isSessionArgument); got != wantSessionArguments {
		t.Fatalf("the method takes %d session tokens and %s uses the scheme %q", got, operation.key, operation.security)
	}

	var opts []conjoin.CallOption
	if operation.security == "scimBearer" {
		opts = append(opts, conjoin.WithBearerToken(contractSCIM))
	}
	call := callArguments{pathValues: pathValues, structArgs: structArgs, headerValues: headerValues, sessionToken: contractSessionToken}
	results := callMethod(method, call, opts)
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
	checkDeclaredHeaders(t, request, headerValues)
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
		checkNextPage(t, server, results[0], operation, body, request)
	}
}

func checkNextPage(t *testing.T, server *contractServer, page reflect.Value, operation *documentOperation, body any, first recordedRequest) {
	t.Helper()
	sample, _ := operation.successBody.(jsonObject)
	cursor, isList := sample["cursor"].(jsonObject)
	if !isList {
		return
	}
	next, _ := cursor["next"].(string)
	if next == "" {
		t.Fatalf("the sampled list response of %s holds no next cursor", operation.key)
	}
	hasNext := page.MethodByName("HasNextPage").Call(nil)[0].Bool()
	if !operation.cursorBody && !operation.cursorQuery {
		if hasNext {
			t.Fatalf("%s takes no cursor, yet its page offers a next page", operation.key)
		}
		return
	}
	results := page.MethodByName("NextPage").Call([]reflect.Value{reflect.ValueOf(context.Background())})
	if err, _ := results[1].Interface().(error); err != nil {
		t.Fatalf("the next page failed: %v", err)
	}
	requests, unmatched := server.take()
	if len(requests) != 1 || len(unmatched) != 0 || requests[0].operation != operation {
		t.Fatalf("the next page reached %d requests and %v undocumented routes", len(requests), unmatched)
	}
	second := requests[0]
	if operation.cursorQuery {
		want := url.Values{}
		for key, values := range first.query {
			want[key] = values
		}
		want.Set("cursor[next]", next)
		if second.query.Encode() != want.Encode() || !bytes.Equal(second.body, first.body) {
			t.Fatalf("the next page sent the query %s and the body %q, want the query %s", second.query.Encode(), second.body, want.Encode())
		}
		return
	}
	wantBody := jsonObject{}
	if object, ok := body.(jsonObject); ok {
		for key, value := range object {
			wantBody[key] = value
		}
	}
	wantBody["cursor"] = jsonObject{"next": next}
	var received any
	if err := json.Unmarshal(second.body, &received); err != nil || !jsonEqual(t, received, wantBody) {
		t.Fatalf("the next page sent the body %q, want %s", second.body, mustJSON(t, wantBody))
	}
	if second.query.Encode() != first.query.Encode() {
		t.Fatalf("the next page sent the query %s, want %s", second.query.Encode(), first.query.Encode())
	}
	if key := first.header.Get("Idempotency-Key"); key != "" && second.header.Get("Idempotency-Key") == key {
		t.Fatalf("the next page reused the Idempotency-Key %q of the first page", key)
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
	wantAuthorization := expectedAuthorizationByScheme[operation.security]
	if got := request.header.Get("Authorization"); got != wantAuthorization {
		t.Fatalf("the Authorization header arrived as %q, want %q", got, wantAuthorization)
	}
}

func declaredHeaderSamples(sampler *sampler, operation *documentOperation) map[string]string {
	values := map[string]string{}
	for _, parameter := range operation.headerParams {
		name, _ := parameter["name"].(string)
		value, _ := sampler.sample(parameter["schema"]).(string)
		values[strings.ToLower(name)] = value
	}
	if operation.security == "conjoinPortalTicketHeader" {
		values[portalTicketHeader] = contractPortalTicket
	}
	return values
}

func checkDeclaredHeaders(t *testing.T, request recordedRequest, headerValues map[string]string) {
	t.Helper()
	for name, want := range headerValues {
		if got := request.header.Get(name); got != want {
			t.Fatalf("the declared header %s arrived as %q, want %q", name, got, want)
		}
	}
	if request.query.Has(portalTicketQueryKey) || strings.Contains(request.query.Encode(), contractPortalTicket) {
		t.Fatalf("the query string carried the portal ticket: %s", request.query.Encode())
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
