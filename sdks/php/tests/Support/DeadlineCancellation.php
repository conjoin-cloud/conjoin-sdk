<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support;

use ConjoinCloud\Cancellation\Cancellation;

final class DeadlineCancellation implements Cancellation
{
    private readonly float $cancelAt;

    public function __construct(float $afterSeconds)
    {
        $this->cancelAt = microtime(true) + $afterSeconds;
    }

    public function isRequested(): bool
    {
        return microtime(true) >= $this->cancelAt;
    }
}
