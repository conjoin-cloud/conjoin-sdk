<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;

final class RelaySettings
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function get(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/settings/',
        ), $options)->dataArray();
    }

    public function update(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'relay/settings/',
            body: $data,
        ), $options)->dataArray();
    }

    public function rotateSigningSecret(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/settings/signing-secret/rotate',
        ), $options)->dataArray();
    }

    public function revealSigningSecret(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/settings/signing-secret',
        ), $options)->dataArray();
    }
}
