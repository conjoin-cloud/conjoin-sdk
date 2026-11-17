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

final class MessagingConversations
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/conversations/',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options);
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

    public function listMessages(string $conversationId, array $query, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/messages',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options);
    }

    public function listRecipients(string $conversationId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/recipients',
            query: $query,
            scopes: [Scope::MessagingProfileId],
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

    public function listCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/conversations/count',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function listMessagesCount(string $conversationId, array $query, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/messages/count',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function listRecipientsCount(string $conversationId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/recipients/count',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function duplicate(string $conversationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/duplicate',
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
            method: HttpMethod::Post,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/archive',
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
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

    public function addManyRecipients(string $conversationId, array $data, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/conversations/' . PathSegment::encode($conversationId) . '/add-recipients',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options);
    }
}
