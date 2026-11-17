<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class SuccessShape
{
    public function __construct(
        public readonly ResponseKind $kind,
        public readonly ReturnType $returnType,
    ) {
    }
}
