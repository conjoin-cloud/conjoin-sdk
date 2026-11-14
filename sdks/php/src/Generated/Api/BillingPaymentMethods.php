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

final class BillingPaymentMethods
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/payment-methods/',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options);
    }

    public function create(array $data, ?CallOptions $options = null): string
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/payment-methods/',
            body: $data,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataString();
    }

    public function listCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/payment-methods/count',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function delete(string $paymentMethodId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'billing/payment-methods/' . PathSegment::encode($paymentMethodId),
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }
}
