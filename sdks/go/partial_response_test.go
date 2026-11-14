package conjoin_test

import (
	"context"
	"errors"
	"net/http"
	"net/http/httptest"
	"strconv"
	"sync/atomic"
	"testing"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

func TestTruncatedRefusalIsNotRetried(t *testing.T) {
	for _, status := range []int{400, 501} {
		t.Run(strconv.Itoa(status), func(t *testing.T) {
			var attempts atomic.Int32
			server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
				attempts.Add(1)
				w.Header().Set("Content-Length", "1000")
				w.WriteHeader(status)
				_, _ = w.Write([]byte(`{"error":`))
			}))
			defer server.Close()
			client, err := conjoin.NewClient(conjoin.WithAPIKey(testAPIKey), conjoin.WithBaseURL(server.URL), conjoin.WithRetryBackoff(0))
			if err != nil {
				t.Fatal(err)
			}
			err = readCustomer(context.Background(), client, http.MethodGet)
			var apiError *conjoin.APIError
			if !errors.As(err, &apiError) || apiError.Status != status || attempts.Load() != 1 {
				t.Fatalf("status %d returned %v after %d attempts", status, err, attempts.Load())
			}
		})
	}
}
