<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;

final class CloudBrandings
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function getProject(?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/branding/',
        ), $options)->dataArray();
    }

    public function patchProject(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'cloud/branding/',
            body: $data,
        ), $options)->dataArray();
    }

    public function getOrgOverride(string $organizationId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'cloud/branding/organizations/' . PathSegment::encode($organizationId),
        ), $options)->dataArray();
    }

    public function patchOrgOverride(string $organizationId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'cloud/branding/organizations/' . PathSegment::encode($organizationId),
            body: $data,
        ), $options)->dataArray();
    }
}
