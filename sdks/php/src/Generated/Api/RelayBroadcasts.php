<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class RelayBroadcasts
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function generateConnectionToken(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/broadcast-connection-tokens/',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readChannels(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/broadcast-channels/',
            query: $query,
        ), $options);
    }

    public function createChannel(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/broadcast-channels/',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readChannelsCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/broadcast-channels/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function updateChannel(string $broadcastChannelId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'relay/broadcast-channels/' . PathSegment::encode($broadcastChannelId),
            body: $data,
        ), $options)->dataArray();
    }

    public function deleteChannel(string $broadcastChannelId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'relay/broadcast-channels/' . PathSegment::encode($broadcastChannelId),
        ), $options)->dataArray();
    }

    public function generateAuthToken(string $broadcastChannelId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/broadcast-channels/' . PathSegment::encode($broadcastChannelId) . '/auth-tokens',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function publishTo(string $broadcastChannelId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/broadcast-channels/' . PathSegment::encode($broadcastChannelId) . '/publish',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readPresence(string $broadcastChannelId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/broadcast-channels/' . PathSegment::encode($broadcastChannelId) . '/presence-members',
        ), $options)->dataArray();
    }
}
