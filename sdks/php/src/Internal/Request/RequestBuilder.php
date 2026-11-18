<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Request;

use ConjoinCloud\AuthMode;
use ConjoinCloud\CallOptions;
use ConjoinCloud\ClientConfig;
use ConjoinCloud\Exception\ConfigurationException;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Tracing\IdempotencyKey;
use ConjoinCloud\Internal\Tracing\RequestId;
use ConjoinCloud\Internal\Validate;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Scope;
use ConjoinCloud\Version;

final class RequestBuilder
{
    private const ABSOLUTE_URL_PATTERN = '/^[a-z][a-z0-9+.-]*:/i';

    private const RESERVED_HEADER_NAMES = [
        'accept',
        'connection',
        'content-length',
        'expect',
        'host',
        'te',
        'transfer-encoding',
        'upgrade',
        'user-agent',
        'x-conjoin-api-version',
        'x-conjoin-sdk-version',
    ];

    private function __construct()
    {
    }

    public static function build(
        #[\SensitiveParameter] ClientConfig $config,
        #[\SensitiveParameter] OperationRequest $request,
        #[\SensitiveParameter] CallOptions $options,
    ): PreparedRequest {
        $url = self::buildUrl($config->baseUrl, $request->path, $request->query);
        $requestId = self::resolveRequestId($config, $options);
        $idempotencyKey = self::resolveIdempotencyKey($request, $options);
        $body = EncodedBody::encode($request->body, $request->bodyType);
        $headers = self::withoutManagedHeaders($options->headers, DeclaredHeaders::names($request->declaredHeaders));
        $headers = array_merge($headers, DeclaredHeaders::resolve($request->declaredHeaders));
        $authorization = self::authorization($config, $request);

        if ($authorization !== null) {
            $headers['Authorization'] = $authorization;
        }

        if ($body !== null) {
            $headers['Content-Type'] = $body->contentType;
        }

        $headers['Accept'] = 'application/json';
        $headers['User-Agent'] = sprintf('conjoin-sdk-php/%s PHP/%s', Version::SDK, PHP_VERSION);
        $headers['X-Conjoin-SDK-Version'] = Version::SDK;
        $headers['X-Conjoin-API-Version'] = $config->apiVersion;

        foreach ($request->scopes as $scope) {
            if ($scope instanceof Scope) {
                $headers[$scope->value] = self::scopeValue($config, $scope);
            }
        }

        $headers[RequestId::HEADER] = $requestId;

        if ($idempotencyKey !== null) {
            $headers[IdempotencyKey::HEADER] = $idempotencyKey;
        }

        return new PreparedRequest($request->method, $url, $headers, $body?->bytes, $requestId);
    }

    private static function buildUrl(string $baseUrl, string $path, ?array $query): string
    {
        if (preg_match(self::ABSOLUTE_URL_PATTERN, $path) === 1 || str_starts_with($path, '//')) {
            throw new ConfigurationException('path must be relative to the Conjoin API');
        }

        if (preg_match('/[\x00-\x20\x7f#?]/', $path) === 1) {
            throw new ConfigurationException('path must be an encoded path without spaces, a query, or a fragment');
        }

        $relative = (string) preg_replace('#^v1/#', '', ltrim($path, '/'));
        $queryString = $query === null ? '' : QueryString::build($query);

        return sprintf('%s/v1/%s%s', $baseUrl, $relative, $queryString === '' ? '' : '?' . $queryString);
    }

    private static function resolveRequestId(#[\SensitiveParameter] ClientConfig $config, #[\SensitiveParameter] CallOptions $options): string
    {
        foreach ([$options->requestId, self::headerValue($options->headers, RequestId::HEADER), $config->requestId] as $candidate) {
            if (RequestId::isValid($candidate) && is_string($candidate)) {
                return $candidate;
            }
        }

        return RequestId::generate();
    }

    private static function resolveIdempotencyKey(#[\SensitiveParameter] OperationRequest $request, #[\SensitiveParameter] CallOptions $options): ?string
    {
        $supplied = $options->idempotencyKey ?? self::headerValue($options->headers, IdempotencyKey::HEADER);

        if ($supplied !== null) {
            if ($request->method !== HttpMethod::Post) {
                throw new ConfigurationException('Only a POST takes an idempotency key');
            }

            return IdempotencyKey::validate($supplied);
        }

        return $request->method === HttpMethod::Post && $request->acceptsIdempotencyKey
            ? IdempotencyKey::generate()
            : null;
    }

    private static function authorization(#[\SensitiveParameter] ClientConfig $config, #[\SensitiveParameter] OperationRequest $request): ?string
    {
        return match ($request->auth) {
            AuthMode::None => null,
            AuthMode::ClientKey => 'Bearer ' . $config->key,
            AuthMode::Bearer => 'Bearer ' . Validate::tokenValue(
                $request->bearerToken ?? throw new ConfigurationException('This call needs a bearer token, such as the SCIM token'),
                'The bearer token',
            ),
            AuthMode::PublishableKey => $config->isPublishableKey
                ? 'Bearer ' . $config->key
                : throw new ConfigurationException('This call needs publishableKey in the client settings'),
            AuthMode::Session => 'Bearer ' . Validate::tokenValue(
                $request->sessionToken?->reveal() ?? throw new ConfigurationException('This call needs sessionToken'),
                'sessionToken',
            ),
        };
    }

    private static function scopeValue(#[\SensitiveParameter] ClientConfig $config, Scope $scope): string
    {
        $value = $config->scopeValue($scope);

        if ($value === null) {
            throw new ConfigurationException(sprintf('This call needs %s in the client settings', $scope->settingName()));
        }

        return $value;
    }

    private static function withoutManagedHeaders(#[\SensitiveParameter] array $headers, array $declaredNames): array
    {
        $managed = array_merge(
            ['authorization', 'content-type', strtolower(RequestId::HEADER), strtolower(IdempotencyKey::HEADER)],
            array_map(static fn (Scope $scope): string => strtolower($scope->value), Scope::cases()),
            self::RESERVED_HEADER_NAMES,
            $declaredNames,
        );
        $kept = [];

        foreach ($headers as $name => $value) {
            if (!in_array(strtolower((string) $name), $managed, true)) {
                $kept[(string) $name] = $value;
            }
        }

        return $kept;
    }

    private static function headerValue(#[\SensitiveParameter] array $headers, string $name): ?string
    {
        foreach ($headers as $headerName => $value) {
            if (strcasecmp((string) $headerName, $name) === 0 && is_string($value)) {
                return $value;
            }
        }

        return null;
    }
}
