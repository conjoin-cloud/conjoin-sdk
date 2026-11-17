<?php

declare(strict_types=1);

namespace ConjoinCloud\Exception;

final class RateLimitException extends ApiException
{
    public function __construct(
        string $message,
        string $errorCode,
        int $status,
        ?string $param,
        mixed $details,
        ?string $requestId,
        private readonly ?float $retryAfterSeconds,
    ) {
        parent::__construct($message, $errorCode, $status, $param, $details, $requestId);
    }

    public function getRetryAfterSeconds(): ?float
    {
        return $this->retryAfterSeconds;
    }
}
