<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class Naming
{
    private function __construct()
    {
    }

    public static function pascal(string $value): string
    {
        $words = preg_split('/[\s\-_]+/', $value);

        if ($words === false) {
            throw new CodegenException(sprintf('Cannot split %s into words', $value));
        }

        return implode('', array_map(static fn (string $word): string => ucfirst($word), $words));
    }

    public static function camel(string $value): string
    {
        return lcfirst(self::pascal($value));
    }

    public static function kebab(string $value): string
    {
        $spaced = (string) preg_replace('/([a-z])([A-Z])/', '$1-$2', $value);

        return strtolower((string) preg_replace('/[\s_]+/', '-', $spaced));
    }

    public static function methodName(string $operationId, string $servicePascal, string $resourcePascal): string
    {
        $serviceResource = $servicePascal . $resourcePascal;
        $candidates = [
            Pluralizer::pluralize($serviceResource),
            $serviceResource,
            Pluralizer::pluralize($resourcePascal),
            $resourcePascal,
            $servicePascal,
        ];

        foreach ($candidates as $token) {
            $index = strpos($operationId, $token);

            if ($index === false) {
                continue;
            }

            $result = substr($operationId, 0, $index) . substr($operationId, $index + strlen($token));

            if ($result !== '') {
                return lcfirst($result);
            }
        }

        return $operationId;
    }

    public static function pathParameters(string $path): array
    {
        if (str_contains($path, '{{')) {
            throw new CodegenException(sprintf('%s uses a double-brace path parameter', $path));
        }

        preg_match_all('/\{(\w+)\}/', $path, $matches);
        $names = [];

        foreach ($matches[1] as $name) {
            $names[] = $name;
        }

        return $names;
    }

    public static function assertIdentifier(string $value, string $pattern, string $what): string
    {
        if (preg_match($pattern, $value) !== 1) {
            throw new CodegenException(sprintf('%s %s is not a valid PHP identifier', $what, $value));
        }

        return $value;
    }
}
