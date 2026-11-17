<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class SchemaResolver
{
    private const MAX_REFERENCE_HOPS = 32;

    public function __construct(private readonly array $document)
    {
    }

    public function resolve(mixed $value): array
    {
        $current = $value;

        for ($hop = 0; $hop <= self::MAX_REFERENCE_HOPS; $hop++) {
            if (!is_array($current)) {
                return [];
            }

            $reference = $current['$ref'] ?? null;

            if (!is_string($reference)) {
                return $current;
            }

            $current = $this->lookup($reference);
        }

        throw new CodegenException('A reference chain is longer than 32 hops');
    }

    private function lookup(string $reference): mixed
    {
        if (!str_starts_with($reference, '#/')) {
            throw new CodegenException(sprintf('Only local references are supported, found %s', $reference));
        }

        $node = $this->document;

        foreach (explode('/', substr($reference, 2)) as $segment) {
            $key = str_replace(['~1', '~0'], ['/', '~'], $segment);

            if (!is_array($node) || !array_key_exists($key, $node)) {
                throw new CodegenException(sprintf('Unresolved reference %s', $reference));
            }

            $node = $node[$key];
        }

        return $node;
    }
}
