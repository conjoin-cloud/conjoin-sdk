<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Frontend;

use ConjoinCloud\AuthMode;
use ConjoinCloud\BodyType;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Credential;
use ConjoinCloud\DeclaredHeader;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;

final class AuthConnectionEnterprises
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function configureSsoPortalConnection(#[\SensitiveParameter] Credential $portalTicket, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/portal/connections',
            body: $data,
            auth: AuthMode::None,
            declaredHeaders: [
                new DeclaredHeader('x-portal-ticket', 'portalTicket', $portalTicket, required: true),
            ],
        ), $options)->dataArray();
    }

    public function updateSsoPortalConnection(
        string $connectionId,
        #[\SensitiveParameter] Credential $portalTicket,
        array $data,
        ?CallOptions $options = null,
    ): array {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/portal/connections/' . PathSegment::encode($connectionId),
            body: $data,
            auth: AuthMode::None,
            declaredHeaders: [
                new DeclaredHeader('x-portal-ticket', 'portalTicket', $portalTicket, required: true),
            ],
        ), $options)->dataArray();
    }

    public function importSsoPortalMetadata(
        string $connectionId,
        #[\SensitiveParameter] Credential $portalTicket,
        array $data,
        ?CallOptions $options = null,
    ): array {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/portal/connections/' . PathSegment::encode($connectionId) . '/import-metadata',
            body: $data,
            bodyType: BodyType::Multipart,
            auth: AuthMode::None,
            declaredHeaders: [
                new DeclaredHeader('x-portal-ticket', 'portalTicket', $portalTicket, required: true),
            ],
        ), $options)->dataArray();
    }

    public function readSsoPortalProviderConfig(string $connectionId, #[\SensitiveParameter] Credential $portalTicket, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/portal/connections/' . PathSegment::encode($connectionId) . '/service-provider-settings',
            auth: AuthMode::None,
            declaredHeaders: [
                new DeclaredHeader('x-portal-ticket', 'portalTicket', $portalTicket, required: true),
            ],
        ), $options)->dataArray();
    }
}
