<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class AiBYOKs
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listByokConfigs(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/byok/',
            query: $query,
        ), $options);
    }

    public function createByokConfig(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/byok/',
            body: $data,
        ), $options)->dataArray();
    }

    public function readByokConfig(string $byokConfigId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/byok/' . PathSegment::encode($byokConfigId),
        ), $options)->dataArray();
    }

    public function updateByokConfig(string $byokConfigId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'ai/byok/' . PathSegment::encode($byokConfigId),
            body: $data,
        ), $options)->dataArray();
    }

    public function deleteByokConfig(string $byokConfigId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'ai/byok/' . PathSegment::encode($byokConfigId),
        ), $options)->dataArray();
    }

    public function testByokConnection(string $byokConfigId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/byok/' . PathSegment::encode($byokConfigId) . '/test',
        ), $options)->dataArray();
    }
}
