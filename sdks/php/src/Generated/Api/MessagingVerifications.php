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

final class MessagingVerifications
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/verifications/send',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function check(string $verificationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/verifications/' . PathSegment::encode($verificationId) . '/check',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function resend(string $verificationId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/verifications/resend/' . PathSegment::encode($verificationId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function listMessages(array $data, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/verifications/messages',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options);
    }
}
