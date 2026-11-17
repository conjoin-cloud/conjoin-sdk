<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Response;

final class JsonDecodeResult
{
    private function __construct(
        public readonly bool $isValid,
        public readonly bool $isEmpty,
        public readonly mixed $value,
    ) {
    }

    public static function value(mixed $value): self
    {
        return new self(true, false, $value);
    }

    public static function empty(): self
    {
        return new self(true, true, null);
    }

    public static function invalid(): self
    {
        return new self(false, false, null);
    }
}
