<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support\Server;

final class ReceivedRequest
{
    public function __construct(
        public readonly string $method,
        public readonly string $path,
        public readonly string $query,
        public readonly array $headers,
        public readonly string $body,
    ) {
    }

    public function header(string $name): ?string
    {
        $value = $this->headers[strtolower($name)] ?? null;

        return is_string($value) ? $value : null;
    }
}
