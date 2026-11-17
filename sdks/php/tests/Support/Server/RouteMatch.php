<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support\Server;

final class RouteMatch
{
    public function __construct(
        public readonly string $template,
        public readonly int $literalSegments,
    ) {
    }
}
