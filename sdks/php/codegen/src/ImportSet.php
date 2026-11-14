<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class ImportSet
{
    private array $classes = [];

    public function add(string $class): void
    {
        $this->classes[$class] = true;
    }

    public function render(): string
    {
        $classes = [];

        foreach (array_keys($this->classes) as $class) {
            $classes[] = (string) $class;
        }

        sort($classes, SORT_STRING);

        return implode('', array_map(static fn (string $class): string => sprintf("use %s;\n", $class), $classes));
    }
}
