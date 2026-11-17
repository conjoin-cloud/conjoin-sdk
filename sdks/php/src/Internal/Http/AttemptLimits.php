<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Http;

use ConjoinCloud\Cancellation\Cancellation;

final class AttemptLimits
{
    public const MAX_ERROR_BODY_BYTES = 65_536;

    public function __construct(
        public readonly float $timeoutSeconds,
        public readonly ?Cancellation $cancellation,
        public readonly int $maxBodyBytes,
    ) {
    }

    public function bodyLimitFor(int $status): int
    {
        return $status >= 200 && $status < 300 ? $this->maxBodyBytes : min($this->maxBodyBytes, self::MAX_ERROR_BODY_BYTES);
    }

    public function isCancelled(): bool
    {
        return $this->cancellation !== null && $this->cancellation->isRequested();
    }
}
