<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class CloudSKUCatalogs
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readSkuCatalog(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/skus/',
            query: $query,
        ), $options);
    }

    public function readSkuCatalogCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/skus/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function readSingleSkuCatalog(string $skuId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/skus/' . PathSegment::encode($skuId),
        ), $options)->dataArray();
    }
}
