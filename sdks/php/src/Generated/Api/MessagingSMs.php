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

final class MessagingSMs
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function sendSms(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms/send',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readSmsMessages(string $messageId, array $data, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms/messages/' . PathSegment::encode($messageId),
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options);
    }

    public function generateSmsSummary(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms/summary',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }
}
