<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Credential;
use ConjoinCloud\Exception\ConfigurationException;
use ConjoinCloud\Generated\Api\AuthAccounts;
use ConjoinCloud\Generated\Frontend\AuthClients;
use ConjoinCloud\Generated\Frontend\AuthSelves;
use ConjoinCloud\Generated\Frontend\AuthSSOPortals;
use ConjoinCloud\Generated\Frontend\CloudSDKs;
use ConjoinCloud\Tests\Support\DocumentOperations;
use ConjoinCloud\Tests\Support\SchemaSampler;
use ConjoinCloud\Tests\Support\ServerProcess;
use LogicException;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;
use RuntimeException;
use Throwable;

final class DeclaredHeadersTest extends TestCase
{
    private const SECRET_API_KEY = 'cak_live_serversidecaller';

    private const PUBLISHABLE_KEY = 'cpk_live_browsercaller';

    private const SESSION_TOKEN = 'sess_signed_in_owner';

    private const PORTAL_TICKET = 'ptk_portal_setup_ticket';

    private const AUTH_APP_ID = 'app_auth_owner';

    private const ACCOUNT_ID = 'acc_account_owner';

    private const STEP_UP_TOKEN = '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08';

    private const DELETE_ACCOUNT = 'DELETE /v1/auth/accounts/{account_id}';

    private const FRONTEND_ROUTES = [
        'GET /v1/auth/client/.well-known/jwks.json',
        'GET /v1/auth/self/',
        'GET /v1/cloud/client/settings/',
        'GET /v1/auth/portal/',
    ];

    private ?ServerProcess $server = null;

    protected function tearDown(): void
    {
        $this->server?->stop();
        $this->server = null;
    }

    public static function malformedStepUpTokens(): array
    {
        return [
            'uppercase' => [strtoupper(self::STEP_UP_TOKEN)],
            '257 characters' => [str_repeat('a', 257)],
            'empty' => [''],
            'line break' => [self::STEP_UP_TOKEN . "\r\nX-Injected: yes"],
        ];
    }

    #[DataProvider('malformedStepUpTokens')]
    public function testAMalformedStepUpTokenIsRefusedWithoutRepeatingIt(string $token): void
    {
        $accounts = new AuthAccounts($this->serverSideClient('openapi.json', self::DELETE_ACCOUNT));

        $error = self::caught(static fn () => $accounts->delete(self::ACCOUNT_ID, stepUpToken: new Credential($token)));

        self::assertInstanceOf(ConfigurationException::class, $error);
        self::assertStringContainsString('stepUpToken', $error->getMessage());

        if ($token !== '') {
            self::assertStringNotContainsString($token, $error->getMessage() . $error->getTraceAsString());
        }

        self::assertSame(0, $this->server()->attemptCount());
    }

    public function testACredentialStaysOutOfEveryPrintedForm(): void
    {
        $credential = new Credential(self::STEP_UP_TOKEN);
        $printed = implode("\n", [
            (string) $credential,
            print_r($credential, true),
            var_export($credential, true),
            json_encode($credential, JSON_THROW_ON_ERROR),
            json_encode(['token' => $credential], JSON_THROW_ON_ERROR),
            self::dump($credential),
        ]);

        self::assertStringNotContainsString(self::STEP_UP_TOKEN, $printed);
        self::assertInstanceOf(LogicException::class, self::caught(static fn () => serialize($credential)));
    }

    public function testFrontendCallsFromASecretKeyClientNeverSendTheSecretKey(): void
    {
        $client = $this->serverSideClient('openapi-frontend.json', ...self::FRONTEND_ROUTES);

        (new AuthClients($client))->getJwks();
        (new AuthSelves($client))->readProfile(new Credential(self::SESSION_TOKEN));
        $error = self::caught(static fn () => (new CloudSDKs($client))->readSdkSettings());

        self::assertInstanceOf(ConfigurationException::class, $error);
        self::assertStringContainsString('publishableKey', $error->getMessage());
        self::assertSame(2, $this->server()->attemptCount());
        self::assertNull($this->server()->attempt(0)->header('authorization'));
        self::assertSame('Bearer ' . self::SESSION_TOKEN, $this->server()->attempt(1)->header('authorization'));
        self::assertStringNotContainsString(self::SECRET_API_KEY, json_encode($this->server()->attempts(), JSON_THROW_ON_ERROR));
        self::assertStringNotContainsString(self::SECRET_API_KEY, self::dump($this->server()->attempts()));
    }

    public function testAPortalTicketTravelsOnlyInItsHeader(): void
    {
        $this->startServer('openapi-frontend.json', ...self::FRONTEND_ROUTES);
        $client = new ConjoinClient(publishableKey: self::PUBLISHABLE_KEY, baseUrl: $this->server()->baseUrl(), maxRetries: 0);

        (new AuthSSOPortals($client))->readSsoPortalContext(new Credential(self::PORTAL_TICKET));

        $attempt = $this->server()->attempt(0);
        self::assertSame(self::PORTAL_TICKET, $attempt->header('x-portal-ticket'));
        self::assertNull($attempt->header('authorization'));
        self::assertStringNotContainsString(self::PORTAL_TICKET, $attempt->query);
    }

    private function serverSideClient(string $file, string ...$routes): ConjoinClient
    {
        $this->startServer($file, ...$routes);

        return new ConjoinClient(apiKey: self::SECRET_API_KEY, baseUrl: $this->server()->baseUrl(), maxRetries: 0, authAppId: self::AUTH_APP_ID);
    }

    private function startServer(string $file, string ...$routes): void
    {
        $documentPath = dirname(__DIR__, 4) . '/spec/' . $file;
        $document = DocumentOperations::load($documentPath);
        $sampler = new SchemaSampler($document);
        $server = ServerProcess::start($documentPath);
        $this->server = $server;

        foreach ($routes as $route) {
            [$method, $template] = explode(' ', $route, 2);
            $operation = $document->operation($method, $template);
            $schema = $document->successSchema($operation);
            $body = $schema === null ? null : $sampler->sample($schema);
            $server->register($method, $template, $document->successStatus($operation), $schema !== null, $body);
        }
    }

    private function server(): ServerProcess
    {
        return $this->server ?? throw new RuntimeException('The test server is not running');
    }

    private static function dump(mixed $value): string
    {
        ob_start();
        var_dump($value);

        return (string) ob_get_clean();
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
