<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Response;

use ConjoinCloud\Exception\ApiException;
use ConjoinCloud\Exception\AuthenticationException;
use ConjoinCloud\Exception\ConflictException;
use ConjoinCloud\Exception\FieldError;
use ConjoinCloud\Exception\NotFoundException;
use ConjoinCloud\Exception\PermissionDeniedException;
use ConjoinCloud\Exception\RateLimitException;
use ConjoinCloud\Exception\ServerException;
use ConjoinCloud\Exception\ValidationException;
use ConjoinCloud\Internal\Http\ReceivedResponse;
use ConjoinCloud\Internal\Transport\RetryRules;

final class ErrorFactory
{
    private const MAX_MESSAGE_BYTES = 1_024;

    private const MAX_FIELD_ERRORS = 100;

    private const FALLBACK_CODES = [
        400 => 'invalid_request',
        401 => 'authentication_failed',
        403 => 'permission_denied',
        404 => 'not_found',
        409 => 'conflict',
        422 => 'invalid_request',
        429 => 'rate_limited',
    ];

    private function __construct()
    {
    }

    public static function fromResponse(ReceivedResponse $response, string $requestId): ApiException
    {
        $payload = JsonBody::decode($response->body)->value;
        $body = is_array($payload) ? $payload : [];
        $meta = is_array($body['response'] ?? null) ? $body['response'] : [];
        $error = is_array($body['error'] ?? null) ? $body['error'] : [];
        $status = $response->status;
        $message = self::text($meta['message'] ?? null) ?? self::text($body['message'] ?? null) ?? sprintf('HTTP %d', $status);
        $code = self::text($error['code'] ?? null) ?? self::fallbackCode($status);
        $param = self::text($error['param'] ?? null);
        $details = $error['details'] ?? (is_array($body['errors'] ?? null) ? $body['errors'] : null);

        return match (true) {
            $status === 400, $status === 422 => new ValidationException($message, $code, $status, $param, $details, $requestId, self::fieldErrors($details)),
            $status === 401 => new AuthenticationException($message, $code, $status, $param, $details, $requestId),
            $status === 403 => new PermissionDeniedException($message, $code, $status, $param, $details, $requestId),
            $status === 404 => new NotFoundException($message, $code, $status, $param, $details, $requestId),
            $status === 409 => new ConflictException($message, $code, $status, $param, $details, $requestId),
            $status === 429 => new RateLimitException(
                $message,
                $code,
                $status,
                $param,
                $details,
                $requestId,
                RetryRules::parseRetryAfterSeconds($response->header('retry-after')),
            ),
            $status >= 500 => new ServerException($message, $code, $status, $param, $details, $requestId),
            default => new ApiException($message, $code, $status, $param, $details, $requestId),
        };
    }

    private static function fieldErrors(mixed $details): array
    {
        if (!is_array($details) || !array_is_list($details)) {
            return [];
        }

        $errors = [];

        foreach (array_slice($details, 0, self::MAX_FIELD_ERRORS) as $item) {
            if (is_array($item) && is_string($item['message'] ?? null) && is_string($item['path'] ?? null)) {
                $errors[] = new FieldError($item['path'], $item['message']);
            }
        }

        return $errors;
    }

    private static function text(mixed $value): ?string
    {
        if (!is_string($value) || trim($value) === '') {
            return null;
        }

        return strlen($value) > self::MAX_MESSAGE_BYTES ? substr($value, 0, self::MAX_MESSAGE_BYTES) : $value;
    }

    private static function fallbackCode(int $status): string
    {
        return self::FALLBACK_CODES[$status] ?? ($status >= 500 ? 'server_error' : 'api_error');
    }
}
