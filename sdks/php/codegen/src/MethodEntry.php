<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class MethodEntry
{
    public function __construct(
        public readonly string $name,
        public readonly OperationInfo $operation,
    ) {
    }
}
