<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support;

use ConjoinCloud\CallOptions;
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

    protected const REQUEST_ID_PATTERN = '/^cnj_req_[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/D';

    protected const SERVER_IDEMPOTENCY_KEY_PATTERN = '/^[A-Za-z0-9\-_:.]{1,64}$/D';

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

    protected function client(
        float $timeoutSeconds = 2.0,
        int $maxRetries = 3,
        float $backoffSeconds = 0.001,
        float $maxRetryDelaySeconds = 0.05,
        int $maxResponseBytes = 16_777_216,
    ): ConjoinClient {
        return new ConjoinClient(
            apiKey: self::API_KEY,
            baseUrl: $this->server()->baseUrl(),
            timeoutSeconds: $timeoutSeconds,
            maxRetries: $maxRetries,
            backoffSeconds: $backoffSeconds,
            maxRetryDelaySeconds: $maxRetryDelaySeconds,
            maxResponseBytes: $maxResponseBytes,
        );
    }

    protected static function read(ConjoinClient $client, string $path = 'billing/customers/cus_1', ?CallOptions $options = null): ApiResponse
    {
        return $client->send(new OperationRequest(HttpMethod::Get, $path), $options);
    }

    protected static function createCustomer(ConjoinClient $client, bool $acceptsIdempotencyKey, ?CallOptions $options = null): ApiResponse
    {
        return $client->send(
            new OperationRequest(HttpMethod::Post, 'billing/customers/', body: self::NEW_CUSTOMER, acceptsIdempotencyKey: $acceptsIdempotencyKey),
            $options,
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
