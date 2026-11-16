<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

enum AuthKind
{
    case ClientKey;
    case None;
    case ScimBearer;
    case PublishableKey;
    case Session;
    case PortalTicket;
}
