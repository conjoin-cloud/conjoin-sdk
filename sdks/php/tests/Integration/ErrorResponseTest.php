<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\Exception\AuthenticationException;
use ConjoinCloud\Exception\ConjoinException;
use ConjoinCloud\Exception\NetworkException;
use ConjoinCloud\Exception\ServerException;
use ConjoinCloud\Generated\Api\AuthSCIMs;
use ConjoinCloud\Tests\Support\Server\Behaviour;
use ConjoinCloud\Tests\Support\ServerTestCase;

final class ErrorResponseTest extends ServerTestCase
{
    public function testKeepsTheKeyOutOfEveryExceptionAndDump(): void
    {
        $client = $this->client(maxRetries: 0);
        $this->server()->queue(Behaviour::dropBeforeStore(), Behaviour::status(503, body: self::errorBody(503)));

        $network = self::caught(fn () => self::read($client));
        $server = self::caught(fn () => self::createCustomer($client, true));

        self::assertInstanceOf(NetworkException::class, $network);
        self::assertInstanceOf(ServerException::class, $server);

        foreach ([$network, $server] as $error) {
            self::assertInstanceOf(ConjoinException::class, $error);
            self::assertStringNotContainsString(self::API_KEY, (string) $error);
            self::assertStringNotContainsString(self::API_KEY, print_r($error, true));
            self::assertStringNotContainsString(self::API_KEY, $error->getTraceAsString());
        }

        ob_start();
        var_dump($client);
        $dump = (string) ob_get_clean();

        self::assertStringNotContainsString(self::API_KEY, $dump);
        self::assertStringNotContainsString(self::API_KEY, print_r($client, true));
        self::assertSame('Bearer ' . self::API_KEY, $this->server()->attempt(0)->header('authorization'));
    }

    public function testKeepsTheScimTokenOutOfTheResourceDumpAndItsExceptions(): void
    {
        $scimToken = 'scim_directory_sync_secret';
        $scim = new AuthSCIMs($this->client(maxRetries: 0), $scimToken);
        $this->server()->queue(Behaviour::status(401, body: self::errorBody(401)));

        $error = self::caught(fn () => $scim->scimListGroups('prj_directory', 'app_directory'));

        ob_start();
        var_dump($scim);
        $dump = (string) ob_get_clean();

        self::assertInstanceOf(AuthenticationException::class, $error);
        self::assertSame('Bearer ' . $scimToken, $this->server()->attempt(0)->header('authorization'));

        foreach ([$dump, print_r($scim, true), (string) $error, print_r($error, true)] as $text) {
            self::assertStringNotContainsString($scimToken, $text);
            self::assertStringNotContainsString(self::API_KEY, $text);
        }
    }
}
