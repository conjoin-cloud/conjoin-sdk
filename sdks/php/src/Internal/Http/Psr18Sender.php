<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Http;

use ConjoinCloud\Exception\CancelledException;
use ConjoinCloud\Exception\NetworkException;
use ConjoinCloud\Internal\Request\PreparedRequest;
use Psr\Http\Client\ClientExceptionInterface;
use Psr\Http\Client\ClientInterface;
use Psr\Http\Message\StreamInterface;

final class Psr18Sender implements HttpSender
{
    private const READ_CHUNK_BYTES = 65_536;

    public function __construct(private readonly ClientInterface $client)
    {
    }

    public function send(#[\SensitiveParameter] PreparedRequest $request, AttemptLimits $limits): ReceivedResponse
    {
        if ($limits->isCancelled()) {
            throw new CancelledException($request->requestId);
        }

        try {
            $response = $this->client->sendRequest($request->toPsrRequest());
        } catch (ClientExceptionInterface) {
            throw new NetworkException('The HTTP client could not complete the request', $request->requestId);
        }

        $stream = $response->getBody();
        $limit = $limits->bodyLimitFor($response->getStatusCode());

        try {
            $body = $this->readAtMost($stream, $limit + 1);
        } catch (\RuntimeException) {
            throw new NetworkException('The connection failed while the response arrived', $request->requestId);
        } finally {
            $stream->close();
        }

        $truncated = strlen($body) > $limit;

        return ReceivedResponse::fromPsr($response, $truncated ? substr($body, 0, $limit) : $body, $truncated);
    }

    private function readAtMost(StreamInterface $stream, int $maxBytes): string
    {
        $body = '';

        while (!$stream->eof() && strlen($body) < $maxBytes) {
            $chunk = $stream->read(min(self::READ_CHUNK_BYTES, $maxBytes - strlen($body)));

            if ($chunk === '') {
                break;
            }

            $body .= $chunk;
        }

        return $body;
    }
}
