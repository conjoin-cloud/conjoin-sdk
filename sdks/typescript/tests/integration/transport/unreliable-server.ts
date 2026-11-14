import { createServer, type IncomingMessage, type ServerResponse } from 'node:http'
import type { AddressInfo } from 'node:net'

export type ServerBehaviour =
  | { kind: 'answer' }
  | { kind: 'drop-before-store' }
  | { kind: 'drop-after-store' }
  | { kind: 'drop-during-response'; status?: number; delayMs?: number }
  | { kind: 'slow'; delayMs: number }
  | { kind: 'status'; status: number; headers?: Record<string, string>; body?: unknown }

export type ReceivedAttempt = {
  method: string
  path: string
  query: URLSearchParams
  headers: Record<string, string | undefined>
  body: string
  receivedAt: number
}

export type StoredCustomer = {
  customer_id: string
  email: string
}

export type ListPageSource = (cursor: string | null) => { data: unknown[]; next: string | null }

export type UnreliableServer = {
  baseUrl: string
  attempts: ReceivedAttempt[]
  storedCustomers: () => StoredCustomer[]
  queue: (...behaviours: ServerBehaviour[]) => void
  servePages: (source: ListPageSource) => void
  stop: () => Promise<void>
}

const LOOPBACK_HOST = '127.0.0.1'
const MAX_BODY_BYTES = 1_048_576
const CUSTOMERS_PATH = '/v1/billing/customers/'

const success = (status: number, data: unknown) => ({
  response: { type: 'SUCCESS', code: status, message: 'Success' },
  data,
})

const readBody = async (request: IncomingMessage): Promise<string> => {
  const chunks: Buffer[] = []
  let total = 0

  for await (const chunk of request) {
    const buffer = Buffer.isBuffer(chunk) ? chunk : Buffer.from(String(chunk))
    total += buffer.byteLength
    if (total > MAX_BODY_BYTES) throw new Error('The request body exceeded 1 MiB')
    chunks.push(buffer)
  }

  return Buffer.concat(chunks).toString('utf8')
}

const writeJson = (response: ServerResponse, status: number, body: unknown, headers: Record<string, string> = {}) => {
  const text = JSON.stringify(body)
  response.writeHead(status, {
    'content-type': 'application/json',
    'content-length': Buffer.byteLength(text),
    ...headers,
  })
  response.end(text)
}

const isAddressInfo = (address: string | AddressInfo | null): address is AddressInfo =>
  typeof address === 'object' && address !== null && 'port' in address

const flattenHeaders = (request: IncomingMessage): Record<string, string | undefined> =>
  Object.fromEntries(
    Object.entries(request.headers).map(([name, value]) => [name, Array.isArray(value) ? value.join(', ') : value]),
  )

export const startUnreliableServer = async (): Promise<UnreliableServer> => {
  const attempts: ReceivedAttempt[] = []
  const behaviours: ServerBehaviour[] = []
  const customersByKey = new Map<string, { body: string; customer: StoredCustomer }>()
  const customers: StoredCustomer[] = []
  let pageSource: ListPageSource | undefined

  const storeCustomer = (attempt: ReceivedAttempt): { status: number; customer?: StoredCustomer } => {
    const key = attempt.headers['idempotency-key']
    const previous = key === undefined ? undefined : customersByKey.get(key)

    if (previous !== undefined) {
      return previous.body === attempt.body ? { status: 200, customer: previous.customer } : { status: 422 }
    }

    const parsed: unknown = JSON.parse(attempt.body)
    const email = parsed && typeof parsed === 'object' && 'email' in parsed ? String(parsed.email) : ''
    const customer = { customer_id: `cus_${customers.length + 1}`, email }

    customers.push(customer)
    if (key !== undefined) customersByKey.set(key, { body: attempt.body, customer })

    return { status: 201, customer }
  }

  const answer = (response: ServerResponse, attempt: ReceivedAttempt): void => {
    if (attempt.method === 'POST' && attempt.path === CUSTOMERS_PATH) {
      const stored = storeCustomer(attempt)
      writeJson(response, stored.status, stored.customer ? success(stored.status, stored.customer) : { data: null })
      return
    }

    if (pageSource !== undefined && attempt.method === 'GET') {
      const page = pageSource(attempt.query.get('cursor[next]'))
      writeJson(response, 200, { ...success(200, page.data), cursor: { prev: null, next: page.next } })
      return
    }

    writeJson(response, 200, success(200, { path: attempt.path, method: attempt.method }))
  }

  const handle = async (request: IncomingMessage, response: ServerResponse): Promise<void> => {
    const url = new URL(request.url ?? '/', `http://${LOOPBACK_HOST}`)
    const attempt: ReceivedAttempt = {
      method: (request.method ?? 'GET').toUpperCase(),
      path: url.pathname,
      query: url.searchParams,
      headers: flattenHeaders(request),
      body: await readBody(request),
      receivedAt: Date.now(),
    }
    attempts.push(attempt)

    const behaviour = behaviours.shift() ?? { kind: 'answer' }

    if (behaviour.kind === 'drop-before-store') {
      request.socket.destroy()
      return
    }

    if (behaviour.kind === 'drop-after-store') {
      if (attempt.method === 'POST' && attempt.path === CUSTOMERS_PATH) storeCustomer(attempt)
      request.socket.destroy()
      return
    }

    if (behaviour.kind === 'drop-during-response') {
      if (attempt.method === 'POST' && attempt.path === CUSTOMERS_PATH) storeCustomer(attempt)
      response.writeHead(behaviour.status ?? 200, { 'content-type': 'application/json', 'content-length': '1000' })
      response.write('{"data":')
      setTimeout(() => response.destroy(), behaviour.delayMs ?? 20)
      return
    }

    if (behaviour.kind === 'slow') {
      await new Promise(resolve => setTimeout(resolve, behaviour.delayMs))
      if (!response.destroyed) answer(response, attempt)
      return
    }

    if (behaviour.kind === 'status') {
      writeJson(response, behaviour.status, behaviour.body ?? { data: null }, behaviour.headers)
      return
    }

    answer(response, attempt)
  }

  const server = createServer((request, response) => {
    handle(request, response).catch(() => {
      if (!response.headersSent) writeJson(response, 400, { data: null })
    })
  })

  await new Promise<void>((resolve, reject) => {
    server.once('error', reject)
    server.listen(0, LOOPBACK_HOST, () => {
      server.off('error', reject)
      resolve()
    })
  })

  const address = server.address()

  if (!isAddressInfo(address)) {
    server.close()
    throw new Error('The unreliable server did not bind to a TCP address')
  }

  return {
    baseUrl: `http://${LOOPBACK_HOST}:${address.port}`,
    attempts,
    storedCustomers: () => [...customers],
    queue: (...next) => {
      behaviours.push(...next)
    },
    servePages: source => {
      pageSource = source
    },
    stop: () =>
      new Promise((resolve, reject) => {
        server.closeAllConnections()
        server.close(error => (error ? reject(error) : resolve()))
      }),
  }
}
