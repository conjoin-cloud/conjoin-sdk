<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Transport;

use ConjoinCloud\HttpMethod;
use DateTimeImmutable;
use DateTimeZone;

final class RetryRules
{
    private const RETRYABLE_STATUSES = [429, 500, 502, 503, 504];

    private const RETRY_AFTER_SECONDS_PATTERN = '/^\d{1,12}(\.\d{1,9})?$/D';

    private const HTTP_DATE_FORMATS = ['D, d M Y H:i:s \G\M\T', 'l, d-M-y H:i:s \G\M\T', 'D M j H:i:s Y'];

    private const MAX_BACKOFF_EXPONENT = 62;

    private const JITTER_RESOLUTION = 1_000_000;

    private function __construct()
    {
    }

    public static function canRetryMethod(HttpMethod $method, bool $hasIdempotencyKey): bool
    {
        return $method !== HttpMethod::Post || $hasIdempotencyKey;
    }

    public static function isRetryableStatus(int $status): bool
    {
        return in_array($status, self::RETRYABLE_STATUSES, true);
    }

    public static function parseRetryAfterSeconds(?string $value, ?float $now = null): ?float
    {
        if ($value === null) {
            return null;
        }

        $trimmed = trim($value);

        if ($trimmed === '' || strlen($trimmed) > 64) {
            return null;
        }

        if (preg_match(self::RETRY_AFTER_SECONDS_PATTERN, $trimmed) === 1) {
            return (float) $trimmed;
        }

        $retryAt = self::parseHttpDate($trimmed);

        if ($retryAt === null) {
            return null;
        }

        return max(0.0, $retryAt - ($now ?? microtime(true)));
    }

    public static function delaySeconds(int $attempt, float $backoffSeconds, float $maxDelaySeconds, ?float $retryAfterSeconds): float
    {
        if ($retryAfterSeconds !== null) {
            return min($retryAfterSeconds, $maxDelaySeconds);
        }

        $ceiling = min($backoffSeconds * (2 ** min($attempt, self::MAX_BACKOFF_EXPONENT)), $maxDelaySeconds);

        return $ceiling * (random_int(0, self::JITTER_RESOLUTION) / self::JITTER_RESOLUTION);
    }

    private static function parseHttpDate(string $value): ?float
    {
        $gmt = new DateTimeZone('GMT');

        foreach (self::HTTP_DATE_FORMATS as $format) {
            $parsed = DateTimeImmutable::createFromFormat('!' . $format, $value, $gmt);

            if ($parsed !== false && DateTimeImmutable::getLastErrors() === false) {
                return (float) $parsed->getTimestamp();
            }
        }

        return null;
    }
}
