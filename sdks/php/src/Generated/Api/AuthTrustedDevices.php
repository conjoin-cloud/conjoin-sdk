<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;
use ConjoinCloud\Scope;

final class AuthTrustedDevices
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(string $accountId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/accounts/' . PathSegment::encode($accountId) . '/trusted-devices/',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options);
    }

    public function listCount(string $accountId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/accounts/' . PathSegment::encode($accountId) . '/trusted-devices/count',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function revokeAll(string $accountId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/accounts/' . PathSegment::encode($accountId) . '/trusted-devices/revoke-all',
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function revoke(string $accountId, string $trustedDeviceId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/accounts/'
                . PathSegment::encode($accountId)
                . '/trusted-devices/'
                . PathSegment::encode($trustedDeviceId)
                . '/revoke',
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }
}
