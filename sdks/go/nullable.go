package conjoin

import (
	"bytes"
	"encoding/json"
)

type nullableState uint8

const (
	nullableUnset nullableState = iota
	nullableNull
	nullableValue
)

type Nullable[T any] struct {
	value T
	state nullableState
}

func Value[T any](value T) Nullable[T] {
	return Nullable[T]{value: value, state: nullableValue}
}

func Null[T any]() Nullable[T] {
	return Nullable[T]{state: nullableNull}
}

func (n Nullable[T]) Get() (T, bool) {
	return n.value, n.state == nullableValue
}

func (n Nullable[T]) IsNull() bool {
	return n.state == nullableNull
}

func (n Nullable[T]) IsZero() bool {
	return n.state == nullableUnset
}

func (n Nullable[T]) MarshalJSON() ([]byte, error) {
	if n.state != nullableValue {
		return []byte("null"), nil
	}
	return json.Marshal(n.value)
}

func (n *Nullable[T]) UnmarshalJSON(data []byte) error {
	if bytes.Equal(bytes.TrimSpace(data), []byte("null")) {
		var zero T
		n.value, n.state = zero, nullableNull
		return nil
	}
	var value T
	if err := json.Unmarshal(data, &value); err != nil {
		return err
	}
	n.value, n.state = value, nullableValue
	return nil
}
