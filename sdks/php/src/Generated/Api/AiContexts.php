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
            path: 'ai/context-indexes/',
            query: $query,
        ), $options);
    }

    public function createIndex(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/context-indexes/',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listIndexesCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/context-indexes/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function readIndex(string $contextIndexId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/context-indexes/' . PathSegment::encode($contextIndexId),
        ), $options)->dataArray();
    }

    public function deleteIndex(string $contextIndexId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'ai/context-indexes/' . PathSegment::encode($contextIndexId),
        ), $options)->dataArray();
    }

    public function syncIndex(string $contextIndexId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/context-indexes/' . PathSegment::encode($contextIndexId) . '/sync',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listQueries(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/context-queries/',
            query: $query,
        ), $options);
    }

    public function createQuery(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/context-queries/',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listQueriesCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/context-queries/count',
            query: $query,
        ), $options)->dataArray();
    }
}
