<?php

declare(strict_types=1);

namespace ConjoinCloud;

enum Region: string
{
    case Us = 'us';
    case Eu = 'eu';
    case Gh = 'gh';

    private const API_ROOT_DOMAIN = 'conjoin.cloud';

    private const KEY_BASE_PREFIXES = ['cak_', 'cpk_'];

    private const KEY_MODE_SEGMENTS = ['live', 'test'];

    public static function fromKey(#[\SensitiveParameter] string $key): self
    {
        foreach (self::KEY_BASE_PREFIXES as $prefix) {
            if (!str_starts_with($key, $prefix)) {
                continue;
            }

            $segments = explode('_', substr($key, strlen($prefix)), 3);
            $region = self::tryFrom($segments[0]);
            $mode = $segments[1] ?? null;

            if ($region !== null && $mode !== null && in_array($mode, self::KEY_MODE_SEGMENTS, true)) {
                return $region;
            }

            return self::Us;
        }

        return self::Us;
    }

    public function baseUrl(): string
    {
        return $this === self::Us
            ? sprintf('https://api.%s', self::API_ROOT_DOMAIN)
            : sprintf('https://api.%s.%s', $this->value, self::API_ROOT_DOMAIN);
    }
}
