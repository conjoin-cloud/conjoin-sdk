<?php

declare(strict_types=1);

namespace ConjoinCloud\Exception;

use RuntimeException;

abstract class ConjoinException extends RuntimeException
{
    public function __construct(
        string $message,
        private readonly string $errorCode,
        private readonly int $status = 0,
        private readonly ?string $param = null,
        private readonly mixed $details = null,
        private readonly ?string $requestId = null,
    ) {
        parent::__construct($message);
    }

    public function getStatus(): int
    {
        return $this->status;
    }

    public function getErrorCode(): string
    {
        return $this->errorCode;
    }

    public function getParam(): ?string
    {
        return $this->param;
    }

    public function getDetails(): mixed
    {
        return $this->details;
    }

    public function getRequestId(): ?string
    {
        return $this->requestId;
    }
}
