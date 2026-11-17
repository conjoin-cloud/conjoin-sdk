<?php

declare(strict_types=1);

namespace ConjoinCloud\Cancellation;

final class CancellationToken implements Cancellation
{
    private bool $requested = false;

    public function cancel(): void
    {
        $this->requested = true;
    }

    public function isRequested(): bool
    {
        return $this->requested;
    }
}
