<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class CloudPublishableKeys
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/publishable-keys/',
            query: $query,
        ), $options);
    }

    public function create(?CallOptions $options = null): string
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'cloud/publishable-keys/',
        ), $options)->dataString();
    }

    public function listCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/publishable-keys/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function rotate(string $publishableKeyId, ?CallOptions $options = null): string
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'cloud/publishable-keys/' . PathSegment::encode($publishableKeyId) . '/rotate',
        ), $options)->dataString();
    }

    public function update(string $publishableKeyId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'cloud/publishable-keys/' . PathSegment::encode($publishableKeyId),
            body: $data,
        ), $options)->dataArray();
    }

    public function revoke(string $publishableKeyId, ?CallOptions $options = null): bool
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'cloud/publishable-keys/' . PathSegment::encode($publishableKeyId),
        ), $options)->dataBool();
    }
}
