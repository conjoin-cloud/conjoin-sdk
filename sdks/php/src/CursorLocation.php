<?php

declare(strict_types=1);

namespace ConjoinCloud;

enum CursorLocation
{
    case Query;
    case Body;
    case NotAccepted;
}
