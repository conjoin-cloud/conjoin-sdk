<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Frontend;

use ConjoinCloud\AuthMode;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;

final class AuthClients
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function getOidcDiscovery(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/client/.well-known/openid-configuration',
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function processHandshake(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/handshakes',
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function processLogout(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/logout',
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function getJwks(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/client/.well-known/jwks.json',
            auth: AuthMode::None,
        ), $options)->dataArray();
    }
}
