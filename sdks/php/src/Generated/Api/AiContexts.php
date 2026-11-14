<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class AiContexts
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listIndexes(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/context/indexes',
            query: $query,
        ), $options);
    }

    public function createIndex(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/context/indexes',
            body: $data,
        ), $options)->dataArray();
    }

    public function readIndex(string $indexId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/context/indexes/' . PathSegment::encode($indexId),
        ), $options)->dataArray();
    }

    public function deleteIndex(string $indexId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'ai/context/indexes/' . PathSegment::encode($indexId),
        ), $options)->dataArray();
    }

    public function syncIndex(string $indexId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/context/indexes/' . PathSegment::encode($indexId) . '/sync',
        ), $options)->dataArray();
    }

    public function query(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/context/query',
            body: $data,
        ), $options)->dataArray();
    }

    public function listQueryLogs(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/context/query-logs',
            query: $query,
        ), $options);
    }
}
