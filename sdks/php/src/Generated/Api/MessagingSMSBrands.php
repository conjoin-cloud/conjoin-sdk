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

final class MessagingSMSBrands
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listSmsBrands(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/sms-brands/',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options);
    }

    public function createSmsBrand(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms-brands/',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listSmsBrandsCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/sms-brands/count',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function readSmsBrand(string $smsBrandId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/sms-brands/' . PathSegment::encode($smsBrandId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function updateSmsBrand(string $smsBrandId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/sms-brands/' . PathSegment::encode($smsBrandId),
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function deleteSmsBrand(string $smsBrandId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/sms-brands/' . PathSegment::encode($smsBrandId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }
}
