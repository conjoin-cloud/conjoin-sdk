<?php

declare(strict_types=1);

namespace ConjoinCloud\Exception;

final class FieldError
{
    public function __construct(
        public readonly string $path,
        public readonly string $message,
    ) {
    }
}
