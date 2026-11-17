<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class CloudAPIKeys
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readApiKeys(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/api-keys/',
            query: $query,
        ), $options);
    }

    public function createApiKey(array $data, ?CallOptions $options = null): string
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'cloud/api-keys/',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataString();
    }

    public function readApiKeysCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/api-keys/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function regenerateApiKey(string $apiKeyId, array $data, ?CallOptions $options = null): string
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'cloud/api-keys/' . PathSegment::encode($apiKeyId) . '/regenerate',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataString();
    }

    public function updateApiKey(string $apiKeyId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'cloud/api-keys/' . PathSegment::encode($apiKeyId),
            body: $data,
        ), $options)->dataArray();
    }

    public function deleteApiKey(string $apiKeyId, ?CallOptions $options = null): bool
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'cloud/api-keys/' . PathSegment::encode($apiKeyId),
        ), $options)->dataBool();
    }
}
