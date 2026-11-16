<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration\EveryOperation;

use ConjoinCloud\UploadFile;
use stdClass;

final class SchemaSampler
{
    private const MAX_DEPTH = 12;

    private const BASE_TEXT = 'samplevalue';

    private const FORMAT_SAMPLES = [
        'uri' => 'https://hooks.example.com/conjoin',
        'email' => 'billing.owner@example.com',
        'date-time' => '2026-11-14T10:00:00.000Z',
        'date' => '2026-11-14',
        'uuid' => '0198f0f7-5d0b-4b4a-8d5a-cf5693f0b2c1',
    ];

    private const PATTERN_SAMPLES = [
        '^[0-9a-f]+$' => '9f86d081884c7d65',
    ];

    public function __construct(private readonly DocumentOperations $document)
    {
    }

    public function sample(mixed $schema): mixed
    {
        return $this->sampleAt($schema, 0);
    }

    private function sampleAt(mixed $raw, int $depth): mixed
    {
        $schema = $this->document->resolve($raw);

        if ($schema === [] || $depth > self::MAX_DEPTH) {
            return null;
        }

        if (array_key_exists('const', $schema)) {
            return $schema['const'];
        }

        if (is_array($schema['enum'] ?? null) && $schema['enum'] !== []) {
            $values = array_values(array_filter($schema['enum'], static fn (mixed $value): bool => $value !== null));

            return $values[0] ?? null;
        }

        foreach (['oneOf', 'anyOf'] as $keyword) {
            if (is_array($schema[$keyword] ?? null)) {
                return $this->firstBranch($schema[$keyword], $depth);
            }
        }

        if (is_array($schema['allOf'] ?? null)) {
            return $this->mergedParts($schema['allOf'], $depth);
        }

        $type = $schema['type'] ?? null;

        if (is_array($type)) {
            $named = array_values(array_filter($type, static fn (mixed $name): bool => $name !== 'null'));
            $type = $named[0] ?? 'null';
        }

        return $this->sampleType($schema, $type, $depth);
    }

    private function firstBranch(array $branches, int $depth): mixed
    {
        foreach ($branches as $branch) {
            $sample = $this->sampleAt($branch, $depth + 1);

            if ($sample !== null) {
                return $sample;
            }
        }

        return null;
    }

    private function mergedParts(array $parts, int $depth): mixed
    {
        $merged = [];

        foreach ($parts as $part) {
            $sample = $this->sampleAt($part, $depth + 1);

            if ($sample instanceof stdClass) {
                continue;
            }

            if (!is_array($sample)) {
                return $sample;
            }

            $merged = array_merge($merged, $sample);
        }

        return $merged === [] ? new stdClass() : $merged;
    }

    private function sampleType(array $schema, mixed $type, int $depth): mixed
    {
        return match (true) {
            $type === 'string' && ($schema['format'] ?? null) === 'binary' => new UploadFile('billing statement contents', 'statement.txt', 'text/plain'),
            $type === 'string' => $this->sampleString($schema),
            $type === 'integer' => (int) ceil($this->sampleNumber($schema)),
            $type === 'number' => $this->sampleNumber($schema),
            $type === 'boolean' => true,
            $type === 'null' => null,
            $type === 'array' => $this->sampleList($schema, $depth),
            $type === 'object' || is_array($schema['properties'] ?? null) => $this->sampleObject($schema, $depth),
            default => 'sample',
        };
    }

    private function sampleList(array $schema, int $depth): array
    {
        $minItems = $schema['minItems'] ?? null;
        $count = is_int($minItems) && $minItems > 0 ? $minItems : 1;
        $items = [];

        for ($index = 0; $index < $count; $index++) {
            $items[] = $this->sampleAt($schema['items'] ?? null, $depth + 1);
        }

        return $items;
    }

    private function sampleObject(array $schema, int $depth): array|stdClass
    {
        $properties = is_array($schema['properties'] ?? null) ? $schema['properties'] : [];
        $required = is_array($schema['required'] ?? null) ? $schema['required'] : array_keys($properties);
        $sample = [];

        foreach ($required as $name) {
            $key = (string) (is_string($name) || is_int($name) ? $name : '');
            $sample[$key] = $this->sampleAt($properties[$key] ?? ['type' => 'string'], $depth + 1);
        }

        return $sample === [] ? new stdClass() : $sample;
    }

    private function sampleString(array $schema): string
    {
        $format = $schema['format'] ?? null;

        if (is_string($format) && isset(self::FORMAT_SAMPLES[$format])) {
            return self::FORMAT_SAMPLES[$format];
        }

        $pattern = $schema['pattern'] ?? null;

        if (is_string($pattern) && isset(self::PATTERN_SAMPLES[$pattern])) {
            return self::PATTERN_SAMPLES[$pattern];
        }

        $minLength = is_int($schema['minLength'] ?? null) ? $schema['minLength'] : 1;
        $maxLength = is_int($schema['maxLength'] ?? null) ? $schema['maxLength'] : max($minLength, 16);
        $text = str_repeat(self::BASE_TEXT, intdiv(max($minLength, 1), strlen(self::BASE_TEXT)) + 1);

        return substr($text, 0, max(min(strlen(self::BASE_TEXT), $maxLength), $minLength));
    }

    private function sampleNumber(array $schema): float
    {
        $minimum = $schema['minimum'] ?? null;
        $exclusiveMinimum = $schema['exclusiveMinimum'] ?? null;
        $maximum = $schema['maximum'] ?? null;
        $value = match (true) {
            is_int($minimum) || is_float($minimum) => (float) $minimum,
            is_int($exclusiveMinimum) || is_float($exclusiveMinimum) => (float) $exclusiveMinimum + 1,
            default => 1.0,
        };

        if ((is_int($maximum) || is_float($maximum)) && $value > $maximum) {
            $value = (float) $maximum;
        }

        return $value;
    }
}
