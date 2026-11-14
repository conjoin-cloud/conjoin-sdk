<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Scope;

final class AuthSSOPortals
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readSsoPortalSettings(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/portal/settings',
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function updateSsoPortalSettings(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/portal/settings',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function mintSsoPortalTicket(string $organizationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/' . PathSegment::encode($organizationId) . '/portal-tickets/',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function revokeSsoPortalTicket(string $organizationId, string $portalTicketId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/organizations/'
                . PathSegment::encode($organizationId)
                . '/portal-tickets/'
                . PathSegment::encode($portalTicketId)
                . '/revoke',
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }
}
