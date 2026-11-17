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

final class AuthOrganizations
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options);
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/',
            body: $data,
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/count',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function read(string $organizationId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId),
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function update(string $organizationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/organizations/' . PathSegment::encode($organizationId),
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function delete(string $organizationId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'auth/organizations/' . PathSegment::encode($organizationId),
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function updateSettings(string $organizationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/settings',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }
}
