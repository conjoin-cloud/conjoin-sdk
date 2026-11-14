<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Request;

use ConjoinCloud\BodyType;
use ConjoinCloud\Exception\ConfigurationException;
use ConjoinCloud\UploadFile;
use GuzzleHttp\Psr7\MultipartStream;
use JsonException;

final class EncodedBody
{
    private const JSON_FLAGS = JSON_THROW_ON_ERROR | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRESERVE_ZERO_FRACTION;

    private const JSON_DEPTH = 64;

    private function __construct(
        public readonly string $bytes,
        public readonly string $contentType,
    ) {
    }

    public static function encode(?array $body, BodyType $type): ?self
    {
        if ($body === null) {
            return null;
        }

        return $type === BodyType::Multipart ? self::multipart($body) : self::json($body);
    }

    private static function json(array $body): self
    {
        try {
            $bytes = $body === [] ? '{}' : json_encode($body, self::JSON_FLAGS, self::JSON_DEPTH);
        } catch (JsonException) {
            throw new ConfigurationException('The request body holds a value that JSON cannot encode, such as invalid UTF-8');
        }

        return new self($bytes, 'application/json');
    }

    private static function multipart(array $body): self
    {
        $elements = [];

        foreach ($body as $name => $value) {
            self::appendPart($elements, (string) $name, $value, true);
        }

        $boundary = 'conjoin-' . bin2hex(random_bytes(16));

        try {
            $bytes = (string) new MultipartStream($elements, $boundary);
        } catch (\InvalidArgumentException) {
            throw new ConfigurationException('The multipart request body holds a field that cannot be encoded');
        }

        return new self($bytes, sprintf('multipart/form-data; boundary=%s', $boundary));
    }

    private static function appendPart(array &$elements, string $name, mixed $value, bool $expandLists): void
    {
        if ($value === null) {
            return;
        }

        if ($value instanceof UploadFile) {
            $elements[] = [
                'name' => $name,
                'contents' => $value->contents,
                'filename' => $value->filename,
                'headers' => ['Content-Type' => $value->contentType],
            ];

            return;
        }

        if ($expandLists && is_array($value) && array_is_list($value)) {
            foreach ($value as $item) {
                self::appendPart($elements, $name, $item, false);
            }

            return;
        }

        $elements[] = ['name' => $name, 'contents' => self::fieldText($value, $name)];
    }

    private static function fieldText(mixed $value, string $name): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }

        if (is_string($value) || is_int($value) || (is_float($value) && is_finite($value))) {
            return (string) $value;
        }

        try {
            return json_encode($value, self::JSON_FLAGS, self::JSON_DEPTH);
        } catch (JsonException) {
            throw new ConfigurationException(sprintf('The multipart field %s holds a value that JSON cannot encode', $name));
        }
    }
}
