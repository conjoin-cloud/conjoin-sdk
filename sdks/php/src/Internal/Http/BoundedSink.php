<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Http;

use GuzzleHttp\Psr7\Utils;
use Psr\Http\Message\StreamInterface;

final class BoundedSink implements StreamInterface
{
    private readonly StreamInterface $inner;

    private int $written = 0;

    private bool $overflowed = false;

    public function __construct(private int $limit)
    {
        $this->inner = Utils::streamFor('');
    }

    public function limitTo(int $limit): void
    {
        $this->limit = $limit;
    }

    public function overflowed(): bool
    {
        return $this->overflowed;
    }

    public function contents(): string
    {
        $this->inner->rewind();

        return $this->inner->getContents();
    }

    public function write(string $string): int
    {
        $room = $this->limit - $this->written;

        if (strlen($string) > $room) {
            $this->overflowed = true;
            $accepted = $room > 0 ? $this->inner->write(substr($string, 0, $room)) : 0;
            $this->written += $accepted;

            return $accepted;
        }

        $accepted = $this->inner->write($string);
        $this->written += $accepted;

        return $accepted;
    }

    public function __toString(): string
    {
        return $this->inner->__toString();
    }

    public function close(): void
    {
        $this->inner->close();
    }

    public function detach(): mixed
    {
        return $this->inner->detach();
    }

    public function getSize(): ?int
    {
        return $this->inner->getSize();
    }

    public function tell(): int
    {
        return $this->inner->tell();
    }

    public function eof(): bool
    {
        return $this->inner->eof();
    }

    public function isSeekable(): bool
    {
        return $this->inner->isSeekable();
    }

    public function seek(int $offset, int $whence = SEEK_SET): void
    {
        $this->inner->seek($offset, $whence);
    }

    public function rewind(): void
    {
        $this->inner->rewind();
    }

    public function isWritable(): bool
    {
        return $this->inner->isWritable();
    }

    public function isReadable(): bool
    {
        return $this->inner->isReadable();
    }

    public function read(int $length): string
    {
        return $this->inner->read($length);
    }

    public function getContents(): string
    {
        return $this->inner->getContents();
    }

    public function getMetadata(?string $key = null): mixed
    {
        return $this->inner->getMetadata($key);
    }
}
