<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Scope;

final class MessagingMultisends
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function create(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/multisend/send',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function read(string $messageId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/multisend/' . PathSegment::encode($messageId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }
}
