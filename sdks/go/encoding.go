package conjoin

import (
	"bytes"
	"encoding/json"
	"mime/multipart"
	"net/url"
	"slices"
)

const jsonContentType = "application/json"

func decodeJSONTree(value any) (any, error) {
	raw, err := json.Marshal(value)
	if err != nil {
		return nil, err
	}
	decoder := json.NewDecoder(bytes.NewReader(raw))
	decoder.UseNumber()
	var tree any
	if err := decoder.Decode(&tree); err != nil {
		return nil, err
	}
	return tree, nil
}

func sortedKeys(object map[string]any) []string {
	keys := make([]string, 0, len(object))
	for key := range object {
		keys = append(keys, key)
	}
	slices.Sort(keys)
	return keys
}

func scalarText(value any) (string, error) {
	switch typed := value.(type) {
	case string:
		return typed, nil
	case json.Number:
		return typed.String(), nil
	case bool:
		if typed {
			return "true", nil
		}
		return "false", nil
	}
	raw, err := json.Marshal(value)
	return string(raw), err
}

func flattenQuery(query any) (url.Values, error) {
	values := url.Values{}
	if isNil(query) {
		return values, nil
	}
	tree, err := decodeJSONTree(query)
	if err != nil {
		return nil, configurationError("the query parameters could not be encoded")
	}
	object, ok := tree.(map[string]any)
	if !ok {
		return nil, configurationError("the query parameters must encode to a JSON object")
	}
	for _, key := range sortedKeys(object) {
		if err := appendQueryValue(values, key, object[key]); err != nil {
			return nil, configurationError("the query parameters could not be encoded")
		}
	}
	return values, nil
}

func appendQueryValue(values url.Values, key string, value any) error {
	switch typed := value.(type) {
	case nil:
		return nil
	case []any:
		for _, item := range typed {
			if item == nil {
				continue
			}
			text, err := scalarText(item)
			if err != nil {
				return err
			}
			values.Add(key, text)
		}
		return nil
	case map[string]any:
		for _, nested := range sortedKeys(typed) {
			if err := appendQueryValue(values, key+"["+nested+"]", typed[nested]); err != nil {
				return err
			}
		}
		return nil
	}
	text, err := scalarText(value)
	if err != nil {
		return err
	}
	values.Add(key, text)
	return nil
}

func encodeBody(op Operation) ([]byte, string, error) {
	if isNil(op.Body) {
		return nil, "", nil
	}
	if op.Multipart {
		return encodeMultipart(op.Body)
	}
	raw, err := json.Marshal(op.Body)
	if err != nil {
		return nil, "", configurationError("the request body could not be encoded as JSON")
	}
	return raw, jsonContentType, nil
}

func encodeMultipart(body any) ([]byte, string, error) {
	tree, err := decodeJSONTree(body)
	if err != nil {
		return nil, "", configurationError("the request body could not be encoded as a form")
	}
	object, ok := tree.(map[string]any)
	if !ok {
		return nil, "", configurationError("a form request body must encode to a JSON object")
	}

	var buffer bytes.Buffer
	writer := multipart.NewWriter(&buffer)
	for _, key := range sortedKeys(object) {
		items, isList := object[key].([]any)
		if !isList {
			items = []any{object[key]}
		}
		for _, item := range items {
			if item == nil {
				continue
			}
			text, err := scalarText(item)
			if err != nil {
				return nil, "", configurationError("the request body could not be encoded as a form")
			}
			if err := writer.WriteField(key, text); err != nil {
				return nil, "", configurationError("the request body could not be encoded as a form")
			}
		}
	}
	if err := writer.Close(); err != nil {
		return nil, "", configurationError("the request body could not be encoded as a form")
	}
	return buffer.Bytes(), writer.FormDataContentType(), nil
}
