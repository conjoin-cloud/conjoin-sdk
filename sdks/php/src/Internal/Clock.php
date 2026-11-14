<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal;

final class Clock
{
    public const NANOSECONDS_PER_SECOND = 1_000_000_000;

    private function __construct()
    {
    }

    public static function nowNanoseconds(): int
    {
        $now = hrtime(true);

        return is_int($now) ? $now : (int) $now;
    }

    public static function deadlineAfter(float $seconds): int
    {
        return self::nowNanoseconds() + (int) ceil($seconds * self::NANOSECONDS_PER_SECOND);
    }
}
