<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class CloudZones
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/zones/',
            query: $query,
        ), $options);
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'cloud/zones/',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/zones/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function read(string $zoneId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/zones/' . PathSegment::encode($zoneId),
        ), $options)->dataArray();
    }

    public function delete(string $zoneId, ?CallOptions $options = null): bool
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'cloud/zones/' . PathSegment::encode($zoneId),
        ), $options)->dataBool();
    }

    public function verifyDns(string $zoneId, ?CallOptions $options = null): mixed
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'cloud/zones/' . PathSegment::encode($zoneId) . '/verify',
            acceptsIdempotencyKey: true,
        ), $options)->data();
    }
}
