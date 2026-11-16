<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class AiPolicies
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function check(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/policy/check',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listRules(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/policy/rules',
            query: $query,
        ), $options);
    }

    public function createRule(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'ai/policy/rules',
            body: $data,
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function readRule(string $ruleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/policy/rules/' . PathSegment::encode($ruleId),
        ), $options)->dataArray();
    }

    public function updateRule(string $ruleId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'ai/policy/rules/' . PathSegment::encode($ruleId),
            body: $data,
        ), $options)->dataArray();
    }

    public function deleteRule(string $ruleId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'ai/policy/rules/' . PathSegment::encode($ruleId),
        ), $options)->dataArray();
    }

    public function listLogs(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'ai/policy/logs',
            query: $query,
        ), $options);
    }
}
