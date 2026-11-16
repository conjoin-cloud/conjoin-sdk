import type { OperationInfo, ResourceGroup } from './operations'
import { buildRuntimePath, lcfirst, operationIdToMethodName, pluralize, toKebabCase } from './utils'

export type MethodEntry = { name: string; op: OperationInfo }

const pascalOf = (name: string): string => name.charAt(0).toUpperCase() + name.slice(1)

export const moduleFileName = (group: ResourceGroup): string => `${group.service}-${toKebabCase(group.resource)}`

export const factoryName = (group: ResourceGroup): string =>
  `create${group.servicePascal}${pluralize(group.resourcePascal)}`

function typeAliases(op: OperationInfo, methodName: string): string[] {
  const pascal = pascalOf(methodName)
  const operation = `operations['${op.operationId}']`
  const lines: string[] = []

  if (op.hasRequestBody) {
    lines.push(`type ${pascal}Body = NonNullable<${operation}['requestBody']>['content']['${op.requestContentType}']`)
  }

  const content = `${operation}['responses']['${op.successCode}']['content']['${op.responseContentType}']`

  if (op.responseKind === 'list') {
    lines.push(`type ${pascal}Data = NonNullable<${content}['data']>[number]`)
  } else if (op.responseKind === 'envelope') {
    lines.push(`type ${pascal}Data = NonNullable<${content}['data']>`)
  } else if (op.responseKind === 'body') {
    lines.push(`type ${pascal}Response = ${content}`)
  }

  if (op.hasQueryParams) {
    lines.push(`type ${pascal}Query = NonNullable<${operation}['parameters']['query']>`)
  }

  if (op.declaredHeaders.length > 0) {
    const fields = op.declaredHeaders.map(header => `${header.argumentName}${header.required ? '' : '?'}: string`)
    lines.push(`type ${pascal}Headers = { ${fields.join('; ')} }`)
  }

  return lines
}

const headerRulesName = (methodName: string): string => `${methodName}HeaderRules`

function headerRulesSource(op: OperationInfo, methodName: string): string {
  const rules = op.declaredHeaders.map(header => {
    const fields = [
      `name: ${JSON.stringify(header.name)}`,
      `argumentName: ${JSON.stringify(header.argumentName)}`,
      `required: ${header.required}`,
      ...(header.minLength === undefined ? [] : [`minLength: ${header.minLength}`]),
      ...(header.maxLength === undefined ? [] : [`maxLength: ${header.maxLength}`]),
      ...(header.pattern === undefined ? [] : [`pattern: ${JSON.stringify(header.pattern)}`]),
    ]

    return `  { ${fields.join(', ')} },`
  })

  return [`const ${headerRulesName(methodName)}: readonly ConjoinDeclaredHeaderRule[] = [`, ...rules, ']'].join('\n')
}

const hasRequiredHeader = (op: OperationInfo): boolean => op.declaredHeaders.some(header => header.required)

function lockedAuthField(op: OperationInfo): string | undefined {
  if (op.authMode === 'none' || op.authMode === 'portalTicket') return "auth: { type: 'none' }"
  if (op.authMode === 'publishableKey') return "auth: { type: 'publishableKey' }"
  if (op.authMode === 'session') return "auth: { type: 'session', token: sessionToken }"

  return undefined
}

function resultType(op: OperationInfo, pascal: string): string {
  if (op.responseKind === 'empty') return 'undefined'
  if (op.responseKind === 'body') return `${pascal}Response`

  return `${pascal}Data`
}

function fetchMethod(op: OperationInfo): string {
  if (op.responseKind === 'list') return 'client.fetchList'
  if (op.responseKind === 'envelope') return 'client.fetch'

  return 'client.fetchJson'
}

function methodSource(op: OperationInfo, methodName: string): string {
  const pascal = pascalOf(methodName)
  const params = op.pathParams.map(p => `${p.camelName}: string`)
  const sendsBody = op.hasRequestBody

  if (op.hasRequestBody) {
    params.push(`data${op.requestBodyRequired ? '' : '?'}: ${pascal}Body`)
  }

  if (op.hasQueryParams) {
    params.push(`query${op.queryRequired ? '' : '?'}: ${pascal}Query`)
  }

  if (op.declaredHeaders.length > 0) {
    const headersRequired = hasRequiredHeader(op)

    if (headersRequired && params.some(param => param.includes('?:'))) {
      throw new Error(`${op.operationId} declares a required header after an optional argument`)
    }

    params.push(`headers${headersRequired ? '' : '?'}: ${pascal}Headers`)
  }

  if (op.authMode === 'session') params.push('sessionToken?: string')

  params.push('options?: ConjoinCallOptions')

  const defaults = op.authMode === 'scimBearer' ? ['...scimBearerRequestOptions(scim.scimToken)'] : []
  const lockedAuth = lockedAuthField(op)

  const fields = [
    ...defaults,
    '...options',
    ...(lockedAuth === undefined ? [] : [lockedAuth]),
    `method: '${op.httpMethod.toUpperCase()}'`,
  ]
  if (sendsBody) fields.push('body: data')
  if (sendsBody && op.requestContentType.toLowerCase() === 'multipart/form-data') {
    fields.push("contentType: 'multipart/form-data'")
  }
  if (op.hasQueryParams) fields.push('query: query as Record<string, unknown> | undefined')
  if (op.scopes.length > 0) fields.push(`scopes: [${op.scopes.map(scope => `'${scope}'`).join(', ')}]`)
  if (op.acceptsIdempotencyKey) fields.push('acceptsIdempotencyKey: true')
  if (op.responseKind === 'list' && op.cursorLocation !== 'query') fields.push(`cursorLocation: '${op.cursorLocation}'`)
  if (op.declaredHeaders.length > 0) {
    fields.push(`declaredHeaders: { rules: ${headerRulesName(methodName)}, values: headers }`)
  }

  const encodedParams = new Map(op.pathParams.map(p => [p.camelName, `\${encodePathParam(${p.camelName})}`]))
  const runtimePath = buildRuntimePath(op.path, op.pathParams).replace(
    /\$\{(\w+)\}/g,
    (match, name: string) => encodedParams.get(name) ?? match,
  )
  const pathLiteral = op.pathParams.length > 0 ? `\`${runtimePath}\`` : `'${runtimePath}'`

  return `    ${methodName}: (${params.join(', ')}) =>\n      ${fetchMethod(op)}<${resultType(op, pascal)}>(${pathLiteral}, { ${fields.join(', ')} }),`
}

function resolveCollisions(entries: MethodEntry[], resourcePascal: string): void {
  const counts = new Map<string, number>()
  for (const entry of entries) counts.set(entry.name, (counts.get(entry.name) ?? 0) + 1)

  for (const entry of entries) {
    if ((counts.get(entry.name) ?? 0) <= 1) continue

    if (entry.op.responseKind === 'list') {
      const base = entry.name
      entry.name = base === 'read' || base === 'get' ? 'list' : `list${pascalOf(base)}`
    } else if (entry.op.operationId.includes(pluralize(resourcePascal))) {
      entry.name = pluralize(entry.name)
    }
  }

  const finalCounts = new Map<string, number>()
  for (const entry of entries) finalCounts.set(entry.name, (finalCounts.get(entry.name) ?? 0) + 1)
  for (const entry of entries) {
    if ((finalCounts.get(entry.name) ?? 0) > 1) entry.name = lcfirst(entry.op.operationId)
  }

  const seen = new Set<string>()
  for (const entry of entries) {
    if (seen.has(entry.name)) throw new Error(`Two operations both generate the method ${entry.name}`)
    seen.add(entry.name)
  }
}

export function resolveMethodEntries(group: ResourceGroup): MethodEntry[] {
  const entries: MethodEntry[] = group.operations.map(op => ({
    name: operationIdToMethodName(op.operationId, group.servicePascal, group.resourcePascal),
    op,
  }))

  resolveCollisions(entries, group.resourcePascal)

  return entries
}

export function renderModule(group: ResourceGroup, apiTypesImport: string, coreImport: string): string {
  const usesScim = group.operations.some(op => op.authMode === 'scimBearer')
  const usesPathParams = group.operations.some(op => op.pathParams.length > 0)
  const usesDeclaredHeaders = group.operations.some(op => op.declaredHeaders.length > 0)
  const entries = resolveMethodEntries(group)

  const coreTypes = [
    'ConjoinCallOptions',
    'ConjoinClient',
    ...(usesDeclaredHeaders ? ['ConjoinDeclaredHeaderRule'] : []),
    ...(usesScim ? ['RequestOptions'] : []),
  ]
  const lines: string[] = [
    ...(usesPathParams ? [`import { encodePathParam } from '${coreImport}/path'`] : []),
    `import type { ${coreTypes.join(', ')} } from '${coreImport}/types'`,
    `import type { operations } from '${apiTypesImport}'`,
    '',
  ]

  const seenTypes = new Set<string>()
  for (const { name, op } of entries) {
    for (const line of typeAliases(op, name)) {
      const typeName = line.match(/^type (\w+)/)?.[1]
      if (typeName && !seenTypes.has(typeName)) {
        seenTypes.add(typeName)
        lines.push(line)
      }
    }
  }

  lines.push('')

  for (const { name, op } of entries) {
    if (op.declaredHeaders.length > 0) lines.push(headerRulesSource(op, name), '')
  }

  if (usesScim) {
    lines.push(
      'export type AuthSCIMOptions = {',
      '  scimToken?: string',
      '}',
      '',
      'function scimBearerRequestOptions(scimToken: string | undefined): RequestOptions {',
      '  if (!scimToken || scimToken.trim().length === 0) {',
      "    throw new Error('SCIM token is required for tenant SCIM operations')",
      '  }',
      '',
      "  return { auth: { type: 'bearer', token: scimToken } }",
      '}',
      '',
    )
  }

  const scimParam = usesScim ? ', scim: AuthSCIMOptions = {}' : ''
  lines.push(`export function ${factoryName(group)}(client: ConjoinClient${scimParam}) {`, '  return {')
  lines.push(entries.map(({ name, op }) => methodSource(op, name)).join('\n\n'))
  lines.push('  }', '}', '')

  return lines.join('\n')
}

export function renderBarrel(groups: ResourceGroup[], service: string): string {
  const lines = groups
    .filter(group => group.service === service)
    .sort((a, b) => a.resource.localeCompare(b.resource))
    .map(group => {
      const exports = [factoryName(group)]
      if (group.operations.some(op => op.authMode === 'scimBearer')) exports.push('type AuthSCIMOptions')
      return `export { ${exports.join(', ')} } from './${moduleFileName(group)}'`
    })

  return `${lines.join('\n')}\n`
}
