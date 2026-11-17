package conjoin

import (
	"bytes"
	"context"
	"encoding/json"
	"net/http"
	"net/url"
	"reflect"
	"time"
)

type response struct {
	status    int
	header    http.Header
	body      []byte
	requestID string
}

func responseRequestID(header http.Header, sent string) string {
	if received := header.Get(requestIDHeader); isValidRequestID(received) {
		return received
	}
	return sent
}

func failureError(result attemptResult, p *preparedRequest) error {
	switch result.failure {
	case failureCanceled:
		return &CanceledError{RequestID: p.requestID, Err: result.err}
	case failureTimeout:
		return &TimeoutError{RequestID: p.requestID, Timeout: p.timeout}
	case failureNetwork:
		return &NetworkError{RequestID: p.requestID, Err: result.err}
	}
	return result.err
}

func (c *Client) execute(ctx context.Context, p *preparedRequest) (*response, error) {
	for attempt := 0; ; attempt++ {
		if err := ctx.Err(); err != nil {
			return nil, &CanceledError{RequestID: p.requestID, Err: err}
		}

		canRetryAgain := p.retryAllowed && attempt < p.maxRetries
		result := c.attempt(ctx, p, canRetryAgain)

		if result.failure != failureNone {
			retryable := result.failure == failureNetwork || result.failure == failureTimeout
			if !canRetryAgain || !retryable {
				return nil, failureError(result, p)
			}
			if err := waitForRetry(ctx, c.retryDelay(attempt, 0, false)); err != nil {
				return nil, &CanceledError{RequestID: p.requestID, Err: err}
			}
			continue
		}

		if canRetryAgain && retryableStatuses[result.status] {
			retryAfter, hasRetryAfter := parseRetryAfter(result.header.Get(retryAfterHeader), time.Now())
			if err := waitForRetry(ctx, c.retryDelay(attempt, retryAfter, hasRetryAfter)); err != nil {
				return nil, &CanceledError{RequestID: p.requestID, Err: err}
			}
			continue
		}

		requestID := responseRequestID(result.header, p.requestID)
		if !isSuccessStatus(result.status) {
			return nil, buildAPIError(result.status, result.header, result.body, requestID, time.Now())
		}
		return &response{status: result.status, header: result.header, body: result.body, requestID: requestID}, nil
	}
}

func (c *Client) send(ctx context.Context, op Operation, query url.Values, opts []CallOption) (*response, error) {
	prepared, err := c.prepare(ctx, op, query, opts)
	if err != nil {
		return nil, err
	}
	return c.execute(ctx, prepared)
}

func isDecodeTarget(out any) bool {
	if out == nil {
		return false
	}
	value := reflect.ValueOf(out)
	return value.Kind() == reflect.Pointer && !value.IsNil()
}

func (c *Client) Do(ctx context.Context, op Operation, out any, opts ...CallOption) error {
	if out != nil && !isDecodeTarget(out) {
		return configurationError("the result must be a non-nil pointer")
	}
	query, err := flattenQuery(op.Query)
	if err != nil {
		return err
	}
	res, err := c.send(ctx, op, query, opts)
	if err != nil {
		return err
	}
	return decodeResult(res, op.Response, out)
}

func invalidResponse(res *response, reason string) error {
	return &ResponseError{Status: res.status, RequestID: res.requestID, Reason: reason}
}

func decodeResult(res *response, shape ResponseShape, out any) error {
	body := bytes.TrimSpace(res.body)
	if shape == ResponseEmpty || len(body) == 0 {
		return nil
	}
	if !json.Valid(body) {
		return invalidResponse(res, "the response body was not valid JSON")
	}
	if out == nil {
		return nil
	}
	if shape == ResponseBody {
		if err := json.Unmarshal(body, out); err != nil {
			return invalidResponse(res, "the response body did not match the documented shape")
		}
		return nil
	}
	envelope := struct {
		Data any `json:"data"`
	}{Data: out}
	if err := json.Unmarshal(body, &envelope); err != nil {
		return invalidResponse(res, "the response data did not match the documented shape")
	}
	return nil
}
