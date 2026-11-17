<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support;

use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Response\ApiResponse;
use PHPUnit\Framework\TestCase;
use RuntimeException;
use Throwable;

abstract class ServerTestCase extends TestCase
{
    protected const API_KEY = 'cak_test_integrationcallerkey';

    protected const NEW_CUSTOMER = ['email' => 'billing.owner@example.com'];

    protected const SERVER_IDEMPOTENCY_KEY_PATTERN = '/^[A-Za-z0-9\-_:.]{1,64}$/D';

    private const TIMEOUT_SECONDS = 2.0;

    private const BACKOFF_SECONDS = 0.001;

    private const MAX_RETRY_DELAY_SECONDS = 0.05;

    private ?ServerProcess $server = null;

    protected function setUp(): void
    {
        $this->server = ServerProcess::start();
    }

    protected function tearDown(): void
    {
        $this->server?->stop();
        $this->server = null;
    }

    protected function server(): ServerProcess
    {
        if ($this->server === null) {
            throw new RuntimeException('The test server is not running');
        }

        return $this->server;
    }

    protected function client(int $maxRetries = 3): ConjoinClient
    {
        return new ConjoinClient(
            apiKey: self::API_KEY,
            baseUrl: $this->server()->baseUrl(),
            timeoutSeconds: self::TIMEOUT_SECONDS,
            maxRetries: $maxRetries,
            backoffSeconds: self::BACKOFF_SECONDS,
            maxRetryDelaySeconds: self::MAX_RETRY_DELAY_SECONDS,
        );
    }

    protected static function read(ConjoinClient $client): ApiResponse
    {
        return $client->send(new OperationRequest(HttpMethod::Get, 'billing/customers/cus_1'));
    }

    protected static function createCustomer(ConjoinClient $client, bool $acceptsIdempotencyKey): ApiResponse
    {
        return $client->send(
            new OperationRequest(HttpMethod::Post, 'billing/customers/', body: self::NEW_CUSTOMER, acceptsIdempotencyKey: $acceptsIdempotencyKey),
        );
    }

    protected static function caught(callable $call): Throwable
    {
        try {
            $call();
        } catch (Throwable $error) {
            return $error;
        }

        throw new RuntimeException('The call finished without an exception');
    }

    protected static function errorBody(int $status): array
    {
        return [
            'response' => ['type' => $status >= 500 ? 'SERVER_ERROR' : 'CLIENT_ERROR', 'code' => $status, 'message' => 'The ledger refused it'],
            'data' => null,
            'error' => ['code' => 'ledger_locked', 'param' => 'email', 'details' => [['message' => 'is locked', 'path' => 'body.email']]],
        ];
    }
}
