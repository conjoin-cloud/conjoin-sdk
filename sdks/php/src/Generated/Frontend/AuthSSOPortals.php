<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Frontend;

use ConjoinCloud\AuthMode;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Credential;
use ConjoinCloud\DeclaredHeader;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;

final class AuthSSOPortals
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readSsoPortalContext(#[\SensitiveParameter] Credential $portalTicket, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/portal/',
            auth: AuthMode::None,
            declaredHeaders: [
                new DeclaredHeader('x-portal-ticket', 'portalTicket', $portalTicket, required: true),
            ],
        ), $options)->dataArray();
    }

    public function readSsoPortalCatalog(#[\SensitiveParameter] Credential $portalTicket, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/portal/providers',
            auth: AuthMode::None,
            declaredHeaders: [
                new DeclaredHeader('x-portal-ticket', 'portalTicket', $portalTicket, required: true),
            ],
        ), $options)->dataArray();
    }

    public function startSsoPortalTest(#[\SensitiveParameter] Credential $portalTicket, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/portal/test/start',
            body: $data,
            auth: AuthMode::None,
            declaredHeaders: [
                new DeclaredHeader('x-portal-ticket', 'portalTicket', $portalTicket, required: true),
            ],
        ), $options)->dataArray();
    }
}
