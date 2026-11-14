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

final class BillingPrices
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/prices/',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options);
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/prices/',
            body: $data,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function listCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/prices/count',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function read(string $priceId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/prices/' . PathSegment::encode($priceId),
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function update(string $priceId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'billing/prices/' . PathSegment::encode($priceId),
            body: $data,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function delete(string $priceId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'billing/prices/' . PathSegment::encode($priceId),
            scopes: [Scope::BillingEntityId],
        ), $options)->bodyArray();
    }

    public function archive(string $priceId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/prices/' . PathSegment::encode($priceId) . '/archive',
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function restore(string $priceId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/prices/' . PathSegment::encode($priceId) . '/restore',
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }
}
