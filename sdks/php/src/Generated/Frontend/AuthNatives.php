<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Frontend;

use ConjoinCloud\AuthMode;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;

final class AuthNatives
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function startSignup(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/native/sign-ups/start',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function completeSignup(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/native/sign-ups/complete',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function confirmLinkSignup(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/native/sign-ups/confirm-link',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function startSignin(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/native/sign-ins/start',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function completeSignin(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/native/sign-ins/complete',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function processTokenMint(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/native/tokens',
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function refreshSession(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/native/tokens/refresh',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function processLogout(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/native/logout',
            auth: AuthMode::None,
        ), $options)->dataArray();
    }
}
