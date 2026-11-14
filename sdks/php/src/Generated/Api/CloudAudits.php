<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class CloudAudits
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readLogs(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/audit-logs/',
            query: $query,
        ), $options);
    }

    public function readLogsCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/audit-logs/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function readStats(array $query, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/audit-logs/stats',
            query: $query,
        ), $options)->dataArray();
    }
}
