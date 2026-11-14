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

final class AuthOrganizationDomains
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(string $organizationId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/domains/',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options);
    }

    public function create(string $organizationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/domains/',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function listCount(string $organizationId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/domains/count',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function verify(string $organizationId, string $domainId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/domains/'
                . PathSegment::encode($domainId)
                . '/verify',
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function delete(string $organizationId, string $domainId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/domains/'
                . PathSegment::encode($domainId),
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }
}
