<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class RelaySearches
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readIndexes(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/search/indexes',
            query: $query,
        ), $options);
    }

    public function createIndex(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/search/indexes',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function deleteIndex(string $indexId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'relay/search/indexes/' . PathSegment::encode($indexId),
        ), $options)->dataArray();
    }

    public function indexDocument(string $indexId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/search/indexes/' . PathSegment::encode($indexId) . '/documents',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function indexDocumentBatch(string $indexId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/search/indexes/' . PathSegment::encode($indexId) . '/documents/batch',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function removeDocument(string $indexId, string $documentId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'relay/search/indexes/'
                . PathSegment::encode($indexId)
                . '/documents/'
                . PathSegment::encode($documentId),
        ), $options)->dataArray();
    }

    public function searchQuery(string $indexId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/search/indexes/' . PathSegment::encode($indexId) . '/query',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function autoSuggest(string $indexId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/search/indexes/' . PathSegment::encode($indexId) . '/suggest',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }
}
