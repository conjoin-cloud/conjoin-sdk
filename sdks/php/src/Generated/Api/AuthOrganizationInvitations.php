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

final class AuthOrganizationInvitations
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listInvitations(string $organizationId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/invitations/',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options);
    }

    public function createInvitation(string $organizationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/invitations/',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function listInvitationsCount(string $organizationId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/invitations/count',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function revokeInvitation(string $organizationId, string $invitationId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/invitations/'
                . PathSegment::encode($invitationId)
                . '/revoke',
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function resendInvitation(string $organizationId, string $invitationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/invitations/'
                . PathSegment::encode($invitationId)
                . '/resend',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }
}
