<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support\Server;

use InvalidArgumentException;

final class Behaviour
{
    public const ANSWER = 'answer';

    public const DROP_BEFORE_STORE = 'drop-before-store';

    public const DROP_AFTER_STORE = 'drop-after-store';

    public const SLOW = 'slow';

    public const STATUS = 'status';

    public const LARGE = 'large';

    private const KINDS = [self::ANSWER, self::DROP_BEFORE_STORE, self::DROP_AFTER_STORE, self::SLOW, self::STATUS, self::LARGE];

    private const MAX_DELAY_SECONDS = 120.0;

    private const MAX_PADDING_BYTES = 67_108_864;

    private const HEADER_NAME_PATTERN = '/^[A-Za-z0-9-]{1,64}$/D';

    private const HEADER_VALUE_PATTERN = '/^[\x20-\x7e]{0,1024}$/D';

    private function __construct(
        public readonly string $kind,
        public readonly float $delaySeconds = 0.0,
        public readonly int $status = 200,
        public readonly array $headers = [],
        public readonly ?string $body = null,
        public readonly int $paddingBytes = 0,
    ) {
    }

    public static function answer(): self
    {
        return new self(self::ANSWER);
    }

    public static function dropBeforeStore(): self
    {
        return new self(self::DROP_BEFORE_STORE);
    }

    public static function dropAfterStore(): self
    {
        return new self(self::DROP_AFTER_STORE);
    }

    public static function slow(float $delaySeconds): self
    {
        return new self(self::SLOW, delaySeconds: $delaySeconds);
    }

    public static function status(int $status, array $headers = [], mixed $body = null): self
    {
        return new self(self::STATUS, status: $status, headers: $headers, body: json_encode($body ?? ['data' => null], JSON_THROW_ON_ERROR));
    }

    public static function rawStatus(int $status, string $body, array $headers = []): self
    {
        return new self(self::STATUS, status: $status, headers: $headers, body: $body);
    }

    public static function large(int $status, int $paddingBytes): self
    {
        return new self(self::LARGE, status: $status, paddingBytes: $paddingBytes);
    }

    public function toArray(): array
    {
        return [
            'kind' => $this->kind,
            'delaySeconds' => $this->delaySeconds,
            'status' => $this->status,
            'headers' => $this->headers,
            'body' => $this->body,
            'paddingBytes' => $this->paddingBytes,
        ];
    }

    public static function fromArray(mixed $value): self
    {
        if (!is_array($value)) {
            throw new InvalidArgumentException('A behaviour must be an object');
        }

        $kind = $value['kind'] ?? null;
        $delay = $value['delaySeconds'] ?? 0.0;
        $status = $value['status'] ?? 200;
        $body = $value['body'] ?? null;
        $padding = $value['paddingBytes'] ?? 0;

        if (!is_string($kind) || !in_array($kind, self::KINDS, true)) {
            throw new InvalidArgumentException('A behaviour needs a known kind');
        }

        if ((!is_int($delay) && !is_float($delay)) || $delay < 0 || $delay > self::MAX_DELAY_SECONDS) {
            throw new InvalidArgumentException('A behaviour delay must be from 0 to 120 seconds');
        }

        if (!is_int($status) || $status < 100 || $status > 599) {
            throw new InvalidArgumentException('A behaviour status must be from 100 to 599');
        }

        if ($body !== null && !is_string($body)) {
            throw new InvalidArgumentException('A behaviour body must be a string');
        }

        if (!is_int($padding) || $padding < 0 || $padding > self::MAX_PADDING_BYTES) {
            throw new InvalidArgumentException('A behaviour padding must be from 0 to 64 MiB');
        }

        return new self($kind, (float) $delay, $status, self::headersFrom($value['headers'] ?? []), $body, $padding);
    }

    private static function headersFrom(mixed $headers): array
    {
        if (!is_array($headers)) {
            throw new InvalidArgumentException('Behaviour headers must be an object');
        }

        $validated = [];

        foreach ($headers as $name => $value) {
            $isValidName = is_string($name) && preg_match(self::HEADER_NAME_PATTERN, $name) === 1;

            if (!$isValidName || !is_string($value) || preg_match(self::HEADER_VALUE_PATTERN, $value) !== 1) {
                throw new InvalidArgumentException('A behaviour header must be a token name and a printable value');
            }

            $validated[strtolower($name)] = $value;
        }

        return $validated;
    }
}
