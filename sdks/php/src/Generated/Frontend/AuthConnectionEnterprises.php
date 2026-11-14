<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Frontend;

use ConjoinCloud\AuthMode;
use ConjoinCloud\BodyType;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;

final class AuthConnectionEnterprises
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function configureSsoPortalConnection(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/portal/connections',
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function updateSsoPortalConnection(string $connectionId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'auth/portal/connections/' . PathSegment::encode($connectionId),
            body: $data,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function importSsoPortalMetadata(string $connectionId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'auth/portal/connections/' . PathSegment::encode($connectionId) . '/import-metadata',
            body: $data,
            bodyType: BodyType::Multipart,
            auth: AuthMode::None,
        ), $options)->dataArray();
    }

    public function readSsoPortalProviderConfig(string $connectionId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/portal/connections/' . PathSegment::encode($connectionId) . '/service-provider-settings',
            auth: AuthMode::None,
        ), $options)->dataArray();
    }
}
