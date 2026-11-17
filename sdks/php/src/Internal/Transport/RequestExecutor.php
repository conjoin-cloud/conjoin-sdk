<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Transport;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ClientConfig;
use ConjoinCloud\Exception\CancelledException;
use ConjoinCloud\Exception\NetworkException;
use ConjoinCloud\Exception\TimeoutException;
use ConjoinCloud\Internal\Http\AttemptLimits;
use ConjoinCloud\Internal\Http\HttpSender;
use ConjoinCloud\Internal\Request\RequestBuilder;
use ConjoinCloud\Internal\Response\ResponseReader;
use ConjoinCloud\Internal\Tracing\IdempotencyKey;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Response\ApiResponse;

final class RequestExecutor
{
    public function __construct(private readonly HttpSender $sender)
    {
    }

    public function execute(
        #[\SensitiveParameter] ClientConfig $config,
        #[\SensitiveParameter] OperationRequest $request,
        #[\SensitiveParameter] CallOptions $options,
    ): ApiResponse {
        $prepared = RequestBuilder::build($config, $request, $options);
        $requestId = $prepared->requestId;
        $hasIdempotencyKey = $prepared->header(IdempotencyKey::HEADER) !== null;
        $retryAllowed = RetryRules::canRetryMethod($request->method, $hasIdempotencyKey && $request->acceptsIdempotencyKey);
        $maxRetries = $options->maxRetries ?? $config->maxRetries;
        $limits = new AttemptLimits(
            $options->timeoutSeconds ?? $config->timeoutSeconds,
            $options->cancellation,
            $config->maxResponseBytes,
        );

        for ($attempt = 0;; $attempt++) {
            if ($limits->isCancelled()) {
                throw new CancelledException($requestId);
            }

            $canRetryAgain = $retryAllowed && $attempt < $maxRetries;

            try {
                $received = $this->sender->send($prepared, $limits);
            } catch (NetworkException | TimeoutException $failure) {
                if (!$canRetryAgain) {
                    throw $failure;
                }

                $this->waitBeforeRetry($config, $attempt, null, $limits, $requestId);

                continue;
            }

            if ($canRetryAgain && RetryRules::isRetryableStatus($received->status)) {
                $retryAfter = RetryRules::parseRetryAfterSeconds($received->header('retry-after'));
                $this->waitBeforeRetry($config, $attempt, $retryAfter, $limits, $requestId);

                continue;
            }

            return ResponseReader::read($received, $requestId);
        }
    }

    private function waitBeforeRetry(
        #[\SensitiveParameter] ClientConfig $config,
        int $attempt,
        ?float $retryAfterSeconds,
        AttemptLimits $limits,
        string $requestId,
    ): void {
        $delay = RetryRules::delaySeconds($attempt, $config->backoffSeconds, $config->maxRetryDelaySeconds, $retryAfterSeconds);
        BackoffWait::sleep($delay, $limits->cancellation, $requestId);
    }
}
