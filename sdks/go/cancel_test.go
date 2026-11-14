package conjoin_test

import (
	"context"
	"errors"
	"net/http"
	"regexp"
	"runtime"
	"testing"
	"time"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

func TestReadThatTimesOutIsRetriedAndReturnsTheNextAnswer(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: slowAnswer, delay: 2 * time.Second})
	if err := readCustomer(context.Background(), server.client(t, conjoin.WithTimeout(100*time.Millisecond)), http.MethodGet); err != nil {
		t.Fatalf("the read failed: %v", err)
	}
	if len(server.recorded()) != 2 {
		t.Fatalf("the server saw %d attempts, want 2", len(server.recorded()))
	}
}

func TestTimeoutErrorDiffersFromCancellation(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: slowAnswer, delay: 2 * time.Second})
	client := server.client(t, conjoin.WithMaxRetries(0))

	err := readCustomer(context.Background(), client, http.MethodGet, conjoin.WithTimeout(100*time.Millisecond))
	var timeoutError *conjoin.TimeoutError
	if !errors.As(err, &timeoutError) || !errors.Is(err, conjoin.ErrTimeout) {
		t.Fatalf("the read gave %v, want a timeout error", err)
	}
	if errors.Is(err, context.Canceled) || errors.Is(err, conjoin.ErrCanceled) || timeoutError.Timeout != 100*time.Millisecond {
		t.Fatalf("the timeout error %v matched a cancellation or carried the wrong timeout", err)
	}
}

func expectCanceled(t *testing.T, err error, startedAt time.Time, limit time.Duration) {
	t.Helper()
	var canceled *conjoin.CanceledError
	if !errors.As(err, &canceled) || !errors.Is(err, context.Canceled) || !errors.Is(err, conjoin.ErrCanceled) {
		t.Fatalf("the call gave %v, want a cancellation that matches context.Canceled", err)
	}
	if errors.Is(err, conjoin.ErrTimeout) {
		t.Fatalf("the cancellation %v matched a timeout", err)
	}
	if elapsed := time.Since(startedAt); elapsed > limit {
		t.Fatalf("the call ended %s after the cancellation, want under %s", elapsed, limit)
	}
}

func TestCancelEndsARequestInFlightAtOnce(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: slowAnswer, delay: 5 * time.Second})
	ctx, cancel := context.WithCancel(context.Background())
	timer := time.AfterFunc(50*time.Millisecond, cancel)
	defer timer.Stop()

	startedAt := time.Now()
	err := readCustomer(ctx, server.client(t), http.MethodGet)
	expectCanceled(t, err, startedAt, time.Second)
	if len(server.recorded()) != 1 {
		t.Fatalf("the server saw %d attempts, want 1", len(server.recorded()))
	}
}

func TestCancelEndsTheWaitBeforeARetry(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: statusAnswer, status: http.StatusServiceUnavailable, header: map[string]string{"Retry-After": "30"}, body: errorBody(503)})
	ctx, cancel := context.WithCancel(context.Background())
	timer := time.AfterFunc(200*time.Millisecond, cancel)
	defer timer.Stop()

	startedAt := time.Now()
	err := readCustomer(ctx, server.client(t, conjoin.WithMaxRetryDelay(time.Minute)), http.MethodGet)
	expectCanceled(t, err, startedAt, 1500*time.Millisecond)
	if len(server.recorded()) != 1 {
		t.Fatalf("the server saw %d attempts, want 1", len(server.recorded()))
	}
}

func TestCanceledContextSendsNothing(t *testing.T) {
	server := startUnreliableServer(t)
	ctx, cancel := context.WithCancel(context.Background())
	cancel()
	expectCanceled(t, readCustomer(ctx, server.client(t), http.MethodGet), time.Now(), time.Second)
	if _, err := createCustomer(ctx, server.client(t), true); !errors.Is(err, context.Canceled) {
		t.Fatalf("a canceled create gave %v", err)
	}
	if len(server.recorded()) != 0 {
		t.Fatalf("the server saw %d attempts, want none", len(server.recorded()))
	}
}

func TestRequestIDsAreFreshPerCallAndStableAcrossRetries(t *testing.T) {
	server := startUnreliableServer(t)
	client := server.client(t)
	pattern := regexp.MustCompile(requestIDExpression)

	server.queue(behaviour{kind: statusAnswer, status: http.StatusBadGateway, body: errorBody(502)})
	if err := readCustomer(context.Background(), client, http.MethodGet); err != nil {
		t.Fatalf("the read failed: %v", err)
	}
	if err := readCustomer(context.Background(), client, http.MethodGet); err != nil {
		t.Fatalf("the read failed: %v", err)
	}
	server.queue(behaviour{kind: statusAnswer, status: http.StatusBadGateway, body: errorBody(502)})
	if err := readCustomer(context.Background(), client, http.MethodGet, conjoin.WithRequestID(callerRequestID)); err != nil {
		t.Fatalf("the read failed: %v", err)
	}

	ids := []string{}
	for _, attempt := range server.recorded() {
		ids = append(ids, attempt.header.Get("Conjoin-Request-Id"))
	}
	if len(ids) != 5 || !pattern.MatchString(ids[0]) || ids[0] != ids[1] || !pattern.MatchString(ids[2]) || ids[2] == ids[0] {
		t.Fatalf("the attempts carried the request IDs %v", ids)
	}
	if ids[3] != callerRequestID || ids[4] != callerRequestID {
		t.Fatalf("the caller request ID was not kept on every retry: %v", ids)
	}
}

func TestClientRequestIDIsSentAndExposedOnErrors(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: statusAnswer, status: http.StatusNotFound, body: errorBody(404)})
	client := server.client(t, conjoin.WithRequestID(callerRequestID))

	err := readCustomer(context.Background(), client, http.MethodGet)
	var apiError *conjoin.APIError
	if !errors.As(err, &apiError) || apiError.RequestID != callerRequestID {
		t.Fatalf("the read gave %v, want a not found error that carries the caller request ID", err)
	}
	if got := server.recorded()[0].header.Get("Conjoin-Request-Id"); got != callerRequestID {
		t.Fatalf("the server saw the request ID %q", got)
	}
}

func TestFailedAndCanceledCallsLeaveNoGoroutinesBehind(t *testing.T) {
	baseline := runtime.NumGoroutine()
	server := startUnreliableServer(t)
	client := server.client(t, conjoin.WithTimeout(50*time.Millisecond))

	for range 3 {
		server.queue(behaviour{kind: slowAnswer, delay: time.Second}, behaviour{kind: dropBeforeStore}, behaviour{kind: statusAnswer, status: http.StatusServiceUnavailable})
		_ = readCustomer(context.Background(), client, http.MethodGet, conjoin.WithMaxRetries(3))
		ctx, cancel := context.WithTimeout(context.Background(), 20*time.Millisecond)
		server.queue(behaviour{kind: slowAnswer, delay: time.Second})
		_ = readCustomer(ctx, client, http.MethodGet)
		cancel()
	}
	server.transport.CloseIdleConnections()
	server.server.CloseClientConnections()
	server.server.Close()

	deadline := time.Now().Add(3 * time.Second)
	for runtime.NumGoroutine() > baseline && time.Now().Before(deadline) {
		time.Sleep(20 * time.Millisecond)
	}
	if count := runtime.NumGoroutine(); count > baseline {
		t.Fatalf("%d goroutines remain, %d more than before the calls", count, count-baseline)
	}
}
