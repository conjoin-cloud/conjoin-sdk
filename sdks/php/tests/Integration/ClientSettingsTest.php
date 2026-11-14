<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Exception\ConfigurationException;
use ConjoinCloud\Generated\Api\BillingCustomers;
use ConjoinCloud\Generated\Api\MessagingEmails;
use ConjoinCloud\Tests\Support\ServerTestCase;

final class ClientSettingsTest extends ServerTestCase
{
    public function testRefusesACallThatNeedsAnUnsetScopeBeforeSendingIt(): void
    {
        $client = $this->client();

        $error = self::caught(fn () => (new BillingCustomers($client))->read('cus_1'));

        self::assertInstanceOf(ConfigurationException::class, $error);
        self::assertStringContainsString('billingEntityId', $error->getMessage());
        self::assertSame(0, $this->server()->attemptCount());
    }

    public function testSendsTheScopeOfAScopedCopyAndLeavesTheOriginalUnscoped(): void
    {
        $client = $this->client();
        $scoped = $client->withScope(billingEntityId: 'ent_billing_owner');

        (new BillingCustomers($scoped))->read('cus_1');
        $error = self::caught(fn () => (new BillingCustomers($client))->read('cus_1'));

        self::assertInstanceOf(ConfigurationException::class, $error);
        self::assertSame(1, $this->server()->attemptCount());
        self::assertSame('ent_billing_owner', $this->server()->attempt(0)->header('billing-entity-id'));
        self::assertNull($this->server()->attempt(0)->header('messaging-profile-id'));
    }

    public function testSendsOnlyTheScopesThatTheOperationDeclares(): void
    {
        $client = new ConjoinClient(
            apiKey: self::API_KEY,
            baseUrl: $this->server()->baseUrl(),
            billingEntityId: 'ent_billing_owner',
            messagingProfileId: 'mpr_messaging_owner',
            authAppId: 'app_auth_owner',
        );

        (new MessagingEmails($client))->getSummary();

        $attempt = $this->server()->attempt(0);
        self::assertSame('mpr_messaging_owner', $attempt->header('messaging-profile-id'));
        self::assertNull($attempt->header('billing-entity-id'));
        self::assertNull($attempt->header('auth-app-id'));
    }

    public function testRefusesAClientWithBothKeysOrNeither(): void
    {
        $both = self::caught(fn () => new ConjoinClient(apiKey: self::API_KEY, publishableKey: 'cpk_test_integrationcaller'));
        $neither = self::caught(fn () => new ConjoinClient());

        self::assertInstanceOf(ConfigurationException::class, $both);
        self::assertInstanceOf(ConfigurationException::class, $neither);
        self::assertStringNotContainsString(self::API_KEY, (string) $both);
    }
}
