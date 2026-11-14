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

    public function createContactProperty(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/contacts/properties',
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function deleteMany(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/contacts/properties',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function fetchOneContactProperty(string $propertyId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/contacts/properties/' . PathSegment::encode($propertyId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function deleteContactProperty(string $propertyId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/contacts/properties/' . PathSegment::encode($propertyId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function list(?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/contacts/properties/retrieve',
            scopes: [Scope::MessagingProfileId],
        ), $options);
    }
}
