<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class RelayEvents
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readEventChannels(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/event-channels/',
            query: $query,
        ), $options);
    }

    public function createEventChannel(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/event-channels/',
            body: $data,
        ), $options)->dataArray();
    }

    public function readEventSubscriptions(string $eventChannelId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/event-channels/' . PathSegment::encode($eventChannelId) . '/subscriptions',
            query: $query,
        ), $options);
    }

    public function createEventSubscription(string $eventChannelId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/event-channels/' . PathSegment::encode($eventChannelId) . '/subscriptions',
            body: $data,
        ), $options)->dataArray();
    }

    public function read(string $eventChannelId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/event-channels/' . PathSegment::encode($eventChannelId) . '/events',
            query: $query,
        ), $options);
    }

    public function readEventChannelsCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/event-channels/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function updateEventChannel(string $eventChannelId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'relay/event-channels/' . PathSegment::encode($eventChannelId),
            body: $data,
        ), $options)->dataArray();
    }

    public function deleteEventChannel(string $eventChannelId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'relay/event-channels/' . PathSegment::encode($eventChannelId),
        ), $options)->dataArray();
    }

    public function readEventSubscriptionsCount(string $eventChannelId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/event-channels/' . PathSegment::encode($eventChannelId) . '/subscriptions/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function updateEventSubscription(string $eventChannelId, string $subscriptionId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'relay/event-channels/'
                . PathSegment::encode($eventChannelId)
                . '/subscriptions/'
                . PathSegment::encode($subscriptionId),
            body: $data,
        ), $options)->dataArray();
    }

    public function deleteEventSubscription(string $eventChannelId, string $subscriptionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'relay/event-channels/'
                . PathSegment::encode($eventChannelId)
                . '/subscriptions/'
                . PathSegment::encode($subscriptionId),
        ), $options)->bodyArray();
    }

    public function pauseEventSubscription(string $eventChannelId, string $subscriptionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/event-channels/'
                . PathSegment::encode($eventChannelId)
                . '/subscriptions/'
                . PathSegment::encode($subscriptionId)
                . '/pause',
        ), $options)->dataArray();
    }

    public function resumeEventSubscription(string $eventChannelId, string $subscriptionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/event-channels/'
                . PathSegment::encode($eventChannelId)
                . '/subscriptions/'
                . PathSegment::encode($subscriptionId)
                . '/resume',
        ), $options)->dataArray();
    }

    public function publishEvent(string $eventChannelId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/event-channels/' . PathSegment::encode($eventChannelId) . '/publish',
            body: $data,
        ), $options)->dataArray();
    }

    public function readCount(string $eventChannelId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/event-channels/' . PathSegment::encode($eventChannelId) . '/events/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function replay(string $eventChannelId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/event-channels/' . PathSegment::encode($eventChannelId) . '/replay',
            body: $data,
        ), $options)->bodyArray();
    }
}
