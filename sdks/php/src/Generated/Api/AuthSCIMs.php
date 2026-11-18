<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\AuthMode;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Credential;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;

final class AuthSCIMs
{
    private readonly ?Credential $scimToken;

    public function __construct(
        private readonly ConjoinClient $client,
        #[\SensitiveParameter] ?string $scimToken = null,
    ) {
        $this->scimToken = $scimToken === null ? null : new Credential($scimToken);
    }

    public function __debugInfo(): array
    {
        return ['client' => $this->client];
    }

    public function scimBulkOperations(string $projectId, string $appId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/scim/v2/' . PathSegment::encode($projectId) . '/' . PathSegment::encode($appId) . '/Bulk',
            body: $data,
            acceptsIdempotencyKey: true,
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options)->bodyArray();
    }

    public function scimListGroups(string $projectId, string $appId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/scim/v2/' . PathSegment::encode($projectId) . '/' . PathSegment::encode($appId) . '/Groups',
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options)->bodyArray();
    }

    public function scimCreateGroup(string $projectId, string $appId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/scim/v2/' . PathSegment::encode($projectId) . '/' . PathSegment::encode($appId) . '/Groups',
            body: $data,
            acceptsIdempotencyKey: true,
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options)->bodyArray();
    }

    public function scimGetGroup(string $projectId, string $appId, string $id, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/scim/v2/'
                . PathSegment::encode($projectId)
                . '/'
                . PathSegment::encode($appId)
                . '/Groups/'
                . PathSegment::encode($id),
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options)->bodyArray();
    }

    public function scimReplaceGroup(string $projectId, string $appId, string $id, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Put,
            path: 'auth/scim/v2/'
                . PathSegment::encode($projectId)
                . '/'
                . PathSegment::encode($appId)
                . '/Groups/'
                . PathSegment::encode($id),
            body: $data,
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options)->bodyArray();
    }

    public function scimPatchGroupMembers(string $projectId, string $appId, string $id, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/scim/v2/'
                . PathSegment::encode($projectId)
                . '/'
                . PathSegment::encode($appId)
                . '/Groups/'
                . PathSegment::encode($id),
            body: $data,
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options)->bodyArray();
    }

    public function scimDeleteGroup(string $projectId, string $appId, string $id, ?CallOptions $options = null): void
    {
        $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'auth/scim/v2/'
                . PathSegment::encode($projectId)
                . '/'
                . PathSegment::encode($appId)
                . '/Groups/'
                . PathSegment::encode($id),
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options);
    }

    public function scimGetServiceProviderConfig(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/scim/v2/ServiceProviderConfig',
            auth: AuthMode::None,
        ), $options)->bodyArray();
    }

    public function scimGetSchemas(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/scim/v2/Schemas',
            auth: AuthMode::None,
        ), $options)->bodyArray();
    }

    public function scimGetResourceTypes(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/scim/v2/ResourceTypes',
            auth: AuthMode::None,
        ), $options)->bodyArray();
    }

    public function scimListUsers(string $projectId, string $appId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/scim/v2/' . PathSegment::encode($projectId) . '/' . PathSegment::encode($appId) . '/Users',
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options)->bodyArray();
    }

    public function scimCreateUser(string $projectId, string $appId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/scim/v2/' . PathSegment::encode($projectId) . '/' . PathSegment::encode($appId) . '/Users',
            body: $data,
            acceptsIdempotencyKey: true,
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options)->bodyArray();
    }

    public function scimGetUser(string $projectId, string $appId, string $id, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/scim/v2/'
                . PathSegment::encode($projectId)
                . '/'
                . PathSegment::encode($appId)
                . '/Users/'
                . PathSegment::encode($id),
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options)->bodyArray();
    }

    public function scimReplaceUser(string $projectId, string $appId, string $id, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Put,
            path: 'auth/scim/v2/'
                . PathSegment::encode($projectId)
                . '/'
                . PathSegment::encode($appId)
                . '/Users/'
                . PathSegment::encode($id),
            body: $data,
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options)->bodyArray();
    }

    public function scimPatchUser(string $projectId, string $appId, string $id, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/scim/v2/'
                . PathSegment::encode($projectId)
                . '/'
                . PathSegment::encode($appId)
                . '/Users/'
                . PathSegment::encode($id),
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options)->bodyArray();
    }

    public function scimDeactivateUser(string $projectId, string $appId, string $id, ?CallOptions $options = null): void
    {
        $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'auth/scim/v2/'
                . PathSegment::encode($projectId)
                . '/'
                . PathSegment::encode($appId)
                . '/Users/'
                . PathSegment::encode($id),
            auth: AuthMode::Bearer,
            bearerToken: $this->scimToken,
        ), $options);
    }
}
