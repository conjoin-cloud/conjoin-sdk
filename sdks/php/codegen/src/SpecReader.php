<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class SpecReader
{
    private const HTTP_METHODS = ['get', 'post', 'put', 'patch', 'delete'];

    private const METHODS_WITHOUT_BODY = ['get', 'delete'];

    private const SCOPE_HEADERS = [
        'billing-entity-id' => 'BillingEntityId',
        'messaging-profile-id' => 'MessagingProfileId',
        'auth-app-id' => 'AuthAppId',
    ];

    private const REQUEST_ID_HEADER = 'conjoin-request-id';

    private const IDEMPOTENCY_KEY_HEADER = 'idempotency-key';

    private const NO_CONTENT_STATUS = '204';

    private readonly SchemaResolver $resolver;

    private readonly SecurityReader $security;

    public function __construct(private readonly array $document)
    {
        $this->resolver = new SchemaResolver($document);
        $this->security = new SecurityReader($document, $this->resolver);
    }

    public function groups(): array
    {
        $paths = is_array($this->document['paths'] ?? null) ? $this->document['paths'] : [];
        $groups = [];

        foreach ($paths as $path => $item) {
            if (!is_array($item)) {
                continue;
            }

            foreach (self::HTTP_METHODS as $method) {
                $operation = $item[$method] ?? null;

                if (!is_array($operation)) {
                    continue;
                }

                $label = sprintf('%s %s', strtoupper($method), (string) $path);
                $tag = is_array($operation['tags'] ?? null) ? ($operation['tags'][0] ?? null) : null;
                $operationId = $operation['operationId'] ?? null;

                if (!is_string($tag) || !is_string($operationId)) {
                    throw new CodegenException(sprintf('%s has no tag or operationId', $label));
                }

                $parsed = ParsedTag::parse($tag);

                if ($parsed->resource === '') {
                    throw new CodegenException(sprintf('%s has the tag %s without a resource', $label, $tag));
                }

                $key = $parsed->service . '-' . Naming::kebab($parsed->resource);
                $group = $groups[$key] ?? new ResourceGroup(
                    $parsed->service,
                    $parsed->resource,
                    Naming::pascal($parsed->service),
                    Naming::pascal($parsed->resource),
                );
                $group->add($this->operation((string) $path, $method, $operationId, $operation));
                $groups[$key] = $group;
            }
        }

        return array_values($groups);
    }

    private function operation(string $path, string $method, string $operationId, array $operation): OperationInfo
    {
        $scopes = [];
        $declaredHeaders = [];
        $acceptsIdempotencyKey = false;
        $hasQuery = false;
        $queryRequired = false;
        $queryTakesCursor = false;

        foreach (is_array($operation['parameters'] ?? null) ? $operation['parameters'] : [] as $raw) {
            $parameter = $this->resolver->resolve($raw);
            $location = $parameter['in'] ?? null;
            $name = strtolower(is_string($parameter['name'] ?? null) ? $parameter['name'] : '');

            if ($location === 'query') {
                $hasQuery = true;
                $queryRequired = $queryRequired || ($parameter['required'] ?? false) === true;
                $queryTakesCursor = $queryTakesCursor || ($parameter['name'] ?? null) === 'cursor';
                continue;
            }

            if ($location !== 'header') {
                continue;
            }

            if (isset(self::SCOPE_HEADERS[$name])) {
                $scopes[] = self::SCOPE_HEADERS[$name];
            } elseif ($name === self::IDEMPOTENCY_KEY_HEADER) {
                $acceptsIdempotencyKey = true;
            } elseif ($name !== self::REQUEST_ID_HEADER) {
                $declaredHeaders[] = $this->security->declaredHeader($parameter, $operationId);
            }
        }

        $auth = $this->security->authKind($operation, $operationId);

        if ($auth === AuthKind::PortalTicket) {
            $declaredHeaders[] = $this->security->portalTicketHeader($operationId);
        }

        $requestBody = isset($operation['requestBody']) ? $this->resolver->resolve($operation['requestBody']) : null;

        if ($requestBody !== null && in_array($method, self::METHODS_WITHOUT_BODY, true)) {
            throw new CodegenException(sprintf('%s is a %s that declares a request body', $operationId, strtoupper($method)));
        }

        $requestContent = is_array($requestBody['content'] ?? null) ? $requestBody['content'] : [];
        $requestContentType = strtolower((string) (array_key_first($requestContent) ?? 'application/json'));
        $success = $this->successShape($operation);
        $cursor = $success->kind === ResponseKind::ListPage
            ? $this->cursorKind($operationId, $requestContent, $queryTakesCursor)
            : CursorKind::NotAccepted;

        return new OperationInfo(
            $operationId,
            $method,
            $path,
            Naming::pathParameters($path),
            $requestBody !== null,
            ($requestBody['required'] ?? false) === true,
            $requestContentType === 'multipart/form-data',
            $success->kind,
            $success->returnType,
            $hasQuery,
            $queryRequired,
            array_values(array_unique($scopes)),
            $method === 'post' && $acceptsIdempotencyKey,
            $auth,
            $declaredHeaders,
            $cursor,
        );
    }

    private function cursorKind(string $operationId, array $requestContent, bool $queryTakesCursor): CursorKind
    {
        $media = is_array($requestContent['application/json'] ?? null) ? $requestContent['application/json'] : [];
        $schema = $this->resolver->resolve($media['schema'] ?? null);
        $bodyTakesCursor = is_array($schema['properties'] ?? null) && array_key_exists('cursor', $schema['properties']);

        if ($bodyTakesCursor && $queryTakesCursor) {
            throw new CodegenException(sprintf('%s declares a cursor in both its query and its body', $operationId));
        }

        return match (true) {
            $bodyTakesCursor => CursorKind::Body,
            $queryTakesCursor => CursorKind::Query,
            default => CursorKind::NotAccepted,
        };
    }

    private function successShape(array $operation): SuccessShape
    {
        $responses = is_array($operation['responses'] ?? null) ? $operation['responses'] : [];
        $codes = array_values(array_filter(
            array_map(static fn (int|string $code): string => (string) $code, array_keys($responses)),
            static fn (string $code): bool => str_starts_with($code, '2'),
        ));
        sort($codes, SORT_STRING);
        $code = $codes[0] ?? '200';
        $success = $this->resolver->resolve($responses[$code] ?? null);
        $content = is_array($success['content'] ?? null) ? $success['content'] : null;
        $contentType = $content === null ? null : array_key_first($content);
        $media = $content !== null && $contentType !== null && is_array($content[$contentType] ?? null) ? $content[$contentType] : null;

        if ($media === null || $code === self::NO_CONTENT_STATUS) {
            return new SuccessShape(ResponseKind::Empty, ReturnType::forData($this->resolver, null));
        }

        $schema = $this->resolver->resolve($media['schema'] ?? null);
        $properties = is_array($schema['properties'] ?? null) ? $schema['properties'] : null;

        if ($properties === null || !array_key_exists('data', $properties)) {
            return new SuccessShape(ResponseKind::Body, ReturnType::forBody(ReturnType::isObjectSchema($this->resolver, $schema)));
        }

        $data = $this->resolver->resolve($properties['data']);
        $isList = ($data['type'] ?? null) === 'array' && array_key_exists('cursor', $properties);

        return new SuccessShape(
            $isList ? ResponseKind::ListPage : ResponseKind::Envelope,
            ReturnType::forData($this->resolver, $properties['data']),
        );
    }
}
