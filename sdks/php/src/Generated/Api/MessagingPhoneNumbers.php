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

final class MessagingPhoneNumbers
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function purchase(string $phoneNumber, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/phone-numbers/' . PathSegment::encode($phoneNumber) . '/provision',
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function update(string $phoneNumber, string $projectId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/phone-numbers/transfer/'
                . PathSegment::encode($phoneNumber)
                . '/project/'
                . PathSegment::encode($projectId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function listAvailable(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/phone-numbers/available',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options);
    }

    public function list(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/phone-numbers/',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options);
    }

    public function release(string $phoneNumber, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/phone-numbers/' . PathSegment::encode($phoneNumber) . '/release',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }
}
