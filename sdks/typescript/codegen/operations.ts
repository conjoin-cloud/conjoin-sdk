import { type AuthMode, readPortalTicketHeader, resolveAuthMode } from './security'
import { extractPathParams, isRecord, type PathParam, parseTag, toKebabCase, toPascalCase } from './utils'

export type HttpMethod = 'get' | 'post' | 'put' | 'patch' | 'delete'

export type ScopeName = 'billingEntityId' | 'messagingProfileId' | 'authAppId'

export type ResponseKind = 'envelope' | 'list' | 'body' | 'empty'

export type CursorLocation = 'query' | 'body' | 'none'

export type DeclaredHeader = {
  name: string
  argumentName: string
  required: boolean
  minLength?: number
  maxLength?: number
  pattern?: string
}

export type OperationInfo = {
  operationId: string
  httpMethod: HttpMethod
  path: string
  pathParams: PathParam[]
  hasRequestBody: boolean
  requestBodyRequired: boolean
  requestContentType: string
  responseContentType: string
  successCode: string
  responseKind: ResponseKind
  cursorLocation: CursorLocation
  hasQueryParams: boolean
  queryRequired: boolean
  scopes: ScopeName[]
  acceptsIdempotencyKey: boolean
  declaredHeaders: DeclaredHeader[]
  authMode: AuthMode
}

export type ResourceGroup = {
  service: string
  resource: string
  servicePascal: string
  resourcePascal: string
  operations: OperationInfo[]
}

type Spec = {
  paths: Record<string, Record<string, unknown>>
  components?: {
    parameters?: Record<string, Record<string, unknown>>
    schemas?: Record<string, unknown>
    securitySchemes?: Record<string, unknown>
  }
}

const HTTP_METHODS = new Set<string>(['get', 'post', 'put', 'patch', 'delete'])

const SCOPE_HEADER_NAMES: Readonly<Record<string, ScopeName>> = {
  'billing-entity-id': 'billingEntityId',
  'messaging-profile-id': 'messagingProfileId',
  'auth-app-id': 'authAppId',
}

const REQUEST_ID_HEADER = 'conjoin-request-id'
const IDEMPOTENCY_KEY_HEADER = 'idempotency-key'
const RESERVED_HEADER_NAMES = new Set([
  'accept',
  'authorization',
  'content-length',
  'content-type',
  'cookie',
  'host',
  'user-agent',
  'x-conjoin-api-version',
  'x-conjoin-sdk-version',
])
const METHODS_WITHOUT_BODY = new Set<HttpMethod>(['get', 'delete'])
const NO_CONTENT_STATUS = '204'

function resolveParameter(spec: Spec, raw: unknown): Record<string, unknown> {
  if (!isRecord(raw)) {
    throw new Error('A parameter is not an object')
  }

  const ref = raw.$ref

  if (typeof ref !== 'string') {
    return raw
  }

  const name = ref.replace('#/components/parameters/', '')
  const resolved = spec.components?.parameters?.[name]

  if (!resolved) {
    throw new Error(`Unresolved parameter reference ${ref}`)
  }

  return resolved
}

function readSuccessSchema(operation: Record<string, unknown>): {
  successCode: string
  contentType: string
  properties: Record<string, unknown> | undefined
  hasContent: boolean
} {
  const responses = isRecord(operation.responses) ? operation.responses : {}
  const successCode = Object.keys(responses).find(code => code.startsWith('2')) ?? '200'
  const success = isRecord(responses[successCode]) ? responses[successCode] : {}
  const content = isRecord(success.content) ? success.content : undefined
  const contentType = content ? (Object.keys(content)[0] ?? 'application/json') : 'application/json'
  const media = content && isRecord(content[contentType]) ? content[contentType] : undefined
  const schema = media && isRecord(media.schema) ? media.schema : undefined
  const properties = schema && isRecord(schema.properties) ? schema.properties : undefined

  return { successCode, contentType, properties, hasContent: media !== undefined && successCode !== NO_CONTENT_STATUS }
}

function readResponseKind(properties: Record<string, unknown> | undefined, hasContent: boolean): ResponseKind {
  if (!hasContent) return 'empty'
  if (!properties || !('data' in properties)) return 'body'

  const data = properties.data

  return isRecord(data) && data.type === 'array' && 'cursor' in properties ? 'list' : 'envelope'
}

function resolveSchema(spec: Spec, raw: unknown): Record<string, unknown> {
  if (!isRecord(raw) || typeof raw.$ref !== 'string') return isRecord(raw) ? raw : {}

  const resolved = spec.components?.schemas?.[raw.$ref.replace('#/components/schemas/', '')]

  if (!isRecord(resolved)) throw new Error(`Unresolved schema reference ${raw.$ref}`)

  return resolved
}

function readCursorLocation(
  spec: Spec,
  operationId: string,
  responseKind: ResponseKind,
  queryParameters: Record<string, unknown>[],
  requestContent: Record<string, unknown>,
): CursorLocation {
  if (responseKind !== 'list') return 'none'

  const media = requestContent['application/json']
  const bodySchema = resolveSchema(spec, isRecord(media) ? media.schema : undefined)
  const bodyProperties = isRecord(bodySchema.properties) ? bodySchema.properties : {}
  const inBody = 'cursor' in bodyProperties
  const inQuery = queryParameters.some(parameter => parameter.name === 'cursor')

  if (inBody && inQuery) throw new Error(`${operationId} declares a cursor in both its query and its body`)

  if (inBody) return 'body'

  return inQuery ? 'query' : 'none'
}

function assertBodyAllowed(httpMethod: HttpMethod, operationId: string): void {
  if (METHODS_WITHOUT_BODY.has(httpMethod)) {
    throw new Error(`${operationId} is a ${httpMethod.toUpperCase()} that declares a request body`)
  }
}

const toHeaderArgumentName = (headerName: string): string =>
  headerName
    .toLowerCase()
    .split('-')
    .map((part, index) => (index === 0 ? part : part.charAt(0).toUpperCase() + part.slice(1)))
    .join('')

const readOptionalBound = (schema: Record<string, unknown>, key: string, operationId: string): number | undefined => {
  const value = schema[key]

  if (value === undefined) return undefined
  if (typeof value !== 'number' || !Number.isSafeInteger(value) || value < 0) {
    throw new Error(`${operationId} declares a header whose ${key} is not a whole number`)
  }

  return value
}

function readDeclaredHeader(parameter: Record<string, unknown>, operationId: string): DeclaredHeader {
  const name = String(parameter.name)

  if (RESERVED_HEADER_NAMES.has(name.toLowerCase())) {
    throw new Error(`${operationId} declares the reserved header ${name} as a parameter`)
  }

  const schema = isRecord(parameter.schema) ? parameter.schema : {}

  if (schema.type !== 'string') {
    throw new Error(`${operationId} declares the header ${name} without a string schema`)
  }

  const pattern = schema.pattern

  if (pattern !== undefined && typeof pattern !== 'string') {
    throw new Error(`${operationId} declares the header ${name} with a pattern that is not a string`)
  }

  return {
    name,
    argumentName: toHeaderArgumentName(name),
    required: parameter.required === true,
    minLength: readOptionalBound(schema, 'minLength', operationId),
    maxLength: readOptionalBound(schema, 'maxLength', operationId),
    pattern,
  }
}

function buildOperation(spec: Spec, path: string, method: HttpMethod, operation: Record<string, unknown>) {
  const operationId = String(operation.operationId)
  const parameters = Array.isArray(operation.parameters) ? operation.parameters.map(p => resolveParameter(spec, p)) : []
  const scopes: ScopeName[] = []
  const declaredHeaders: DeclaredHeader[] = []
  let acceptsIdempotencyKey = false

  for (const parameter of parameters) {
    if (parameter.in !== 'header') continue

    const headerName = String(parameter.name).toLowerCase()
    const scope = SCOPE_HEADER_NAMES[headerName]

    if (scope) {
      scopes.push(scope)
    } else if (headerName === IDEMPOTENCY_KEY_HEADER) {
      acceptsIdempotencyKey = true
    } else if (headerName !== REQUEST_ID_HEADER) {
      declaredHeaders.push(readDeclaredHeader(parameter, operationId))
    }
  }

  const authMode = resolveAuthMode(operation, operationId)

  if (authMode === 'portalTicket') declaredHeaders.push(readPortalTicketHeader(spec.components?.securitySchemes))

  const argumentNames = new Set(declaredHeaders.map(header => header.argumentName))

  if (argumentNames.size !== declaredHeaders.length) {
    throw new Error(`${operationId} declares two headers that generate the same argument`)
  }

  const queryParameters = parameters.filter(parameter => parameter.in === 'query')
  const requestBody = isRecord(operation.requestBody) ? operation.requestBody : undefined
  const requestContent = requestBody && isRecord(requestBody.content) ? requestBody.content : {}
  const requestContentType = Object.keys(requestContent)[0] ?? 'application/json'
  const success = readSuccessSchema(operation)
  const responseKind = readResponseKind(success.properties, success.hasContent)
  if (requestBody !== undefined) assertBodyAllowed(method, String(operation.operationId))

  return {
    operationId: String(operation.operationId),
    httpMethod: method,
    path,
    pathParams: extractPathParams(path),
    hasRequestBody: requestBody !== undefined,
    requestBodyRequired: requestBody?.required === true,
    requestContentType,
    responseContentType: success.contentType,
    successCode: success.successCode,
    responseKind,
    cursorLocation: readCursorLocation(spec, operationId, responseKind, queryParameters, requestContent),
    hasQueryParams: queryParameters.length > 0,
    queryRequired: queryParameters.some(parameter => parameter.required === true),
    scopes,
    acceptsIdempotencyKey: method === 'post' && acceptsIdempotencyKey,
    declaredHeaders,
    authMode,
  } satisfies OperationInfo
}

export function collectResourceGroups(spec: Spec): ResourceGroup[] {
  const groups = new Map<string, ResourceGroup>()

  for (const [path, methods] of Object.entries(spec.paths)) {
    for (const [method, operation] of Object.entries(methods)) {
      if (!HTTP_METHODS.has(method) || !isRecord(operation)) continue

      const tags = Array.isArray(operation.tags) ? operation.tags : []
      const tag = typeof tags[0] === 'string' ? tags[0] : undefined

      if (!tag || typeof operation.operationId !== 'string') {
        throw new Error(`${method.toUpperCase()} ${path} has no tag or operationId`)
      }

      const { service, resource } = parseTag(tag)

      if (!resource) {
        throw new Error(`${method.toUpperCase()} ${path} has the tag ${tag} without a resource`)
      }

      const key = `${service}-${toKebabCase(resource)}`
      const group = groups.get(key) ?? {
        service,
        resource,
        servicePascal: toPascalCase(service),
        resourcePascal: toPascalCase(resource),
        operations: [],
      }

      group.operations.push(buildOperation(spec, path, method as HttpMethod, operation))
      groups.set(key, group)
    }
  }

  return Array.from(groups.values())
}
