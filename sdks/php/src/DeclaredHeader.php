<?php

declare(strict_types=1);

namespace ConjoinCloud;

final class DeclaredHeader
{
    public function __construct(
        public readonly string $name,
        public readonly string $argument,
        #[\SensitiveParameter] private readonly string|Credential|null $value,
        public readonly bool $required = false,
        public readonly ?int $minLength = null,
        public readonly ?int $maxLength = null,
        public readonly ?string $pattern = null,
    ) {
    }

    public function value(): ?string
    {
        return $this->value instanceof Credential ? $this->value->reveal() : $this->value;
    }

    public function __debugInfo(): array
    {
        return [
            'name' => $this->name,
            'argument' => $this->argument,
            'required' => $this->required,
        ];
    }
}
