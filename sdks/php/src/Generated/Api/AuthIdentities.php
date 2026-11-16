<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Scope;

final class AuthIdentities
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function discoverAccount(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/accounts/discover',
            body: $data,
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function link(string $accountId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/accounts/' . PathSegment::encode($accountId) . '/identities/link',
            body: $data,
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function unlink(string $accountId, array $data, ?CallOptions $options = null): mixed
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/accounts/' . PathSegment::encode($accountId) . '/identities/unlink',
            body: $data,
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->data();
    }
}
