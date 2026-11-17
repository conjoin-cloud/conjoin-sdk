<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class AiUsages
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listRecords(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/usage-records/',
            query: $query,
        ), $options);
    }

    public function listRecordsCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/usage-records/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function readSummary(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/usage/',
            query: $query,
        ), $options)->dataArray();
    }
}
