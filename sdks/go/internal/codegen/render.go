package codegen

import (
	"fmt"
	"strconv"
	"strings"
)

func renderStruct(def *structDef) string {
	if def.target != "" {
		return fmt.Sprintf("type %s = %s\n", def.name, def.target)
	}
	var builder strings.Builder
	fmt.Fprintf(&builder, "type %s struct {\n", def.name)
	for _, field := range def.fields {
		fmt.Fprintf(&builder, "\t%s %s %s\n", field.goName, field.expr(), field.tag())
	}
	builder.WriteString("}\n")
	return builder.String()
}

func renderServiceType(typeName string) string {
	return fmt.Sprintf("type %s struct {\n\tclient *conjoin.Client\n}\n", typeName)
}

func operationLiteral(op *operation, pathArgs []string, types operationTypes) []string {
	fields := []string{
		"Method: " + strconv.Quote(op.method) + ",",
		"Path: " + strconv.Quote(strings.TrimPrefix(op.path, "/v1/")) + ",",
	}
	if len(pathArgs) > 0 {
		fields = append(fields, "PathParams: []string{"+strings.Join(pathArgs, ", ")+"},")
	}
	if types.queryParam != "" {
		fields = append(fields, "Query: query,")
		for _, parameter := range op.query {
			if parameter.required {
				fields = append(fields, "QueryRequired: true,")
				break
			}
		}
	}
	if types.bodyParam != "" {
		fields = append(fields, "Body: body,")
		if op.bodyRequired {
			fields = append(fields, "BodyRequired: true,")
		}
		if op.multipart {
			fields = append(fields, "Multipart: true,")
		}
	}
	if len(op.scopes) > 0 {
		fields = append(fields, "Scopes: []conjoin.ScopeName{"+strings.Join(op.scopes, ", ")+"},")
	}
	if op.acceptsIdempotencyKey {
		fields = append(fields, "AcceptsIdempotencyKey: true,")
	}
	if op.auth != "" {
		fields = append(fields, "Auth: "+op.auth+",")
	}
	switch op.kind {
	case responseBody:
		fields = append(fields, "Response: conjoin.ResponseBody,")
	case responseEmpty:
		fields = append(fields, "Response: conjoin.ResponseEmpty,")
	}
	return fields
}

func pathArguments(op *operation) []string {
	used := map[string]bool{}
	names := make([]string, 0, len(op.pathParams))
	for _, param := range op.pathParams {
		name := goParameterName(param)
		for suffix := 2; used[name]; suffix++ {
			name = goParameterName(param) + strconv.Itoa(suffix)
		}
		used[name] = true
		names = append(names, name)
	}
	return names
}

func renderMethod(serviceType string, op *operation, types operationTypes) string {
	pathArgs := pathArguments(op)
	params := []string{"ctx context.Context"}
	for _, name := range pathArgs {
		params = append(params, name+" string")
	}
	if types.bodyParam != "" {
		params = append(params, "body "+types.bodyParam)
	}
	if types.queryParam != "" {
		params = append(params, "query "+types.queryParam)
	}
	params = append(params, "opts ...conjoin.CallOption")

	literal := "conjoin.Operation{\n\t\t" + strings.Join(operationLiteral(op, pathArgs, types), "\n\t\t") + "\n\t}"
	signature := fmt.Sprintf("func (s *%s) %s(%s)", serviceType, op.methodName, strings.Join(params, ", "))

	var builder strings.Builder
	switch {
	case op.kind == responseList:
		fmt.Fprintf(&builder, "%s (*conjoin.Page[%s], error) {\n", signature, types.listItem)
		fmt.Fprintf(&builder, "\treturn conjoin.List[%s](ctx, s.client, %s, opts...)\n}\n", types.listItem, literal)
	case types.result == "":
		fmt.Fprintf(&builder, "%s error {\n", signature)
		fmt.Fprintf(&builder, "\treturn s.client.Do(ctx, %s, nil, opts...)\n}\n", literal)
	case types.resultKind == kindStruct:
		fmt.Fprintf(&builder, "%s (*%s, error) {\n\tvar out %s\n", signature, types.result, types.result)
		fmt.Fprintf(&builder, "\tif err := s.client.Do(ctx, %s, &out, opts...); err != nil {\n\t\treturn nil, err\n\t}\n\treturn &out, nil\n}\n", literal)
	default:
		fmt.Fprintf(&builder, "%s (%s, error) {\n\tvar out %s\n", signature, types.result, types.result)
		fmt.Fprintf(&builder, "\terr := s.client.Do(ctx, %s, &out, opts...)\n\treturn out, err\n}\n", literal)
	}
	return builder.String()
}

func renderPackageClient(packageName string, fields []string) string {
	var builder strings.Builder
	fmt.Fprintf(&builder, "package %s\n\nimport conjoin %q\n\ntype Client struct {\n", packageName, modulePath)
	for _, field := range fields {
		fmt.Fprintf(&builder, "\t%s *%sService\n", field, field)
	}
	builder.WriteString("}\n\nfunc New(client *conjoin.Client) *Client {\n\treturn &Client{\n")
	for _, field := range fields {
		fmt.Fprintf(&builder, "\t\t%s: &%sService{client: client},\n", field, field)
	}
	builder.WriteString("\t}\n}\n")
	return builder.String()
}
