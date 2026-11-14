<?php

declare(strict_types=1);

namespace ConjoinCloud;

use ConjoinCloud\Cancellation\Cancellation;
use ConjoinCloud\Internal\Validate;

final class CallOptions
{
    public readonly ?float $timeoutSeconds;

    public readonly ?int $maxRetries;

    public readonly array $headers;

    public function __construct(
        public readonly ?string $idempotencyKey = null,
        public readonly ?string $requestId = null,
        ?float $timeoutSeconds = null,
        ?int $maxRetries = null,
        public readonly ?Cancellation $cancellation = null,
        #[\SensitiveParameter] array $headers = [],
    ) {
        $this->timeoutSeconds = $timeoutSeconds === null
            ? null
            : Validate::timeoutSeconds($timeoutSeconds, 'timeoutSeconds');
        $this->maxRetries = $maxRetries === null ? null : Validate::retryCount($maxRetries, 'maxRetries');
        $this->headers = Validate::headers($headers);
    }

    public function __debugInfo(): array
    {
        return [
            'idempotencyKey' => $this->idempotencyKey,
            'requestId' => $this->requestId,
            'timeoutSeconds' => $this->timeoutSeconds,
            'maxRetries' => $this->maxRetries,
            'cancellation' => $this->cancellation,
            'headers' => array_keys($this->headers),
        ];
    }
}
