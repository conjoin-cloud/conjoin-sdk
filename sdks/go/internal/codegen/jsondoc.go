package codegen

import (
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"strings"
)

const (
	maxDocumentDepth = 512
	maxRefHops       = 32
)

type object struct {
	keys   []string
	values map[string]any
}

func (o *object) get(key string) any {
	if o == nil {
		return nil
	}
	return o.values[key]
}

func (o *object) orderedKeys() []string {
	if o == nil {
		return nil
	}
	return o.keys
}

func (o *object) has(key string) bool {
	if o == nil {
		return false
	}
	_, ok := o.values[key]
	return ok
}

func (o *object) object(key string) *object {
	value, _ := o.get(key).(*object)
	return value
}

func (o *object) list(key string) []any {
	value, _ := o.get(key).([]any)
	return value
}

func (o *object) text(key string) string {
	value, _ := o.get(key).(string)
	return value
}

func parseDocument(data []byte) (*object, error) {
	decoder := json.NewDecoder(bytes.NewReader(data))
	decoder.UseNumber()
	root, err := readValue(decoder, 0)
	if err != nil {
		return nil, err
	}
	if _, err := decoder.Token(); !errors.Is(err, io.EOF) {
		return nil, errors.New("the document holds data after its root value")
	}
	document, ok := root.(*object)
	if !ok {
		return nil, errors.New("the document root is not an object")
	}
	return document, nil
}

func readValue(decoder *json.Decoder, depth int) (any, error) {
	if depth > maxDocumentDepth {
		return nil, errors.New("the document nests deeper than the generator allows")
	}
	token, err := decoder.Token()
	if err != nil {
		return nil, err
	}
	delimiter, isDelimiter := token.(json.Delim)
	if !isDelimiter {
		return token, nil
	}
	switch delimiter {
	case '{':
		result := &object{values: map[string]any{}}
		for decoder.More() {
			keyToken, err := decoder.Token()
			if err != nil {
				return nil, err
			}
			key, ok := keyToken.(string)
			if !ok {
				return nil, errors.New("an object key is not a string")
			}
			value, err := readValue(decoder, depth+1)
			if err != nil {
				return nil, err
			}
			if _, duplicate := result.values[key]; !duplicate {
				result.keys = append(result.keys, key)
			}
			result.values[key] = value
		}
		_, err := decoder.Token()
		return result, err
	case '[':
		items := []any{}
		for decoder.More() {
			value, err := readValue(decoder, depth+1)
			if err != nil {
				return nil, err
			}
			items = append(items, value)
		}
		_, err := decoder.Token()
		return items, err
	}
	return nil, fmt.Errorf("unexpected delimiter %v", delimiter)
}

func canonical(value any) string {
	var builder strings.Builder
	writeCanonical(&builder, value)
	return builder.String()
}

func writeCanonical(builder *strings.Builder, value any) {
	switch typed := value.(type) {
	case *object:
		builder.WriteByte('{')
		for index, key := range typed.keys {
			if index > 0 {
				builder.WriteByte(',')
			}
			writeCanonical(builder, key)
			builder.WriteByte(':')
			writeCanonical(builder, typed.values[key])
		}
		builder.WriteByte('}')
	case []any:
		builder.WriteByte('[')
		for index, item := range typed {
			if index > 0 {
				builder.WriteByte(',')
			}
			writeCanonical(builder, item)
		}
		builder.WriteByte(']')
	default:
		raw, _ := json.Marshal(typed)
		builder.Write(raw)
	}
}

type document struct {
	root *object
}

func (d *document) resolve(node any) (*object, error) {
	current, _ := node.(*object)
	for hop := 0; current != nil && current.has("$ref"); hop++ {
		if hop >= maxRefHops {
			return nil, errors.New("a $ref chain is longer than the generator allows")
		}
		ref := current.text("$ref")
		path, found := strings.CutPrefix(ref, "#/")
		if !found {
			return nil, fmt.Errorf("the reference %q is not local to the document", ref)
		}
		var target any = d.root
		for _, segment := range strings.Split(path, "/") {
			segment = strings.ReplaceAll(strings.ReplaceAll(segment, "~1", "/"), "~0", "~")
			parent, ok := target.(*object)
			if !ok || !parent.has(segment) {
				return nil, fmt.Errorf("the reference %q does not resolve", ref)
			}
			target = parent.get(segment)
		}
		next, ok := target.(*object)
		if !ok {
			return nil, fmt.Errorf("the reference %q does not point at an object", ref)
		}
		current = next
	}
	return current, nil
}
