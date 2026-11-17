package conjoin

import (
	"bytes"
	"context"
	"encoding/json"
	"iter"
	"net/url"
	"sync"
)

const (
	cursorNextQueryKey = "cursor[next]"
	cursorPrevQueryKey = "cursor[prev]"
)

type ResponseMeta struct {
	Type    string `json:"type"`
	Code    int    `json:"code"`
	Message string `json:"message"`
}

type Cursor struct {
	Prev string
	Next string
}

type Page[T any] struct {
	Response  ResponseMeta
	Data      []T
	Cursor    Cursor
	RequestID string

	client *Client
	op     Operation
	query  url.Values
	opts   []CallOption
	trail  *cursorTrail
	depth  int
	status int
}

type cursorTrail struct {
	mu      sync.Mutex
	depthOf map[string]int
}

func (t *cursorTrail) claim(cursor string, depth int) bool {
	t.mu.Lock()
	defer t.mu.Unlock()
	if previous, seen := t.depthOf[cursor]; seen && previous != depth {
		return false
	}
	t.depthOf[cursor] = depth
	return true
}

type listBody struct {
	Response ResponseMeta    `json:"response"`
	Data     json.RawMessage `json:"data"`
	Cursor   *struct {
		Prev *string `json:"prev"`
		Next *string `json:"next"`
	} `json:"cursor"`
}

func cursorToken(value *string) string {
	if value == nil {
		return ""
	}
	return *value
}

func List[T any](ctx context.Context, client *Client, op Operation, opts ...CallOption) (*Page[T], error) {
	query, err := flattenQuery(op.Query)
	if err != nil {
		return nil, err
	}
	trail := &cursorTrail{depthOf: map[string]int{}}
	return fetchPage[T](ctx, client, op, query, opts, trail, 0)
}

func fetchPage[T any](ctx context.Context, client *Client, op Operation, query url.Values, opts []CallOption, trail *cursorTrail, depth int) (*Page[T], error) {
	res, err := client.send(ctx, op, query, opts)
	if err != nil {
		return nil, err
	}
	var body listBody
	if err := json.Unmarshal(res.body, &body); err != nil {
		return nil, invalidResponse(res, "the list response did not match the documented shape")
	}
	if !bytes.HasPrefix(bytes.TrimSpace(body.Data), []byte("[")) {
		return nil, invalidResponse(res, "the list response did not hold a data array")
	}
	var data []T
	if err := json.Unmarshal(body.Data, &data); err != nil {
		return nil, invalidResponse(res, "the list items did not match the documented shape")
	}
	page := &Page[T]{
		Response:  body.Response,
		Data:      data,
		RequestID: res.requestID,
		client:    client,
		op:        op,
		query:     query,
		opts:      opts,
		trail:     trail,
		depth:     depth,
		status:    res.status,
	}
	if body.Cursor != nil {
		page.Cursor = Cursor{Prev: cursorToken(body.Cursor.Prev), Next: cursorToken(body.Cursor.Next)}
	}
	return page, nil
}

func (p *Page[T]) HasNextPage() bool {
	return p != nil && p.Cursor.Next != "" && p.client != nil
}

func (p *Page[T]) NextPage(ctx context.Context) (*Page[T], error) {
	if !p.HasNextPage() {
		return nil, ErrNoNextPage
	}
	if !p.trail.claim(p.Cursor.Next, p.depth) {
		return nil, &ResponseError{Status: p.status, RequestID: p.RequestID, Reason: "the list returned a cursor that it had returned before"}
	}
	query := url.Values{}
	for key, values := range p.query {
		if key != cursorNextQueryKey && key != cursorPrevQueryKey {
			query[key] = append([]string(nil), values...)
		}
	}
	query.Set(cursorNextQueryKey, p.Cursor.Next)
	return fetchPage[T](ctx, p.client, p.op, query, p.opts, p.trail, p.depth+1)
}

func (p *Page[T]) All(ctx context.Context) iter.Seq2[T, error] {
	return func(yield func(T, error) bool) {
		page := p
		for page != nil {
			for _, item := range page.Data {
				if !yield(item, nil) {
					return
				}
			}
			if !page.HasNextPage() {
				return
			}
			next, err := page.NextPage(ctx)
			if err != nil {
				var zero T
				yield(zero, err)
				return
			}
			page = next
		}
	}
}
