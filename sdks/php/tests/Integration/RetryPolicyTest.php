<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\CallOptions;
use ConjoinCloud\Exception\RateLimitException;
use ConjoinCloud\Exception\ServerException;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Tests\Support\Server\Behaviour;
use ConjoinCloud\Tests\Support\ServerTestCase;
use PHPUnit\Framework\Attributes\DataProvider;

final class RetryPolicyTest extends ServerTestCase
{
    public static function retryableStatuses(): array
    {
        return [[429], [500], [502], [503], [504]];
    }

    public static function idempotentWrites(): array
    {
        return [[HttpMethod::Put], [HttpMethod::Patch], [HttpMethod::Delete]];
    }

    #[DataProvider('retryableStatuses')]
    public function testRetriesAReadAfterARetryableStatus(int $status): void
    {
        $this->server()->queue(Behaviour::status($status, body: self::errorBody($status)));

        $response = self::read($this->client());

        self::assertSame(['path' => '/v1/billing/customers/cus_1', 'method' => 'GET'], $response->dataArray());
        $requestIds = $this->server()->headerValues('conjoin-request-id');
        self::assertCount(2, $requestIds);
        self::assertSame($requestIds[0], $requestIds[1]);
    }

    #[DataProvider('idempotentWrites')]
    public function testRetriesAnIdempotentWriteAfterADroppedConnection(HttpMethod $method): void
    {
        $this->server()->queue(Behaviour::dropBeforeStore());

        $body = $method === HttpMethod::Delete ? null : ['name' => 'Billing owner'];

        $this->client()->send(new OperationRequest($method, 'billing/customers/cus_1', body: $body));

        self::assertSame([$method->value, $method->value], $this->server()->methods());
    }

    public function testStopsAfterTheConfiguredNumberOfRetries(): void
    {
        $this->server()->queue(...array_fill(0, 5, Behaviour::status(503, body: self::errorBody(503))));

        $error = self::caught(fn () => self::read($this->client(maxRetries: 2)));

        self::assertInstanceOf(ServerException::class, $error);
        self::assertSame(3, $this->server()->attemptCount());
    }

    public function testLetsOneCallOverrideTheRetryCount(): void
    {
        $this->server()->queue(...array_fill(0, 5, Behaviour::status(503, body: self::errorBody(503))));

        $error = self::caught(fn () => self::read($this->client(maxRetries: 4), options: new CallOptions(maxRetries: 0)));

        self::assertInstanceOf(ServerException::class, $error);
        self::assertSame(1, $this->server()->attemptCount());
    }

    public function testWaitsTheRetryAfterSecondsBeforeItRetries(): void
    {
        $this->server()->queue(Behaviour::status(429, ['retry-after' => '1'], self::errorBody(429)));

        self::read($this->client(backoffSeconds: 0.0, maxRetryDelaySeconds: 60.0));

        $gaps = $this->server()->gapsSeconds();
        self::assertCount(1, $gaps);
        self::assertGreaterThanOrEqual(0.95, $gaps[0]);
    }

    public function testCapsARetryAfterDateAtTheClientMaximumDelay(): void
    {
        $retryAt = gmdate('D, d M Y H:i:s \G\M\T', time() + 30);
        $this->server()->queue(Behaviour::status(503, ['retry-after' => $retryAt], self::errorBody(503)));

        self::read($this->client(backoffSeconds: 0.0, maxRetryDelaySeconds: 0.2));

        $gaps = $this->server()->gapsSeconds();
        self::assertCount(1, $gaps);
        self::assertGreaterThanOrEqual(0.15, $gaps[0]);
        self::assertLessThan(2.0, $gaps[0]);
    }

    public function testKeepsEveryBackoffWaitUnderTheClientMaximumDelay(): void
    {
        $this->server()->queue(...array_fill(0, 3, Behaviour::status(502, body: self::errorBody(502))));

        self::read($this->client(backoffSeconds: 30.0, maxRetryDelaySeconds: 0.1));

        $gaps = $this->server()->gapsSeconds();
        self::assertCount(3, $gaps);

        foreach ($gaps as $gap) {
            self::assertLessThan(0.6, $gap);
        }
    }

    public function testReportsTheRetryAfterOfA429OnceTheRetriesRunOut(): void
    {
        $this->server()->queue(Behaviour::status(429, ['retry-after' => '7'], self::errorBody(429)));

        $error = self::caught(fn () => self::read($this->client(maxRetries: 0)));

        self::assertInstanceOf(RateLimitException::class, $error);
        self::assertSame(7.0, $error->getRetryAfterSeconds());
        self::assertSame(429, $error->getStatus());
    }
}
