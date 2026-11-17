<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class CloudWebhooks
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/webhooks/',
            query: $query,
        ), $options);
    }

    public function register(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'cloud/webhooks/',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/webhooks/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function read(string $webhookId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/webhooks/' . PathSegment::encode($webhookId),
        ), $options)->dataArray();
    }

    public function update(string $webhookId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'cloud/webhooks/' . PathSegment::encode($webhookId),
            body: $data,
        ), $options)->dataArray();
    }

    public function delete(string $webhookId, ?CallOptions $options = null): bool
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'cloud/webhooks/' . PathSegment::encode($webhookId),
        ), $options)->dataBool();
    }

    public function readEvents(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/webhook-events/',
            query: $query,
        ), $options);
    }

    public function readEventsCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/webhook-events/count',
            query: $query,
        ), $options)->dataArray();
    }
}
