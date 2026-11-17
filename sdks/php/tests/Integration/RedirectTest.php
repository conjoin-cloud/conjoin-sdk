<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Credential;
use ConjoinCloud\Exception\ConjoinException;
use ConjoinCloud\Generated\Api\AuthAccounts;
use ConjoinCloud\Tests\Support\Server\Behaviour;
use ConjoinCloud\Tests\Support\ServerProcess;
use GuzzleHttp\Client;
use GuzzleHttp\RequestOptions;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;
use Psr\Http\Client\ClientInterface;
use RuntimeException;
use Throwable;

final class RedirectTest extends TestCase
{
    private const API_KEY = 'cak_test_redirectedcaller';

    private const AUTH_APP_ID = 'app_auth_owner';

    private const ACCOUNT_ID = 'acc_account_owner';

    private const STEP_UP_SESSION_ID = 'sus_0198f0f7';

    private const STEP_UP_TOKEN = '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08';

    private const TEMPORARY_REDIRECT_STATUS = 307;

    private ?ServerProcess $apiHost = null;

    private ?ServerProcess $otherHost = null;

    protected function tearDown(): void
    {
        $this->apiHost?->stop();
        $this->otherHost?->stop();
        $this->apiHost = null;
        $this->otherHost = null;
    }

    public static function httpClients(): array
    {
        return [
            'the sender the SDK builds' => [null],
            'a Guzzle client whose own setting follows redirects' => [new Client([RequestOptions::ALLOW_REDIRECTS => true])],
        ];
    }

    #[DataProvider('httpClients')]
    public function testARedirectNeverCarriesTheStepUpTokenToAnotherHost(?ClientInterface $httpClient): void
    {
        $otherHost = ServerProcess::start();
        $apiHost = ServerProcess::start();
        $this->otherHost = $otherHost;
        $this->apiHost = $apiHost;
        $location = $otherHost->baseUrl() . '/v1/auth/accounts/' . self::ACCOUNT_ID;
        $apiHost->queue(Behaviour::status(self::TEMPORARY_REDIRECT_STATUS, ['Location' => $location]));
        $client = new ConjoinClient(
            apiKey: self::API_KEY,
            baseUrl: $apiHost->baseUrl(),
            maxRetries: 0,
            authAppId: self::AUTH_APP_ID,
            httpClient: $httpClient,
        );

        $error = self::caught(static fn () => (new AuthAccounts($client))->delete(
            self::ACCOUNT_ID,
            stepUpSessionId: self::STEP_UP_SESSION_ID,
            stepUpToken: new Credential(self::STEP_UP_TOKEN),
        ));

        self::assertInstanceOf(ConjoinException::class, $error);
        self::assertSame(1, $apiHost->attemptCount());
        self::assertSame(self::STEP_UP_TOKEN, $apiHost->attempt(0)->header('step-up-token'));
        self::assertSame(0, $otherHost->attemptCount());
    }

    private static function caught(callable $call): Throwable
    {
        try {
            $call();
        } catch (Throwable $error) {
            return $error;
        }

        throw new RuntimeException('The call finished without an exception');
    }
}
