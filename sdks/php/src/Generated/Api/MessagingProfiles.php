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

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/profiles/',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function enable(string $profileId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/profiles/' . PathSegment::encode($profileId) . '/enable',
        ), $options)->dataArray();
    }

    public function disable(string $profileId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/profiles/' . PathSegment::encode($profileId) . '/disable',
        ), $options)->dataArray();
    }

    public function close(string $profileId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/profiles/' . PathSegment::encode($profileId) . '/close',
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

    public function updateEmailConfig(string $profileId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/profiles/' . PathSegment::encode($profileId) . '/emails-config',
            body: $data,
        ), $options)->dataArray();
    }

    public function updateMultisendConfig(string $profileId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/profiles/' . PathSegment::encode($profileId) . '/multisend-config',
            body: $data,
        ), $options)->dataArray();
    }

    public function updateVerificationsConfig(string $profileId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/profiles/' . PathSegment::encode($profileId) . '/verifications-config',
            body: $data,
        ), $options)->dataArray();
    }

    public function list(array $data, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/profiles/retrieve',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options);
    }
}
