<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support\Server;

final class Reply
{
    private const NO_CONTENT_STATUS = 204;

    private function __construct(
        public readonly bool $drop,
        public readonly float $delaySeconds,
        public readonly string $bytes,
    ) {
    }

    public static function drop(): self
    {
        return new self(true, 0.0, '');
    }

    public static function json(int $status, mixed $body, array $headers = []): self
    {
        return self::raw($status, json_encode($body, JSON_THROW_ON_ERROR | JSON_UNESCAPED_SLASHES), $headers);
    }

    public static function raw(int $status, string $body, array $headers = []): self
    {
        $lines = [sprintf('HTTP/1.1 %d Test', $status), 'Connection: close'];

        if ($status !== self::NO_CONTENT_STATUS) {
            $lines[] = 'Content-Type: application/json';
            $declaredLength = $headers['content-length'] ?? null;
            $lines[] = sprintf('Content-Length: %s', is_string($declaredLength) ? $declaredLength : strlen($body));
        }

        foreach ($headers as $name => $value) {
            if ($name === 'content-length') {
                continue;
            }
            if (is_string($name) && is_string($value)) {
                $lines[] = sprintf('%s: %s', $name, $value);
            }
        }

        $payload = $status === self::NO_CONTENT_STATUS ? '' : $body;

        return new self(false, 0.0, implode("\r\n", $lines) . "\r\n\r\n" . $payload);
    }

    public function delayed(float $seconds): self
    {
        return new self($this->drop, $seconds, $this->bytes);
    }
}
