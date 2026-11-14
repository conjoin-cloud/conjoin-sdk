<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Response;

use JsonException;

final class JsonBody
{
    private const DEPTH = 512;

    private function __construct()
    {
    }

    public static function decode(string $text): JsonDecodeResult
    {
        if ($text === '') {
            return JsonDecodeResult::empty();
        }

        try {
            return JsonDecodeResult::value(json_decode($text, true, self::DEPTH, JSON_THROW_ON_ERROR | JSON_BIGINT_AS_STRING));
        } catch (JsonException) {
            return JsonDecodeResult::invalid();
        }
    }
}
