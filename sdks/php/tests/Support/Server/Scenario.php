<?php

declare(strict_types=1);

namespace ConjoinCloud\Tests\Support\Server;

use InvalidArgumentException;
use JsonException;

final class Scenario
{
    public const CONTROL_PREFIX = '/__control/';

    private const CUSTOMERS_PATH = '/v1/billing/customers/';

    private array $behaviours = [];

    private array $attempts = [];

    private array $customers = [];

    private array $customersByKey = [];

    private ?array $pages = null;

    private array $contract = [];

    public function __construct(private readonly ?ContractRoutes $routes)
    {
    }

    public function handle(ReceivedRequest $request): Reply
    {
        if (str_starts_with($request->path, self::CONTROL_PREFIX)) {
            return $this->control($request);
        }

        $match = $this->routes?->match($request->path);
        $this->attempts[] = [
            'method' => $request->method,
            'path' => $request->path,
            'query' => $request->query,
            'headers' => $request->headers,
            'body' => base64_encode($request->body),
            'receivedAt' => $request->receivedAt,
            'pathTemplate' => $match?->template,
            'pathParams' => $match === null ? [] : $match->params,
        ];
        $behaviour = array_shift($this->behaviours);

        if (!$behaviour instanceof Behaviour) {
            return $this->answer($request, $match);
        }

        return match ($behaviour->kind) {
            Behaviour::DROP_BEFORE_STORE => Reply::drop(),
            Behaviour::DROP_AFTER_STORE => $this->storeThenDrop($request),
            Behaviour::SLOW => $this->answer($request, $match)->delayed($behaviour->delaySeconds),
            Behaviour::STATUS => Reply::raw($behaviour->status, $behaviour->body ?? '{"data":null}', $behaviour->headers),
            Behaviour::LARGE => Reply::raw($behaviour->status, '{"data":"' . str_repeat('a', $behaviour->paddingBytes) . '"}'),
            default => $this->answer($request, $match),
        };
    }

    private function storeThenDrop(ReceivedRequest $request): Reply
    {
        if ($this->isCustomerCreate($request)) {
            $this->storeCustomer($request);
        }

        return Reply::drop();
    }

    private function answer(ReceivedRequest $request, ?RouteMatch $match): Reply
    {
        if ($this->routes !== null) {
            return $this->contractReply($request, $match);
        }

        if ($this->isCustomerCreate($request)) {
            return $this->storeCustomer($request);
        }

        if ($this->pages !== null && $request->method === 'GET') {
            return $this->page($request);
        }

        return Reply::json(200, self::success(200, ['path' => $request->path, 'method' => $request->method]));
    }

    private function contractReply(ReceivedRequest $request, ?RouteMatch $match): Reply
    {
        $registered = $match === null ? null : ($this->contract[$request->method . ' ' . $match->template] ?? null);

        if ($registered instanceof Reply) {
            return $registered;
        }

        return Reply::json(404, [
            'response' => ['type' => 'CLIENT_ERROR', 'code' => 404, 'message' => 'No contract response matches this request'],
            'data' => null,
            'error' => ['code' => 'no_contract_route', 'param' => null, 'details' => null],
        ]);
    }

    private function page(ReceivedRequest $request): Reply
    {
        parse_str($request->query, $query);
        $cursor = is_array($query['cursor'] ?? null) ? ($query['cursor']['next'] ?? '') : '';
        $page = $this->pages[is_string($cursor) ? $cursor : ''] ?? null;
        $data = is_array($page) ? ($page['data'] ?? []) : [];
        $next = is_array($page) ? ($page['next'] ?? null) : null;

        return Reply::json(200, self::success(200, $data) + ['cursor' => ['prev' => null, 'next' => $next]]);
    }

    private function isCustomerCreate(ReceivedRequest $request): bool
    {
        return $request->method === 'POST' && $request->path === self::CUSTOMERS_PATH;
    }

    private function storeCustomer(ReceivedRequest $request): Reply
    {
        $key = $request->header('idempotency-key');
        $previous = $key === null ? null : ($this->customersByKey[$key] ?? null);

        if (is_array($previous)) {
            return $previous['body'] === $request->body
                ? Reply::json(200, self::success(200, $previous['customer'] ?? null))
                : Reply::json(422, ['data' => null]);
        }

        try {
            $parsed = json_decode($request->body, true, 32, JSON_THROW_ON_ERROR);
        } catch (JsonException) {
            return Reply::json(400, ['data' => null]);
        }

        $email = is_array($parsed) && is_string($parsed['email'] ?? null) ? $parsed['email'] : '';
        $customer = ['customer_id' => sprintf('cus_%d', count($this->customers) + 1), 'email' => $email];
        $this->customers[] = $customer;

        if ($key !== null) {
            $this->customersByKey[$key] = ['body' => $request->body, 'customer' => $customer];
        }

        return Reply::json(201, self::success(201, $customer));
    }

    private function control(ReceivedRequest $request): Reply
    {
        try {
            $payload = $request->body === '' ? null : json_decode($request->body, true, 512, JSON_THROW_ON_ERROR);

            return match (substr($request->path, strlen(self::CONTROL_PREFIX))) {
                'queue' => $this->queue($payload),
                'state' => Reply::json(200, ['attempts' => $this->attempts, 'customers' => $this->customers]),
                'reset' => $this->reset(),
                'pages' => $this->servePages($payload),
                'contract' => $this->register($payload),
                default => Reply::json(404, ['message' => 'Unknown control call']),
            };
        } catch (JsonException | InvalidArgumentException $error) {
            return Reply::json(400, ['message' => $error->getMessage()]);
        }
    }

    private function queue(mixed $payload): Reply
    {
        if (!is_array($payload) || !array_is_list($payload)) {
            throw new InvalidArgumentException('The queue call takes a list of behaviours');
        }

        foreach ($payload as $item) {
            $this->behaviours[] = Behaviour::fromArray($item);
        }

        return self::accepted();
    }

    private function reset(): Reply
    {
        $this->behaviours = [];
        $this->attempts = [];
        $this->customers = [];
        $this->customersByKey = [];
        $this->pages = null;
        $this->contract = [];

        return self::accepted();
    }

    private function servePages(mixed $payload): Reply
    {
        if (!is_array($payload)) {
            throw new InvalidArgumentException('The pages call takes an object of pages keyed by cursor');
        }

        $pages = [];

        foreach ($payload as $cursor => $page) {
            if (!is_array($page) || !is_array($page['data'] ?? null) || !array_is_list($page['data'])) {
                throw new InvalidArgumentException('Every page needs a data list');
            }

            $next = $page['next'] ?? null;
            $pages[(string) $cursor] = ['data' => $page['data'], 'next' => is_string($next) ? $next : null];
        }

        $this->pages = $pages;

        return self::accepted();
    }

    private function register(mixed $payload): Reply
    {
        $method = is_array($payload) ? ($payload['method'] ?? null) : null;
        $template = is_array($payload) ? ($payload['template'] ?? null) : null;
        $status = is_array($payload) ? ($payload['status'] ?? null) : null;

        if (!is_array($payload) || !is_string($method) || !is_string($template) || !is_int($status)) {
            throw new InvalidArgumentException('The contract call takes a method, a template, and a status');
        }

        $this->contract[$method . ' ' . $template] = ($payload['hasBody'] ?? false) === true
            ? Reply::json($status, $payload['body'] ?? null)
            : Reply::raw($status, '');

        return self::accepted();
    }

    private static function accepted(): Reply
    {
        return Reply::json(200, ['accepted' => true]);
    }

    private static function success(int $status, mixed $data): array
    {
        return ['response' => ['type' => 'SUCCESS', 'code' => $status, 'message' => 'Success'], 'data' => $data];
    }
}
