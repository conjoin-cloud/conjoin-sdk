<?php

declare(strict_types=1);

namespace ConjoinCloud;

enum Scope: string
{
    case BillingEntityId = 'Billing-Entity-ID';
    case MessagingProfileId = 'Messaging-Profile-ID';
    case AuthAppId = 'Auth-App-ID';

    public function settingName(): string
    {
        return match ($this) {
            self::BillingEntityId => 'billingEntityId',
            self::MessagingProfileId => 'messagingProfileId',
            self::AuthAppId => 'authAppId',
        };
    }
}
