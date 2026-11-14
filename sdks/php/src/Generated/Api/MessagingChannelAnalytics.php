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

final class MessagingChannelAnalytics
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/analytics/',
            scopes: [Scope::MessagingProfileId],
        ), $options);
    }

    public function generateSummaries(string $channelId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/analytics/channels/' . PathSegment::encode($channelId) . '/generate',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function createReport(string $messageId, string $channelId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'messaging/analytics/messages/'
                . PathSegment::encode($messageId)
                . '/channels/'
                . PathSegment::encode($channelId)
                . '/reports',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataArray();
    }

    public function incrementOpens(string $analyticsId, ?CallOptions $options = null): bool
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/analytics/' . PathSegment::encode($analyticsId) . '/opens',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataBool();
    }

    public function incrementClicks(string $analyticsId, ?CallOptions $options = null): bool
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/analytics/' . PathSegment::encode($analyticsId) . '/clicks',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataBool();
    }

    public function incrementDeliveries(string $analyticsId, ?CallOptions $options = null): bool
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/analytics/' . PathSegment::encode($analyticsId) . '/deliveries',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataBool();
    }

    public function incrementSubscribes(string $analyticsId, ?CallOptions $options = null): bool
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/analytics/' . PathSegment::encode($analyticsId) . '/subscribes',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataBool();
    }

    public function incrementUnsubscribes(string $analyticsId, ?CallOptions $options = null): bool
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'messaging/analytics/' . PathSegment::encode($analyticsId) . '/unsubscribes',
            scopes: [Scope::MessagingProfileId],
        ), $options)->dataBool();
    }
}
