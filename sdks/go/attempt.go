package conjoin

import (
	"bytes"
	"context"
	"errors"
	"io"
	"net/http"
	"net/url"
)

const (
	maxSuccessBodyBytes = 64 << 20
	maxDiscardBytes     = 64 << 10
)

type failureKind int

const (
	failureNone failureKind = iota
	failureNetwork
	failureTimeout
	failureCanceled
	failureFatal
)

type attemptResult struct {
	status  int
	header  http.Header
	body    []byte
	failure failureKind
	err     error
}

var errBodyTooLarge = errors.New("the response body exceeded the size limit")

func readBounded(body io.Reader, limit int64) ([]byte, error) {
	data, err := io.ReadAll(io.LimitReader(body, limit+1))
	if err != nil {
		return nil, err
	}
	if int64(len(data)) > limit {
		return nil, errBodyTooLarge
	}
	return data, nil
}

func classifyFailure(ctx, attemptCtx context.Context, err error) attemptResult {
	if ctx.Err() != nil {
		return attemptResult{failure: failureCanceled, err: ctx.Err()}
	}
	if attemptCtx.Err() != nil {
		return attemptResult{failure: failureTimeout, err: attemptCtx.Err()}
	}
	var urlError *url.Error
	if errors.As(err, &urlError) {
		err = urlError.Err
	}
	return attemptResult{failure: failureNetwork, err: err}
}

func isSuccessStatus(status int) bool {
	return status >= http.StatusOK && status < http.StatusMultipleChoices
}

func (c *Client) attempt(ctx context.Context, p *preparedRequest, canRetryAgain bool) attemptResult {
	attemptCtx, cancel := context.WithTimeout(ctx, p.timeout)
	defer cancel()

	var body io.Reader = http.NoBody
	if p.hasBody {
		body = bytes.NewReader(p.body)
	}
	request, err := http.NewRequestWithContext(attemptCtx, p.method, p.url, body)
	if err != nil {
		return attemptResult{failure: failureFatal, err: configurationError("the request could not be built")}
	}
	request.Header = p.header.Clone()

	response, err := c.httpClient.Do(request)
	if err != nil {
		return classifyFailure(ctx, attemptCtx, err)
	}
	defer response.Body.Close()

	result := attemptResult{status: response.StatusCode, header: response.Header}
	if isSuccessStatus(response.StatusCode) {
		data, err := readBounded(response.Body, maxSuccessBodyBytes)
		if errors.Is(err, errBodyTooLarge) {
			return attemptResult{failure: failureFatal, err: &ResponseError{
				Status:    response.StatusCode,
				RequestID: p.requestID,
				Reason:    "the response body exceeded the size limit",
			}}
		}
		if err != nil {
			return classifyFailure(ctx, attemptCtx, err)
		}
		result.body = data
		return result
	}

	if canRetryAgain && retryableStatuses[response.StatusCode] {
		_, _ = io.Copy(io.Discard, io.LimitReader(response.Body, maxDiscardBytes))
		return result
	}
	data, err := io.ReadAll(io.LimitReader(response.Body, maxErrorBodyBytes))
	if err != nil {
		return classifyFailure(ctx, attemptCtx, err)
	}
	result.body = data
	return result
}
