package conjoin

import (
	"fmt"
	"io"
	"log/slog"
)

const redactedCredential = "[redacted]"

type Credential string

func (c Credential) String() string {
	return redactedCredential
}

func (c Credential) GoString() string {
	return redactedCredential
}

func (c Credential) Format(state fmt.State, _ rune) {
	_, _ = io.WriteString(state, redactedCredential)
}

func (c Credential) LogValue() slog.Value {
	return slog.StringValue(redactedCredential)
}

func (c Credential) MarshalText() ([]byte, error) {
	return []byte(redactedCredential), nil
}
