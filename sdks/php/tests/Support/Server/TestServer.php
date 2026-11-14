<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support\Server;

use RuntimeException;

final class TestServer
{
    private const LOOPBACK_ADDRESS = 'tcp://127.0.0.1:0';

    private const READ_CHUNK_BYTES = 65_536;

    private const IDLE_WAIT_SECONDS = 0.5;

    private const LISTENER_KEY = 'listener';

    private const STDIN_KEY = 'stdin';

    private array $connections = [];

    private int $nextConnectionId = 0;

    public function __construct(private readonly Scenario $scenario)
    {
    }

    public function serve(mixed $stdin, mixed $stdout, mixed $stderr): int
    {
        $listener = stream_socket_server(self::LOOPBACK_ADDRESS, $errorCode, $errorMessage);

        if ($listener === false || !is_resource($stdin) || !is_resource($stdout) || !is_resource($stderr)) {
            throw new RuntimeException(sprintf('The test server could not listen: %s', (string) $errorMessage));
        }

        stream_set_blocking($listener, false);
        stream_set_blocking($stdin, false);
        $address = (string) stream_socket_get_name($listener, false);
        fwrite($stdout, sprintf("PORT %s\n", substr($address, (int) strrpos($address, ':') + 1)));
        fflush($stdout);

        try {
            while ($this->tick($listener, $stdin)) {
                continue;
            }
        } finally {
            foreach (array_keys($this->connections) as $id) {
                $this->close((string) $id);
            }

            fclose($listener);
        }

        return 0;
    }

    private function tick(mixed $listener, mixed $stdin): bool
    {
        if (!is_resource($listener) || !is_resource($stdin)) {
            return false;
        }

        $now = microtime(true);
        $read = [self::LISTENER_KEY => $listener, self::STDIN_KEY => $stdin];
        $write = [];
        $except = null;
        $wait = self::IDLE_WAIT_SECONDS;

        foreach ($this->connections as $id => $connection) {
            if (!$connection instanceof Connection || !is_resource($connection->socket)) {
                continue;
            }

            $read[$id] = $connection->socket;
            $until = $connection->secondsUntilWrite($now);

            if ($connection->wantsWrite($now)) {
                $write[$id] = $connection->socket;
            } elseif ($until !== null) {
                $wait = min($wait, $until);
            }
        }

        $seconds = (int) floor($wait);

        if (stream_select($read, $write, $except, $seconds, (int) (($wait - $seconds) * 1_000_000)) === false) {
            throw new RuntimeException('The test server could not wait on its sockets');
        }

        if (isset($read[self::STDIN_KEY]) && $this->parentClosed($stdin)) {
            return false;
        }

        if (isset($read[self::LISTENER_KEY])) {
            $this->accept($listener);
        }

        foreach (array_keys($read) as $id) {
            if ($id !== self::LISTENER_KEY && $id !== self::STDIN_KEY) {
                $this->readFrom((string) $id);
            }
        }

        foreach (array_keys($write) as $id) {
            $this->writeTo((string) $id);
        }

        return true;
    }

    private function parentClosed(mixed $stdin): bool
    {
        if (!is_resource($stdin)) {
            return true;
        }

        fread($stdin, self::READ_CHUNK_BYTES);

        return feof($stdin);
    }

    private function accept(mixed $listener): void
    {
        if (!is_resource($listener)) {
            return;
        }

        $socket = stream_socket_accept($listener, 0);

        if ($socket === false) {
            return;
        }

        stream_set_blocking($socket, false);
        $this->connections[sprintf('c%d', $this->nextConnectionId++)] = new Connection($socket);
    }

    private function readFrom(string $id): void
    {
        $connection = $this->connections[$id] ?? null;

        if (!$connection instanceof Connection || !is_resource($connection->socket)) {
            return;
        }

        $chunk = fread($connection->socket, self::READ_CHUNK_BYTES);

        if ($chunk === false || ($chunk === '' && feof($connection->socket))) {
            $this->close($id);

            return;
        }

        try {
            $request = $connection->receive($chunk);
        } catch (ProtocolError $error) {
            $connection->schedule(Reply::json(400, ['message' => $error->getMessage()]));

            return;
        }

        if ($request === null) {
            return;
        }

        $reply = $this->scenario->handle($request);

        if ($reply->drop) {
            $this->close($id);

            return;
        }

        $connection->schedule($reply);
    }

    private function writeTo(string $id): void
    {
        $connection = $this->connections[$id] ?? null;

        if (!$connection instanceof Connection || !is_resource($connection->socket)) {
            return;
        }

        $written = fwrite($connection->socket, $connection->pendingBytes());

        if ($written === false || $connection->consumed($written)) {
            $this->close($id);
        }
    }

    private function close(string $id): void
    {
        $connection = $this->connections[$id] ?? null;
        unset($this->connections[$id]);

        if ($connection instanceof Connection && is_resource($connection->socket)) {
            fclose($connection->socket);
        }
    }
}
