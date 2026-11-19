<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Frontend;

use ConjoinCloud\AuthMode;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Credential;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;
use ConjoinCloud\Scope;

final class BillingSelves
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listEntitlementOverrides(#[\SensitiveParameter] Credential $sessionToken, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/self/entitlement-overrides/',
            query: $query,
            scopes: [Scope::BillingEntityId],
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options);
    }

    public function listPriceBundles(#[\SensitiveParameter] Credential $sessionToken, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/self/price-bundles/',
            query: $query,
            scopes: [Scope::BillingEntityId],
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options);
    }

    public function listEntitlementOverridesCount(#[\SensitiveParameter] Credential $sessionToken, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/self/entitlement-overrides/count',
            query: $query,
            scopes: [Scope::BillingEntityId],
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
    }

    public function listPriceBundlesCount(#[\SensitiveParameter] Credential $sessionToken, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/self/price-bundles/count',
            query: $query,
            scopes: [Scope::BillingEntityId],
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
    }
}
