<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class BillingEntities
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/entities/',
            query: $query,
        ), $options);
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/entities/',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/entities/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function onboard(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/entities/onboard',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->bodyArray();
    }

    public function read(string $entityId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/entities/' . PathSegment::encode($entityId),
            query: $query,
        ), $options)->dataArray();
    }

    public function update(string $entityId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'billing/entities/' . PathSegment::encode($entityId),
            body: $data,
        ), $options)->dataArray();
    }

    public function createPayoutBankAccount(string $entityId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/entities/' . PathSegment::encode($entityId) . '/payout-bank-accounts',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function createAccountLink(string $entityId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/entities/' . PathSegment::encode($entityId) . '/account-links',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->bodyArray();
    }

    public function syncOnboarding(string $entityId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/entities/' . PathSegment::encode($entityId) . '/sync',
            acceptsIdempotencyKey: true,
        ), $options)->bodyArray();
    }

    public function createPaystackCredentials(string $entityId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/entities/' . PathSegment::encode($entityId) . '/paystack-credentials',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->bodyArray();
    }
}
