<?php

declare(strict_types=1);

namespace ConjoinCloud;

use ConjoinCloud\Exception\ConfigurationException;

final class OperationRequest
{
    public readonly array $scopes;

    public readonly array $declaredHeaders;

    public readonly ?Credential $bearerToken;

    public function __construct(
        public readonly HttpMethod $method,
        public readonly string $path,
        public readonly ?array $query = null,
        public readonly ?array $body = null,
        public readonly BodyType $bodyType = BodyType::Json,
        array $scopes = [],
        public readonly bool $acceptsIdempotencyKey = false,
        public readonly AuthMode $auth = AuthMode::ClientKey,
        #[\SensitiveParameter] string|Credential|null $bearerToken = null,
        #[\SensitiveParameter] array $declaredHeaders = [],
        #[\SensitiveParameter] public readonly ?Credential $sessionToken = null,
    ) {
        foreach ($scopes as $scope) {
            if (!$scope instanceof Scope) {
                throw new ConfigurationException('Every operation scope must be a Scope');
            }
        }

        foreach ($declaredHeaders as $header) {
            if (!$header instanceof DeclaredHeader) {
                throw new ConfigurationException('Every declared header must be a DeclaredHeader');
            }
        }

        $this->scopes = array_values($scopes);
        $this->declaredHeaders = array_values($declaredHeaders);
        $this->bearerToken = is_string($bearerToken) ? new Credential($bearerToken) : $bearerToken;
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
            $this->declaredHeaders,
            $this->sessionToken,
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
            'declaredHeaders' => $this->declaredHeaders,
        ];
    }
}
