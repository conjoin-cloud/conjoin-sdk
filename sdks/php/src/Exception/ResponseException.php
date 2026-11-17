<?php

declare(strict_types=1);

namespace ConjoinCloud\Exception;

final class ResponseException extends ConjoinException
{
    public const INVALID_RESPONSE = 'invalid_response';

    public const RESPONSE_TOO_LARGE = 'response_too_large';

    public function __construct(string $message, int $status, ?string $requestId, string $errorCode = self::INVALID_RESPONSE)
    {
        parent::__construct($message, $errorCode, $status, requestId: $requestId);
    }
}
