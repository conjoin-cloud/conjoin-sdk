<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Scope;

final class AuthSLOs
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function oidcLogout(string $accountId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/accounts/' . PathSegment::encode($accountId) . '/logout-oidc',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function samlSpLogout(string $accountId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/accounts/' . PathSegment::encode($accountId) . '/logout-saml',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function samlIdpLogout(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/saml-logout-requests',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }
}
