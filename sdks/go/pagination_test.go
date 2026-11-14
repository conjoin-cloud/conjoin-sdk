package conjoin_test

import (
	"context"
	"errors"
	"net/http"
	"reflect"
	"testing"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type customerQuery struct {
	Limit int `json:"limit,omitzero"`
}

func listCustomers(ctx context.Context, client *conjoin.Client) (*conjoin.Page[string], error) {
	return conjoin.List[string](ctx, client, conjoin.Operation{
		Method: http.MethodGet,
		Path:   "billing/customers/",
		Query:  &customerQuery{Limit: 2},
	})
}

func TestListPagesWithTheNextCursorAndKeepsTheOtherQueryParameters(t *testing.T) {
	server := startUnreliableServer(t)
	pages := map[string]struct {
		data []string
		next string
	}{
		"":           {[]string{"cus_1", "cus_2"}, "page_two"},
		"page_two":   {[]string{"cus_3", "cus_4"}, "page_three"},
		"page_three": {[]string{"cus_5"}, ""},
	}
	server.servePages(func(cursor string) ([]string, string) {
		page := pages[cursor]
		return page.data, page.next
	})

	first, err := listCustomers(context.Background(), server.client(t))
	if err != nil {
		t.Fatalf("the list failed: %v", err)
	}
	if first.Cursor.Next != "page_two" || first.Cursor.Prev != "" || first.Response.Code != http.StatusOK || !first.HasNextPage() {
		t.Fatalf("the first page was %+v", first)
	}

	var customers []string
	for customer, err := range first.All(context.Background()) {
		if err != nil {
			t.Fatalf("the iteration failed: %v", err)
		}
		customers = append(customers, customer)
	}
	if want := []string{"cus_1", "cus_2", "cus_3", "cus_4", "cus_5"}; !reflect.DeepEqual(customers, want) {
		t.Fatalf("the iteration returned %v, want %v", customers, want)
	}

	var seen [][2]string
	for _, attempt := range server.recorded() {
		seen = append(seen, [2]string{attempt.query.Get("cursor[next]"), attempt.query.Get("limit")})
	}
	if want := [][2]string{{"", "2"}, {"page_two", "2"}, {"page_three", "2"}}; !reflect.DeepEqual(seen, want) {
		t.Fatalf("the pages were requested with %v, want %v", seen, want)
	}

	last, err := first.NextPage(context.Background())
	if err != nil {
		t.Fatalf("the second page failed: %v", err)
	}
	last, err = last.NextPage(context.Background())
	if err != nil || last.HasNextPage() {
		t.Fatalf("the last page was %+v with %v", last, err)
	}
	if after, err := last.NextPage(context.Background()); after != nil || !errors.Is(err, conjoin.ErrNoNextPage) {
		t.Fatalf("a page after the last gave %v and %v", after, err)
	}
}

func TestListRefusesACursorThatTheServerReturnedBefore(t *testing.T) {
	server := startUnreliableServer(t)
	server.servePages(func(cursor string) ([]string, string) {
		if cursor == "" {
			return []string{"cus_1"}, "page_loop"
		}
		return []string{"cus_2"}, "page_loop"
	})

	first, err := listCustomers(context.Background(), server.client(t))
	if err != nil {
		t.Fatalf("the list failed: %v", err)
	}
	var iterationError error
	count := 0
	for _, err := range first.All(context.Background()) {
		if err != nil {
			iterationError = err
			break
		}
		count++
		if count > 10 {
			break
		}
	}
	if !errors.Is(iterationError, conjoin.ErrInvalidResponse) || count != 2 || len(server.recorded()) != 2 {
		t.Fatalf("a looping cursor gave %v after %d items and %d requests", iterationError, count, len(server.recorded()))
	}
}

func TestListWithoutADataArrayIsAResponseError(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: statusAnswer, status: http.StatusOK, body: map[string]any{"data": map[string]any{"customer_id": "cus_1"}}})
	if _, err := listCustomers(context.Background(), server.client(t)); !errors.Is(err, conjoin.ErrInvalidResponse) {
		t.Fatalf("a list without an array gave %v", err)
	}
}
