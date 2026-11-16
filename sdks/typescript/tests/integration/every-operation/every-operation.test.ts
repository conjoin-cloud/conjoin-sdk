import { readdirSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'
import { afterAll, afterEach, beforeAll, describe, expect, it } from 'vitest'
import { collectResourceGroups } from '../../../codegen/operations'
import { factoryName, resolveMethodEntries } from '../../../codegen/render'
import { createConjoinClient } from '../../../src/core/client'
import type { ConjoinClient } from '../../../src/core/types'
import { type ConjoinContractServer, startConjoinContractServer } from '../contract-server/conjoin-contract-server'
import {
  type ConjoinOpenApiDocumentFile,
  createOpenApiContract,
  loadConjoinOpenApiDocument,
} from '../contract-server/openapi-contract'
import type { RecordedContractRequest } from '../contract-server/request-recorder'
import { SchemaSampler } from './schema-sample'

type JsonRecord = Record<string, unknown>
type GeneratedFactory = (client: ConjoinClient, scim?: { scimToken?: string }) => Record<string, unknown>

type OperationCase = {
  name: string
  factory: string
  methodName: string
  httpMethod: string
  pathTemplate: string
  operation: JsonRecord
}

const API_KEY = 'cak_test_harbourledgerintegration'
const PUBLISHABLE_KEY = 'cpk_test_harbourledgerintegration'
const SESSION_TOKEN = 'sess_harbourledger_signedin'
const PORTAL_TICKET = 'ptk_harbourledger_portal'
const PORTAL_TICKET_HEADER = 'x-portal-ticket'
const SCIM_TOKEN = 'scim_harbourledger_directory'
const EXPECTED_AUTHORIZATION_BY_SCHEME: Readonly<Record<string, string>> = {
  conjoinApiKey: `Bearer ${API_KEY}`,
  scimBearer: `Bearer ${SCIM_TOKEN}`,
  conjoinPublishableKey: `Bearer ${PUBLISHABLE_KEY}`,
  conjoinSessionBearer: `Bearer ${SESSION_TOKEN}`,
}
const SESSION_SCHEMES = new Set(['conjoinSessionBearer', 'conjoinSessionCookie'])
const PORTAL_TICKET_SCHEMES = new Set(['conjoinPortalTicketHeader', 'conjoinPortalTicketQuery'])
const SDK_MANAGED_HEADER_NAMES = new Set([
  'billing-entity-id',
  'messaging-profile-id',
  'auth-app-id',
  'idempotency-key',
  'conjoin-request-id',
])
const SCOPE_HEADER_VALUES: Readonly<Record<string, string>> = {
  'billing-entity-id': 'ent_harbourledger',
  'messaging-profile-id': 'mpr_harbourledger',
  'auth-app-id': 'app_harbourledger',
}
const SERVER_IDEMPOTENCY_KEY_PATTERN = /^[A-Za-z0-9\-_:.]{1,64}$/
const HTTP_METHODS = ['get', 'post', 'put', 'patch', 'delete']
const NO_CONTENT_STATUS = '204'

const DOCUMENTS: ReadonlyArray<{
  file: ConjoinOpenApiDocumentFile
  moduleDirectory: string
  clientKey: { apiKey: string } | { publishableKey: string }
}> = [
  { file: 'openapi.json', moduleDirectory: 'modules', clientKey: { apiKey: API_KEY } },
  { file: 'openapi-frontend.json', moduleDirectory: 'frontend', clientKey: { publishableKey: PUBLISHABLE_KEY } },
]

const generatedDirectory = resolve(dirname(fileURLToPath(import.meta.url)), '../../../src/generated')

const isRecord = (value: unknown): value is JsonRecord =>
  Boolean(value) && typeof value === 'object' && !Array.isArray(value)

const resolveRef = (document: JsonRecord, value: unknown): JsonRecord => {
  if (!isRecord(value)) return {}
  if (typeof value.$ref !== 'string') return value

  const target = value.$ref
    .replace(/^#\//, '')
    .split('/')
    .reduce<unknown>((node, key) => (isRecord(node) ? node[key] : undefined), document)

  return resolveRef(document, target)
}

const readParameters = (document: JsonRecord, operation: JsonRecord): JsonRecord[] =>
  Array.isArray(operation.parameters) ? operation.parameters.map(parameter => resolveRef(document, parameter)) : []

const readHeaderParameterNames = (document: JsonRecord, operation: JsonRecord): Set<string> =>
  new Set(
    readParameters(document, operation)
      .filter(parameter => parameter.in === 'header')
      .map(parameter => String(parameter.name).toLowerCase()),
  )

const readSuccessResponse = (document: JsonRecord, operation: JsonRecord): { status: string; schema: unknown } => {
  const responses = isRecord(operation.responses) ? operation.responses : {}
  const status = Object.keys(responses).find(code => code.startsWith('2'))

  if (status === undefined) throw new Error(`${String(operation.operationId)} declares no success response`)

  const response = resolveRef(document, responses[status])
  const content = isRecord(response.content) ? response.content : {}
  const media = isRecord(content['application/json']) ? content['application/json'] : {}

  return { status, schema: status === NO_CONTENT_STATUS ? undefined : media.schema }
}

const readRequestBody = (
  document: JsonRecord,
  operation: JsonRecord,
): { type: string; schema: unknown } | undefined => {
  if (operation.requestBody === undefined) return undefined

  const requestBody = resolveRef(document, operation.requestBody)
  const content = isRecord(requestBody.content) ? requestBody.content : {}
  const [type] = Object.keys(content)

  if (type === undefined) throw new Error(`${String(operation.operationId)} declares a body without content`)

  return { type, schema: resolveRef(document, content[type]).schema }
}

const readRequestIdPattern = (document: JsonRecord, operation: JsonRecord): RegExp => {
  const parameter = readParameters(document, operation).find(
    candidate => candidate.in === 'header' && String(candidate.name).toLowerCase() === 'conjoin-request-id',
  )
  const schema = resolveRef(document, parameter?.schema)

  if (typeof schema.pattern !== 'string') throw new Error('The document declares no Conjoin-Request-Id pattern')

  return new RegExp(schema.pattern)
}

const readSecurityScheme = (operation: JsonRecord): string | undefined => {
  const security = Array.isArray(operation.security) ? operation.security : []
  const [requirement] = security

  return isRecord(requirement) ? Object.keys(requirement)[0] : undefined
}

const pathParameterValue = (name: string): string => `ledger/${name} 7?#%ä`

const listDocumentOperations = (document: JsonRecord): string[] => {
  const paths = isRecord(document.paths) ? document.paths : {}

  return Object.entries(paths).flatMap(([path, item]) =>
    HTTP_METHODS.filter(method => isRecord(item) && isRecord(item[method])).map(
      method => `${method.toUpperCase()} ${path}`,
    ),
  )
}

const buildCases = (document: JsonRecord): OperationCase[] =>
  collectResourceGroups(document as Parameters<typeof collectResourceGroups>[0]).flatMap(group =>
    resolveMethodEntries(group).map(({ name, op }) => {
      const paths = isRecord(document.paths) ? document.paths : {}
      const item = isRecord(paths[op.path]) ? paths[op.path] : {}
      const operation = isRecord(item) && isRecord(item[op.httpMethod]) ? item[op.httpMethod] : {}

      return {
        name: `${factoryName(group)}.${name}`,
        factory: factoryName(group),
        methodName: name,
        httpMethod: op.httpMethod.toUpperCase(),
        pathTemplate: op.path,
        operation: isRecord(operation) ? operation : {},
      }
    }),
  )

const loadFactories = async (moduleDirectory: string): Promise<Map<string, GeneratedFactory>> => {
  const directory = resolve(generatedDirectory, moduleDirectory)
  const factories = new Map<string, GeneratedFactory>()

  for (const file of readdirSync(directory).filter(name => name.endsWith('.ts') && !name.endsWith('-index.ts'))) {
    const exports: JsonRecord = await import(pathToFileURL(resolve(directory, file)).href)

    for (const [name, value] of Object.entries(exports)) {
      if (name.startsWith('create') && typeof value === 'function') factories.set(name, value as GeneratedFactory)
    }
  }

  return factories
}

const expectScopedRequest = (
  request: RecordedContractRequest,
  testCase: OperationCase,
  document: JsonRecord,
  pathParams: Record<string, string>,
): void => {
  const declaredHeaders = readHeaderParameterNames(document, testCase.operation)

  expect(request).toMatchObject({ method: testCase.httpMethod, pathTemplate: testCase.pathTemplate, pathParams })
  expect(request.headers['conjoin-request-id']).toMatch(readRequestIdPattern(document, testCase.operation))

  for (const [header, value] of Object.entries(SCOPE_HEADER_VALUES)) {
    expect(request.headers[header]).toBe(declaredHeaders.has(header) ? value : undefined)
  }

  if (testCase.httpMethod === 'POST' && declaredHeaders.has('idempotency-key')) {
    expect(request.headers['idempotency-key']).toMatch(SERVER_IDEMPOTENCY_KEY_PATTERN)
  } else {
    expect(request.headers['idempotency-key']).toBeUndefined()
  }

  const scheme = readSecurityScheme(testCase.operation)
  const isPortalTicketOperation = scheme !== undefined && PORTAL_TICKET_SCHEMES.has(scheme)

  expect(request.headers.authorization).toBe(
    scheme === undefined ? undefined : EXPECTED_AUTHORIZATION_BY_SCHEME[scheme],
  )
  expect(request.headers[PORTAL_TICKET_HEADER]).toBe(isPortalTicketOperation ? PORTAL_TICKET : undefined)
  expect(JSON.stringify(request.query)).not.toContain(PORTAL_TICKET)
}

const hasCallerSuppliedHeaders = (document: JsonRecord, operation: JsonRecord): boolean =>
  readParameters(document, operation).some(
    parameter => parameter.in === 'header' && !SDK_MANAGED_HEADER_NAMES.has(String(parameter.name).toLowerCase()),
  )

const expectReturnedData = (result: unknown, body: unknown, schema: unknown, document: JsonRecord): void => {
  if (body === undefined) {
    expect(result).toBeUndefined()
    return
  }

  const properties = resolveRef(document, schema).properties

  if (!isRecord(properties) || !('data' in properties) || !isRecord(body)) {
    expect(result).toEqual(body)
    return
  }

  if ('cursor' in properties && isRecord(result)) {
    expect(result.data).toEqual(body.data)
    expect(result.cursor).toEqual(body.cursor)
    return
  }

  expect(result).toEqual(body.data)
}

describe.each(DOCUMENTS)('every operation in $file', ({ file, moduleDirectory, clientKey }) => {
  const document = loadConjoinOpenApiDocument(file) as unknown as JsonRecord
  const sampler = new SchemaSampler(document)
  const cases = buildCases(document)
  let server: ConjoinContractServer | undefined
  let client: ConjoinClient | undefined
  let factories = new Map<string, GeneratedFactory>()

  beforeAll(async () => {
    server = await startConjoinContractServer({
      openApiContract: createOpenApiContract(loadConjoinOpenApiDocument(file)),
    })
    client = createConjoinClient({
      ...clientKey,
      baseUrl: server.baseUrl,
      billingEntityId: SCOPE_HEADER_VALUES['billing-entity-id'],
      messagingProfileId: SCOPE_HEADER_VALUES['messaging-profile-id'],
      authAppId: SCOPE_HEADER_VALUES['auth-app-id'],
      retry: { maxRetries: 0 },
    })
    factories = await loadFactories(moduleDirectory)
  })

  afterEach(() => {
    server?.reset()
  })

  afterAll(async () => {
    await server?.stop()
  })

  it('generates exactly one method for every operation in the document', () => {
    const generated = cases.map(testCase => `${testCase.httpMethod} ${testCase.pathTemplate}`)

    expect(new Set(generated).size).toBe(generated.length)
    expect([...generated].sort()).toEqual(listDocumentOperations(document).sort())
  })

  it('exposes only the generated methods on every factory', () => {
    if (client === undefined) throw new Error('The client did not start')

    const expected = new Map<string, string[]>()
    for (const testCase of cases)
      expected.set(testCase.factory, [...(expected.get(testCase.factory) ?? []), testCase.methodName])

    expect([...factories.keys()].sort()).toEqual([...expected.keys()].sort())

    for (const [name, factory] of factories) {
      expect(Object.keys(factory(client)).sort()).toEqual((expected.get(name) ?? []).sort())
    }
  })

  it.each(cases)('$name sends the documented request and returns the documented data', async testCase => {
    if (server === undefined || client === undefined) throw new Error('The contract server did not start')

    const factory = factories.get(testCase.factory)
    if (factory === undefined) throw new Error(`${testCase.factory} is not exported`)

    const method = factory(client, { scimToken: SCIM_TOKEN })[testCase.methodName]
    if (typeof method !== 'function') throw new Error(`${testCase.name} is not a function`)

    const pathParams = Object.fromEntries(
      [...testCase.pathTemplate.matchAll(/\{([^}]+)\}/g)].map(([, name]) => [name, pathParameterValue(String(name))]),
    )
    const args: unknown[] = Object.values(pathParams)
    const requestBody = readRequestBody(document, testCase.operation)
    const data = requestBody === undefined ? undefined : sampler.sample(requestBody.schema)

    if (requestBody !== undefined) args.push(data)

    const queryParameters = readParameters(document, testCase.operation).filter(parameter => parameter.in === 'query')

    if (queryParameters.length > 0) {
      const required = queryParameters.filter(parameter => parameter.required === true)
      args.push(
        required.length > 0
          ? Object.fromEntries(required.map(parameter => [String(parameter.name), sampler.sample(parameter.schema)]))
          : undefined,
      )
    }

    const scheme = readSecurityScheme(testCase.operation)

    if (scheme !== undefined && PORTAL_TICKET_SCHEMES.has(scheme)) {
      args.push({ portalTicket: PORTAL_TICKET })
    } else if (hasCallerSuppliedHeaders(document, testCase.operation)) {
      args.push(undefined)
    }

    if (scheme !== undefined && SESSION_SCHEMES.has(scheme)) args.push(SESSION_TOKEN)

    const success = readSuccessResponse(document, testCase.operation)
    const body = success.schema === undefined ? undefined : sampler.sample(success.schema)

    server.register({
      method: testCase.httpMethod,
      path: testCase.pathTemplate,
      handler: () => ({ status: Number(success.status), headers: { 'content-type': 'application/json' }, body }),
    })

    const result = await method(...args)
    const requests = server.recorder.all()

    expect(requests).toHaveLength(1)

    const [request] = requests
    if (request === undefined) throw new Error('The contract server recorded no request')

    expectScopedRequest(request, testCase, document, pathParams)

    if (requestBody?.type === 'application/json') expect(request.body).toEqual(data)

    expectReturnedData(result, body, success.schema, document)
  })
})
