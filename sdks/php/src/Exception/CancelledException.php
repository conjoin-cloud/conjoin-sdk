<?php

declare(strict_types=1);

namespace ConjoinCloud\Exception;

final class CancelledException extends ConjoinException
{
    public const CODE = 'request_aborted';

    public function __construct(?string $requestId)
    {
        parent::__construct('The caller cancelled the request', self::CODE, requestId: $requestId);
    }
}
