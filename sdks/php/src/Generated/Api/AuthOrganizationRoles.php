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

final class AuthOrganizationRoles
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listOrgRoles(string $organizationId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/roles/',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options);
    }

    public function createOrgRole(string $organizationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/roles/',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function listOrgRolesCount(string $organizationId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/roles/count',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function readOrgRole(string $organizationId, string $roleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/roles/'
                . PathSegment::encode($roleId),
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function updateOrgRole(string $organizationId, string $roleId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/roles/'
                . PathSegment::encode($roleId),
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function deleteOrgRole(string $organizationId, string $roleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/roles/'
                . PathSegment::encode($roleId),
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function archiveOrgRole(string $organizationId, string $roleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/roles/'
                . PathSegment::encode($roleId)
                . '/archive',
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function restoreOrgRole(string $organizationId, string $roleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/roles/'
                . PathSegment::encode($roleId)
                . '/restore',
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }
}
