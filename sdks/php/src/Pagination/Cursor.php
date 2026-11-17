<?php

declare(strict_types=1);

namespace ConjoinCloud\Pagination;

final class Cursor
{
    public function __construct(
        public readonly ?string $prev,
        public readonly ?string $next,
    ) {
    }

    public static function fromBody(mixed $value): self
    {
        if (!is_array($value)) {
            return new self(null, null);
        }

        return new self(self::token($value['prev'] ?? null), self::token($value['next'] ?? null));
    }

    private static function token(mixed $value): ?string
    {
        return is_string($value) && $value !== '' ? $value : null;
    }
}
