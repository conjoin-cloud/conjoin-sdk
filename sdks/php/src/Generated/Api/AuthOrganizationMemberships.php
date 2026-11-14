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

final class AuthOrganizationMemberships
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listMemberships(string $organizationId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/memberships/',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options);
    }

    public function createMembership(string $organizationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/memberships/',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function listMembershipsCount(string $organizationId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/memberships/count',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function updateMembership(string $organizationId, string $membershipId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/memberships/'
                . PathSegment::encode($membershipId),
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function deleteMembership(string $organizationId, string $membershipId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/memberships/'
                . PathSegment::encode($membershipId),
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function grantOrgAccountRole(string $organizationId, string $membershipId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/memberships/'
                . PathSegment::encode($membershipId)
                . '/grant-role',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function revokeOrgAccountRole(string $organizationId, string $membershipId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/memberships/'
                . PathSegment::encode($membershipId)
                . '/revoke-role',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }
}
