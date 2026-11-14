<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class MethodNames
{
    private const IDENTIFIER_PATTERN = '/^[a-z][A-Za-z0-9]*$/D';

    private function __construct()
    {
    }

    public static function resolve(ResourceGroup $group): array
    {
        $operations = [];
        $names = [];

        foreach ($group->operations() as $operation) {
            if (!$operation instanceof OperationInfo) {
                throw new CodegenException(sprintf('%s holds an entry that is not an operation', $group->className()));
            }

            $operations[] = $operation;
            $names[] = Naming::methodName($operation->operationId, $group->servicePascal, $group->resourcePascal);
        }

        $counts = array_count_values($names);
        $pluralResource = Pluralizer::pluralize($group->resourcePascal);

        foreach ($operations as $index => $operation) {
            $name = $names[$index];

            if (($counts[$name] ?? 0) <= 1) {
                continue;
            }

            if ($operation->responseKind === ResponseKind::ListPage) {
                $names[$index] = $name === 'read' || $name === 'get' ? 'list' : 'list' . ucfirst($name);
            } elseif (str_contains($operation->operationId, $pluralResource)) {
                $names[$index] = Pluralizer::pluralize($name);
            }
        }

        $finalCounts = array_count_values($names);

        foreach ($operations as $index => $operation) {
            if (($finalCounts[$names[$index]] ?? 0) > 1) {
                $names[$index] = lcfirst($operation->operationId);
            }
        }

        $seen = [];
        $resolved = [];

        foreach ($operations as $index => $operation) {
            $name = Naming::assertIdentifier($names[$index], self::IDENTIFIER_PATTERN, 'The method name');
            $folded = strtolower($name);

            if (isset($seen[$folded])) {
                throw new CodegenException(sprintf('Two operations in %s both generate the method %s', $group->className(), $name));
            }

            $seen[$folded] = true;
            $resolved[] = new MethodEntry($name, $operation);
        }

        return $resolved;
    }
}
