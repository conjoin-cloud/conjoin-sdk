<?php

declare(strict_types=1);

namespace ConjoinCloud;

use ConjoinCloud\Internal\Http\GuzzleSender;
use ConjoinCloud\Internal\Http\Psr18Sender;
use ConjoinCloud\Internal\Tracing\RequestId;
use ConjoinCloud\Internal\Transport\ListPageFetcher;
use ConjoinCloud\Internal\Transport\RequestExecutor;
use ConjoinCloud\Pagination\ListPage;
use ConjoinCloud\Response\ApiResponse;
use Psr\Http\Client\ClientInterface;

final class ConjoinClient
{
    private ClientConfig $config;

    private readonly RequestExecutor $executor;

    public function __construct(
        #[\SensitiveParameter] ?string $apiKey = null,
        #[\SensitiveParameter] ?string $publishableKey = null,
        ?string $baseUrl = null,
        ?string $apiVersion = null,
        float $timeoutSeconds = ClientConfig::DEFAULT_TIMEOUT_SECONDS,
        int $maxRetries = ClientConfig::DEFAULT_MAX_RETRIES,
        float $backoffSeconds = ClientConfig::DEFAULT_BACKOFF_SECONDS,
        float $maxRetryDelaySeconds = ClientConfig::DEFAULT_MAX_RETRY_DELAY_SECONDS,
        int $maxResponseBytes = ClientConfig::DEFAULT_MAX_RESPONSE_BYTES,
        ?string $requestId = null,
        ?string $billingEntityId = null,
        ?string $messagingProfileId = null,
        ?string $authAppId = null,
        ?ClientInterface $httpClient = null,
    ) {
        $this->config = ClientConfig::resolve(
            $apiKey,
            $publishableKey,
            $baseUrl,
            $apiVersion,
            $timeoutSeconds,
            $maxRetries,
            $backoffSeconds,
            $maxRetryDelaySeconds,
            $maxResponseBytes,
            $requestId,
            $billingEntityId,
            $messagingProfileId,
            $authAppId,
        );
        $this->executor = new RequestExecutor($httpClient === null ? new GuzzleSender() : new Psr18Sender($httpClient));
    }

    public function withScope(?string $billingEntityId = null, ?string $messagingProfileId = null, ?string $authAppId = null): self
    {
        $copy = clone $this;
        $copy->config = $this->config->withScope($billingEntityId, $messagingProfileId, $authAppId);

        return $copy;
    }

    public function withRequestTrace(?string $requestId = null): self
    {
        $copy = clone $this;
        $copy->config = $this->config->withRequestId(RequestId::resolve($requestId ?? $this->config->requestId));

        return $copy;
    }

    public function requestId(): ?string
    {
        return $this->config->requestId;
    }

    public function baseUrl(): string
    {
        return $this->config->baseUrl;
    }

    public function scope(Scope $scope): ?string
    {
        return $this->config->scopeValue($scope);
    }

    public function send(#[\SensitiveParameter] OperationRequest $request, #[\SensitiveParameter] ?CallOptions $options = null): ApiResponse
    {
        return $this->executor->execute($this->config, $request, $options ?? new CallOptions());
    }

    public function sendList(#[\SensitiveParameter] OperationRequest $request, #[\SensitiveParameter] ?CallOptions $options = null): ListPage
    {
        return (new ListPageFetcher($this->executor, $this->config, $request, $options ?? new CallOptions()))->first();
    }

    public function __debugInfo(): array
    {
        return ['config' => $this->config];
    }
}
