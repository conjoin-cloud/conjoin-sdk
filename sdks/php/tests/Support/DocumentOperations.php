<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support;

use RuntimeException;

final class DocumentOperations
{
    private const MAX_REFERENCE_HOPS = 32;

    private const NO_CONTENT_STATUS = 204;

    private function __construct(public readonly array $document)
    {
    }

    public static function load(string $path): self
    {
        $text = file_get_contents($path);
        $document = $text === false ? null : json_decode($text, true, 512, JSON_THROW_ON_ERROR);

        if (!is_array($document) || !is_array($document['paths'] ?? null)) {
            throw new RuntimeException(sprintf('%s has no paths object', $path));
        }

        return new self($document);
    }

    public function operation(string $method, string $template): array
    {
        $paths = is_array($this->document['paths'] ?? null) ? $this->document['paths'] : [];
        $item = is_array($paths[$template] ?? null) ? $paths[$template] : [];
        $operation = $item[strtolower($method)] ?? null;

        if (!is_array($operation)) {
            throw new RuntimeException(sprintf('The document has no operation %s %s', $method, $template));
        }

        return $operation;
    }

    public function resolve(mixed $value): array
    {
        for ($hop = 0; $hop < self::MAX_REFERENCE_HOPS; $hop++) {
            if (!is_array($value)) {
                return [];
            }

            $reference = $value['$ref'] ?? null;

            if (!is_string($reference)) {
                return $value;
            }

            $value = $this->document;

            foreach (explode('/', (string) preg_replace('#^\#/#', '', $reference)) as $key) {
                $value = is_array($value) ? ($value[$key] ?? null) : null;
            }
        }

        throw new RuntimeException('A schema reference chain is longer than 32 hops');
    }

    public function successStatus(array $operation): int
    {
        $responses = is_array($operation['responses'] ?? null) ? $operation['responses'] : [];

        foreach (array_keys($responses) as $status) {
            if (str_starts_with((string) $status, '2')) {
                return (int) $status;
            }
        }

        throw new RuntimeException('The operation declares no success response');
    }

    public function successSchema(array $operation): ?array
    {
        $status = $this->successStatus($operation);

        if ($status === self::NO_CONTENT_STATUS) {
            return null;
        }

        $responses = is_array($operation['responses'] ?? null) ? $operation['responses'] : [];
        $content = $this->resolve($responses[(string) $status] ?? null)['content'] ?? null;
        $media = is_array($content) ? ($content['application/json'] ?? null) : null;
        $schema = is_array($media) ? ($media['schema'] ?? null) : null;

        return is_array($schema) ? $schema : null;
    }
}
