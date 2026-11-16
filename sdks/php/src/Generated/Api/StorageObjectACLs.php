<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;

final class StorageObjectACLs
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function grantObjectAcl(string $containerNameOrId, string $objectNameOrId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'storage/storage-object/'
                . PathSegment::encode($containerNameOrId)
                . '/'
                . PathSegment::encode($objectNameOrId)
                . '/acl/grant',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function revokeObjectAcl(string $containerNameOrId, string $objectNameOrId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'storage/storage-object/'
                . PathSegment::encode($containerNameOrId)
                . '/'
                . PathSegment::encode($objectNameOrId)
                . '/acl/revoke',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function setObjectPublic(string $containerNameOrId, string $objectNameOrId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'storage/storage-object/'
                . PathSegment::encode($containerNameOrId)
                . '/'
                . PathSegment::encode($objectNameOrId)
                . '/acl/public',
            body: $data,
        ), $options)->dataArray();
    }
}
