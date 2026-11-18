<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Frontend;

use ConjoinCloud\AuthMode;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Credential;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;
use ConjoinCloud\Scope;

final class BillingSelves
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function listPaymentMethods(#[\SensitiveParameter] Credential $sessionToken, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/self/payment-methods/',
            query: $query,
            scopes: [Scope::BillingEntityId],
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options);
    }

    public function createPaymentMethod(#[\SensitiveParameter] Credential $sessionToken, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/self/payment-methods/',
            body: $data,
            scopes: [Scope::BillingEntityId],
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
    }

    public function listPaymentMethodsCount(#[\SensitiveParameter] Credential $sessionToken, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'billing/self/payment-methods/count',
            query: $query,
            scopes: [Scope::BillingEntityId],
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
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

    public function activatePriceBundles(#[\SensitiveParameter] Credential $sessionToken, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/self/price-bundle-activations/',
            body: $data,
            scopes: [Scope::BillingEntityId],
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
    }

    public function deactivatePriceBundle(
        string $priceBundleActivationId,
        #[\SensitiveParameter] Credential $sessionToken,
        array $data,
        ?CallOptions $options = null,
    ): array {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'billing/self/price-bundle-activations/'
                . PathSegment::encode($priceBundleActivationId)
                . '/deactivate',
            body: $data,
            scopes: [Scope::BillingEntityId],
            auth: AuthMode::Session,
            sessionToken: $sessionToken,
        ), $options)->dataArray();
    }
}
