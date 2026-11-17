<?php

declare(strict_types=1);

use ConjoinCloud\Codegen\CodegenException;
use ConjoinCloud\Codegen\Generator;

require dirname(__DIR__) . '/vendor/autoload.php';

$generator = new Generator(dirname(__DIR__, 3) . '/spec', dirname(__DIR__) . '/src/Generated');

try {
    foreach ($generator->run() as $summary) {
        fwrite(STDOUT, (is_string($summary) ? $summary : '') . PHP_EOL);
    }
} catch (CodegenException $error) {
    fwrite(STDERR, $error->getMessage() . PHP_EOL);
    exit(1);
}
