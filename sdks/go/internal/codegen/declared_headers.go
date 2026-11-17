package codegen

import (
	"encoding/json"
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

type declaredHeader struct {
	name         string
	field        string
	required     bool
	minLength    int
	maxLength    int
	hasMaxLength bool
	pattern      string
	credential   bool
}

var reservedHeaderNames = map[string]bool{
	"accept":                true,
	"authorization":         true,
	"content-length":        true,
	"content-type":          true,
	"cookie":                true,
	"host":                  true,
	"user-agent":            true,
	"x-conjoin-api-version": true,
	"x-conjoin-sdk-version": true,
}

var credentialHeaderNames = map[string]bool{
	"step-up-token": true,
}

func (d *document) readDeclaredHeader(parameter *object, operationID string) (declaredHeader, error) {
	name := parameter.text("name")
	lower := strings.ToLower(name)
	if reservedHeaderNames[lower] {
		return declaredHeader{}, fmt.Errorf("%s declares the reserved header %s as a parameter", operationID, name)
	}
	schema, err := d.resolve(parameter.get("schema"))
	if err != nil {
		return declaredHeader{}, err
	}
	if schema.text("type") != "string" {
		return declaredHeader{}, fmt.Errorf("%s declares the header %s without a string schema", operationID, name)
	}
	header := declaredHeader{
		name:       name,
		field:      goIdentifier(name),
		required:   parameter.get("required") == true,
		credential: credentialHeaderNames[lower],
	}
	if header.minLength, _, err = readHeaderBound(schema, "minLength", operationID, name); err != nil {
		return declaredHeader{}, err
	}
	if header.maxLength, header.hasMaxLength, err = readHeaderBound(schema, "maxLength", operationID, name); err != nil {
		return declaredHeader{}, err
	}
	if header.hasMaxLength && header.maxLength < max(header.minLength, 1) {
		return declaredHeader{}, fmt.Errorf("%s declares the header %s with a maxLength that no value can meet", operationID, name)
	}
	if schema.has("pattern") {
		pattern, isText := schema.get("pattern").(string)
		if !isText {
			return declaredHeader{}, fmt.Errorf("%s declares the header %s with a pattern that is not a string", operationID, name)
		}
		if _, err := regexp.Compile(pattern); err != nil {
			return declaredHeader{}, fmt.Errorf("%s declares the header %s with a pattern that Go cannot check: %w", operationID, name, err)
		}
		header.pattern = pattern
	}
	return header, nil
}

func readHeaderBound(schema *object, key, operationID, name string) (int, bool, error) {
	if !schema.has(key) {
		return 0, false, nil
	}
	number, isNumber := schema.get(key).(json.Number)
	value, err := strconv.Atoi(number.String())
	if !isNumber || err != nil || value < 0 {
		return 0, false, fmt.Errorf("%s declares the header %s with a %s that is not a whole number", operationID, name, key)
	}
	return value, true, nil
}

func checkDeclaredHeaderFields(headers []declaredHeader, operationID string) error {
	fields := map[string]bool{}
	for _, header := range headers {
		if fields[header.field] {
			return fmt.Errorf("%s declares two headers that generate the field %s", operationID, header.field)
		}
		fields[header.field] = true
	}
	return nil
}

func (h declaredHeader) fieldType() string {
	if h.credential {
		return "conjoin.Credential"
	}
	return "string"
}

func renderHeadersType(typeName string, headers []declaredHeader) string {
	var builder strings.Builder
	fmt.Fprintf(&builder, "type %s struct {\n", typeName)
	for _, header := range headers {
		fmt.Fprintf(&builder, "\t%s %s `header:%s`\n", header.field, header.fieldType(), strconv.Quote(header.name))
	}
	builder.WriteString("}\n")
	return builder.String()
}

func declaredHeadersLiteral(headers []declaredHeader) string {
	entries := make([]string, 0, len(headers))
	for _, header := range headers {
		value := "headers." + header.field
		if !header.credential {
			value = "conjoin.Credential(" + value + ")"
		}
		fields := []string{
			"Name: " + strconv.Quote(header.name),
			"Argument: " + strconv.Quote(header.field),
			"Value: " + value,
		}
		if header.required {
			fields = append(fields, "Required: true")
		}
		if header.minLength > 0 {
			fields = append(fields, "MinLength: "+strconv.Itoa(header.minLength))
		}
		if header.hasMaxLength {
			fields = append(fields, "MaxLength: "+strconv.Itoa(header.maxLength))
		}
		if header.pattern != "" {
			fields = append(fields, "Pattern: "+strconv.Quote(header.pattern))
		}
		entries = append(entries, "{"+strings.Join(fields, ", ")+"}")
	}
	return "Headers: []conjoin.DeclaredHeader{" + strings.Join(entries, ", ") + "},"
}
