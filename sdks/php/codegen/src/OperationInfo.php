<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class OperationInfo
{
    public function __construct(
        public readonly string $operationId,
        public readonly string $httpMethod,
        public readonly string $path,
        public readonly array $pathParameters,
        public readonly bool $hasRequestBody,
        public readonly bool $requestBodyRequired,
        public readonly bool $multipart,
        public readonly ResponseKind $responseKind,
        public readonly ReturnType $returnType,
        public readonly bool $hasQuery,
        public readonly bool $queryRequired,
        public readonly array $scopes,
        public readonly bool $acceptsIdempotencyKey,
        public readonly AuthKind $auth,
    ) {
    }
}
