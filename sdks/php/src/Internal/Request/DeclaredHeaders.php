<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Request;

use ConjoinCloud\DeclaredHeader;
use ConjoinCloud\Exception\ConfigurationException;

final class DeclaredHeaders
{
    private const HEADER_VALUE_PATTERN = '/^[\x21-\x7e]+$/D';

    private const PATTERN_DELIMITER = '~';

    private function __construct()
    {
    }

    public static function names(array $declared): array
    {
        $names = [];

        foreach ($declared as $header) {
            if ($header instanceof DeclaredHeader) {
                $names[] = strtolower($header->name);
            }
        }

        return $names;
    }

    public static function resolve(#[\SensitiveParameter] array $declared): array
    {
        $headers = [];

        foreach ($declared as $header) {
            if (!$header instanceof DeclaredHeader) {
                continue;
            }

            $value = $header->value();

            if ($value === null) {
                if ($header->required) {
                    throw new ConfigurationException(sprintf('This call needs %s', $header->argument));
                }

                continue;
            }

            self::check($header, $value);
            $headers[$header->name] = $value;
        }

        return $headers;
    }

    private static function check(DeclaredHeader $header, #[\SensitiveParameter] string $value): void
    {
        $length = strlen($value);
        $isTooShort = $header->minLength !== null && $length < $header->minLength;
        $isTooLong = $header->maxLength !== null && $length > $header->maxLength;

        if (preg_match(self::HEADER_VALUE_PATTERN, $value) !== 1 || $isTooShort || $isTooLong || !self::matchesPattern($header, $value)) {
            throw new ConfigurationException(sprintf('%s does not meet the documented length or format', $header->argument));
        }
    }

    private static function matchesPattern(DeclaredHeader $header, #[\SensitiveParameter] string $value): bool
    {
        if ($header->pattern === null) {
            return true;
        }

        $expression = self::PATTERN_DELIMITER
            . str_replace(self::PATTERN_DELIMITER, '\\' . self::PATTERN_DELIMITER, $header->pattern)
            . self::PATTERN_DELIMITER . 'Du';
        $matched = preg_match($expression, $value);

        if ($matched === false) {
            throw new ConfigurationException(sprintf('The documented format of %s cannot be checked', $header->argument));
        }

        return $matched === 1;
    }
}
