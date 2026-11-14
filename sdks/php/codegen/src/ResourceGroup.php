<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class ResourceGroup
{
    private array $operations = [];

    public function __construct(
        public readonly string $service,
        public readonly string $resource,
        public readonly string $servicePascal,
        public readonly string $resourcePascal,
    ) {
    }

    public function add(OperationInfo $operation): void
    {
        $this->operations[] = $operation;
    }

    public function operations(): array
    {
        $operations = [];

        foreach ($this->operations as $operation) {
            if ($operation instanceof OperationInfo) {
                $operations[] = $operation;
            }
        }

        return $operations;
    }

    public function className(): string
    {
        return Naming::assertIdentifier(
            $this->servicePascal . Pluralizer::pluralize($this->resourcePascal),
            '/^[A-Z][A-Za-z0-9]*$/D',
            'The class name',
        );
    }
}
