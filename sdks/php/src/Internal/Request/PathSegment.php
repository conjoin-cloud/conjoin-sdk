<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Request;

use ConjoinCloud\Exception\ConfigurationException;

final class PathSegment
{
    private const MAX_BYTES = 1_024;

    private function __construct()
    {
    }

    public static function encode(string $value): string
    {
        if ($value === '' || $value === '.' || $value === '..' || strlen($value) > self::MAX_BYTES) {
            throw new ConfigurationException('A path parameter must be a non-empty ID of at most 1024 bytes');
        }

        return rawurlencode($value);
    }
}
