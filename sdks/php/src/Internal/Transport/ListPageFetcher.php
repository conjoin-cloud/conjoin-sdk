<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Transport;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ClientConfig;
use ConjoinCloud\CursorLocation;
use ConjoinCloud\Internal\Tracing\IdempotencyKey;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;
use ConjoinCloud\Pagination\PageFetcher;

final class ListPageFetcher implements PageFetcher
{
    public function __construct(
        private readonly RequestExecutor $executor,
        #[\SensitiveParameter] private readonly ClientConfig $config,
        #[\SensitiveParameter] private readonly OperationRequest $request,
        #[\SensitiveParameter] private readonly CallOptions $options,
    ) {
    }

    public function first(): ListPage
    {
        $response = $this->executor->execute($this->config, $this->request, $this->options);

        return ListPage::fromResponse($response, $this->request->cursor === CursorLocation::NotAccepted ? null : $this);
    }

    public function fetch(string $nextCursor, array $seenCursors): ListPage
    {
        $response = $this->request->cursor === CursorLocation::Body
            ? $this->executor->execute($this->config, $this->requestWithBodyCursor($nextCursor), $this->nextPageOptions())
            : $this->executor->execute($this->config, $this->requestWithQueryCursor($nextCursor), $this->options);

        return ListPage::fromResponse($response, $this, $seenCursors);
    }

    public function __debugInfo(): array
    {
        return ['request' => $this->request];
    }

    private function requestWithQueryCursor(string $nextCursor): OperationRequest
    {
        $query = $this->request->query ?? [];
        $query['cursor'] = ['next' => $nextCursor];

        return $this->request->withQuery($query);
    }

    private function requestWithBodyCursor(string $nextCursor): OperationRequest
    {
        $body = $this->request->body ?? [];
        $body['cursor'] = ['next' => $nextCursor];

        return $this->request->withBody($body);
    }

    private function nextPageOptions(): CallOptions
    {
        return new CallOptions(
            idempotencyKey: $this->request->acceptsIdempotencyKey ? IdempotencyKey::generate() : $this->options->idempotencyKey,
            requestId: $this->options->requestId,
            timeoutSeconds: $this->options->timeoutSeconds,
            maxRetries: $this->options->maxRetries,
            cancellation: $this->options->cancellation,
            headers: $this->options->headers,
        );
    }
}
