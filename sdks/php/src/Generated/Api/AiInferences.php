<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class AiInferences
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function createChatCompletion(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/inference/chat/completions',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function createAiMultiModel(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/inference/multi-model',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function createAiBestOfN(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/inference/best-of-n',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listRequests(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/inference/requests',
            query: $query,
        ), $options);
    }

    public function readRequest(string $requestId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/inference/requests/' . PathSegment::encode($requestId),
        ), $options)->dataArray();
    }
}
