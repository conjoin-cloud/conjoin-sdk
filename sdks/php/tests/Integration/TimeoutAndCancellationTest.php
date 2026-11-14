<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\CallOptions;
use ConjoinCloud\Cancellation\CancellationToken;
use ConjoinCloud\Exception\CancelledException;
use ConjoinCloud\Exception\TimeoutException;
use ConjoinCloud\Tests\Support\DeadlineCancellation;
use ConjoinCloud\Tests\Support\Server\Behaviour;
use ConjoinCloud\Tests\Support\ServerTestCase;

final class TimeoutAndCancellationTest extends ServerTestCase
{
    public function testRetriesAReadThatTimedOutAndReturnsTheNextAnswer(): void
    {
        $this->server()->queue(Behaviour::slow(1.0));

        $response = self::read($this->client(timeoutSeconds: 0.1));

        self::assertSame('GET', $response->dataArray()['method'] ?? null);
        self::assertSame(2, $this->server()->attemptCount());
    }

    public function testRaisesATimeoutThatDiffersFromACancellation(): void
    {
        $this->server()->queue(Behaviour::slow(1.0));
        $startedAt = microtime(true);

        $error = self::caught(fn () => self::read($this->client(timeoutSeconds: 0.1, maxRetries: 0)));

        self::assertInstanceOf(TimeoutException::class, $error);
        self::assertSame('timeout_error', $error->getErrorCode());
        self::assertSame($this->server()->attempt(0)->header('conjoin-request-id'), $error->getRequestId());
        self::assertLessThan(0.8, microtime(true) - $startedAt);
    }

    public function testLetsOneCallShortenTheTimeout(): void
    {
        $this->server()->queue(Behaviour::slow(2.0));
        $startedAt = microtime(true);

        $error = self::caught(fn () => self::read($this->client(timeoutSeconds: 30.0), options: new CallOptions(timeoutSeconds: 0.1, maxRetries: 0)));

        self::assertInstanceOf(TimeoutException::class, $error);
        self::assertLessThan(1.0, microtime(true) - $startedAt);
    }

    public function testCancelsARequestInFlightWhenTheCallerAsksToStop(): void
    {
        $this->server()->queue(Behaviour::slow(5.0));
        $startedAt = microtime(true);

        $error = self::caught(fn () => self::read($this->client(timeoutSeconds: 10.0), options: new CallOptions(cancellation: new DeadlineCancellation(0.05))));

        self::assertInstanceOf(CancelledException::class, $error);
        self::assertSame('request_aborted', $error->getErrorCode());
        self::assertLessThan(1.0, microtime(true) - $startedAt);
        self::assertSame(1, $this->server()->attemptCount());
    }

    public function testCancelsDuringTheWaitBeforeARetry(): void
    {
        $this->server()->queue(Behaviour::status(503, ['retry-after' => '30'], self::errorBody(503)));
        $startedAt = microtime(true);
        $client = $this->client(maxRetryDelaySeconds: 60.0);

        $error = self::caught(fn () => self::read($client, options: new CallOptions(cancellation: new DeadlineCancellation(0.2))));

        self::assertInstanceOf(CancelledException::class, $error);
        self::assertLessThan(1.5, microtime(true) - $startedAt);
        self::assertSame(1, $this->server()->attemptCount());
    }

    public function testSendsNothingWhenTheCallerHasAlreadyCancelled(): void
    {
        $token = new CancellationToken();
        $token->cancel();

        $error = self::caught(fn () => self::read($this->client(), options: new CallOptions(cancellation: $token)));

        self::assertInstanceOf(CancelledException::class, $error);
        self::assertSame(0, $this->server()->attemptCount());
    }
}
