<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class RelayQueues
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readQueueDefinitions(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/queues/',
            query: $query,
        ), $options);
    }

    public function createQueueDefinition(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/queues/',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readQueueTasks(string $queueId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/queues/' . PathSegment::encode($queueId) . '/tasks',
            query: $query,
        ), $options);
    }

    public function enqueueTask(string $queueId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/queues/' . PathSegment::encode($queueId) . '/tasks',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readDeadLetterTasks(string $queueId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/queues/' . PathSegment::encode($queueId) . '/dead-letters',
            query: $query,
        ), $options);
    }

    public function readQueueDefinitionsCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/queues/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function updateQueueDefinition(string $queueId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'relay/queues/' . PathSegment::encode($queueId),
            body: $data,
        ), $options)->dataArray();
    }

    public function deleteQueueDefinition(string $queueId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'relay/queues/' . PathSegment::encode($queueId),
        ), $options)->dataArray();
    }

    public function pauseQueue(string $queueId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/queues/' . PathSegment::encode($queueId) . '/pause',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function resumeQueue(string $queueId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/queues/' . PathSegment::encode($queueId) . '/resume',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function batchEnqueueTasks(string $queueId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/queues/' . PathSegment::encode($queueId) . '/enqueue-batch',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readQueueTasksCount(string $queueId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/queues/' . PathSegment::encode($queueId) . '/tasks/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function readDeadLetterTasksCount(string $queueId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/queues/' . PathSegment::encode($queueId) . '/dead-letters/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function replayDeadLetterTask(string $queueId, string $deadLetterId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/queues/'
                . PathSegment::encode($queueId)
                . '/dead-letters/'
                . PathSegment::encode($deadLetterId)
                . '/replay',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function purgeQueueTasks(string $queueId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/queues/' . PathSegment::encode($queueId) . '/purge',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }
}
