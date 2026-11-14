import { extractPathParams, type PathParam, parseTag, toKebabCase, toPascalCase } from './utils'

export type HttpMethod = 'get' | 'post' | 'put' | 'patch' | 'delete'

export type ScopeName = 'billingEntityId' | 'messagingProfileId' | 'authAppId'

export type ResponseKind = 'envelope' | 'list' | 'body' | 'empty'

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
  hasQueryParams: boolean
  queryRequired: boolean
  scopes: ScopeName[]
  acceptsIdempotencyKey: boolean
  authMode: 'default' | 'none' | 'scimBearer'
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
  components?: { parameters?: Record<string, Record<string, unknown>> }
}

const HTTP_METHODS = new Set<string>(['get', 'post', 'put', 'patch', 'delete'])

const SCOPE_HEADER_NAMES: Readonly<Record<string, ScopeName>> = {
  'billing-entity-id': 'billingEntityId',
  'messaging-profile-id': 'messagingProfileId',
  'auth-app-id': 'authAppId',
}

const REQUEST_ID_HEADER = 'conjoin-request-id'
const IDEMPOTENCY_KEY_HEADER = 'idempotency-key'
const METHODS_WITHOUT_BODY = new Set<HttpMethod>(['get', 'delete'])
const NO_CONTENT_STATUS = '204'

const isRecord = (value: unknown): value is Record<string, unknown> =>
  Boolean(value) && typeof value === 'object' && !Array.isArray(value)

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

function resolveAuthMode(operation: Record<string, unknown>): OperationInfo['authMode'] {
  const security = operation.security

  if (!Array.isArray(security)) return 'default'
  if (security.length === 0) return 'none'
  if (security.every(requirement => isRecord(requirement) && Object.keys(requirement).length === 0)) return 'none'
  if (security.some(requirement => isRecord(requirement) && Object.hasOwn(requirement, 'scimBearer'))) {
    return 'scimBearer'
  }

  return 'default'
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

function assertBodyAllowed(httpMethod: HttpMethod, operationId: string): void {
  if (METHODS_WITHOUT_BODY.has(httpMethod)) {
    throw new Error(`${operationId} is a ${httpMethod.toUpperCase()} that declares a request body`)
  }
}

function buildOperation(spec: Spec, path: string, method: HttpMethod, operation: Record<string, unknown>) {
  const parameters = Array.isArray(operation.parameters) ? operation.parameters.map(p => resolveParameter(spec, p)) : []
  const scopes: ScopeName[] = []
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
      throw new Error(`${String(operation.operationId)} declares the unknown header ${String(parameter.name)}`)
    }
  }

  const queryParameters = parameters.filter(parameter => parameter.in === 'query')
  const requestBody = isRecord(operation.requestBody) ? operation.requestBody : undefined
  const requestContent = requestBody && isRecord(requestBody.content) ? requestBody.content : {}
  const requestContentType = Object.keys(requestContent)[0] ?? 'application/json'
  const requestMedia = isRecord(requestContent[requestContentType]) ? requestContent[requestContentType] : {}
  const success = readSuccessSchema(operation)
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
    responseKind: readResponseKind(success.properties, success.hasContent),
    hasQueryParams: queryParameters.length > 0,
    queryRequired: queryParameters.some(parameter => parameter.required === true),
    scopes,
    acceptsIdempotencyKey: method === 'post' && acceptsIdempotencyKey,
    authMode: resolveAuthMode(operation),
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
