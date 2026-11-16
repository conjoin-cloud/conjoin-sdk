<?php

declare(strict_types=1);

namespace ConjoinCloud;

use ConjoinCloud\Exception\ConfigurationException;

final class OperationRequest
{
    public readonly array $scopes;

    public readonly array $declaredHeaders;

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
        #[\SensitiveParameter] array $declaredHeaders = [],
        #[\SensitiveParameter] public readonly ?Credential $sessionToken = null,
        public readonly CursorLocation $cursor = CursorLocation::Query,
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
    }

    public function withQuery(?array $query): self
    {
        return $this->copy($query, $this->body);
    }

    public function withBody(?array $body): self
    {
        return $this->copy($this->query, $body);
    }

    private function copy(?array $query, ?array $body): self
    {
        return new self(
            $this->method,
            $this->path,
            $query,
            $body,
            $this->bodyType,
            $this->scopes,
            $this->acceptsIdempotencyKey,
            $this->auth,
            $this->bearerToken,
            $this->declaredHeaders,
            $this->sessionToken,
            $this->cursor,
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
