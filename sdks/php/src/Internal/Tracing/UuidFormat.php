<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Tracing;

final class UuidFormat
{
    private function __construct()
    {
    }

    public static function fromHex(string $hex): string
    {
        return sprintf(
            '%s-%s-%s-%s-%s',
            substr($hex, 0, 8),
            substr($hex, 8, 4),
            substr($hex, 12, 4),
            substr($hex, 16, 4),
            substr($hex, 20, 12),
        );
    }
}
