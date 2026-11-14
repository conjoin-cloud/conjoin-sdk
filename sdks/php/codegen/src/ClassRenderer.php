<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class ClassRenderer
{
    private const RESERVED_PARAMETER_NAMES = ['client', 'data', 'query', 'options', 'scimToken', 'this'];

    private const PARAMETER_PATTERN = '/^[a-z][A-Za-z0-9]*$/D';

    private const BASE_IMPORTS = ['ConjoinCloud\\CallOptions', 'ConjoinCloud\\ConjoinClient', 'ConjoinCloud\\HttpMethod', 'ConjoinCloud\\OperationRequest'];

    private const FIELD_INDENT = '            ';

    private const MAX_FIELD_LINE_LENGTH = 120;

    private function __construct()
    {
    }

    public static function render(ResourceGroup $group, string $namespace): string
    {
        $imports = new ImportSet();
        $usesScim = false;
        $methods = '';

        foreach (self::BASE_IMPORTS as $class) {
            $imports->add($class);
        }

        foreach (MethodNames::resolve($group) as $entry) {
            if (!$entry instanceof MethodEntry) {
                throw new CodegenException(sprintf('%s resolved an entry that is not a method', $group->className()));
            }

            $operation = $entry->operation;
            $usesScim = $usesScim || $operation->auth === AuthKind::ScimBearer;
            self::addImportsFor($operation, $imports);
            $methods .= ($methods === '' ? '' : "\n\n") . self::method($entry->name, $operation);
        }

        return "<?php\n\ndeclare(strict_types=1);\n\n"
            . sprintf("namespace %s;\n\n", $namespace)
            . $imports->render()
            . sprintf("\nfinal class %s\n{\n", $group->className())
            . self::constructor($usesScim)
            . "\n\n"
            . $methods
            . "\n}\n";
    }

    private static function constructor(bool $usesScim): string
    {
        if (!$usesScim) {
            return "    public function __construct(private readonly ConjoinClient \$client)\n    {\n    }";
        }

        return "    public function __construct(\n"
            . "        private readonly ConjoinClient \$client,\n"
            . "        #[\\SensitiveParameter] private readonly ?string \$scimToken = null,\n"
            . "    ) {\n"
            . "    }\n\n"
            . "    public function __debugInfo(): array\n"
            . "    {\n"
            . "        return ['client' => \$this->client];\n"
            . '    }';
    }

    private static function addImportsFor(OperationInfo $operation, ImportSet $imports): void
    {
        if ($operation->pathParameters !== []) {
            $imports->add('ConjoinCloud\\Internal\\Request\\PathSegment');
        }

        if ($operation->scopes !== []) {
            $imports->add('ConjoinCloud\\Scope');
        }

        if ($operation->auth !== AuthKind::ClientKey) {
            $imports->add('ConjoinCloud\\AuthMode');
        }

        if ($operation->multipart && $operation->hasRequestBody) {
            $imports->add('ConjoinCloud\\BodyType');
        }

        if ($operation->responseKind === ResponseKind::ListPage) {
            $imports->add('ConjoinCloud\\Pagination\\ListPage');
        }
    }

    private static function method(string $name, OperationInfo $operation): string
    {
        $call = sprintf("new OperationRequest(\n%s        ), \$options", self::requestFields($operation));
        $signature = sprintf('    public function %s(%s): %s', $name, self::parameters($operation), self::returnType($operation));
        $body = match ($operation->responseKind) {
            ResponseKind::ListPage => sprintf('        return $this->client->sendList(%s);', $call),
            ResponseKind::Empty => sprintf('        $this->client->send(%s);', $call),
            ResponseKind::Envelope, ResponseKind::Body => sprintf('        return $this->client->send(%s)%s;', $call, self::accessor($operation->returnType)),
        };

        return sprintf("%s\n    {\n%s\n    }", $signature, $body);
    }

    private static function returnType(OperationInfo $operation): string
    {
        return match ($operation->responseKind) {
            ResponseKind::ListPage => 'ListPage',
            ResponseKind::Empty => 'void',
            ResponseKind::Envelope, ResponseKind::Body => $operation->returnType->phpType,
        };
    }

    private static function accessor(ReturnType $returnType): string
    {
        return $returnType->accessor === 'body' ? '->body' : sprintf('->%s()', $returnType->accessor);
    }

    private static function parameters(OperationInfo $operation): string
    {
        $parameters = '';

        foreach ($operation->pathParameters as $pathParameter) {
            if (!is_string($pathParameter)) {
                throw new CodegenException(sprintf('%s has a path parameter that is not a string', $operation->operationId));
            }

            $parameters .= sprintf('string $%s, ', self::parameterName($pathParameter));
        }

        $bodyNeedsValue = $operation->hasRequestBody && ($operation->requestBodyRequired || $operation->queryRequired);

        if ($operation->hasRequestBody) {
            $parameters .= match (true) {
                $operation->requestBodyRequired => 'array $data, ',
                $bodyNeedsValue => '?array $data, ',
                default => '?array $data = null, ',
            };
        }

        if ($operation->hasQuery) {
            $parameters .= $operation->queryRequired ? 'array $query, ' : '?array $query = null, ';
        }

        return $parameters . '?CallOptions $options = null';
    }

    private static function requestFields(OperationInfo $operation): string
    {
        $fields = self::field(sprintf('method: HttpMethod::%s', ucfirst($operation->httpMethod)))
            . self::field(sprintf('path: %s', self::pathExpression($operation)));

        if ($operation->hasQuery) {
            $fields .= self::field('query: $query');
        }

        if ($operation->hasRequestBody) {
            $fields .= self::field('body: $data');
        }

        if ($operation->hasRequestBody && $operation->multipart) {
            $fields .= self::field('bodyType: BodyType::Multipart');
        }

        if ($operation->scopes !== []) {
            $fields .= self::field(sprintf('scopes: [%s]', self::scopeList($operation)));
        }

        if ($operation->acceptsIdempotencyKey) {
            $fields .= self::field('acceptsIdempotencyKey: true');
        }

        if ($operation->auth === AuthKind::None) {
            $fields .= self::field('auth: AuthMode::None');
        }

        if ($operation->auth === AuthKind::ScimBearer) {
            $fields .= self::field('auth: AuthMode::Bearer') . self::field('bearerToken: $this->scimToken');
        }

        return $fields;
    }

    private static function field(string $field): string
    {
        return self::FIELD_INDENT . $field . ",\n";
    }

    private static function scopeList(OperationInfo $operation): string
    {
        $scopes = [];

        foreach ($operation->scopes as $scope) {
            if (!is_string($scope)) {
                throw new CodegenException(sprintf('%s has a scope that is not a string', $operation->operationId));
            }

            $scopes[] = 'Scope::' . $scope;
        }

        return implode(', ', $scopes);
    }

    private static function pathExpression(OperationInfo $operation): string
    {
        $relative = (string) preg_replace('#^/v1/#', '', $operation->path);
        $pieces = preg_split('/(\{\w+\})/', $relative, -1, PREG_SPLIT_DELIM_CAPTURE | PREG_SPLIT_NO_EMPTY);

        if ($pieces === false) {
            throw new CodegenException(sprintf('Cannot split the path %s', $operation->path));
        }

        $parts = [];

        foreach ($pieces as $piece) {
            if (preg_match('/^\{(\w+)\}$/D', $piece, $match) === 1) {
                $parts[] = sprintf('PathSegment::encode($%s)', self::parameterName($match[1]));
                continue;
            }

            $parts[] = "'" . str_replace(['\\', "'"], ['\\\\', "\\'"], $piece) . "'";
        }

        if ($parts === []) {
            return "''";
        }

        $inline = implode(' . ', $parts);

        if (strlen(self::FIELD_INDENT . 'path: ' . $inline . ',') <= self::MAX_FIELD_LINE_LENGTH) {
            return $inline;
        }

        return implode("\n" . self::FIELD_INDENT . '    . ', $parts);
    }

    private static function parameterName(string $pathParameter): string
    {
        $name = Naming::assertIdentifier(Naming::camel($pathParameter), self::PARAMETER_PATTERN, 'The path parameter');

        if (in_array($name, self::RESERVED_PARAMETER_NAMES, true)) {
            throw new CodegenException(sprintf('The path parameter %s collides with a generated parameter', $pathParameter));
        }

        return $name;
    }
}
