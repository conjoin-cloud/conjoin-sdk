<?php

declare(strict_types=1);

namespace ConjoinCloud\Exception;

final class TimeoutException extends ConjoinException
{
    public const CODE = 'timeout_error';

    public function __construct(float $timeoutSeconds, ?string $requestId)
    {
        parent::__construct(
            sprintf('The request timed out after %s seconds', rtrim(rtrim(sprintf('%.3F', $timeoutSeconds), '0'), '.')),
            self::CODE,
            requestId: $requestId,
        );
    }
}
