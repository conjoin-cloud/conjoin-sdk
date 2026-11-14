<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Scope;

final class AuthDeprovisionings
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function deprovisionAccount(string $accountId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/accounts/' . PathSegment::encode($accountId) . '/deprovision',
            body: $data,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }
}
