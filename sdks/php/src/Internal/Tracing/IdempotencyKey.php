<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Tracing;

use ConjoinCloud\Exception\ConfigurationException;

final class IdempotencyKey
{
    public const HEADER = 'Idempotency-Key';

    private const PATTERN = '/^[A-Za-z0-9\-_:.]{1,64}$/D';

    private function __construct()
    {
    }

    public static function generate(): string
    {
        $bytes = random_bytes(16);
        $bytes[6] = chr((ord($bytes[6]) & 0x0f) | 0x40);
        $bytes[8] = chr((ord($bytes[8]) & 0x3f) | 0x80);

        return UuidFormat::fromHex(bin2hex($bytes));
    }

    public static function validate(string $key): string
    {
        if (preg_match(self::PATTERN, $key) !== 1) {
            throw new ConfigurationException(
                'idempotencyKey must be 1 to 64 characters of letters, digits, hyphens, underscores, colons, and dots',
            );
        }

        return $key;
    }
}
