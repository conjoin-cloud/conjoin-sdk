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

final class BillingEntitlementOverrides
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/entitlement-overrides/',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options);
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/entitlement-overrides/',
            body: $data,
            scopes: [Scope::BillingEntityId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/entitlement-overrides/count',
            query: $query,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function update(string $entitlementOverrideId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'billing/entitlement-overrides/' . PathSegment::encode($entitlementOverrideId),
            body: $data,
            scopes: [Scope::BillingEntityId],
        ), $options)->dataArray();
    }

    public function delete(string $entitlementOverrideId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'billing/entitlement-overrides/' . PathSegment::encode($entitlementOverrideId),
            scopes: [Scope::BillingEntityId],
        ), $options)->bodyArray();
    }
}
