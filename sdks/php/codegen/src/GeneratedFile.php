<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class GeneratedFile
{
    public function __construct(
        public readonly string $name,
        public readonly string $source,
    ) {
    }
}
