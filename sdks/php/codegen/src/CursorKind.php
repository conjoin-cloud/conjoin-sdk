<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

enum CursorKind
{
    case Query;
    case Body;
    case NotAccepted;
}
