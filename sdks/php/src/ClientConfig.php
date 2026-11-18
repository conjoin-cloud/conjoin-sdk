<?php

declare(strict_types=1);

namespace ConjoinCloud;

use ConjoinCloud\Exception\ConfigurationException;
use ConjoinCloud\Internal\Tracing\RequestId;
use ConjoinCloud\Internal\Validate;

final class ClientConfig
{
    public const DEFAULT_TIMEOUT_SECONDS = 30.0;

    public const DEFAULT_MAX_RETRIES = 3;

    public const DEFAULT_BACKOFF_SECONDS = 0.5;

    public const DEFAULT_MAX_RETRY_DELAY_SECONDS = 60.0;

    public const DEFAULT_MAX_RESPONSE_BYTES = 16_777_216;

    private const API_VERSION_PATTERN = '/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/D';

    private function __construct(
        #[\SensitiveParameter] public readonly string $key,
        public readonly bool $isPublishableKey,
        public readonly string $baseUrl,
        public readonly string $apiVersion,
        public readonly float $timeoutSeconds,
        public readonly int $maxRetries,
        public readonly float $backoffSeconds,
        public readonly float $maxRetryDelaySeconds,
        public readonly int $maxResponseBytes,
        public readonly ?string $requestId,
        public readonly array $scopeValues,
    ) {
    }

    public static function resolve(
        #[\SensitiveParameter] ?string $apiKey,
        #[\SensitiveParameter] ?string $publishableKey,
        ?string $baseUrl,
        ?string $apiVersion,
        float $timeoutSeconds,
        int $maxRetries,
        float $backoffSeconds,
        float $maxRetryDelaySeconds,
        int $maxResponseBytes,
        ?string $requestId,
        ?string $billingEntityId,
        ?string $messagingProfileId,
        ?string $authAppId,
    ): self {
        if ($apiKey !== null && $publishableKey !== null) {
            throw new ConfigurationException('Provide exactly one of apiKey or publishableKey');
        }

        $key = $apiKey ?? $publishableKey;

        if ($key === null || $key === '') {
            throw new ConfigurationException('Either apiKey or publishableKey must be provided');
        }

        $key = Validate::tokenValue($key, $apiKey !== null ? 'apiKey' : 'publishableKey');
        $version = $apiVersion ?? Version::DEFAULT_API_VERSION;

        if (preg_match(self::API_VERSION_PATTERN, $version) !== 1) {
            throw new ConfigurationException('apiVersion must be a date such as 2026-06-01');
        }

        return new self(
            $key,
            $apiKey === null,
            $baseUrl === null ? Region::fromKey($key)->baseUrl() : self::validateBaseUrl($baseUrl),
            $version,
            Validate::timeoutSeconds($timeoutSeconds, 'timeoutSeconds'),
            Validate::retryCount($maxRetries, 'maxRetries'),
            Validate::delaySeconds($backoffSeconds, 'backoffSeconds'),
            Validate::delaySeconds($maxRetryDelaySeconds, 'maxRetryDelaySeconds'),
            Validate::responseBytes($maxResponseBytes),
            self::validateRequestId($requestId),
            self::scopeValues($billingEntityId, $messagingProfileId, $authAppId),
        );
    }

    public function withScope(?string $billingEntityId, ?string $messagingProfileId, ?string $authAppId): self
    {
        $merged = array_merge($this->scopeValues, self::scopeValues($billingEntityId, $messagingProfileId, $authAppId));

        return $this->copy($merged, $this->requestId);
    }

    public function withRequestId(string $requestId): self
    {
        return $this->copy($this->scopeValues, self::validateRequestId($requestId));
    }

    public function scopeValue(Scope $scope): ?string
    {
        $value = $this->scopeValues[$scope->value] ?? null;

        return is_string($value) ? $value : null;
    }

    public function __debugInfo(): array
    {
        return [
            'key' => '[redacted]',
            'isPublishableKey' => $this->isPublishableKey,
            'baseUrl' => $this->baseUrl,
            'apiVersion' => $this->apiVersion,
            'timeoutSeconds' => $this->timeoutSeconds,
            'maxRetries' => $this->maxRetries,
            'backoffSeconds' => $this->backoffSeconds,
            'maxRetryDelaySeconds' => $this->maxRetryDelaySeconds,
            'maxResponseBytes' => $this->maxResponseBytes,
            'requestId' => $this->requestId,
            'scopeValues' => $this->scopeValues,
        ];
    }

    private function copy(array $scopeValues, ?string $requestId): self
    {
        return new self(
            $this->key,
            $this->isPublishableKey,
            $this->baseUrl,
            $this->apiVersion,
            $this->timeoutSeconds,
            $this->maxRetries,
            $this->backoffSeconds,
            $this->maxRetryDelaySeconds,
            $this->maxResponseBytes,
            $requestId,
            $scopeValues,
        );
    }

    private static function scopeValues(?string $billingEntityId, ?string $messagingProfileId, ?string $authAppId): array
    {
        $values = [];
        $settings = [
            Scope::BillingEntityId->value => $billingEntityId,
            Scope::MessagingProfileId->value => $messagingProfileId,
            Scope::AuthAppId->value => $authAppId,
        ];

        foreach ($settings as $header => $value) {
            if ($value === null) {
                continue;
            }

            $scope = Scope::from($header);
            $values[$header] = Validate::tokenValue($value, $scope->settingName());
        }

        return $values;
    }

    private static function validateRequestId(?string $requestId): ?string
    {
        return $requestId !== null && RequestId::isValid($requestId) ? $requestId : null;
    }

    private static function validateBaseUrl(string $baseUrl): string
    {
        $parts = preg_match('/[\x00-\x20\x7f]/', $baseUrl) === 1 ? false : parse_url($baseUrl);

        if (
            !is_array($parts)
            || !in_array(strtolower($parts['scheme'] ?? ''), ['http', 'https'], true)
            || ($parts['host'] ?? '') === ''
            || isset($parts['user'])
            || isset($parts['pass'])
            || isset($parts['query'])
            || isset($parts['fragment'])
        ) {
            throw new ConfigurationException('baseUrl must be an absolute http or https URL without credentials, query, or fragment');
        }

        return rtrim($baseUrl, '/');
    }
}
