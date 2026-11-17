<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Frontend;

use ConjoinCloud\AuthMode;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;

final class AuthFlows
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function startSignup(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/sign-ups/start',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function completeSignup(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/sign-ups/complete',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function confirmLinkSignup(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/sign-ups/confirm-link',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function startSignin(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/sign-ins/start',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function completeSignin(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/sign-ins/complete',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function startPasswordReset(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/password-resets/start',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function completePasswordReset(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/client/password-resets/complete',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }
}
