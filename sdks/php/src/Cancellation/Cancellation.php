<?php

declare(strict_types=1);

namespace ConjoinCloud\Cancellation;

interface Cancellation
{
    public function isRequested(): bool;
}
