<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class DeclaredHeaderInfo
{
    public function __construct(
        public readonly string $name,
        public readonly string $parameterName,
        public readonly bool $required,
        public readonly bool $credential,
        public readonly ?int $minLength = null,
        public readonly ?int $maxLength = null,
        public readonly ?string $pattern = null,
    ) {
    }
}
