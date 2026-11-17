<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Response;

use ConjoinCloud\Exception\ResponseException;
use ConjoinCloud\Internal\Http\ReceivedResponse;
use ConjoinCloud\Internal\Tracing\RequestId;
use ConjoinCloud\Response\ApiResponse;

final class ResponseReader
{
    private function __construct()
    {
    }

    public static function read(ReceivedResponse $response, string $sentRequestId): ApiResponse
    {
        $returned = $response->header(RequestId::HEADER);
        $requestId = $returned !== null && RequestId::isValid($returned) ? $returned : $sentRequestId;

        if (!$response->isSuccess()) {
            throw ErrorFactory::fromResponse($response, $requestId);
        }

        if ($response->bodyTruncated) {
            throw new ResponseException(
                'The response body exceeded maxResponseBytes',
                $response->status,
                $requestId,
                ResponseException::RESPONSE_TOO_LARGE,
            );
        }

        $decoded = JsonBody::decode($response->body);

        if (!$decoded->isValid) {
            throw new ResponseException('The response body was not valid JSON', $response->status, $requestId);
        }

        return new ApiResponse($response->status, $response->headers, $requestId, $decoded->value);
    }
}
