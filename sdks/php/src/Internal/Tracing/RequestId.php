<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Tracing;

final class RequestId
{
    public const HEADER = 'Conjoin-Request-Id';

    private const PREFIX = 'cnj_req_';

    private const PATTERN = '/^cnj_req_[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/D';

    private const UINT32_MASK = 0xFFFFFFFF;

    private static int $lastMilliseconds = PHP_INT_MIN;

    private static int $sequence = 0;

    private function __construct()
    {
    }

    public static function isValid(mixed $value): bool
    {
        return is_string($value) && preg_match(self::PATTERN, $value) === 1;
    }

    public static function resolve(?string $value): string
    {
        return $value !== null && self::isValid($value) ? $value : self::generate();
    }

    public static function generate(): string
    {
        $random = random_bytes(16);
        $milliseconds = self::advanceClock((int) floor(microtime(true) * 1000), $random);
        $sequence = self::$sequence;
        $bytes = [
            ($milliseconds >> 40) & 0xff,
            ($milliseconds >> 32) & 0xff,
            ($milliseconds >> 24) & 0xff,
            ($milliseconds >> 16) & 0xff,
            ($milliseconds >> 8) & 0xff,
            $milliseconds & 0xff,
            0x70 | (($sequence >> 28) & 0x0f),
            ($sequence >> 20) & 0xff,
            0x80 | (($sequence >> 14) & 0x3f),
            ($sequence >> 6) & 0xff,
            (($sequence << 2) & 0xff) | (ord($random[10]) & 0x03),
            ord($random[11]),
            ord($random[12]),
            ord($random[13]),
            ord($random[14]),
            ord($random[15]),
        ];
        $hex = bin2hex(pack('C*', ...$bytes));

        return self::PREFIX . UuidFormat::fromHex($hex);
    }

    private static function advanceClock(int $now, string $random): int
    {
        if ($now > self::$lastMilliseconds) {
            self::$sequence = (ord($random[6]) << 23) | (ord($random[7]) << 16) | (ord($random[8]) << 8) | ord($random[9]);
            self::$lastMilliseconds = $now;

            return $now;
        }

        self::$sequence = (self::$sequence + 1) & self::UINT32_MASK;

        if (self::$sequence === 0) {
            self::$lastMilliseconds++;
        }

        return self::$lastMilliseconds;
    }
}
