<?php

declare(strict_types=1);

namespace ConjoinCloud;

enum AuthMode
{
    case ClientKey;
    case None;
    case Bearer;
    case PublishableKey;
    case Session;
}
