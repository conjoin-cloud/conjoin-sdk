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

final class AuthOrganizationPermissions
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listOrgPermissions(string $organizationId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/permissions/',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options);
    }

    public function createOrgPermission(string $organizationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/permissions/',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function listOrgPermissionsCount(string $organizationId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/permissions/count',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function readOrgPermission(string $organizationId, string $permissionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/permissions/'
                . PathSegment::encode($permissionId),
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function updateOrgPermission(string $organizationId, string $permissionId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/permissions/'
                . PathSegment::encode($permissionId),
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function deleteOrgPermission(string $organizationId, string $permissionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/permissions/'
                . PathSegment::encode($permissionId),
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function archiveOrgPermission(string $organizationId, string $permissionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/permissions/'
                . PathSegment::encode($permissionId)
                . '/archive',
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function restoreOrgPermission(string $organizationId, string $permissionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/permissions/'
                . PathSegment::encode($permissionId)
                . '/restore',
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }
}
