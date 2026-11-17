package conjoin

import (
	"context"
	"math"
	"math/rand/v2"
	"net/http"
	"regexp"
	"strconv"
	"strings"
	"time"
)

var (
	retryableStatuses = map[int]bool{
		http.StatusTooManyRequests:     true,
		http.StatusInternalServerError: true,
		http.StatusBadGateway:          true,
		http.StatusServiceUnavailable:  true,
		http.StatusGatewayTimeout:      true,
	}
	retryAfterSecondsPattern = regexp.MustCompile(`^\d+(\.\d+)?$`)
)

const maxBackoffShift = 62

func parseRetryAfter(value string, now time.Time) (time.Duration, bool) {
	trimmed := strings.TrimSpace(value)
	if trimmed == "" {
		return 0, false
	}
	if retryAfterSecondsPattern.MatchString(trimmed) {
		seconds, err := strconv.ParseFloat(trimmed, 64)
		if err != nil {
			return 0, false
		}
		if seconds >= float64(math.MaxInt64)/float64(time.Second) {
			return time.Duration(math.MaxInt64), true
		}
		return time.Duration(seconds * float64(time.Second)), true
	}
	retryAt, err := http.ParseTime(trimmed)
	if err != nil {
		return 0, false
	}
	return max(retryAt.Sub(now), 0), true
}

func backoffCeiling(attempt int, base, limit time.Duration) time.Duration {
	if base <= 0 || limit <= 0 {
		return 0
	}
	if attempt >= maxBackoffShift || base > limit>>attempt {
		return limit
	}
	return min(base<<attempt, limit)
}

func (c *Client) retryDelay(attempt int, retryAfter time.Duration, hasRetryAfter bool) time.Duration {
	if hasRetryAfter {
		return min(retryAfter, c.maxRetryDelay)
	}
	ceiling := backoffCeiling(attempt, c.retryBackoff, c.maxRetryDelay)
	if ceiling <= 0 {
		return 0
	}
	return rand.N(ceiling)
}

func waitForRetry(ctx context.Context, delay time.Duration) error {
	if delay <= 0 {
		return ctx.Err()
	}
	timer := time.NewTimer(delay)
	defer timer.Stop()
	select {
	case <-ctx.Done():
		return ctx.Err()
	case <-timer.C:
		return nil
	}
}
