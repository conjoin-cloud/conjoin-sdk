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

    public function createSmsCampaign(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms/campaigns/',
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function readSmsCampaign(string $campaignId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'messaging/sms/campaigns/' . PathSegment::encode($campaignId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function updateSmsCampaign(string $campaignId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/sms/campaigns/' . PathSegment::encode($campaignId),
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function deleteSmsCampaign(string $campaignId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'messaging/sms/campaigns/' . PathSegment::encode($campaignId),
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function listSmsCampaigns(array $data, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/sms/campaigns/retrieve',
            body: $data,
            scopes: [Scope::MessagingProfileId],
        ), $options);
    }
}
