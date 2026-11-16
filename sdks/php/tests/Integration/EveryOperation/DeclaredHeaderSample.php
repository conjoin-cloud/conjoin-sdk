<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration\EveryOperation;

final class DeclaredHeaderSample
{
    public function __construct(
        public readonly string $parameter,
        public readonly string $header,
        public readonly string $value,
        public readonly bool $isCredential,
    ) {
    }
}
