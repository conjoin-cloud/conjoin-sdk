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

final class BillingSubscriptions
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/subscriptions/',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options);
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/subscriptions/',
            body: $data,
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listCycles(string $subscriptionId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId) . '/cycles',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options);
    }

    public function listCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/subscriptions/count',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function read(string $subscriptionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId),
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function update(string $subscriptionId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId),
            body: $data,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function createPlanChange(string $subscriptionId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId) . '/plan-changes',
            body: $data,
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function cancel(string $subscriptionId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId) . '/cancel',
            body: $data,
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function pause(string $subscriptionId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId) . '/pause',
            body: $data,
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function resume(string $subscriptionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId) . '/resume',
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function recordUsage(string $subscriptionId, array $data, ?CallOptions $options = null): bool
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId) . '/usage-records',
            body: $data,
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataBool();
    }

    public function readUsageSummary(string $subscriptionId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId) . '/usage-summaries',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function listCyclesCount(string $subscriptionId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId) . '/cycles/count',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }
}
