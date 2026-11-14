<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Transport;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ClientConfig;
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
        return ListPage::fromResponse($this->executor->execute($this->config, $this->request, $this->options), $this);
    }

    public function fetch(string $nextCursor, array $seenCursors): ListPage
    {
        $query = $this->request->query ?? [];
        $query['cursor'] = ['next' => $nextCursor];
        $response = $this->executor->execute($this->config, $this->request->withQuery($query), $this->options);

        return ListPage::fromResponse($response, $this, $seenCursors);
    }

    public function __debugInfo(): array
    {
        return ['request' => $this->request];
    }
}
