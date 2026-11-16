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

final class BillingCreditWallets
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/credit-wallets/',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options);
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/credit-wallets/',
            body: $data,
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/credit-wallets/count',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function update(string $creditWalletId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'billing/credit-wallets/' . PathSegment::encode($creditWalletId),
            body: $data,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function grantCredits(string $creditWalletId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/credit-wallets/' . PathSegment::encode($creditWalletId) . '/grant',
            body: $data,
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }
}
