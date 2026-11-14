<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Scope;

final class MessagingSMSSenders
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function createSmsSender(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms/senders/',
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function enableSmsSender(string $senderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/sms/senders/' . PathSegment::encode($senderId) . '/enable',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function disableSmsSender(string $senderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/sms/senders/' . PathSegment::encode($senderId) . '/disable',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function listSmsSender(string $senderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/sms/senders/' . PathSegment::encode($senderId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function updateOneSmsSender(string $senderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/sms/senders/' . PathSegment::encode($senderId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function deleteSmsSender(string $senderId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/sms/senders/' . PathSegment::encode($senderId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function transferSmsSender(string $senderId, string $projectId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/sms/senders/transfers/'
                . PathSegment::encode($senderId)
                . '/'
                . PathSegment::encode($projectId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }
}
