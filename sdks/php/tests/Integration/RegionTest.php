<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Integration;

use ConjoinCloud\ConjoinClient;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;

final class RegionTest extends TestCase
{
    public static function keysAndAddresses(): array
    {
        return [
            ['cak_gh_live_regionalcaller', 'https://api.gh.conjoin.cloud'],
            ['cak_eu_test_regionalcaller', 'https://api.eu.conjoin.cloud'],
            ['cpk_gh_test_regionalcaller', 'https://api.gh.conjoin.cloud'],
            ['cpk_eu_live_regionalcaller', 'https://api.eu.conjoin.cloud'],
            ['cak_live_regionalcaller', 'https://api.conjoin.cloud'],
            ['cak_us_live_regionalcaller', 'https://api.conjoin.cloud'],
            ['cak_gh_staging_regionalcaller', 'https://api.conjoin.cloud'],
            ['sk_eu_live_regionalcaller', 'https://api.conjoin.cloud'],
        ];
    }

    #[DataProvider('keysAndAddresses')]
    public function testSendsTheKeyToTheAddressOfItsRegion(string $key, string $baseUrl): void
    {
        $client = str_starts_with($key, 'cpk_') ? new ConjoinClient(publishableKey: $key) : new ConjoinClient(apiKey: $key);

        self::assertSame($baseUrl, $client->baseUrl());
    }
}
