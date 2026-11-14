<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Exception\ApiException;
use ConjoinCloud\Exception\NetworkException;
use ConjoinCloud\Exception\ResponseException;
use ConjoinCloud\Tests\Support\Server\Behaviour;
use ConjoinCloud\Tests\Support\ServerTestCase;
use GuzzleHttp\Client;

final class Psr18ClientTest extends ServerTestCase
{
    public function testTruncatedRefusalsFromTheCallerClientAreNotRetried(): void
    {
        foreach ([400, 501] as $status) {
            $this->server()->reset();
            $this->server()->queue(Behaviour::rawStatus($status, '{"error":', ['content-length' => '1000']));
            $error = self::caught(fn () => self::read($this->psr18Client()));
            self::assertInstanceOf(ApiException::class, $error);
            self::assertSame($status, $error->getStatus());
            self::assertSame(1, $this->server()->attemptCount());
        }
    }

    private function psr18Client(int $maxRetries = 3, int $maxResponseBytes = 16_777_216): ConjoinClient
    {
        return new ConjoinClient(
            apiKey: self::API_KEY,
            baseUrl: $this->server()->baseUrl(),
            maxRetries: $maxRetries,
            backoffSeconds: 0.001,
            maxRetryDelaySeconds: 0.05,
            maxResponseBytes: $maxResponseBytes,
            httpClient: new Client(['timeout' => 5.0]),
        );
    }

    public function testRetriesThroughACallerHttpClientWithTheSameRequestId(): void
    {
        $this->server()->queue(Behaviour::status(503, body: self::errorBody(503)), Behaviour::dropBeforeStore());

        $response = self::read($this->psr18Client());

        self::assertSame('GET', $response->dataArray()['method'] ?? null);
        $ids = $this->server()->headerValues('conjoin-request-id');
        self::assertCount(3, $ids);
        self::assertSame([$ids[0], $ids[0], $ids[0]], $ids);
    }

    public function testNeverRetriesACreateWithoutAKeyThroughACallerHttpClient(): void
    {
        $this->server()->queue(Behaviour::dropAfterStore());

        $error = self::caught(fn () => self::createCustomer($this->psr18Client(), false));

        self::assertInstanceOf(NetworkException::class, $error);
        self::assertSame(1, $this->server()->attemptCount());
        self::assertCount(1, $this->server()->customers());
    }

    public function testRefusesAnOversizedBodyFromACallerHttpClient(): void
    {
        $this->server()->queue(Behaviour::large(200, 50_000));

        $error = self::caught(fn () => self::read($this->psr18Client(maxResponseBytes: 4_096)));

        self::assertInstanceOf(ResponseException::class, $error);
        self::assertSame(ResponseException::RESPONSE_TOO_LARGE, $error->getErrorCode());
    }
}
