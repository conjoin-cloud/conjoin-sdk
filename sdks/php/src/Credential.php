<?php

declare(strict_types=1);

namespace ConjoinCloud;

use Closure;
use LogicException;

final class Credential implements \JsonSerializable, \Stringable
{
    private const REDACTED = '[redacted]';

    private readonly Closure $read;

    public function __construct(#[\SensitiveParameter] string $value)
    {
        $this->read = static fn (): string => $value;
    }

    public function reveal(): string
    {
        $value = ($this->read)();

        return is_string($value) ? $value : throw new LogicException('A Credential holds a value that is not a string');
    }

    public function __toString(): string
    {
        return self::REDACTED;
    }

    public function jsonSerialize(): string
    {
        return self::REDACTED;
    }

    public function __debugInfo(): array
    {
        return ['value' => self::REDACTED];
    }

    public function __serialize(): array
    {
        throw new LogicException('A Credential cannot be serialized');
    }

    public function __unserialize(array $data): void
    {
        throw new LogicException('A Credential cannot be unserialized');
    }
}
