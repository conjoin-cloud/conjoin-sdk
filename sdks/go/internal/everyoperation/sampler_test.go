package everyoperation

import "strings"

const maxSampleDepth = 48

var patternSamples = map[string]string{
	"^[0-9a-f]+$": "9f86d081884c7d65",
}

type sampler struct {
	doc *openAPIDocument
}

func newSampler(doc *openAPIDocument) *sampler {
	return &sampler{doc: doc}
}

func (s *sampler) sample(schema any) any {
	return s.sampleAt(schema, 0)
}

func firstNonNullType(schema jsonObject) string {
	switch typed := schema["type"].(type) {
	case string:
		return typed
	case []any:
		for _, entry := range typed {
			if name, _ := entry.(string); name != "null" {
				return name
			}
		}
		return "null"
	}
	return ""
}

func isNullSchema(schema jsonObject) bool {
	_, hasConst := schema["const"]
	return firstNonNullType(schema) == "null" || (hasConst && schema["const"] == nil)
}

func (s *sampler) sampleAt(raw any, depth int) any {
	schema := s.doc.resolve(raw)
	if schema == nil || depth > maxSampleDepth {
		return nil
	}
	if value, ok := schema["const"]; ok {
		return value
	}
	if values, ok := schema["enum"].([]any); ok && len(values) > 0 {
		for _, value := range values {
			if value != nil {
				return value
			}
		}
		return values[0]
	}
	if _, hasProperties := schema["properties"]; !hasProperties {
		for _, key := range []string{"oneOf", "anyOf"} {
			if branches, ok := schema[key].([]any); ok && len(branches) > 0 {
				for _, branch := range branches {
					if resolved := s.doc.resolve(branch); resolved != nil && !isNullSchema(resolved) {
						return s.sampleAt(resolved, depth+1)
					}
				}
				return nil
			}
		}
	}
	if parts, ok := schema["allOf"].([]any); ok {
		merged := jsonObject{}
		for _, part := range parts {
			if sampled, ok := s.sampleAt(part, depth+1).(jsonObject); ok {
				for key, value := range sampled {
					merged[key] = value
				}
			}
		}
		if own, ok := s.sampleObject(schema, depth).(jsonObject); ok {
			for key, value := range own {
				merged[key] = value
			}
		}
		return merged
	}
	return s.sampleType(schema, firstNonNullType(schema), depth)
}

func (s *sampler) sampleObject(schema jsonObject, depth int) any {
	properties, _ := schema["properties"].(jsonObject)
	result := jsonObject{}
	required, hasRequired := schema["required"].([]any)
	if !hasRequired {
		for name := range properties {
			required = append(required, name)
		}
	}
	for _, entry := range required {
		name, _ := entry.(string)
		result[name] = s.sampleAt(properties[name], depth+1)
	}
	if branches, ok := schema["oneOf"].([]any); ok && len(branches) > 0 {
		if sampled, ok := s.sampleAt(branches[0], depth+1).(jsonObject); ok {
			for key, value := range sampled {
				result[key] = value
			}
		}
	}
	return result
}

func (s *sampler) sampleType(schema jsonObject, typeName string, depth int) any {
	switch typeName {
	case "string":
		if pattern, _ := schema["pattern"].(string); patternSamples[pattern] != "" {
			return patternSamples[pattern]
		}
		minimum, _ := schema["minLength"].(float64)
		maximum, hasMaximum := schema["maxLength"].(float64)
		text := strings.Repeat("harbourledger", int(minimum)/13+1)
		length := max(int(minimum), min(13, len(text)))
		if hasMaximum && length > int(maximum) {
			length = int(maximum)
		}
		return text[:length]
	case "integer", "number":
		if minimum, ok := schema["minimum"].(float64); ok {
			return minimum
		}
		if exclusive, ok := schema["exclusiveMinimum"].(float64); ok {
			return exclusive + 1
		}
		if maximum, ok := schema["maximum"].(float64); ok && maximum < 1 {
			return maximum
		}
		return float64(1)
	case "boolean":
		return true
	case "null":
		return nil
	case "array":
		count := 1
		if minimum, ok := schema["minItems"].(float64); ok && minimum > 1 {
			count = int(minimum)
		}
		items := make([]any, 0, count)
		for range count {
			items = append(items, s.sampleAt(schema["items"], depth+1))
		}
		return items
	case "object":
		return s.sampleObject(schema, depth)
	}
	if _, hasProperties := schema["properties"]; hasProperties {
		return s.sampleObject(schema, depth)
	}
	return "sample"
}
