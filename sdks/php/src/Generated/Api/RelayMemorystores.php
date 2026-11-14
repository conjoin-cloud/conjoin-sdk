<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class RelayMemorystores
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readClusters(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/memorystore-clusters/',
            query: $query,
        ), $options);
    }

    public function createCluster(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/memorystore-clusters/',
            body: $data,
        ), $options)->dataArray();
    }

    public function readClustersCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/memorystore-clusters/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function readCluster(string $memorystoreClusterId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/memorystore-clusters/' . PathSegment::encode($memorystoreClusterId),
        ), $options)->dataArray();
    }

    public function updateCluster(string $memorystoreClusterId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'relay/memorystore-clusters/' . PathSegment::encode($memorystoreClusterId),
            body: $data,
        ), $options)->dataArray();
    }

    public function deleteCluster(string $memorystoreClusterId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'relay/memorystore-clusters/' . PathSegment::encode($memorystoreClusterId),
        ), $options)->dataArray();
    }

    public function suspendCluster(string $memorystoreClusterId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/memorystore-clusters/' . PathSegment::encode($memorystoreClusterId) . '/suspend',
        ), $options)->dataArray();
    }

    public function executeCommand(string $memorystoreClusterId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/memorystore-clusters/' . PathSegment::encode($memorystoreClusterId) . '/execute',
            body: $data,
        ), $options)->dataArray();
    }
}
