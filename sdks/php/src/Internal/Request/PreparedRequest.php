<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Request;

use ConjoinCloud\Exception\ConfigurationException;
use ConjoinCloud\HttpMethod;
use GuzzleHttp\Psr7\Request;
use Psr\Http\Message\RequestInterface;

final class PreparedRequest
{
    public function __construct(
        public readonly HttpMethod $method,
        public readonly string $url,
        #[\SensitiveParameter] private readonly array $headers,
        private readonly ?string $body,
        public readonly string $requestId,
    ) {
    }

    public function toPsrRequest(): RequestInterface
    {
        $headers = [];

        foreach ($this->headers as $name => $value) {
            if (is_string($value)) {
                $headers[(string) $name] = $value;
            }
        }

        try {
            return new Request($this->method->value, $this->url, $headers, $this->body);
        } catch (\InvalidArgumentException) {
            throw new ConfigurationException('The request URL or a request header is not valid HTTP');
        }
    }

    public function header(string $name): ?string
    {
        foreach ($this->headers as $headerName => $value) {
            if (is_string($headerName) && strcasecmp($headerName, $name) === 0 && is_string($value)) {
                return $value;
            }
        }

        return null;
    }

    public function __debugInfo(): array
    {
        return ['method' => $this->method, 'url' => $this->url, 'requestId' => $this->requestId];
    }
}
