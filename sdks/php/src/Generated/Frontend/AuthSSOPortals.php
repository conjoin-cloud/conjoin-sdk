<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Frontend;

use ConjoinCloud\AuthMode;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;

final class AuthSSOPortals
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readSsoPortalContext(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/portal/',
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function readSsoPortalCatalog(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/portal/providers',
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function startSsoPortalTest(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/portal/test/start',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }
}
