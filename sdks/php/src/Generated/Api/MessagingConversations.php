<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\CursorLocation;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;
use ConjoinCloud\Scope;

final class MessagingConversations
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/conversations/',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function clone(string $conversationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/clone',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function sendMessage(string $conversationId, array $data, ?CallOptions $options = null): mixed
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/send',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->data();
    }

    public function update(string $conversationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId),
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function delete(string $conversationId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function archive(string $conversationId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/archive',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function list(array $data, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/conversations/retrieve',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
            cursor: CursorLocation::Body,
        ), $options);
    }

    public function readMessages(string $conversationId, string $parentMessageId, array $data, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/conversations/'
                . PathSegment::encode($conversationId)
                . '/messages/'
                . PathSegment::encode($parentMessageId),
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
            cursor: CursorLocation::Body,
        ), $options);
    }

    public function readOneRecipient(string $conversationId, string $recipientId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/conversations/'
                . PathSegment::encode($conversationId)
                . '/recipients/'
                . PathSegment::encode($recipientId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function deleteRecipients(string $conversationId, string $recipientId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/conversations/'
                . PathSegment::encode($conversationId)
                . '/recipients/'
                . PathSegment::encode($recipientId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function readManyRecipients(string $conversationId, array $data, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/recipients/retrieve',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
            cursor: CursorLocation::Body,
        ), $options);
    }

    public function addOneRecipient(string $conversationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/recipients',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function addManyRecipients(string $conversationId, array $data, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/recipients/batch',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
            cursor: CursorLocation::NotAccepted,
        ), $options);
    }
}
