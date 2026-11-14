<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration\EveryOperation;

use ConjoinCloud\ConjoinClient;
use ReflectionClass;
use ReflectionMethod;
use ReflectionNamedType;
use RuntimeException;

final class GeneratedMethod
{
    private const GENERATED_PARAMETERS = ['data', 'query', 'options'];

    private function __construct(
        public readonly string $label,
        private readonly ReflectionMethod $method,
        public readonly int $pathParameterCount,
        public readonly bool $hasData,
        public readonly bool $hasQuery,
        public readonly bool $queryRequired,
    ) {
    }

    public static function discover(string $directory, string $namespace): array
    {
        $files = glob($directory . '/*.php');
        $methods = [];

        foreach ($files === false ? [] : $files as $file) {
            $className = $namespace . '\\' . basename($file, '.php');

            if (!class_exists($className)) {
                throw new RuntimeException(sprintf('%s does not declare %s', $file, $className));
            }

            foreach ((new ReflectionClass($className))->getMethods(ReflectionMethod::IS_PUBLIC) as $method) {
                $isOperation = !str_starts_with($method->getName(), '__') && $method->getDeclaringClass()->getName() === $className;

                if ($isOperation) {
                    $methods[] = self::fromReflection($method);
                }
            }
        }

        return $methods;
    }

    public function invoke(ConjoinClient $client, string $scimToken, array $arguments): mixed
    {
        $class = $this->method->getDeclaringClass();
        $constructor = $class->getConstructor();
        $instance = $constructor !== null && $constructor->getNumberOfParameters() === 2
            ? $class->newInstance($client, $scimToken)
            : $class->newInstance($client);

        return $this->method->invokeArgs($instance, array_values($arguments));
    }

    private static function fromReflection(ReflectionMethod $method): self
    {
        $pathParameterCount = 0;
        $hasData = false;
        $hasQuery = false;
        $queryRequired = false;

        foreach ($method->getParameters() as $parameter) {
            $name = $parameter->getName();
            $type = $parameter->getType();

            if (!in_array($name, self::GENERATED_PARAMETERS, true)) {
                if (!$type instanceof ReflectionNamedType || $type->getName() !== 'string') {
                    throw new RuntimeException(sprintf('%s takes the path parameter %s as a type other than string', $method->getName(), $name));
                }

                $pathParameterCount++;
            }

            $hasData = $hasData || $name === 'data';
            $hasQuery = $hasQuery || $name === 'query';
            $queryRequired = $queryRequired || ($name === 'query' && $type !== null && !$type->allowsNull());
        }

        return new self(
            sprintf('%s::%s', $method->getDeclaringClass()->getShortName(), $method->getName()),
            $method,
            $pathParameterCount,
            $hasData,
            $hasQuery,
            $queryRequired,
        );
    }
}
