<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class RelaySchedulers
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readDefinitions(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/schedules/',
            query: $query,
        ), $options);
    }

    public function createDefinition(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/schedules/',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readExecutions(string $scheduleId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/schedules/' . PathSegment::encode($scheduleId) . '/executions',
            query: $query,
        ), $options);
    }

    public function readDeadLetterEntries(string $scheduleId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/schedules/' . PathSegment::encode($scheduleId) . '/dead-letters',
            query: $query,
        ), $options);
    }

    public function readDefinitionsCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/schedules/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function updateDefinition(string $scheduleId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'relay/schedules/' . PathSegment::encode($scheduleId),
            body: $data,
        ), $options)->dataArray();
    }

    public function pause(string $scheduleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/schedules/' . PathSegment::encode($scheduleId) . '/pause',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function resume(string $scheduleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/schedules/' . PathSegment::encode($scheduleId) . '/resume',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function cancel(string $scheduleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/schedules/' . PathSegment::encode($scheduleId) . '/cancel',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function triggerExecution(string $scheduleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/schedules/' . PathSegment::encode($scheduleId) . '/trigger',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readExecutionsCount(string $scheduleId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/schedules/' . PathSegment::encode($scheduleId) . '/executions/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function readDeadLetterEntriesCount(string $scheduleId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/schedules/' . PathSegment::encode($scheduleId) . '/dead-letters/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function replayDeadLetterEntry(string $scheduleId, string $deadLetterId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/schedules/'
                . PathSegment::encode($scheduleId)
                . '/dead-letters/'
                . PathSegment::encode($deadLetterId)
                . '/replay',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }
}
