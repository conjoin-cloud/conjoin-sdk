<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Scope;

final class MessagingSegments
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function createOne(array $data, ?CallOptions $options = null): mixed
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/segments/',
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->data();
    }

    public function updateOne(string $segmentId, array $data, ?CallOptions $options = null): mixed
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/segments/' . PathSegment::encode($segmentId),
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->data();
    }

    public function deleteOne(string $segmentId, ?CallOptions $options = null): mixed
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/segments/' . PathSegment::encode($segmentId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->data();
    }

    public function listMany(array $data, ?CallOptions $options = null): mixed
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/segments/retrieve',
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->data();
    }
}
