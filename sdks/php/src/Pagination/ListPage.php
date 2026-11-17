<?php

declare(strict_types=1);

namespace ConjoinCloud\Pagination;

use ConjoinCloud\Exception\ResponseException;
use ConjoinCloud\Response\ApiResponse;
use Generator;
use IteratorAggregate;

final class ListPage implements IteratorAggregate
{
    public readonly array $data;

    public readonly Cursor $cursor;

    public readonly array $response;

    public readonly ?string $requestId;

    public readonly int $status;

    private function __construct(
        ApiResponse $apiResponse,
        private readonly ?PageFetcher $fetcher,
        private readonly array $seenCursors,
    ) {
        $body = $apiResponse->bodyArray();
        $data = $body['data'] ?? null;

        if (!is_array($data) || !array_is_list($data)) {
            throw new ResponseException('The list response did not hold a data array', $apiResponse->status, $apiResponse->requestId);
        }

        $this->data = $data;
        $this->cursor = Cursor::fromBody($body['cursor'] ?? null);
        $this->response = is_array($body['response'] ?? null) ? $body['response'] : [];
        $this->requestId = $apiResponse->requestId;
        $this->status = $apiResponse->status;
    }

    public static function fromResponse(ApiResponse $response, ?PageFetcher $fetcher, array $seenCursors = []): self
    {
        return new self($response, $fetcher, $seenCursors);
    }

    public function hasNextPage(): bool
    {
        return $this->cursor->next !== null && $this->fetcher !== null;
    }

    public function nextPage(): ?self
    {
        $next = $this->cursor->next;

        if ($next === null || $this->fetcher === null) {
            return null;
        }

        if (isset($this->seenCursors[$next])) {
            throw new ResponseException('The list returned a cursor that it had returned before', $this->status, $this->requestId);
        }

        $seen = $this->seenCursors;
        $seen[$next] = true;

        return $this->fetcher->fetch($next, $seen);
    }

    public function getIterator(): Generator
    {
        $page = $this;

        while ($page !== null) {
            foreach ($page->data as $item) {
                yield $item;
            }

            $page = $page->nextPage();
        }
    }
}
