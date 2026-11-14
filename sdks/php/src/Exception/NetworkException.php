<?php

declare(strict_types=1);

namespace ConjoinCloud\Exception;

final class NetworkException extends ConjoinException
{
    public const CODE = 'network_error';

    public function __construct(string $message, ?string $requestId)
    {
        parent::__construct($message, self::CODE, requestId: $requestId);
    }
}
