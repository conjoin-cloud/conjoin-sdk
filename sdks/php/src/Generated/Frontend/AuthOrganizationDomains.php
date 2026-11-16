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

final class AuthOrganizationDomains
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function verifySsoPortalDomain(#[\SensitiveParameter] Credential $portalTicket, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/portal/domains',
            body: $data,
            auth: AuthMode::None,
            declaredHeaders: [
                new DeclaredHeader('x-portal-ticket', 'portalTicket', $portalTicket, required: true),
            ],
        ), $options)->dataArray();
    }
}
