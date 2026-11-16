<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Scope;

final class BillingFeatureAccesses
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function checkEntitlement(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/entitlements/check',
            body: $data,
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function trackFeatureUsage(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/entitlements/track',
            body: $data,
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }
}
