<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class SecurityReader
{
    private const SECURITY_SCHEME_GROUPS = [
        [AuthKind::ClientKey, ['conjoinApiKey']],
        [AuthKind::ScimBearer, ['scimBearer']],
        [AuthKind::PublishableKey, ['conjoinPublishableKey']],
        [AuthKind::Session, ['conjoinSessionBearer', 'conjoinSessionCookie']],
        [AuthKind::PortalTicket, ['conjoinPortalTicketHeader', 'conjoinPortalTicketQuery']],
    ];

    private const PORTAL_TICKET_HEADER_SCHEME = 'conjoinPortalTicketHeader';

    private const PORTAL_TICKET_PARAMETER = 'portalTicket';

    private const RESERVED_HEADER_NAMES = [
        'accept',
        'authorization',
        'content-length',
        'content-type',
        'cookie',
        'host',
        'user-agent',
        'x-conjoin-api-version',
        'x-conjoin-sdk-version',
    ];

    private const CREDENTIAL_HEADER_NAMES = ['step-up-token'];

    private const PATTERN_DELIMITER = '~';

    public function __construct(private readonly array $document, private readonly SchemaResolver $resolver)
    {
    }

    public function authKind(array $operation, string $operationId): AuthKind
    {
        $security = $operation['security'] ?? null;

        if (!is_array($security)) {
            return AuthKind::ClientKey;
        }

        $schemes = [];

        foreach ($security as $requirement) {
            if (is_array($requirement)) {
                $schemes = array_merge($schemes, array_map('strval', array_keys($requirement)));
            }
        }

        if ($schemes === []) {
            return AuthKind::None;
        }

        foreach (self::SECURITY_SCHEME_GROUPS as [$kind, $group]) {
            if (array_diff($schemes, $group) === []) {
                return $kind;
            }
        }

        throw new CodegenException(sprintf('%s declares the security schemes %s, which no SDK call supports', $operationId, implode(', ', $schemes)));
    }

    public function portalTicketHeader(string $operationId): DeclaredHeaderInfo
    {
        $components = is_array($this->document['components'] ?? null) ? $this->document['components'] : [];
        $schemes = is_array($components['securitySchemes'] ?? null) ? $components['securitySchemes'] : [];
        $scheme = is_array($schemes[self::PORTAL_TICKET_HEADER_SCHEME] ?? null) ? $schemes[self::PORTAL_TICKET_HEADER_SCHEME] : [];

        if (($scheme['in'] ?? null) !== 'header' || !is_string($scheme['name'] ?? null)) {
            throw new CodegenException(sprintf('%s needs %s as a header', $operationId, self::PORTAL_TICKET_HEADER_SCHEME));
        }

        return new DeclaredHeaderInfo($scheme['name'], self::PORTAL_TICKET_PARAMETER, true, true);
    }

    public function declaredHeader(array $parameter, string $operationId): DeclaredHeaderInfo
    {
        $name = is_string($parameter['name'] ?? null) ? $parameter['name'] : '';

        if (in_array(strtolower($name), self::RESERVED_HEADER_NAMES, true)) {
            throw new CodegenException(sprintf('%s declares the reserved header %s as a parameter', $operationId, $name));
        }

        $schema = $this->resolver->resolve($parameter['schema'] ?? null);

        if (($schema['type'] ?? null) !== 'string') {
            throw new CodegenException(sprintf('%s declares the header %s without a string schema', $operationId, $name));
        }

        $pattern = $schema['pattern'] ?? null;

        if ($pattern !== null && (!is_string($pattern) || !self::compiles($pattern))) {
            throw new CodegenException(sprintf('%s declares the header %s with a pattern PHP cannot check', $operationId, $name));
        }

        return new DeclaredHeaderInfo(
            $name,
            Naming::camel(strtolower($name)),
            ($parameter['required'] ?? false) === true,
            in_array(strtolower($name), self::CREDENTIAL_HEADER_NAMES, true),
            self::bound($schema, 'minLength', $operationId, $name),
            self::bound($schema, 'maxLength', $operationId, $name),
            $pattern,
        );
    }

    private static function compiles(string $pattern): bool
    {
        $expression = self::PATTERN_DELIMITER
            . str_replace(self::PATTERN_DELIMITER, '\\' . self::PATTERN_DELIMITER, $pattern)
            . self::PATTERN_DELIMITER . 'Du';

        return @preg_match($expression, '') !== false;
    }

    private static function bound(array $schema, string $key, string $operationId, string $name): ?int
    {
        $value = $schema[$key] ?? null;

        if ($value === null) {
            return null;
        }

        if (!is_int($value) || $value < 0) {
            throw new CodegenException(sprintf('%s declares the header %s with a %s that is not a whole number', $operationId, $name, $key));
        }

        return $value;
    }
}
