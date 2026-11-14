<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class ParsedTag
{
    public function __construct(
        public readonly string $service,
        public readonly string $resource,
    ) {
    }

    public static function parse(string $tag): self
    {
        $separator = strpos($tag, ' - ');

        if ($separator === false) {
            return new self(strtolower(trim($tag)), '');
        }

        return new self(strtolower(trim(substr($tag, 0, $separator))), trim(substr($tag, $separator + 3)));
    }
}
