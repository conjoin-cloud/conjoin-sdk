<?php

declare(strict_types=1);

namespace ConjoinCloud\Response;

use ConjoinCloud\Exception\ResponseException;

final class ApiResponse
{
    public function __construct(
        public readonly int $status,
        public readonly array $headers,
        public readonly ?string $requestId,
        public readonly mixed $body,
    ) {
    }

    public function header(string $name): ?string
    {
        $values = $this->headers[strtolower($name)] ?? null;

        return is_array($values) && isset($values[0]) && is_string($values[0]) ? $values[0] : null;
    }

    public function bodyArray(): array
    {
        if (!is_array($this->body)) {
            throw $this->unexpected('The response body was not a JSON object');
        }

        return $this->body;
    }

    public function data(): mixed
    {
        $body = $this->bodyArray();

        if (!array_key_exists('data', $body)) {
            throw $this->unexpected('The response body held no data field');
        }

        return $body['data'];
    }

    public function dataArray(): array
    {
        $data = $this->data();

        return is_array($data) ? $data : throw $this->mismatch('an object or an array');
    }

    public function dataNullableArray(): ?array
    {
        $data = $this->data();

        return $data === null || is_array($data) ? $data : throw $this->mismatch('an object, an array, or null');
    }

    public function dataString(): string
    {
        $data = $this->data();

        return is_string($data) ? $data : throw $this->mismatch('a string');
    }

    public function dataNullableString(): ?string
    {
        $data = $this->data();

        return $data === null || is_string($data) ? $data : throw $this->mismatch('a string or null');
    }

    public function dataBool(): bool
    {
        $data = $this->data();

        return is_bool($data) ? $data : throw $this->mismatch('a boolean');
    }

    public function dataNullableBool(): ?bool
    {
        $data = $this->data();

        return $data === null || is_bool($data) ? $data : throw $this->mismatch('a boolean or null');
    }

    public function dataInt(): int
    {
        $data = $this->data();

        return is_int($data) ? $data : throw $this->mismatch('an integer');
    }

    public function dataNullableInt(): ?int
    {
        $data = $this->data();

        return $data === null || is_int($data) ? $data : throw $this->mismatch('an integer or null');
    }

    public function dataNumber(): int|float
    {
        $data = $this->data();

        return is_int($data) || is_float($data) ? $data : throw $this->mismatch('a number');
    }

    public function dataNullableNumber(): int|float|null
    {
        $data = $this->data();

        return $data === null || is_int($data) || is_float($data) ? $data : throw $this->mismatch('a number or null');
    }

    private function mismatch(string $expected): ResponseException
    {
        return $this->unexpected(sprintf('The response data was not %s', $expected));
    }

    private function unexpected(string $message): ResponseException
    {
        return new ResponseException($message, $this->status, $this->requestId);
    }
}
