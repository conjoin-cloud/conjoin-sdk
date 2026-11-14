<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Frontend;

use ConjoinCloud\AuthMode;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;

final class AuthOrganizationDomains
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function verifySsoPortalDomain(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/portal/domains',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }
}
