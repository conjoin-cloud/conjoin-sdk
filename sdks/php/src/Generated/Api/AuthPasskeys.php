<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Credential;
use ConjoinCloud\DeclaredHeader;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;
use ConjoinCloud\Scope;

final class AuthPasskeys
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function list(string $accountId, ?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/accounts/' . PathSegment::encode($accountId) . '/passkeys/',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options);
    }

    public function listCount(string $accountId, ?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/accounts/' . PathSegment::encode($accountId) . '/passkeys/count',
            query: $query,
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function read(string $accountId, string $passkeyId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'auth/accounts/' . PathSegment::encode($accountId) . '/passkeys/' . PathSegment::encode($passkeyId),
            scopes: [Scope::AuthAppId],
        ), $options)->dataArray();
    }

    public function delete(
        string $accountId,
        string $passkeyId,
        ?string $stepUpSessionId = null,
        #[\SensitiveParameter] ?Credential $stepUpToken = null,
        ?CallOptions $options = null,
    ): array {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'auth/accounts/' . PathSegment::encode($accountId) . '/passkeys/' . PathSegment::encode($passkeyId),
            scopes: [Scope::AuthAppId],
            declaredHeaders: [
                new DeclaredHeader('Step-Up-Session-ID', 'stepUpSessionId', $stepUpSessionId, minLength: 1, maxLength: 48),
                new DeclaredHeader('Step-Up-Token', 'stepUpToken', $stepUpToken, minLength: 1, maxLength: 256, pattern: '^[0-9a-f]+$'),
            ],
        ), $options)->dataArray();
    }
}
