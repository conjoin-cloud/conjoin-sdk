<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\Exception\ResponseException;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Tests\Support\ServerTestCase;

final class PaginationTest extends ServerTestCase
{
    public function testPagesThroughEveryItemWithTheNextCursorAndKeepsTheOtherQueryParameters(): void
    {
        $this->server()->servePages([
            '' => ['data' => ['cus_1', 'cus_2'], 'next' => 'page_two'],
            'page_two' => ['data' => ['cus_3', 'cus_4'], 'next' => 'page_three'],
            'page_three' => ['data' => ['cus_5'], 'next' => null],
        ]);

        $page = $this->client()->sendList(new OperationRequest(HttpMethod::Get, 'billing/customers/', query: ['limit' => 2]));

        self::assertSame(['cus_1', 'cus_2'], $page->data);
        self::assertSame('page_two', $page->cursor->next);
        self::assertTrue($page->hasNextPage());
        self::assertSame(['cus_1', 'cus_2', 'cus_3', 'cus_4', 'cus_5'], iterator_to_array($page, false));

        $queries = [];

        for ($index = 0; $index < 3; $index++) {
            $values = $this->server()->attempt($index)->queryValues();
            $cursor = is_array($values['cursor'] ?? null) ? ($values['cursor']['next'] ?? null) : null;
            $queries[] = [$cursor, $values['limit'] ?? null];
        }

        self::assertSame([[null, '2'], ['page_two', '2'], ['page_three', '2']], $queries);
        self::assertSame(3, $this->server()->attemptCount());
    }

    public function testStopsPagingWhenTheServerRepeatsACursor(): void
    {
        $this->server()->servePages([
            '' => ['data' => ['cus_1'], 'next' => 'page_loop'],
            'page_loop' => ['data' => ['cus_2'], 'next' => 'page_loop'],
        ]);

        $page = $this->client()->sendList(new OperationRequest(HttpMethod::Get, 'billing/customers/'));
        $items = [];

        $error = self::caught(static function () use ($page, &$items): void {
            foreach ($page as $item) {
                $items[] = $item;
            }
        });

        self::assertInstanceOf(ResponseException::class, $error);
        self::assertSame(['cus_1', 'cus_2'], $items);
        self::assertSame(2, $this->server()->attemptCount());
    }
}
