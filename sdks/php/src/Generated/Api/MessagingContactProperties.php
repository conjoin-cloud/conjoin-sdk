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

final class MessagingContactProperties
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/contact-properties/',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options);
    }

    public function createContactProperty(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/contact-properties/',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/contact-properties/count',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function fetchOneContactProperty(string $contactPropertyId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/contact-properties/' . PathSegment::encode($contactPropertyId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function deleteContactProperty(string $contactPropertyId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/contact-properties/' . PathSegment::encode($contactPropertyId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }
}
