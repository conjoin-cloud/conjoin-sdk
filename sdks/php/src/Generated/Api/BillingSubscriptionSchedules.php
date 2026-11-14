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

final class BillingSubscriptionSchedules
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(string $subscriptionId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId) . '/schedules',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options);
    }

    public function create(string $subscriptionId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId) . '/schedules',
            body: $data,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function listCount(string $subscriptionId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/subscriptions/' . PathSegment::encode($subscriptionId) . '/schedules/count',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function get(string $subscriptionScheduleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/subscription-schedules/' . PathSegment::encode($subscriptionScheduleId),
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function cancel(string $subscriptionScheduleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/subscription-schedules/' . PathSegment::encode($subscriptionScheduleId) . '/cancel',
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function release(string $subscriptionScheduleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/subscription-schedules/' . PathSegment::encode($subscriptionScheduleId) . '/release',
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }
}
