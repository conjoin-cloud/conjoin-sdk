<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration\EveryOperation;

use RuntimeException;

final class DocumentOperations
{
    private const HTTP_METHODS = ['get', 'post', 'put', 'patch', 'delete'];

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

    public function keys(): array
    {
        $keys = [];
        $paths = is_array($this->document['paths'] ?? null) ? $this->document['paths'] : [];

        foreach ($paths as $template => $item) {
            foreach (self::HTTP_METHODS as $method) {
                if (is_array($item) && is_array($item[$method] ?? null)) {
                    $keys[] = strtoupper($method) . ' ' . (string) $template;
                }
            }
        }

        return $keys;
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

    public function parameters(array $operation, string $location): array
    {
        $parameters = [];

        foreach (is_array($operation['parameters'] ?? null) ? $operation['parameters'] : [] as $raw) {
            $parameter = $this->resolve($raw);

            if (($parameter['in'] ?? null) === $location) {
                $parameters[] = $parameter;
            }
        }

        return $parameters;
    }

    public function declaresHeader(array $operation, string $name): bool
    {
        foreach ($this->parameters($operation, 'header') as $parameter) {
            if (is_array($parameter) && is_string($parameter['name'] ?? null) && strtolower($parameter['name']) === $name) {
                return true;
            }
        }

        return false;
    }

    public function requestIdPattern(array $operation): string
    {
        foreach ($this->parameters($operation, 'header') as $parameter) {
            $isRequestId = is_array($parameter) && is_string($parameter['name'] ?? null) && strtolower($parameter['name']) === 'conjoin-request-id';
            $pattern = $isRequestId ? ($this->resolve($parameter['schema'] ?? null)['pattern'] ?? null) : null;

            if (is_string($pattern)) {
                return '/' . str_replace('/', '\\/', $pattern) . '/D';
            }
        }

        throw new RuntimeException('The operation declares no Conjoin-Request-Id pattern');
    }

    public function securityScheme(array $operation): ?string
    {
        $security = is_array($operation['security'] ?? null) ? $operation['security'] : [];
        $requirement = $security[0] ?? null;
        $scheme = is_array($requirement) ? array_key_first($requirement) : null;

        return is_string($scheme) ? $scheme : null;
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

    public function requestBodyType(array $operation): ?string
    {
        if (!isset($operation['requestBody'])) {
            return null;
        }

        $content = $this->resolve($operation['requestBody'])['content'] ?? null;
        $type = is_array($content) ? array_key_first($content) : null;

        if (!is_string($type)) {
            throw new RuntimeException('The operation declares a request body without content');
        }

        return $type;
    }

    public function requestBodySchema(array $operation): mixed
    {
        $type = $this->requestBodyType($operation);
        $content = $type === null ? null : ($this->resolve($operation['requestBody'] ?? null)['content'] ?? null);
        $media = is_array($content) ? ($content[$type] ?? null) : null;

        return is_array($media) ? ($media['schema'] ?? null) : null;
    }

    public function schemaProperties(mixed $schema): ?array
    {
        $properties = $this->resolve($schema)['properties'] ?? null;

        return is_array($properties) ? $properties : null;
    }
}
