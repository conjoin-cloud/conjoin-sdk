<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\Exception\NetworkException;
use ConjoinCloud\Tests\Support\Server\Behaviour;
use ConjoinCloud\Tests\Support\ServerTestCase;

final class IdempotentCreateTest extends ServerTestCase
{
    public function testStoresOneCustomerWhenTheConnectionDropsAfterTheServerStoredTheFirstAttempt(): void
    {
        $this->server()->queue(Behaviour::dropAfterStore());

        $response = self::createCustomer($this->client(), true);

        self::assertSame([['customer_id' => 'cus_1', 'email' => self::NEW_CUSTOMER['email']]], $this->server()->customers());
        self::assertSame(['customer_id' => 'cus_1', 'email' => self::NEW_CUSTOMER['email']], $response->dataArray());

        $keys = $this->server()->headerValues('idempotency-key');
        self::assertCount(2, $keys);
        self::assertIsString($keys[0]);
        self::assertMatchesRegularExpression(self::SERVER_IDEMPOTENCY_KEY_PATTERN, $keys[0]);
        self::assertSame($keys[0], $keys[1]);
    }

    public function testSendsADifferentIdempotencyKeyForEachSeparateCreate(): void
    {
        $client = $this->client();

        self::createCustomer($client, true);
        self::createCustomer($client, true);

        $keys = $this->server()->headerValues('idempotency-key');
        self::assertCount(2, $this->server()->customers());
        self::assertNotSame($keys[0], $keys[1]);
    }

    public function testNeverRetriesACreateWhoseOperationTakesNoIdempotencyKey(): void
    {
        $this->server()->queue(Behaviour::dropAfterStore());

        $error = self::caught(fn () => self::createCustomer($this->client(), false));

        self::assertInstanceOf(NetworkException::class, $error);
        self::assertSame([null], $this->server()->headerValues('idempotency-key'));
        self::assertCount(1, $this->server()->customers());
    }
}
