<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class MessagingProfiles
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/profiles/',
            query: $query,
        ), $options);
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/profiles/',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/profiles/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function enable(string $profileId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/profiles/' . PathSegment::encode($profileId) . '/enable',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function disable(string $profileId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/profiles/' . PathSegment::encode($profileId) . '/disable',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function enableChannels(string $profileId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/profiles/' . PathSegment::encode($profileId) . '/enable-channels',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function disableChannels(string $profileId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/profiles/' . PathSegment::encode($profileId) . '/disable-channels',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function close(string $profileId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/profiles/' . PathSegment::encode($profileId) . '/close',
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function read(string $profileId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/profiles/' . PathSegment::encode($profileId),
        ), $options)->dataArray();
    }

    public function update(string $profileId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/profiles/' . PathSegment::encode($profileId),
            body: $data,
        ), $options)->dataArray();
    }

    public function delete(string $profileId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/profiles/' . PathSegment::encode($profileId),
        ), $options)->dataArray();
    }
}
