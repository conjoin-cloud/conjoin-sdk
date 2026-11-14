<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class StorageContainers
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'storage/storage-container/',
            query: $query,
        ), $options);
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'storage/storage-container/',
            body: $data,
        ), $options)->dataArray();
    }

    public function read(string $containerNameOrId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'storage/storage-container/' . PathSegment::encode($containerNameOrId),
        ), $options)->dataArray();
    }

    public function requestDeletion(string $containerNameOrId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'storage/storage-container/' . PathSegment::encode($containerNameOrId),
        ), $options)->dataArray();
    }

    public function archive(string $containerNameOrId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'storage/storage-container/archive/' . PathSegment::encode($containerNameOrId),
        ), $options)->dataArray();
    }

    public function restore(string $containerNameOrId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'storage/storage-container/restore/' . PathSegment::encode($containerNameOrId),
        ), $options)->dataArray();
    }

    public function updateLifecyclePolicy(string $containerNameOrId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'storage/storage-container/lifecycle-policy/' . PathSegment::encode($containerNameOrId),
            body: $data,
        ), $options)->dataArray();
    }

    public function updateSettings(string $containerNameOrId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'storage/storage-container/settings/' . PathSegment::encode($containerNameOrId),
            body: $data,
        ), $options)->dataArray();
    }

    public function cancelDeletion(string $containerNameOrId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'storage/storage-container/cancel-deletion/' . PathSegment::encode($containerNameOrId),
        ), $options)->dataArray();
    }

    public function changeClass(string $containerNameOrId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'storage/storage-container/storage-class/' . PathSegment::encode($containerNameOrId),
            body: $data,
        ), $options)->dataArray();
    }

    public function updateTransitionPolicy(string $containerNameOrId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'storage/storage-container/transition-policy/' . PathSegment::encode($containerNameOrId),
            body: $data,
        ), $options)->dataArray();
    }
}
