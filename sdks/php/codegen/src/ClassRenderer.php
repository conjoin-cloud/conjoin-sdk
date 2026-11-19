<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class ClassRenderer
{
    private const RESERVED_PARAMETER_NAMES = ['client', 'data', 'query', 'options', 'scimToken', 'sessionToken', 'this'];

    private const PARAMETER_PATTERN = '/^[a-z][A-Za-z0-9]*$/D';

    private const BASE_IMPORTS = ['ConjoinCloud\\CallOptions', 'ConjoinCloud\\ConjoinClient', 'ConjoinCloud\\HttpMethod', 'ConjoinCloud\\OperationRequest'];

    private const FIELD_INDENT = '            ';

    private const MAX_FIELD_LINE_LENGTH = 120;

    private const MAX_SIGNATURE_LINE_LENGTH = 160;

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

        return "    private readonly ?Credential \$scimToken;\n\n"
            . "    public function __construct(\n"
            . "        private readonly ConjoinClient \$client,\n"
            . "        #[\\SensitiveParameter] ?string \$scimToken = null,\n"
            . "    ) {\n"
            . "        \$this->scimToken = \$scimToken === null ? null : new Credential(\$scimToken);\n"
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

        if ($operation->declaredHeaders !== []) {
            $imports->add('ConjoinCloud\\DeclaredHeader');
        }

        if (
            $operation->auth === AuthKind::Session
            || $operation->auth === AuthKind::ScimBearer
            || self::takesCredentialHeader($operation)
        ) {
            $imports->add('ConjoinCloud\\Credential');
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
        $body = match ($operation->responseKind) {
            ResponseKind::ListPage => sprintf('        return $this->client->sendList(%s);', $call),
            ResponseKind::Empty => sprintf('        $this->client->send(%s);', $call),
            ResponseKind::Envelope, ResponseKind::Body => sprintf('        return $this->client->send(%s)%s;', $call, self::accessor($operation->returnType)),
        };

        return sprintf("%s\n%s\n    }", self::signature($name, $operation), $body);
    }

    private static function signature(string $name, OperationInfo $operation): string
    {
        $returnType = self::returnType($operation);
        $inline = sprintf('    public function %s(%s): %s', $name, self::parameters($operation, ', '), $returnType);

        if (strlen($inline) <= self::MAX_SIGNATURE_LINE_LENGTH) {
            return $inline . "\n    {";
        }

        return sprintf("    public function %s(\n        %s,\n    ): %s {", $name, self::parameters($operation, ",\n        "), $returnType);
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

    private static function parameters(OperationInfo $operation, string $separator): string
    {
        $parameters = [];

        foreach ($operation->pathParameters as $pathParameter) {
            $parameters[] = sprintf('string $%s', self::parameterName(self::pathParameter($pathParameter, $operation)));
        }

        if ($operation->auth === AuthKind::Session) {
            $parameters[] = '#[\\SensitiveParameter] Credential $sessionToken';
        }

        foreach ($operation->declaredHeaders as $entry) {
            $header = self::header($entry, $operation);

            if ($header->required) {
                $parameters[] = self::headerParameter($header, $operation);
            }
        }

        $bodyNeedsValue = $operation->hasRequestBody && ($operation->requestBodyRequired || $operation->queryRequired);

        if ($operation->hasRequestBody) {
            $parameters[] = match (true) {
                $operation->requestBodyRequired => 'array $data',
                $bodyNeedsValue => '?array $data',
                default => '?array $data = null',
            };
        }

        if ($operation->hasQuery) {
            $parameters[] = $operation->queryRequired ? 'array $query' : '?array $query = null';
        }

        foreach ($operation->declaredHeaders as $entry) {
            $header = self::header($entry, $operation);

            if (!$header->required) {
                $parameters[] = self::headerParameter($header, $operation);
            }
        }

        $parameters[] = '?CallOptions $options = null';

        return implode($separator, $parameters);
    }

    private static function pathParameter(mixed $pathParameter, OperationInfo $operation): string
    {
        return is_string($pathParameter)
            ? $pathParameter
            : throw new CodegenException(sprintf('%s has a path parameter that is not a string', $operation->operationId));
    }

    private static function header(mixed $header, OperationInfo $operation): DeclaredHeaderInfo
    {
        return $header instanceof DeclaredHeaderInfo
            ? $header
            : throw new CodegenException(sprintf('%s has a declared header that is not a DeclaredHeaderInfo', $operation->operationId));
    }

    private static function takesCredentialHeader(OperationInfo $operation): bool
    {
        foreach ($operation->declaredHeaders as $entry) {
            if (self::header($entry, $operation)->credential) {
                return true;
            }
        }

        return false;
    }

    private static function headerParameter(DeclaredHeaderInfo $header, OperationInfo $operation): string
    {
        $name = Naming::assertIdentifier($header->parameterName, self::PARAMETER_PATTERN, 'The header parameter');
        $pathNames = [];

        foreach ($operation->pathParameters as $pathParameter) {
            $pathNames[] = Naming::camel(self::pathParameter($pathParameter, $operation));
        }

        if (in_array($name, self::RESERVED_PARAMETER_NAMES, true) || in_array($name, $pathNames, true)) {
            throw new CodegenException(sprintf('The header %s of %s collides with another parameter', $header->name, $operation->operationId));
        }

        $type = $header->credential ? 'Credential' : 'string';
        $attribute = $header->credential ? '#[\\SensitiveParameter] ' : '';

        return $header->required
            ? sprintf('%s%s $%s', $attribute, $type, $name)
            : sprintf('%s?%s $%s = null', $attribute, $type, $name);
    }

    private static function declaredHeadersField(OperationInfo $operation): string
    {
        $entries = '';

        foreach ($operation->declaredHeaders as $entry) {
            $header = self::header($entry, $operation);
            $arguments = [var_export($header->name, true), var_export($header->parameterName, true), '$' . $header->parameterName];

            if ($header->required) {
                $arguments[] = 'required: true';
            }

            if ($header->minLength !== null) {
                $arguments[] = sprintf('minLength: %d', $header->minLength);
            }

            if ($header->maxLength !== null) {
                $arguments[] = sprintf('maxLength: %d', $header->maxLength);
            }

            if ($header->pattern !== null) {
                $arguments[] = 'pattern: ' . var_export($header->pattern, true);
            }

            $entries .= sprintf("%s    new DeclaredHeader(%s),\n", self::FIELD_INDENT, implode(', ', $arguments));
        }

        return sprintf("declaredHeaders: [\n%s%s]", $entries, self::FIELD_INDENT);
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

        if ($operation->auth === AuthKind::None || $operation->auth === AuthKind::PortalTicket) {
            $fields .= self::field('auth: AuthMode::None');
        }

        if ($operation->auth === AuthKind::PublishableKey) {
            $fields .= self::field('auth: AuthMode::PublishableKey');
        }

        if ($operation->auth === AuthKind::Session) {
            $fields .= self::field('auth: AuthMode::Session') . self::field('sessionToken: $sessionToken');
        }

        if ($operation->declaredHeaders !== []) {
            $fields .= self::field(self::declaredHeadersField($operation));
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
