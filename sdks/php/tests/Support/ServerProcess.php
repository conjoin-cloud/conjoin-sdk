<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support;

use ConjoinCloud\Tests\Support\Server\Behaviour;
use RuntimeException;

final class ServerProcess
{
    private const START_TIMEOUT_SECONDS = 10.0;

    private const STOP_TIMEOUT_SECONDS = 5.0;

    private const CONTROL_TIMEOUT_SECONDS = 10.0;

    private const PORT_LINE_PATTERN = '/^PORT (\d{1,5})$/D';

    private const STATUS_LINE_PATTERN = '#^HTTP/1\.[01] (\d{3}) #';

    private bool $stopped = false;

    private function __construct(
        private readonly mixed $process,
        private readonly mixed $stdin,
        private readonly mixed $stdout,
        private readonly string $logPath,
        private readonly int $port,
    ) {
    }

    public static function start(?string $documentPath = null): self
    {
        $logPath = tempnam(sys_get_temp_dir(), 'conjoin-php-server-');

        if ($logPath === false) {
            throw new RuntimeException('Cannot create the test server log file');
        }

        $command = [PHP_BINARY, __DIR__ . '/Server/serve.php'];

        if ($documentPath !== null) {
            $command[] = $documentPath;
        }

        $process = proc_open($command, [0 => ['pipe', 'r'], 1 => ['pipe', 'w'], 2 => ['file', $logPath, 'w']], $pipes);
        $stdin = $pipes[0] ?? null;
        $stdout = $pipes[1] ?? null;

        if (!is_resource($process) || !is_resource($stdin) || !is_resource($stdout)) {
            unlink($logPath);

            throw new RuntimeException('Cannot start the test server process');
        }

        $port = self::readPort($stdout);

        if ($port === null) {
            $log = (string) file_get_contents($logPath);
            (new self($process, $stdin, $stdout, $logPath, 0))->stop();

            throw new RuntimeException(sprintf('The test server did not report its port: %s', $log));
        }

        return new self($process, $stdin, $stdout, $logPath, $port);
    }

    public function baseUrl(): string
    {
        return sprintf('http://127.0.0.1:%d', $this->port);
    }

    public function queue(Behaviour ...$behaviours): void
    {
        $this->control('queue', array_map(static fn (Behaviour $behaviour): array => $behaviour->toArray(), $behaviours));
    }

    public function servePages(array $pages): void
    {
        $this->control('pages', (object) $pages);
    }

    public function register(string $method, string $template, int $status, bool $hasBody, mixed $body): void
    {
        $this->control('contract', ['method' => $method, 'template' => $template, 'status' => $status, 'hasBody' => $hasBody, 'body' => $body]);
    }

    public function reset(): void
    {
        $this->control('reset', null);
    }

    public function attempts(): array
    {
        $state = $this->control('state', null);
        $records = is_array($state) && is_array($state['attempts'] ?? null) ? $state['attempts'] : [];

        return array_map(static fn (mixed $record): Attempt => Attempt::fromRecord($record), $records);
    }

    public function attempt(int $index): Attempt
    {
        $attempt = $this->attempts()[$index] ?? null;

        if (!$attempt instanceof Attempt) {
            throw new RuntimeException(sprintf('The test server recorded no attempt %d', $index));
        }

        return $attempt;
    }

    public function attemptCount(): int
    {
        return count($this->attempts());
    }

    public function headerValues(string $name): array
    {
        $values = [];

        foreach ($this->attempts() as $attempt) {
            $values[] = $attempt instanceof Attempt ? $attempt->header($name) : null;
        }

        return $values;
    }

    public function methods(): array
    {
        $methods = [];

        foreach ($this->attempts() as $attempt) {
            $methods[] = $attempt instanceof Attempt ? $attempt->method : null;
        }

        return $methods;
    }

    public function gapsSeconds(): array
    {
        $gaps = [];
        $previous = null;

        foreach ($this->attempts() as $attempt) {
            if (!$attempt instanceof Attempt) {
                continue;
            }

            if ($previous !== null) {
                $gaps[] = $attempt->receivedAt - $previous;
            }

            $previous = $attempt->receivedAt;
        }

        return $gaps;
    }

    public function customers(): array
    {
        $state = $this->control('state', null);

        return is_array($state) && is_array($state['customers'] ?? null) ? $state['customers'] : [];
    }

    public function stop(): void
    {
        if ($this->stopped) {
            return;
        }

        $this->stopped = true;

        if (is_resource($this->stdin)) {
            fclose($this->stdin);
        }

        if (is_resource($this->stdout)) {
            fclose($this->stdout);
        }

        if (is_resource($this->process)) {
            $deadline = microtime(true) + self::STOP_TIMEOUT_SECONDS;

            while (proc_get_status($this->process)['running'] && microtime(true) < $deadline) {
                usleep(10_000);
            }

            if (proc_get_status($this->process)['running']) {
                proc_terminate($this->process);
            }

            proc_close($this->process);
        }

        if (is_file($this->logPath)) {
            unlink($this->logPath);
        }
    }

    public function __destruct()
    {
        $this->stop();
    }

    private static function readPort(mixed $stdout): ?int
    {
        if (!is_resource($stdout)) {
            return null;
        }

        $read = [$stdout];
        $write = null;
        $except = null;
        $seconds = (int) self::START_TIMEOUT_SECONDS;

        if (stream_select($read, $write, $except, $seconds) !== 1) {
            return null;
        }

        $line = fgets($stdout);

        if ($line === false || preg_match(self::PORT_LINE_PATTERN, trim($line), $match) !== 1) {
            return null;
        }

        return (int) $match[1];
    }

    private function control(string $call, mixed $payload): mixed
    {
        $socket = stream_socket_client(sprintf('tcp://127.0.0.1:%d', $this->port), $errorCode, $errorMessage, self::CONTROL_TIMEOUT_SECONDS);

        if ($socket === false) {
            throw new RuntimeException(sprintf('Cannot reach the test server: %s', $errorMessage));
        }

        try {
            stream_set_timeout($socket, (int) self::CONTROL_TIMEOUT_SECONDS);
            $body = $payload === null ? '' : json_encode($payload, JSON_THROW_ON_ERROR | JSON_UNESCAPED_SLASHES);
            $request = sprintf(
                "POST /__control/%s HTTP/1.1\r\nHost: 127.0.0.1\r\nContent-Type: application/json\r\nContent-Length: %d\r\nConnection: close\r\n\r\n%s",
                $call,
                strlen($body),
                $body,
            );

            for ($offset = 0; $offset < strlen($request);) {
                $written = fwrite($socket, substr($request, $offset));

                if ($written === false || $written === 0) {
                    throw new RuntimeException('The test server closed the control connection early');
                }

                $offset += $written;
            }

            $response = (string) stream_get_contents($socket);
        } finally {
            fclose($socket);
        }

        $headerEnd = strpos($response, "\r\n\r\n");
        $status = preg_match(self::STATUS_LINE_PATTERN, $response, $match) === 1 ? (int) $match[1] : 0;
        $text = $headerEnd === false ? '' : substr($response, $headerEnd + 4);

        if ($status !== 200) {
            throw new RuntimeException(sprintf('The test server refused the %s call with %d: %s', $call, $status, $text));
        }

        return json_decode($text, true, 512, JSON_THROW_ON_ERROR);
    }
}
