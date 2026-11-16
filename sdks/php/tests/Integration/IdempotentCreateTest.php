<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Exception\ConfigurationException;
use ConjoinCloud\Exception\NetworkException;
use ConjoinCloud\Exception\ServerException;
use ConjoinCloud\Generated\Api\BillingCustomers;
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
        $requestIds = $this->server()->headerValues('conjoin-request-id');
        self::assertCount(2, $keys);
        self::assertIsString($keys[0]);
        self::assertMatchesRegularExpression(self::SERVER_IDEMPOTENCY_KEY_PATTERN, $keys[0]);
        self::assertSame($keys[0], $keys[1]);
        self::assertSame($requestIds[0], $requestIds[1]);
    }

    public function testStoresOneCustomerWhenACreateTimesOutAfterTheServerStoredIt(): void
    {
        $this->server()->queue(Behaviour::slow(1.5));

        $response = self::createCustomer($this->client(timeoutSeconds: 0.2), true);

        self::assertCount(1, $this->server()->customers());
        self::assertSame('cus_1', $response->dataArray()['customer_id'] ?? null);
        self::assertSame(200, $response->status);

        $keys = $this->server()->headerValues('idempotency-key');
        self::assertCount(2, $keys);
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

    public function testKeepsTheCallerKeyOnEveryRetryOfACreate(): void
    {
        $this->server()->queue(Behaviour::status(503, body: self::errorBody(503)), Behaviour::dropBeforeStore());

        self::createCustomer($this->client(), true, new CallOptions(idempotencyKey: 'ledger-order:7731_a.b'));

        self::assertSame(['ledger-order:7731_a.b', 'ledger-order:7731_a.b', 'ledger-order:7731_a.b'], $this->server()->headerValues('idempotency-key'));
        self::assertCount(1, $this->server()->customers());
    }

    public function testNeverRetriesACreateWhoseOperationTakesNoIdempotencyKey(): void
    {
        $this->server()->queue(Behaviour::dropAfterStore());

        $error = self::caught(fn () => self::createCustomer($this->client(), false));

        self::assertInstanceOf(NetworkException::class, $error);
        self::assertSame([null], $this->server()->headerValues('idempotency-key'));
        self::assertCount(1, $this->server()->customers());
    }

    public function testNeverRetriesACreateWithoutADeclaredKeyEvenWhenTheCallerPassesOne(): void
    {
        $this->server()->queue(Behaviour::status(503, body: self::errorBody(503)));

        $error = self::caught(fn () => self::createCustomer($this->client(), false, new CallOptions(idempotencyKey: 'ledger-order-7732')));

        self::assertInstanceOf(ServerException::class, $error);
        self::assertSame(1, $this->server()->attemptCount());
    }

    public function testRetriesTheGeneratedCustomerCreateUnderOneKeyBecauseTheDocumentDeclaresIt(): void
    {
        $client = new ConjoinClient(apiKey: self::API_KEY, baseUrl: $this->server()->baseUrl(), backoffSeconds: 0.001, billingEntityId: 'ent_billing_owner');
        $this->server()->queue(Behaviour::dropAfterStore());

        $customer = (new BillingCustomers($client))->create(self::NEW_CUSTOMER);

        $keys = $this->server()->headerValues('idempotency-key');
        self::assertSame(['customer_id' => 'cus_1', 'email' => self::NEW_CUSTOMER['email']], $customer);
        self::assertCount(1, $this->server()->customers());
        self::assertSame(2, $this->server()->attemptCount());
        self::assertSame('ent_billing_owner', $this->server()->attempt(1)->header('billing-entity-id'));
        self::assertIsString($keys[0]);
        self::assertMatchesRegularExpression(self::SERVER_IDEMPOTENCY_KEY_PATTERN, $keys[0]);
        self::assertSame($keys[0], $keys[1]);
    }

    public function testRefusesAMalformedCallerKeyBeforeSending(): void
    {
        $client = $this->client();

        foreach (['', 'has space', str_repeat('k', 65), "line\nbreak", 'key/with/slash'] as $key) {
            $error = self::caught(fn () => self::createCustomer($client, true, new CallOptions(idempotencyKey: $key)));
            self::assertInstanceOf(ConfigurationException::class, $error, $key);
        }

        self::createCustomer($client, true, new CallOptions(idempotencyKey: str_repeat('k', 64)));

        self::assertSame(1, $this->server()->attemptCount());
    }
}
