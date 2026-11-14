<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;

final class CloudSpendControls
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function read(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/spend-control/',
        ), $options)->dataArray();
    }

    public function update(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'cloud/spend-control/',
            body: $data,
        ), $options)->dataArray();
    }

    public function readUsage(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/spend-control/usage',
        ), $options)->dataArray();
    }
}
