<?php

declare(strict_types=1);

namespace ConjoinCloud;

use ConjoinCloud\Exception\ConfigurationException;

final class OperationRequest
{
    public readonly array $scopes;

    public function __construct(
        public readonly HttpMethod $method,
        public readonly string $path,
        public readonly ?array $query = null,
        public readonly ?array $body = null,
        public readonly BodyType $bodyType = BodyType::Json,
        array $scopes = [],
        public readonly bool $acceptsIdempotencyKey = false,
        public readonly AuthMode $auth = AuthMode::ClientKey,
        #[\SensitiveParameter] public readonly ?string $bearerToken = null,
    ) {
        foreach ($scopes as $scope) {
            if (!$scope instanceof Scope) {
                throw new ConfigurationException('Every operation scope must be a Scope');
            }
        }

        $this->scopes = array_values($scopes);
    }

    public function withQuery(?array $query): self
    {
        return new self(
            $this->method,
            $this->path,
            $query,
            $this->body,
            $this->bodyType,
            $this->scopes,
            $this->acceptsIdempotencyKey,
            $this->auth,
            $this->bearerToken,
        );
    }

    public function __debugInfo(): array
    {
        return [
            'method' => $this->method,
            'path' => $this->path,
            'scopes' => $this->scopes,
            'acceptsIdempotencyKey' => $this->acceptsIdempotencyKey,
            'auth' => $this->auth,
        ];
    }
}
