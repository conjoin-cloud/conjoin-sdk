<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Frontend;

use ConjoinCloud\AuthMode;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;

final class CloudSDKs
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readSdkSettings(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/client/settings/',
            auth: AuthMode::None,
        ), $options)->dataArray();
    }
}
