<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\BodyType;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;
use ConjoinCloud\Scope;

final class MessagingEmails
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listMessages(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/email-messages/',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options);
    }

    public function send(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/email-messages/',
            body: $data,
            bodyType: BodyType::Multipart,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listMessagesCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/email-messages/count',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function readMessage(string $emailMessageId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/email-messages/' . PathSegment::encode($emailMessageId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function generateSummary(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/email-message-previews/',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }
}
