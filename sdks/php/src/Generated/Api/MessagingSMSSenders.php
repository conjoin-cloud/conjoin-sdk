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

final class MessagingSMSSenders
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listManySmsSenders(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/sms-senders/',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options);
    }

    public function createSmsSender(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms-senders/',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listManySmsSendersCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/sms-senders/count',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function readSmsSender(string $smsSenderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/sms-senders/' . PathSegment::encode($smsSenderId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function updateOneSmsSender(string $smsSenderId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/sms-senders/' . PathSegment::encode($smsSenderId),
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function deleteSmsSender(string $smsSenderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/sms-senders/' . PathSegment::encode($smsSenderId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function enableSmsSender(string $smsSenderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms-senders/' . PathSegment::encode($smsSenderId) . '/enable',
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function disableSmsSender(string $smsSenderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms-senders/' . PathSegment::encode($smsSenderId) . '/disable',
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function transferSmsSender(string $smsSenderId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms-senders/' . PathSegment::encode($smsSenderId) . '/transfer',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }
}
