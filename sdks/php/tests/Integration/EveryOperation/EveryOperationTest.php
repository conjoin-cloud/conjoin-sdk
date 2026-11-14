<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration\EveryOperation;

use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Exception\NotFoundException;
use ConjoinCloud\Pagination\ListPage;
use ConjoinCloud\Tests\Support\Attempt;
use ConjoinCloud\Tests\Support\ServerProcess;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;
use RuntimeException;
use stdClass;

final class EveryOperationTest extends TestCase
{
    private const API_KEY = 'cak_test_everyoperationcaller';

    private const SCIM_TOKEN = 'scim_directory_sync_token';

    private const SCOPE_HEADER_VALUES = [
        'billing-entity-id' => 'ent_billing_owner',
        'messaging-profile-id' => 'mpr_messaging_owner',
        'auth-app-id' => 'app_auth_owner',
    ];

    private const SERVER_IDEMPOTENCY_KEY_PATTERN = '/^[A-Za-z0-9\-_:.]{1,64}$/D';

    private const JSON_FLAGS = JSON_THROW_ON_ERROR | JSON_UNESCAPED_SLASHES | JSON_PRESERVE_ZERO_FRACTION;

    public static function documents(): array
    {
        return [['openapi.json', 'Api'], ['openapi-frontend.json', 'Frontend']];
    }

    #[DataProvider('documents')]
    public function testEveryGeneratedMethodSendsTheDocumentedRequestAndReturnsTheDocumentedData(string $file, string $namespace): void
    {
        $documentPath = dirname(__DIR__, 5) . '/spec/' . $file;
        $document = DocumentOperations::load($documentPath);
        $sampler = new SchemaSampler($document);
        $server = ServerProcess::start($documentPath);

        try {
            $client = new ConjoinClient(
                apiKey: self::API_KEY,
                baseUrl: $server->baseUrl(),
                maxRetries: 0,
                billingEntityId: self::SCOPE_HEADER_VALUES['billing-entity-id'],
                messagingProfileId: self::SCOPE_HEADER_VALUES['messaging-profile-id'],
                authAppId: self::SCOPE_HEADER_VALUES['auth-app-id'],
            );
            $methods = GeneratedMethod::discover(dirname(__DIR__, 3) . '/src/Generated/' . $namespace, 'ConjoinCloud\\Generated\\' . $namespace);
            $routes = self::learnRoutes($server, $client, $methods);
            $expected = $document->keys();
            $actual = array_keys($routes);
            sort($expected);
            sort($actual);

            self::assertSame($expected, $actual, 'Every document operation has exactly one generated method');
            self::assertCount(count($expected), $methods);

            foreach ($routes as $key => $method) {
                if ($method instanceof GeneratedMethod) {
                    self::checkOperation($server, $client, $document, $sampler, (string) $key, $method);
                }
            }
        } finally {
            $server->stop();
        }
    }

    private static function learnRoutes(ServerProcess $server, ConjoinClient $client, array $methods): array
    {
        $routes = [];

        foreach ($methods as $method) {
            if (!$method instanceof GeneratedMethod) {
                continue;
            }

            $server->reset();
            $arguments = [];

            for ($index = 0; $index < $method->pathParameterCount; $index++) {
                $arguments[] = sprintf('p%d', $index);
            }

            if ($method->hasData) {
                $arguments[] = [];
            }

            if ($method->hasQuery) {
                $arguments[] = $method->queryRequired ? [] : null;
            }

            $error = null;

            try {
                $method->invoke($client, self::SCIM_TOKEN, $arguments);
            } catch (NotFoundException $caught) {
                $error = $caught;
            }

            self::assertInstanceOf(NotFoundException::class, $error, $method->label);
            $attempt = $server->attempt(0);
            $key = $attempt->method . ' ' . (string) $attempt->pathTemplate;
            self::assertNotNull($attempt->pathTemplate, $method->label . ' reached no document route');
            self::assertArrayNotHasKey($key, $routes, $method->label . ' sends the same request as another method');
            $routes[$key] = $method;
        }

        return $routes;
    }

    private static function checkOperation(
        ServerProcess $server,
        ConjoinClient $client,
        DocumentOperations $document,
        SchemaSampler $sampler,
        string $key,
        GeneratedMethod $method,
    ): void {
        [$httpMethod, $template] = explode(' ', $key, 2);
        $operation = $document->operation($httpMethod, $template);
        preg_match_all('/\{([^}]+)\}/', $template, $names);
        $pathParams = [];

        foreach ($names[1] as $name) {
            $pathParams[$name] = sprintf('segment/%s 7?#%%ä', $name);
        }

        $bodyType = $document->requestBodyType($operation);
        $queryParameters = $document->parameters($operation, 'query');
        self::assertCount($method->pathParameterCount, $pathParams, $method->label);
        self::assertSame($bodyType !== null, $method->hasData, $method->label);
        self::assertSame($queryParameters !== [], $method->hasQuery, $method->label);

        $data = $bodyType === null ? null : self::topLevelObject($sampler->sample($document->requestBodySchema($operation)));
        $arguments = array_values($pathParams);

        if ($method->hasData) {
            $arguments[] = $data;
        }

        if ($method->hasQuery) {
            $arguments[] = self::requiredQuery($sampler, $queryParameters);
        }

        $schema = $document->successSchema($operation);
        $body = $schema === null ? null : $sampler->sample($schema);
        $server->reset();
        $server->register($httpMethod, $template, $document->successStatus($operation), $schema !== null, $body);

        $result = $method->invoke($client, self::SCIM_TOKEN, $arguments);

        self::assertSame(1, $server->attemptCount(), $method->label);
        $attempt = $server->attempt(0);
        self::assertSame($httpMethod, $attempt->method, $method->label);
        self::assertSame($template, $attempt->pathTemplate, $method->label);
        self::assertSame($pathParams, $attempt->pathParams, $method->label);
        self::checkHeaders($attempt, $document, $operation, $httpMethod, $method->label);
        self::checkBody($attempt, $bodyType, $data, $method->label);
        self::checkResult($result, $body, $document->schemaProperties($schema), $method->label);
    }

    private static function checkHeaders(Attempt $attempt, DocumentOperations $document, array $operation, string $httpMethod, string $label): void
    {
        self::assertMatchesRegularExpression($document->requestIdPattern($operation), (string) $attempt->header('conjoin-request-id'), $label);

        foreach (self::SCOPE_HEADER_VALUES as $header => $value) {
            self::assertSame($document->declaresHeader($operation, $header) ? $value : null, $attempt->header($header), $label . ' ' . $header);
        }

        if ($httpMethod === 'POST' && $document->declaresHeader($operation, 'idempotency-key')) {
            self::assertMatchesRegularExpression(self::SERVER_IDEMPOTENCY_KEY_PATTERN, (string) $attempt->header('idempotency-key'), $label);
        } else {
            self::assertNull($attempt->header('idempotency-key'), $label);
        }

        $expectedAuthorization = match ($document->securityScheme($operation)) {
            'conjoinApiKey' => 'Bearer ' . self::API_KEY,
            'scimBearer' => 'Bearer ' . self::SCIM_TOKEN,
            default => null,
        };

        self::assertSame($expectedAuthorization, $attempt->header('authorization'), $label);
    }

    private static function checkBody(Attempt $attempt, ?string $bodyType, ?array $data, string $label): void
    {
        if ($bodyType === 'application/json') {
            self::assertEquals(self::roundTrip($data), $attempt->jsonBody(), $label);

            return;
        }

        if ($bodyType !== 'multipart/form-data') {
            return;
        }

        self::assertStringStartsWith('multipart/form-data; boundary=', (string) $attempt->header('content-type'), $label);

        foreach (array_keys($data ?? []) as $field) {
            self::assertStringContainsString(sprintf('name="%s"', (string) $field), $attempt->body, $label);
        }
    }

    private static function checkResult(mixed $result, mixed $body, ?array $properties, string $label): void
    {
        $expected = self::roundTrip($body);

        if ($body === null) {
            self::assertNull($result, $label);

            return;
        }

        if ($properties === null || !array_key_exists('data', $properties) || !is_array($expected)) {
            self::assertEquals($expected, $result, $label);

            return;
        }

        if (!array_key_exists('cursor', $properties)) {
            self::assertEquals($expected['data'] ?? null, $result, $label);

            return;
        }

        self::assertInstanceOf(ListPage::class, $result, $label);
        $cursor = is_array($expected['cursor'] ?? null) ? $expected['cursor'] : [];
        self::assertEquals($expected['data'] ?? null, $result->data, $label);
        self::assertSame($cursor['next'] ?? null, $result->cursor->next, $label);
    }

    private static function requiredQuery(SchemaSampler $sampler, array $parameters): ?array
    {
        $query = [];

        foreach ($parameters as $parameter) {
            if (is_array($parameter) && ($parameter['required'] ?? false) === true && is_string($parameter['name'] ?? null)) {
                $query[$parameter['name']] = $sampler->sample($parameter['schema'] ?? null);
            }
        }

        return $query === [] ? null : $query;
    }

    private static function topLevelObject(mixed $sample): array
    {
        if ($sample instanceof stdClass || $sample === null) {
            return [];
        }

        if (!is_array($sample)) {
            throw new RuntimeException('A request body sample must be an object');
        }

        return $sample;
    }

    private static function roundTrip(mixed $value): mixed
    {
        return $value === null ? null : json_decode(json_encode($value, self::JSON_FLAGS), true, 512, JSON_THROW_ON_ERROR);
    }
}
