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
        public readonly float $receivedAt,
        public readonly ?string $pathTemplate,
        public readonly array $pathParams,
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
        $receivedAt = $record['receivedAt'] ?? null;
        $template = $record['pathTemplate'] ?? null;
        $params = $record['pathParams'] ?? [];

        if (!is_string($method) || !is_string($path) || !is_string($query) || !is_array($headers) || $body === false) {
            throw new RuntimeException('The test server returned an attempt without its request line, headers, or body');
        }

        if ((!is_float($receivedAt) && !is_int($receivedAt)) || ($template !== null && !is_string($template)) || !is_array($params)) {
            throw new RuntimeException('The test server returned an attempt without its time or route');
        }

        return new self($method, $path, $query, $headers, $body, (float) $receivedAt, $template, $params);
    }

    public function header(string $name): ?string
    {
        $value = $this->headers[strtolower($name)] ?? null;

        return is_string($value) ? $value : null;
    }

    public function queryValues(): array
    {
        parse_str($this->query, $values);

        return $values;
    }

    public function jsonBody(): mixed
    {
        return json_decode($this->body, true, 512, JSON_THROW_ON_ERROR);
    }
}
