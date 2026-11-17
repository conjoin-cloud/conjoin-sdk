<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Request;

use ConjoinCloud\Exception\ConfigurationException;

final class QueryString
{
    private const MAX_DEPTH = 8;

    private function __construct()
    {
    }

    public static function build(array $query): string
    {
        $encoded = '';

        foreach ($query as $name => $value) {
            self::append($encoded, (string) $name, $value, 0);
        }

        return $encoded;
    }

    private static function append(string &$encoded, string $prefix, mixed $value, int $depth): void
    {
        if ($value === null) {
            return;
        }

        if ($depth > self::MAX_DEPTH) {
            throw new ConfigurationException('A query parameter nests deeper than 8 levels');
        }

        if (is_array($value) && array_is_list($value)) {
            foreach ($value as $item) {
                if ($item !== null) {
                    self::appendPair($encoded, $prefix, self::scalar($item, $prefix));
                }
            }

            return;
        }

        if (is_array($value)) {
            foreach ($value as $key => $nested) {
                self::append($encoded, sprintf('%s[%s]', $prefix, (string) $key), $nested, $depth + 1);
            }

            return;
        }

        self::appendPair($encoded, $prefix, self::scalar($value, $prefix));
    }

    private static function appendPair(string &$encoded, string $name, string $value): void
    {
        $encoded .= ($encoded === '' ? '' : '&') . rawurlencode($name) . '=' . rawurlencode($value);
    }

    private static function scalar(mixed $value, string $name): string
    {
        return match (true) {
            is_bool($value) => $value ? 'true' : 'false',
            is_int($value), is_string($value) => (string) $value,
            is_float($value) && is_finite($value) => self::formatFloat($value),
            $value instanceof \BackedEnum => (string) $value->value,
            default => throw new ConfigurationException(sprintf('The query parameter %s holds a value that a URL cannot carry', $name)),
        };
    }

    private static function formatFloat(float $value): string
    {
        $encoded = json_encode($value);

        return is_string($encoded) ? $encoded : (string) $value;
    }
}
