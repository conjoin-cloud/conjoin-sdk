<?php

declare(strict_types=1);

namespace ConjoinCloud\Internal\Http;

use ConjoinCloud\Exception\CancelledException;
use ConjoinCloud\Exception\ConjoinException;
use ConjoinCloud\Exception\NetworkException;
use ConjoinCloud\Exception\TimeoutException;
use ConjoinCloud\Internal\Clock;
use ConjoinCloud\Internal\Request\PreparedRequest;
use GuzzleHttp\Client;
use GuzzleHttp\Exception\ConnectTimeoutException;
use GuzzleHttp\Exception\NetworkTimeoutException;
use GuzzleHttp\Exception\ResponseException;
use GuzzleHttp\Exception\ResponseTimeoutException;
use GuzzleHttp\Exception\TransferException;
use GuzzleHttp\Handler\CurlMultiHandler;
use GuzzleHttp\HandlerStack;
use GuzzleHttp\Promise\PromiseInterface;
use GuzzleHttp\Promise\RejectionException;
use GuzzleHttp\RequestOptions;
use Psr\Http\Message\ResponseInterface;

final class GuzzleSender implements HttpSender
{
    private const SELECT_TIMEOUT_SECONDS = 0.01;

    private readonly CurlMultiHandler $handler;

    private readonly Client $client;

    public function __construct()
    {
        $this->handler = new CurlMultiHandler(['select_timeout' => self::SELECT_TIMEOUT_SECONDS]);
        $this->client = new Client([
            'handler' => HandlerStack::create($this->handler),
            RequestOptions::HTTP_ERRORS => false,
            RequestOptions::ALLOW_REDIRECTS => false,
            RequestOptions::COOKIES => false,
            RequestOptions::EXPECT => false,
            RequestOptions::DECODE_CONTENT => true,
        ]);
    }

    public function send(#[\SensitiveParameter] PreparedRequest $request, AttemptLimits $limits): ReceivedResponse
    {
        $sink = new BoundedSink($limits->maxBodyBytes);
        $deadline = Clock::deadlineAfter($limits->timeoutSeconds);
        $promise = $this->client->sendAsync($request->toPsrRequest(), [
            RequestOptions::TIMEOUT => $limits->timeoutSeconds,
            RequestOptions::SINK => $sink,
            RequestOptions::ON_HEADERS => static function (ResponseInterface $response) use ($sink, $limits): void {
                $sink->limitTo($limits->bodyLimitFor($response->getStatusCode()));
            },
        ]);

        try {
            $this->drive($promise, $deadline, $limits, $request->requestId);
            return ReceivedResponse::fromPsr($promise->wait(), $sink->contents(), false);
        } catch (ConjoinException $error) {
            throw $error;
        } catch (ResponseTimeoutException | ConnectTimeoutException | NetworkTimeoutException) {
            throw new TimeoutException($limits->timeoutSeconds, $request->requestId);
        } catch (ResponseException $error) {
            if ($sink->overflowed()) {
                return ReceivedResponse::fromPsr($error->getResponse(), $sink->contents(), true);
            }

            throw new NetworkException('The connection failed while the response arrived', $request->requestId);
        } catch (TransferException | RejectionException) {
            throw new NetworkException('The connection to the Conjoin API failed', $request->requestId);
        } finally {
            if ($promise->getState() === PromiseInterface::PENDING) {
                $promise->cancel();
            }

            $sink->close();
        }
    }

    private function drive(PromiseInterface $promise, int $deadline, AttemptLimits $limits, string $requestId): void
    {
        while ($promise->getState() === PromiseInterface::PENDING) {
            if ($limits->isCancelled()) {
                throw new CancelledException($requestId);
            }

            if (Clock::nowNanoseconds() >= $deadline) {
                throw new TimeoutException($limits->timeoutSeconds, $requestId);
            }

            $this->handler->tick();
        }
    }
}
