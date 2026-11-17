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

final class MessagingSMSCampaigns
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listSmsCampaigns(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/sms-campaigns/',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options);
    }

    public function createSmsCampaign(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms-campaigns/',
            body: $data,
            scopes: [Scope::MessagingProfileId],
            acceptsIdempotencyKey: true,
        ), $options)->dataArray();
    }

    public function listSmsCampaignsCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/sms-campaigns/count',
            query: $query,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function readSmsCampaign(string $smsCampaignId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/sms-campaigns/' . PathSegment::encode($smsCampaignId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function updateSmsCampaign(string $smsCampaignId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/sms-campaigns/' . PathSegment::encode($smsCampaignId),
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function deleteSmsCampaign(string $smsCampaignId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/sms-campaigns/' . PathSegment::encode($smsCampaignId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }
}
