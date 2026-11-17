<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Http;

use ConjoinCloud\Internal\Request\PreparedRequest;

interface HttpSender
{
    public function send(#[\SensitiveParameter] PreparedRequest $request, AttemptLimits $limits): ReceivedResponse;
}
