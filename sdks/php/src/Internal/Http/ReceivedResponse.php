<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Http;

use Psr\Http\Message\ResponseInterface;

final class ReceivedResponse
{
    private function __construct(
        public readonly int $status,
        public readonly array $headers,
        public readonly string $body,
        public readonly bool $bodyTruncated,
    ) {
    }

    public static function fromPsr(ResponseInterface $response, string $body, bool $bodyTruncated): self
    {
        $headers = [];

        foreach ($response->getHeaders() as $name => $values) {
            $headers[strtolower((string) $name)] = array_values($values);
        }

        return new self($response->getStatusCode(), $headers, $body, $bodyTruncated);
    }

    public function header(string $name): ?string
    {
        $values = $this->headers[strtolower($name)] ?? [];

        if (!is_array($values) || $values === []) {
            return null;
        }

        $first = $values[0];

        return is_string($first) ? $first : null;
    }

    public function isSuccess(): bool
    {
        return $this->status >= 200 && $this->status < 300;
    }
}
