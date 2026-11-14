<?php

declare(strict_types=1);

namespace ConjoinCloud\Exception;

final class ValidationException extends ApiException
{
    private readonly array $fieldErrors;

    public function __construct(
        string $message,
        string $errorCode,
        int $status,
        ?string $param,
        mixed $details,
        ?string $requestId,
        array $fieldErrors,
    ) {
        parent::__construct($message, $errorCode, $status, $param, $details, $requestId);
        $this->fieldErrors = array_values(array_filter(
            $fieldErrors,
            static fn (mixed $fieldError): bool => $fieldError instanceof FieldError,
        ));
    }

    public function getFieldErrors(): array
    {
        return $this->fieldErrors;
    }
}
