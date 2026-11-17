<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class ReturnType
{
    private const ACCESSORS = [
        'array' => ['array', 'dataArray'],
        '?array' => ['?array', 'dataNullableArray'],
        'string' => ['string', 'dataString'],
        '?string' => ['?string', 'dataNullableString'],
        'bool' => ['bool', 'dataBool'],
        '?bool' => ['?bool', 'dataNullableBool'],
        'int' => ['int', 'dataInt'],
        '?int' => ['?int', 'dataNullableInt'],
        'number' => ['int|float', 'dataNumber'],
        '?number' => ['int|float|null', 'dataNullableNumber'],
    ];

    private const JSON_TYPE_TO_PHP = [
        'object' => 'array',
        'array' => 'array',
        'string' => 'string',
        'boolean' => 'bool',
        'integer' => 'int',
        'number' => 'number',
    ];

    private const MAX_DEPTH = 16;

    private function __construct(
        public readonly string $phpType,
        public readonly string $accessor,
    ) {
    }

    public static function forData(SchemaResolver $resolver, mixed $schema): self
    {
        $types = self::jsonTypes($resolver, $schema, 0);

        if ($types === null) {
            return new self('mixed', 'data');
        }

        $nullable = false;
        $base = [];

        foreach ($types as $type) {
            if ($type === 'null') {
                $nullable = true;
            } elseif (is_string($type)) {
                $base[$type] = true;
            }
        }

        $only = array_key_first($base);

        if (count($base) !== 1 || !is_string($only)) {
            return new self('mixed', 'data');
        }

        $key = ($nullable ? '?' : '') . $only;
        $accessor = self::ACCESSORS[$key] ?? null;

        return $accessor === null ? new self('mixed', 'data') : new self($accessor[0], $accessor[1]);
    }

    public static function forBody(bool $isObject): self
    {
        return $isObject ? new self('array', 'bodyArray') : new self('mixed', 'body');
    }

    public static function isObjectSchema(SchemaResolver $resolver, mixed $schema): bool
    {
        return self::jsonTypes($resolver, $schema, 0) === ['array'];
    }

    private static function jsonTypes(SchemaResolver $resolver, mixed $raw, int $depth): ?array
    {
        $schema = $resolver->resolve($raw);

        if ($schema === [] || $depth > self::MAX_DEPTH) {
            return null;
        }

        foreach (['oneOf', 'anyOf'] as $keyword) {
            if (is_array($schema[$keyword] ?? null)) {
                return self::branchTypes($resolver, $schema[$keyword], $depth);
            }
        }

        if (is_array($schema['allOf'] ?? null)) {
            return self::allOfTypes($resolver, $schema['allOf'], $depth);
        }

        $declared = $schema['type'] ?? (is_array($schema['properties'] ?? null) ? 'object' : null);
        $names = is_array($declared) ? $declared : [$declared];
        $types = [];

        foreach ($names as $name) {
            if ($name === 'null') {
                $types[] = 'null';
                continue;
            }

            $mapped = is_string($name) ? (self::JSON_TYPE_TO_PHP[$name] ?? null) : null;

            if ($mapped === null) {
                return null;
            }

            $types[] = $mapped;
        }

        return $types === [] ? null : $types;
    }

    private static function branchTypes(SchemaResolver $resolver, array $branches, int $depth): ?array
    {
        $seen = [];
        $types = [];

        foreach ($branches as $branch) {
            $branchTypes = self::jsonTypes($resolver, $branch, $depth + 1);

            if ($branchTypes === null) {
                return null;
            }

            foreach ($branchTypes as $type) {
                if (is_string($type) && !isset($seen[$type])) {
                    $seen[$type] = true;
                    $types[] = $type;
                }
            }
        }

        return $types === [] ? null : $types;
    }

    private static function allOfTypes(SchemaResolver $resolver, array $parts, int $depth): ?array
    {
        foreach ($parts as $part) {
            if (self::jsonTypes($resolver, $part, $depth + 1) !== ['array']) {
                return null;
            }
        }

        return ['array'];
    }
}
