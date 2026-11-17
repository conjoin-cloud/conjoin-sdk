<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support;

use RuntimeException;

final class Attempt
{
    private function __construct(
        public readonly string $method,
        public readonly string $path,
        public readonly string $query,
        public readonly array $headers,
        public readonly string $body,
    ) {
    }

    public static function fromRecord(mixed $record): self
    {
        if (!is_array($record)) {
            throw new RuntimeException('The test server returned an attempt that is not an object');
        }

        $method = $record['method'] ?? null;
        $path = $record['path'] ?? null;
        $query = $record['query'] ?? null;
        $headers = $record['headers'] ?? null;
        $body = is_string($record['body'] ?? null) ? base64_decode($record['body'], true) : false;

        if (!is_string($method) || !is_string($path) || !is_string($query) || !is_array($headers) || $body === false) {
            throw new RuntimeException('The test server returned an attempt without its request line, headers, or body');
        }

        return new self($method, $path, $query, $headers, $body);
    }

    public function header(string $name): ?string
    {
        $value = $this->headers[strtolower($name)] ?? null;

        return is_string($value) ? $value : null;
    }
}
