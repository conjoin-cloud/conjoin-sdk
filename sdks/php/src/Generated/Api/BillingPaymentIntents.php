<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;
use ConjoinCloud\Scope;

final class BillingPaymentIntents
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/payment-intents/',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options);
    }

    public function create(array $data, ?CallOptions $options = null): string
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/payment-intents/',
            body: $data,
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataString();
    }

    public function listCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/payment-intents/count',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function verify(string $paymentIntentId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/payment-intents/' . PathSegment::encode($paymentIntentId) . '/verify',
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }
}
