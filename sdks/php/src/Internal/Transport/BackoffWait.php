<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Transport;

use ConjoinCloud\Cancellation\Cancellation;
use ConjoinCloud\Exception\CancelledException;
use ConjoinCloud\Internal\Clock;

final class BackoffWait
{
    private const POLL_MICROSECONDS = 10_000;

    private const NANOSECONDS_PER_MICROSECOND = 1_000;

    private function __construct()
    {
    }

    public static function sleep(float $seconds, ?Cancellation $cancellation, string $requestId): void
    {
        $deadline = Clock::deadlineAfter($seconds);

        while (true) {
            if ($cancellation !== null && $cancellation->isRequested()) {
                throw new CancelledException($requestId);
            }

            $remaining = $deadline - Clock::nowNanoseconds();

            if ($remaining <= 0) {
                return;
            }

            usleep(max(1, min(self::POLL_MICROSECONDS, intdiv($remaining, self::NANOSECONDS_PER_MICROSECOND))));
        }
    }
}
