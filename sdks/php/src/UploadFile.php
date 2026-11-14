<?php

declare(strict_types=1);

namespace ConjoinCloud;

use ConjoinCloud\Exception\ConfigurationException;

final class UploadFile
{
    private const CONTENT_TYPE_PATTERN = '/^[!#$%&\'*+.^_`|~0-9A-Za-z-]+\/[!#$%&\'*+.^_`|~0-9A-Za-z-]+(;[\x20-\x7e]*)?$/D';

    public function __construct(
        public readonly string $contents,
        public readonly string $filename,
        public readonly string $contentType = 'application/octet-stream',
    ) {
        if ($filename === '' || strlen($filename) > 255 || preg_match('/[\x00-\x1f\x7f]/', $filename) === 1) {
            throw new ConfigurationException('An upload filename must be 1 to 255 bytes without control characters');
        }

        if (preg_match(self::CONTENT_TYPE_PATTERN, $contentType) !== 1) {
            throw new ConfigurationException('An upload content type must be a media type such as text/plain');
        }
    }

    public static function fromPath(string $path, ?string $filename = null, string $contentType = 'application/octet-stream'): self
    {
        if (!is_file($path) || !is_readable($path)) {
            throw new ConfigurationException('The upload path must name a readable file');
        }

        $contents = file_get_contents($path);

        if ($contents === false) {
            throw new ConfigurationException('The upload file could not be read');
        }

        return new self($contents, $filename ?? basename($path), $contentType);
    }

    public function __debugInfo(): array
    {
        return ['filename' => $this->filename, 'contentType' => $this->contentType, 'bytes' => strlen($this->contents)];
    }
}
