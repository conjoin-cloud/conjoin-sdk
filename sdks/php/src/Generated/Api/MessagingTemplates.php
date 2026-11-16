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

final class MessagingTemplates
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function createMessage(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/templates/',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listMessage(array $data, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/templates/retrieve',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options);
    }

    public function readMessage(string $templateId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/templates/' . PathSegment::encode($templateId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function updateMessage(string $templateId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/templates/' . PathSegment::encode($templateId),
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function deleteMessage(string $templateId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/templates/' . PathSegment::encode($templateId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function deleteMessages(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/templates/wipe',
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->bodyArray();
    }
}
