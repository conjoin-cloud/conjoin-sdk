<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Frontend;

use ConjoinCloud\AuthMode;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Credential;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class AuthSelves
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listOrganizations(#[\SensitiveParameter] Credential $sessionToken, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/self/organizations',
            query: $query,
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options);
    }

    public function listSessions(#[\SensitiveParameter] Credential $sessionToken, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/self/sessions',
            query: $query,
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options);
    }

    public function readProfile(#[\SensitiveParameter] Credential $sessionToken, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/self/',
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
    }

    public function updateProfile(#[\SensitiveParameter] Credential $sessionToken, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/self/',
            body: $data,
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
    }

    public function listSessionsCount(#[\SensitiveParameter] Credential $sessionToken, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/self/sessions/count',
            query: $query,
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
    }

    public function revokeSession(string $sessionId, #[\SensitiveParameter] Credential $sessionToken, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'auth/self/sessions/' . PathSegment::encode($sessionId),
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
    }

    public function listOrganizationsCount(#[\SensitiveParameter] Credential $sessionToken, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/self/organizations/count',
            query: $query,
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
    }

    public function readActiveOrganization(#[\SensitiveParameter] Credential $sessionToken, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/self/active-organization',
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
    }

    public function updateActiveOrganization(#[\SensitiveParameter] Credential $sessionToken, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/self/active-organization',
            body: $data,
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
    }
}
