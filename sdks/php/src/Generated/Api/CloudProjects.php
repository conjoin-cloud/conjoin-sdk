<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class CloudProjects
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(string $organizationId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/organizations/' . PathSegment::encode($organizationId) . '/projects/',
            query: $query,
        ), $options);
    }

    public function create(string $organizationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'cloud/organizations/' . PathSegment::encode($organizationId) . '/projects/',
            body: $data,
        ), $options)->dataArray();
    }

    public function readCount(string $organizationId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/organizations/' . PathSegment::encode($organizationId) . '/projects/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function read(string $projectId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/projects/' . PathSegment::encode($projectId),
        ), $options)->dataArray();
    }

    public function update(string $projectId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'cloud/projects/' . PathSegment::encode($projectId),
            body: $data,
        ), $options)->dataArray();
    }
}
