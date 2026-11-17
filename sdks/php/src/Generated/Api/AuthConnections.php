<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Scope;

final class AuthConnections
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listFirstParty(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/connection-configs/',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function upsertFirstParty(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/connection-configs/',
            body: $data,
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }
}
