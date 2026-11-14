<?php

declare(strict_types=1);

use ConjoinCloud\Tests\Support\Server\ContractRoutes;
use ConjoinCloud\Tests\Support\Server\Scenario;
use ConjoinCloud\Tests\Support\Server\TestServer;

require dirname(__DIR__, 3) . '/vendor/autoload.php';

$arguments = $_SERVER['argv'] ?? [];
$documentPath = is_array($arguments) && is_string($arguments[1] ?? null) ? $arguments[1] : null;
$routes = $documentPath === null ? null : ContractRoutes::fromDocument($documentPath);

exit((new TestServer(new Scenario($routes)))->serve(STDIN, STDOUT, STDERR));
