<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\BodyType;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;
use ConjoinCloud\Scope;

final class AuthConnectionEnterprises
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listEnterpriseConnections(string $organizationId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/connections/',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options);
    }

    public function createEnterpriseConnection(string $organizationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/connections/',
            body: $data,
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listEnterpriseConnectionsCount(string $organizationId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/connections/count',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function readEnterpriseConnection(string $organizationId, string $connectionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/connections/'
                . PathSegment::encode($connectionId),
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function updateEnterpriseConnection(string $organizationId, string $connectionId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/connections/'
                . PathSegment::encode($connectionId),
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function deleteEnterpriseConnection(string $organizationId, string $connectionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/connections/'
                . PathSegment::encode($connectionId),
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function enableEnterpriseConnection(string $organizationId, string $connectionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/connections/'
                . PathSegment::encode($connectionId)
                . '/enable',
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function disableEnterpriseConnection(string $organizationId, string $connectionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/connections/'
                . PathSegment::encode($connectionId)
                . '/disable',
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function rotateEnterpriseConnectionSigningKey(string $organizationId, string $connectionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/connections/'
                . PathSegment::encode($connectionId)
                . '/signing-keys/rotate',
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function activateEnterpriseConnectionSigningKey(string $organizationId, string $connectionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/connections/'
                . PathSegment::encode($connectionId)
                . '/signing-keys/activate',
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function cancelEnterpriseConnectionSigningKey(string $organizationId, string $connectionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/connections/'
                . PathSegment::encode($connectionId)
                . '/signing-keys/cancel',
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function revokeEnterpriseConnectionSigningKey(string $organizationId, string $connectionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/connections/'
                . PathSegment::encode($connectionId)
                . '/signing-keys/revoke',
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readEnterpriseProviderSettings(string $organizationId, string $connectionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/connections/'
                . PathSegment::encode($connectionId)
                . '/provider-settings',
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function importEnterpriseSamlMetadata(string $organizationId, string $connectionId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/connections/'
                . PathSegment::encode($connectionId)
                . '/import-metadata',
            body: $data,
            bodyType: BodyType::Multipart,
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function syncEnterpriseSamlMetadata(string $organizationId, string $connectionId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/connections/'
                . PathSegment::encode($connectionId)
                . '/sync-metadata',
            body: $data,
            scopes: [Scope::AuthAppId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }
}
