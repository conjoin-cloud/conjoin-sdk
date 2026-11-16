package everyoperation

import (
	"context"
	"encoding/json"
	"net/http"
	"reflect"
	"strings"
	"testing"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
	"github.com/conjoin-cloud/conjoin-sdk/sdks/go/ai"
	"github.com/conjoin-cloud/conjoin-sdk/sdks/go/auth"
	"github.com/conjoin-cloud/conjoin-sdk/sdks/go/billing"
	"github.com/conjoin-cloud/conjoin-sdk/sdks/go/cloud"
	frontendauth "github.com/conjoin-cloud/conjoin-sdk/sdks/go/frontend/auth"
	frontendcloud "github.com/conjoin-cloud/conjoin-sdk/sdks/go/frontend/cloud"
	"github.com/conjoin-cloud/conjoin-sdk/sdks/go/messaging"
	"github.com/conjoin-cloud/conjoin-sdk/sdks/go/relay"
	"github.com/conjoin-cloud/conjoin-sdk/sdks/go/storage"
)

const (
	contractAPIKey         = "cak_test_harbourledgerintegration"
	contractPublishableKey = "cpk_test_harbourledgerbrowser"
	contractSCIM           = "scim_harbourledger_directory"
	contractSessionToken   = "sess_harbourledger_signedin_owner"
	contractPortalTicket   = "ptk_harbourledger_portal_ticket"
	portalTicketHeader     = "x-portal-ticket"
	portalTicketQueryKey   = "ticket"
	billingEntity          = "ent_harbourledger"
	messagingProfile       = "mpr_harbourledger"
	authApp                = "app_harbourledger"
)

var expectedAuthorizationByScheme = map[string]string{
	"conjoinApiKey":         "Bearer " + contractAPIKey,
	"scimBearer":            "Bearer " + contractSCIM,
	"conjoinPublishableKey": "Bearer " + contractPublishableKey,
	"conjoinSessionBearer":  "Bearer " + contractSessionToken,
}

var credentialType = reflect.TypeFor[conjoin.Credential]()

type callArguments struct {
	pathValues   []string
	structArgs   []any
	headerValues map[string]string
	sessionToken conjoin.Credential
}

var scopeHeaders = map[string]string{
	"billing-entity-id":    billingEntity,
	"messaging-profile-id": messagingProfile,
	"auth-app-id":          authApp,
}

type generatedMethod struct {
	name  string
	value reflect.Value
}

func packageClients(document string, client *conjoin.Client) map[string]any {
	if document == "openapi-frontend.json" {
		return map[string]any{"frontend/auth": frontendauth.New(client), "frontend/cloud": frontendcloud.New(client)}
	}
	return map[string]any{
		"ai": ai.New(client), "auth": auth.New(client), "billing": billing.New(client), "cloud": cloud.New(client),
		"messaging": messaging.New(client), "relay": relay.New(client), "storage": storage.New(client),
	}
}

func generatedMethods(clients map[string]any) []generatedMethod {
	var methods []generatedMethod
	for packageName, client := range clients {
		services := reflect.ValueOf(client).Elem()
		for field := range services.NumField() {
			service := services.Field(field)
			for index := range service.NumMethod() {
				name := packageName + "." + services.Type().Field(field).Name + "." + service.Type().Method(index).Name
				methods = append(methods, generatedMethod{name: name, value: service.Method(index)})
			}
		}
	}
	return methods
}

func sampleArgument(argumentType reflect.Type, sample any) (reflect.Value, error) {
	target := reflect.New(argumentType)
	if sample != nil {
		raw, err := json.Marshal(sample)
		if err != nil {
			return reflect.Value{}, err
		}
		if err := json.Unmarshal(raw, target.Interface()); err != nil {
			return reflect.Value{}, err
		}
	}
	if argumentType.Kind() == reflect.Pointer && target.Elem().IsNil() {
		target.Elem().Set(reflect.New(argumentType.Elem()))
	}
	if argumentType.Kind() == reflect.Interface && target.Elem().IsNil() {
		target.Elem().Set(reflect.ValueOf(map[string]any{}))
	}
	if argumentType.Kind() == reflect.Map && target.Elem().IsNil() {
		target.Elem().Set(reflect.MakeMap(argumentType))
	}
	if argumentType.Kind() == reflect.Slice && target.Elem().IsNil() {
		target.Elem().Set(reflect.MakeSlice(argumentType, 0, 0))
	}
	return target.Elem(), nil
}

func pathValue(name string) string {
	return "ledger/" + name + " 7?#%ä"
}

func isPathArgument(argumentType reflect.Type) bool {
	return argumentType.Kind() == reflect.String && argumentType != credentialType
}

func isHeadersArgument(argumentType reflect.Type) bool {
	if argumentType.Kind() != reflect.Struct || argumentType.NumField() == 0 {
		return false
	}
	_, isTagged := argumentType.Field(0).Tag.Lookup("header")
	return isTagged
}

func headersArgument(argumentType reflect.Type, values map[string]string) reflect.Value {
	target := reflect.New(argumentType).Elem()
	for index := range argumentType.NumField() {
		field := argumentType.Field(index)
		if value, found := values[strings.ToLower(field.Tag.Get("header"))]; found {
			target.Field(index).SetString(value)
		}
	}
	return target
}

func countArguments(method generatedMethod, matches func(reflect.Type) bool) int {
	count := 0
	for index := 1; index < method.value.Type().NumIn()-1; index++ {
		if matches(method.value.Type().In(index)) {
			count++
		}
	}
	return count
}

func isSampledArgument(argumentType reflect.Type) bool {
	return argumentType.Kind() != reflect.String && !isHeadersArgument(argumentType)
}

func isSessionArgument(argumentType reflect.Type) bool {
	return argumentType == credentialType
}

func callMethod(method generatedMethod, call callArguments, opts []conjoin.CallOption) []reflect.Value {
	methodType := method.value.Type()
	args := []reflect.Value{reflect.ValueOf(context.Background())}
	stringIndex, structIndex := 0, 0
	for index := 1; index < methodType.NumIn()-1; index++ {
		argumentType := methodType.In(index)
		switch {
		case isSessionArgument(argumentType):
			args = append(args, reflect.ValueOf(call.sessionToken))
			continue
		case isPathArgument(argumentType):
			args = append(args, reflect.ValueOf(call.pathValues[stringIndex]))
			stringIndex++
			continue
		case isHeadersArgument(argumentType):
			args = append(args, headersArgument(argumentType, call.headerValues))
			continue
		}
		var sample any
		if structIndex < len(call.structArgs) {
			sample = call.structArgs[structIndex]
		}
		structIndex++
		value, err := sampleArgument(argumentType, sample)
		if err != nil {
			panic(method.name + ": " + err.Error())
		}
		args = append(args, value)
	}
	for _, opt := range opts {
		args = append(args, reflect.ValueOf(opt))
	}
	return method.value.Call(args)
}

func pathArgumentCount(method generatedMethod) int {
	return countArguments(method, isPathArgument)
}

func jsonEqual(t *testing.T, got, want any) bool {
	t.Helper()
	normalize := func(value any) any {
		raw, err := json.Marshal(value)
		if err != nil {
			t.Fatalf("a value could not be encoded: %v", err)
		}
		var decoded any
		if err := json.Unmarshal(raw, &decoded); err != nil {
			t.Fatalf("a value could not be decoded: %v", err)
		}
		return decoded
	}
	return reflect.DeepEqual(normalize(got), normalize(want))
}

func TestEveryOperationInBothDocuments(t *testing.T) {
	for _, file := range []string{"openapi.json", "openapi-frontend.json"} {
		t.Run(file, func(t *testing.T) {
			doc := loadDocument(t, file)
			server := startContractServer(t, doc)
			key := conjoin.WithAPIKey(contractAPIKey)
			if file == "openapi-frontend.json" {
				key = conjoin.WithPublishableKey(contractPublishableKey)
			}
			client, err := conjoin.NewClient(
				key,
				conjoin.WithBaseURL(server.server.URL),
				conjoin.WithHTTPClient(&http.Client{Transport: server.transport}),
				conjoin.WithBillingEntityID(billingEntity),
				conjoin.WithMessagingProfileID(messagingProfile),
				conjoin.WithAuthAppID(authApp),
				conjoin.WithMaxRetries(0),
			)
			if err != nil {
				t.Fatalf("the client did not start: %v", err)
			}

			called := map[string]string{}
			sampler := newSampler(doc)
			for _, method := range generatedMethods(packageClients(file, client)) {
				operation := probe(t, server, method)
				if previous, seen := called[operation.key]; seen {
					t.Fatalf("%s and %s both call %s", previous, method.name, operation.key)
				}
				called[operation.key] = method.name
				t.Run(method.name, func(t *testing.T) {
					checkOperation(t, server, sampler, method, operation)
				})
			}
			for _, operation := range doc.operations {
				if _, ok := called[operation.key]; !ok {
					t.Errorf("no generated method calls %s", operation.key)
				}
			}
		})
	}
}

func probe(t *testing.T, server *contractServer, method generatedMethod) *documentOperation {
	t.Helper()
	pathValues := make([]string, pathArgumentCount(method))
	for index := range pathValues {
		pathValues[index] = "probe"
	}
	call := callArguments{
		pathValues:   pathValues,
		headerValues: map[string]string{portalTicketHeader: contractPortalTicket},
		sessionToken: contractSessionToken,
	}
	results := callMethod(method, call, nil)
	requests, unmatched := server.take()
	if len(requests) == 0 && len(unmatched) == 0 {
		results = callMethod(method, call, []conjoin.CallOption{conjoin.WithBearerToken(contractSCIM)})
		requests, unmatched = server.take()
	}
	if len(requests) != 1 || len(unmatched) != 0 {
		t.Fatalf("%s reached %d documented routes and %v undocumented ones, and returned %v", method.name, len(requests), unmatched, results[len(results)-1].Interface())
	}
	return requests[0].operation
}
