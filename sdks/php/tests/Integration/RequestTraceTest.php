<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Exception\NotFoundException;
use ConjoinCloud\Tests\Support\Server\Behaviour;
use ConjoinCloud\Tests\Support\ServerTestCase;

final class RequestTraceTest extends ServerTestCase
{
    private const CALLER_REQUEST_ID = 'cnj_req_0198f0f7-5d0b-7b4a-8d5a-cf5693f0b2c1';

    private const CLIENT_REQUEST_ID = 'cnj_req_0198f0f7-5d0b-7b4a-9d5a-cf5693f0b2c2';

    public function testCreatesADifferentIdForSeparateCallsAndKeepsTheCallerIdOnRetries(): void
    {
        $client = $this->client();

        self::read($client, 'billing/customers/cus_1');
        self::read($client, 'billing/customers/cus_2');
        $this->server()->queue(Behaviour::status(502, body: self::errorBody(502)));
        self::read($client, 'billing/customers/cus_3', new CallOptions(requestId: self::CALLER_REQUEST_ID));

        $ids = $this->server()->headerValues('conjoin-request-id');
        self::assertCount(4, $ids);
        self::assertIsString($ids[0]);
        self::assertIsString($ids[1]);
        self::assertMatchesRegularExpression(self::REQUEST_ID_PATTERN, $ids[0]);
        self::assertMatchesRegularExpression(self::REQUEST_ID_PATTERN, $ids[1]);
        self::assertNotSame($ids[0], $ids[1]);
        self::assertSame([self::CALLER_REQUEST_ID, self::CALLER_REQUEST_ID], array_slice($ids, 2));
    }

    public function testSendsTheClientRequestIdOnEveryCallOfThatClient(): void
    {
        $client = new ConjoinClient(apiKey: self::API_KEY, baseUrl: $this->server()->baseUrl(), requestId: self::CLIENT_REQUEST_ID);

        self::read($client);
        self::read($client->withRequestTrace(self::CALLER_REQUEST_ID));
        self::read($client);

        self::assertSame(
            [self::CLIENT_REQUEST_ID, self::CALLER_REQUEST_ID, self::CLIENT_REQUEST_ID],
            $this->server()->headerValues('conjoin-request-id'),
        );
    }

    public function testExposesTheSentRequestIdOnAnApiException(): void
    {
        $this->server()->queue(Behaviour::status(404, body: self::errorBody(404)));

        $error = self::caught(fn () => self::read($this->client(), options: new CallOptions(requestId: self::CALLER_REQUEST_ID)));

        self::assertInstanceOf(NotFoundException::class, $error);
        self::assertSame(self::CALLER_REQUEST_ID, $error->getRequestId());
    }
}
