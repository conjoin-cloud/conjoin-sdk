<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class StorageObjects
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function createUploadSignedUrl(string $containerNameOrId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'storage/storage-object/' . PathSegment::encode($containerNameOrId) . '/signed-url/upload',
            body: $data,
        ), $options)->dataArray();
    }

    public function createDownloadSignedUrl(string $containerNameOrId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'storage/storage-object/' . PathSegment::encode($containerNameOrId) . '/signed-url/download',
            body: $data,
        ), $options)->dataArray();
    }

    public function rename(string $containerNameOrId, string $oldName, string $newName, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'storage/storage-object/rename/'
                . PathSegment::encode($containerNameOrId)
                . '/'
                . PathSegment::encode($oldName)
                . '/'
                . PathSegment::encode($newName),
        ), $options)->dataArray();
    }

    public function archive(string $containerNameOrId, string $objectNameOrId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'storage/storage-object/archive/'
                . PathSegment::encode($containerNameOrId)
                . '/'
                . PathSegment::encode($objectNameOrId),
        ), $options)->dataArray();
    }

    public function restore(string $containerNameOrId, string $objectNameOrId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'storage/storage-object/restore/'
                . PathSegment::encode($containerNameOrId)
                . '/'
                . PathSegment::encode($objectNameOrId),
        ), $options)->dataArray();
    }

    public function delete(string $containerNameOrId, string $prefix, string $name, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'storage/storage-object/'
                . PathSegment::encode($containerNameOrId)
                . '/'
                . PathSegment::encode($prefix)
                . '/'
                . PathSegment::encode($name),
        ), $options)->dataArray();
    }

    public function listVersions(string $containerNameOrId, string $objectNameOrId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'storage/storage-object/versions/'
                . PathSegment::encode($containerNameOrId)
                . '/'
                . PathSegment::encode($objectNameOrId),
            query: $query,
        ), $options);
    }

    public function restoreVersion(string $containerNameOrId, string $objectNameOrId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'storage/storage-object/versions/restore/'
                . PathSegment::encode($containerNameOrId)
                . '/'
                . PathSegment::encode($objectNameOrId),
            body: $data,
        ), $options)->dataArray();
    }

    public function checkDuplicate(string $containerNameOrId, array $query, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'storage/storage-object/check-duplicate/' . PathSegment::encode($containerNameOrId),
            query: $query,
        ), $options)->dataArray();
    }

    public function read(string $containerNameOrId, string $objectNameOrId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'storage/storage-object/'
                . PathSegment::encode($containerNameOrId)
                . '/'
                . PathSegment::encode($objectNameOrId),
        ), $options)->dataArray();
    }

    public function list(string $containerNameOrId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'storage/storage-object/' . PathSegment::encode($containerNameOrId),
            query: $query,
        ), $options);
    }
}
