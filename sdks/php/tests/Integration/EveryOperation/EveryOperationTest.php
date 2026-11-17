<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration\EveryOperation;

use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Credential;
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

    private const PUBLISHABLE_KEY = 'cpk_test_everyoperationcaller';

    private const SCIM_TOKEN = 'scim_directory_sync_token';

    private const SESSION_TOKEN = 'sess_signed_in_owner';

    private const PORTAL_TICKET = 'ptk_portal_setup_ticket';

    private const PORTAL_TICKET_HEADER = 'x-portal-ticket';

    private const PORTAL_TICKET_PARAMETER = 'portalTicket';

    private const PORTAL_TICKET_QUERY_KEY = 'ticket';

    private const SDK_MANAGED_HEADER_NAMES = ['billing-entity-id', 'messaging-profile-id', 'auth-app-id', 'idempotency-key', 'conjoin-request-id'];

    private const EXPECTED_AUTHORIZATION_BY_SCHEME = [
        'conjoinApiKey' => 'Bearer ' . self::API_KEY,
        'scimBearer' => 'Bearer ' . self::SCIM_TOKEN,
        'conjoinPublishableKey' => 'Bearer ' . self::PUBLISHABLE_KEY,
        'conjoinSessionBearer' => 'Bearer ' . self::SESSION_TOKEN,
    ];

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
            $isFrontend = $namespace === 'Frontend';
            $client = new ConjoinClient(
                apiKey: $isFrontend ? null : self::API_KEY,
                publishableKey: $isFrontend ? self::PUBLISHABLE_KEY : null,
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
            $placeholders = [];

            for ($index = 0; $index < count($method->pathParameterNames); $index++) {
                $placeholders[] = sprintf('p%d', $index);
            }

            $arguments = self::pathArguments($method, $placeholders);

            if ($method->hasData) {
                $arguments['data'] = [];
            }

            if ($method->hasQuery) {
                $arguments['query'] = $method->queryRequired ? [] : null;
            }

            if ($method->takesSessionToken) {
                $arguments['sessionToken'] = new Credential(self::SESSION_TOKEN);
            }

            if (array_key_exists(self::PORTAL_TICKET_PARAMETER, $method->headerParameters)) {
                $arguments[self::PORTAL_TICKET_PARAMETER] = new Credential(self::PORTAL_TICKET);
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
        self::assertCount(count($method->pathParameterNames), $pathParams, $method->label);
        self::assertSame($bodyType !== null, $method->hasData, $method->label);
        self::assertSame($queryParameters !== [], $method->hasQuery, $method->label);

        $isSession = $document->securityScheme($operation) === 'conjoinSessionBearer';
        $headerValues = self::declaredHeaderValues($document, $sampler, $operation);
        self::assertSame($isSession, $method->takesSessionToken, $method->label);
        self::assertSame(array_keys($headerValues), array_keys($method->headerParameters), $method->label);

        $data = $bodyType === null ? null : self::topLevelObject($sampler->sample($document->requestBodySchema($operation)));
        $arguments = self::pathArguments($method, array_values($pathParams));

        if ($method->hasData) {
            $arguments['data'] = $data;
        }

        if ($method->hasQuery) {
            $arguments['query'] = self::requiredQuery($sampler, $queryParameters);
        }

        if ($isSession) {
            $arguments['sessionToken'] = new Credential(self::SESSION_TOKEN);
        }

        foreach ($headerValues as $sample) {
            if ($sample instanceof DeclaredHeaderSample) {
                $arguments[$sample->parameter] = $sample->isCredential ? new Credential($sample->value) : $sample->value;
            }
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

        foreach ($headerValues as $sample) {
            if ($sample instanceof DeclaredHeaderSample) {
                self::assertSame($sample->value, $attempt->header($sample->header), $method->label . ' ' . $sample->header);
            }
        }

        self::assertArrayNotHasKey(self::PORTAL_TICKET_QUERY_KEY, $attempt->queryValues(), $method->label);
        self::assertStringNotContainsString(self::PORTAL_TICKET, $attempt->query, $method->label);
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

        $expectedAuthorization = self::EXPECTED_AUTHORIZATION_BY_SCHEME[(string) $document->securityScheme($operation)] ?? null;

        self::assertSame($expectedAuthorization, $attempt->header('authorization'), $label);
    }

    private static function declaredHeaderValues(DocumentOperations $document, SchemaSampler $sampler, array $operation): array
    {
        $values = [];

        foreach ($document->parameters($operation, 'header') as $parameter) {
            $name = is_array($parameter) && is_string($parameter['name'] ?? null) ? strtolower($parameter['name']) : '';

            if ($name === '' || in_array($name, self::SDK_MANAGED_HEADER_NAMES, true)) {
                continue;
            }

            $sample = $sampler->sample($parameter['schema'] ?? null);
            $parameterName = lcfirst(str_replace(' ', '', ucwords(str_replace('-', ' ', $name))));
            $values[$parameterName] = new DeclaredHeaderSample($parameterName, $name, is_string($sample) ? $sample : '', $name === 'step-up-token');
        }

        if ($document->securityScheme($operation) === 'conjoinPortalTicketHeader') {
            $values[self::PORTAL_TICKET_PARAMETER] = new DeclaredHeaderSample(
                self::PORTAL_TICKET_PARAMETER,
                self::PORTAL_TICKET_HEADER,
                self::PORTAL_TICKET,
                true,
            );
        }

        return $values;
    }

    private static function pathArguments(GeneratedMethod $method, array $values): array
    {
        $arguments = [];

        foreach ($method->pathParameterNames as $index => $name) {
            if (!is_string($name)) {
                self::fail($method->label . ' has a path parameter name that is not a string');
            }

            $arguments[$name] = $values[$index] ?? null;
        }

        return $arguments;
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
