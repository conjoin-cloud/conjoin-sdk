<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support\Server;

final class Connection
{
    private const MAX_HEADER_BYTES = 65_536;

    private const MAX_BODY_BYTES = 16_777_216;

    private const REQUEST_LINE_PATTERN = '#^([A-Z]{1,16}) (/[\x21-\x7e]*) HTTP/1\.[01]$#D';

    private const CONTENT_LENGTH_PATTERN = '/^\d{1,9}$/D';

    private string $inbound = '';

    private string $outbound = '';

    private bool $requestTaken = false;

    private bool $isReplyScheduled = false;

    public function __construct(public readonly mixed $socket)
    {
    }

    public function receive(string $bytes): ?ReceivedRequest
    {
        if ($this->requestTaken) {
            return null;
        }

        $this->inbound .= $bytes;

        return $this->parse();
    }

    public function schedule(Reply $reply): void
    {
        $this->requestTaken = true;
        $this->inbound = '';
        $this->outbound = $reply->bytes;
        $this->isReplyScheduled = true;
    }

    public function wantsWrite(): bool
    {
        return $this->isReplyScheduled;
    }

    public function pendingBytes(): string
    {
        return $this->outbound;
    }

    public function consumed(int $bytes): bool
    {
        $this->outbound = substr($this->outbound, $bytes);

        return $this->outbound === '';
    }

    private function parse(): ?ReceivedRequest
    {
        $headerEnd = strpos($this->inbound, "\r\n\r\n");

        if ($headerEnd === false) {
            if (strlen($this->inbound) > self::MAX_HEADER_BYTES) {
                throw new ProtocolError('The request headers exceeded 64 KiB');
            }

            return null;
        }

        $lines = explode("\r\n", substr($this->inbound, 0, $headerEnd));
        $requestLine = array_shift($lines);

        if (preg_match(self::REQUEST_LINE_PATTERN, $requestLine, $match) !== 1) {
            throw new ProtocolError('The request line was malformed');
        }

        $headers = self::headers($lines);

        if (isset($headers['transfer-encoding'])) {
            throw new ProtocolError('The test server reads only Content-Length bodies');
        }

        $declaredLength = $headers['content-length'] ?? '0';

        if (!is_string($declaredLength) || preg_match(self::CONTENT_LENGTH_PATTERN, $declaredLength) !== 1) {
            throw new ProtocolError('The Content-Length was malformed');
        }

        $length = (int) $declaredLength;

        if ($length > self::MAX_BODY_BYTES) {
            throw new ProtocolError('The Content-Length was above 16 MiB');
        }

        $bodyStart = $headerEnd + 4;

        if (strlen($this->inbound) < $bodyStart + $length) {
            return null;
        }

        $this->requestTaken = true;
        $target = $match[2];
        $queryStart = strpos($target, '?');

        return new ReceivedRequest(
            $match[1],
            $queryStart === false ? $target : substr($target, 0, $queryStart),
            $queryStart === false ? '' : substr($target, $queryStart + 1),
            $headers,
            substr($this->inbound, $bodyStart, $length),
        );
    }

    private static function headers(array $lines): array
    {
        $headers = [];

        foreach ($lines as $line) {
            $separator = is_string($line) ? strpos($line, ':') : false;

            if (!is_string($line) || $separator === false || $separator === 0) {
                throw new ProtocolError('A request header was malformed');
            }

            $name = strtolower(substr($line, 0, $separator));
            $value = trim(substr($line, $separator + 1));
            $previous = $headers[$name] ?? null;
            $headers[$name] = is_string($previous) ? $previous . ', ' . $value : $value;
        }

        return $headers;
    }
}
