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

final class MessagingEmailSenders
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function verify(string $senderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/email/senders/' . PathSegment::encode($senderId) . '/verify',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function listMany(array $data, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/email/senders/retrieve',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options);
    }

    public function listOne(string $senderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/email/senders/' . PathSegment::encode($senderId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function delete(string $senderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/email/senders/' . PathSegment::encode($senderId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/email/senders/',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function enable(string $senderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/email/senders/' . PathSegment::encode($senderId) . '/enable',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function disable(string $senderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/email/senders/' . PathSegment::encode($senderId) . '/disable',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function transfer(string $senderId, string $projectId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/email/senders/transfers/'
                . PathSegment::encode($senderId)
                . '/'
                . PathSegment::encode($projectId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }
}
