<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

enum ResponseKind
{
    case Envelope;
    case ListPage;
    case Body;
    case Empty;
}
