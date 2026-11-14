<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\Exception\ApiException;
use ConjoinCloud\Exception\AuthenticationException;
use ConjoinCloud\Exception\ConflictException;
use ConjoinCloud\Exception\ConjoinException;
use ConjoinCloud\Exception\FieldError;
use ConjoinCloud\Exception\NetworkException;
use ConjoinCloud\Exception\NotFoundException;
use ConjoinCloud\Exception\PermissionDeniedException;
use ConjoinCloud\Exception\ResponseException;
use ConjoinCloud\Exception\ServerException;
use ConjoinCloud\Exception\ValidationException;
use ConjoinCloud\Generated\Api\AuthSCIMs;
use ConjoinCloud\Tests\Support\Server\Behaviour;
use ConjoinCloud\Tests\Support\ServerTestCase;
use PHPUnit\Framework\Attributes\DataProvider;

final class ErrorResponseTest extends ServerTestCase
{
    public static function refusedStatuses(): array
    {
        return [
            [400, ValidationException::class],
            [401, AuthenticationException::class],
            [403, PermissionDeniedException::class],
            [404, NotFoundException::class],
            [409, ConflictException::class],
            [422, ValidationException::class],
            [501, ServerException::class],
        ];
    }

    #[DataProvider('refusedStatuses')]
    public function testNeverRetriesARefusalAndReportsItsCodeParamAndDetails(int $status, string $exceptionClass): void
    {
        $this->server()->queue(Behaviour::status($status, body: self::errorBody($status)));

        $error = self::caught(fn () => self::read($this->client()));

        self::assertSame($exceptionClass, $error::class);
        self::assertInstanceOf(ApiException::class, $error);
        self::assertSame($status, $error->getStatus());
        self::assertSame('ledger_locked', $error->getErrorCode());
        self::assertSame('email', $error->getParam());
        self::assertSame([['message' => 'is locked', 'path' => 'body.email']], $error->getDetails());
        self::assertSame('The ledger refused it', $error->getMessage());
        self::assertSame($this->server()->attempt(0)->header('conjoin-request-id'), $error->getRequestId());
        self::assertSame(1, $this->server()->attemptCount());
    }

    public function testListsTheFieldErrorsOfAValidationFailure(): void
    {
        $this->server()->queue(Behaviour::status(422, body: self::errorBody(422)));

        $error = self::caught(fn () => self::read($this->client()));

        self::assertInstanceOf(ValidationException::class, $error);
        $fieldErrors = [];

        foreach ($error->getFieldErrors() as $fieldError) {
            self::assertInstanceOf(FieldError::class, $fieldError);
            $fieldErrors[] = [$fieldError->path, $fieldError->message];
        }

        self::assertSame([['body.email', 'is locked']], $fieldErrors);
    }

    public function testReadsOnlyTheFirst64KiBOfAnErrorBody(): void
    {
        $this->server()->queue(Behaviour::large(400, 5_000_000));

        $error = self::caught(fn () => self::read($this->client()));

        self::assertInstanceOf(ValidationException::class, $error);
        self::assertSame('invalid_request', $error->getErrorCode());
        self::assertSame('HTTP 400', $error->getMessage());
    }

    public function testRefusesASuccessBodyAboveTheResponseLimit(): void
    {
        $this->server()->queue(Behaviour::large(200, 50_000));

        $error = self::caught(fn () => self::read($this->client(maxResponseBytes: 4_096)));

        self::assertInstanceOf(ResponseException::class, $error);
        self::assertSame(ResponseException::RESPONSE_TOO_LARGE, $error->getErrorCode());
        self::assertSame(1, $this->server()->attemptCount());
    }

    public function testRefusesASuccessBodyThatIsNotJson(): void
    {
        $this->server()->queue(Behaviour::rawStatus(200, '<html>maintenance</html>'));

        $error = self::caught(fn () => self::read($this->client()));

        self::assertInstanceOf(ResponseException::class, $error);
        self::assertSame(ResponseException::INVALID_RESPONSE, $error->getErrorCode());
    }

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
