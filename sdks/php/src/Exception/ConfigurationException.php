<?php

declare(strict_types=1);

namespace ConjoinCloud\Exception;

final class ConfigurationException extends ConjoinException
{
    public const CODE = 'configuration_error';

    public function __construct(string $message)
    {
        parent::__construct($message, self::CODE);
    }
}
