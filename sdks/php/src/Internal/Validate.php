<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal;

use ConjoinCloud\Exception\ConfigurationException;

final class Validate
{
    public const MAX_SECONDS = 86_400.0;

    public const MIN_TIMEOUT_SECONDS = 0.001;

    public const MAX_RETRIES = 100;

    public const MIN_RESPONSE_BYTES = 1_024;

    public const MAX_RESPONSE_BYTES = 1_073_741_824;

    private const HEADER_NAME_PATTERN = '/^[!#$%&\'*+.^_`|~0-9A-Za-z-]{1,256}$/D';

    private const HEADER_VALUE_PATTERN = '/^[\x20-\x7e\t]{0,8192}$/D';

    private const TOKEN_VALUE_PATTERN = '/^[\x21-\x7e]{1,4096}$/D';

    private function __construct()
    {
    }

    public static function timeoutSeconds(float $value, string $name): float
    {
        if (!is_finite($value) || $value < self::MIN_TIMEOUT_SECONDS || $value > self::MAX_SECONDS) {
            throw new ConfigurationException(sprintf(
                '%s must be a number of seconds from %s to %s',
                $name,
                (string) self::MIN_TIMEOUT_SECONDS,
                (string) self::MAX_SECONDS,
            ));
        }

        return $value;
    }

    public static function delaySeconds(float $value, string $name): float
    {
        if (!is_finite($value) || $value < 0.0 || $value > self::MAX_SECONDS) {
            throw new ConfigurationException(sprintf(
                '%s must be a number of seconds from 0 to %s',
                $name,
                (string) self::MAX_SECONDS,
            ));
        }

        return $value;
    }

    public static function retryCount(int $value, string $name): int
    {
        if ($value < 0 || $value > self::MAX_RETRIES) {
            throw new ConfigurationException(sprintf('%s must be a whole number from 0 to %d', $name, self::MAX_RETRIES));
        }

        return $value;
    }

    public static function responseBytes(int $value): int
    {
        if ($value < self::MIN_RESPONSE_BYTES || $value > self::MAX_RESPONSE_BYTES) {
            throw new ConfigurationException(sprintf(
                'maxResponseBytes must be a whole number from %d to %d',
                self::MIN_RESPONSE_BYTES,
                self::MAX_RESPONSE_BYTES,
            ));
        }

        return $value;
    }

    public static function tokenValue(#[\SensitiveParameter] string $value, string $name): string
    {
        if (preg_match(self::TOKEN_VALUE_PATTERN, $value) !== 1) {
            throw new ConfigurationException(sprintf(
                '%s must be 1 to 4096 printable ASCII characters without spaces',
                $name,
            ));
        }

        return $value;
    }

    public static function isHeaderName(string $name): bool
    {
        return preg_match(self::HEADER_NAME_PATTERN, $name) === 1;
    }

    public static function headers(#[\SensitiveParameter] array $headers): array
    {
        $validated = [];

        foreach ($headers as $name => $value) {
            if (!is_string($name) || !self::isHeaderName($name)) {
                throw new ConfigurationException('A header name must be an HTTP token of 1 to 256 characters');
            }

            if (!is_string($value) || preg_match(self::HEADER_VALUE_PATTERN, $value) !== 1) {
                throw new ConfigurationException(sprintf(
                    'The %s header value must be printable ASCII of at most 8192 characters',
                    $name,
                ));
            }

            $validated[$name] = $value;
        }

        return $validated;
    }
}
