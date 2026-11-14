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

    public function createSmsBrand(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms/brands/',
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function readSmsBrand(string $brandId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/sms/brands/' . PathSegment::encode($brandId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function updateSmsBrand(string $brandId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/sms/brands/' . PathSegment::encode($brandId),
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function deleteSmsBrand(string $brandId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/sms/brands/' . PathSegment::encode($brandId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function listSmsBrands(array $data, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms/brands/retrieve',
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options);
    }
}
