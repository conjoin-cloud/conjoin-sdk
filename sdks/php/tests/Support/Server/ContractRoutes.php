<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support\Server;

use InvalidArgumentException;

final class ContractRoutes
{
    private const MAX_DOCUMENT_BYTES = 67_108_864;

    private const PARAMETER_PATTERN = '/^\{([^{}\/]+)\}$/D';

    private function __construct(private readonly array $templates)
    {
    }

    public static function fromDocument(string $path): self
    {
        $size = is_file($path) ? filesize($path) : false;

        if ($size === false || $size > self::MAX_DOCUMENT_BYTES) {
            throw new InvalidArgumentException(sprintf('%s is missing or larger than 64 MiB', $path));
        }

        $text = file_get_contents($path);
        $document = $text === false ? null : json_decode($text, true, 512, JSON_THROW_ON_ERROR);
        $paths = is_array($document) && is_array($document['paths'] ?? null) ? $document['paths'] : [];
        $templates = [];

        foreach (array_keys($paths) as $template) {
            $templates[] = (string) $template;
        }

        return new self($templates);
    }

    public function match(string $rawPath): ?RouteMatch
    {
        $segments = explode('/', $rawPath);
        $best = null;

        foreach ($this->templates as $template) {
            if (!is_string($template)) {
                continue;
            }

            $candidate = self::matchTemplate($template, $segments);

            if ($candidate !== null && ($best === null || $candidate->literalSegments > $best->literalSegments)) {
                $best = $candidate;
            }
        }

        return $best;
    }

    private static function matchTemplate(string $template, array $segments): ?RouteMatch
    {
        $parts = explode('/', $template);

        if (count($parts) !== count($segments)) {
            return null;
        }

        $params = [];
        $literals = 0;

        foreach ($parts as $index => $part) {
            $segment = $segments[$index] ?? null;

            if (!is_string($segment)) {
                return null;
            }

            if (preg_match(self::PARAMETER_PATTERN, $part, $match) === 1) {
                if ($segment === '') {
                    return null;
                }

                $params[$match[1]] = rawurldecode($segment);
                continue;
            }

            if ($part !== $segment) {
                return null;
            }

            $literals++;
        }

        return new RouteMatch($template, $params, $literals);
    }
}
