import { afterEach, describe, expect, it } from 'vitest'
import { DEFAULT_API_VERSION } from '../../../src/core/version'
import type { ConjoinContractServer } from './conjoin-contract-server'
import { startConjoinContractServer } from './conjoin-contract-server'
import { conjoinList, conjoinSuccess } from './response-fixtures'

const CREATE_ORGANIZATION_PATH = '/v1/cloud/organizations/'
const EFFECTIVE_TAX_RATES_PATH = '/v1/billing/tax-jurisdictions/effective-rates'
const ZONES_PATH = '/v1/cloud/zones/'

const createdOrganization = {
  cloud_account_id: 'account_harbourledger',
  entity_id: 'entity_harbourledger',
  organization_id: 'organization_harbourledger',
  name: 'Harbour Ledger',
  date_created: '2026-11-14T10:00:00.000Z',
}

const postOrganization = (server: ConjoinContractServer, init: { body?: unknown; headers?: Record<string, string> }) =>
  fetch(`${server.baseUrl}${CREATE_ORGANIZATION_PATH}`, {
    method: 'POST',
    headers: { 'content-type': 'application/json', ...init.headers },
    ...(init.body === undefined ? {} : { body: JSON.stringify(init.body) }),
  })

const registerOrganizationRoute = (server: ConjoinContractServer, onCall: () => void, status = 201) =>
  server.register({
    method: 'POST',
    path: CREATE_ORGANIZATION_PATH,
    handler: () => {
      onCall()
      return conjoinSuccess(createdOrganization, { status })
    },
  })

describe('Conjoin contract server', () => {
  let server: ConjoinContractServer | undefined

  afterEach(async () => {
    await server?.stop()
    server = undefined
  })

  it('records the request that a declared route receives', async () => {
    server = await startConjoinContractServer()
    registerOrganizationRoute(server, () => undefined)

    const response = await postOrganization(server, {
      body: { name: 'Harbour Ledger' },
      headers: { 'x-conjoin-api-version': DEFAULT_API_VERSION },
    })

    expect(response.status).toBe(201)
    await expect(response.json()).resolves.toMatchObject({ data: createdOrganization })
    expect(server.recorder.last()).toMatchObject({
      method: 'POST',
      path: CREATE_ORGANIZATION_PATH,
      pathTemplate: CREATE_ORGANIZATION_PATH,
      body: { name: 'Harbour Ledger' },
    })
    expect(server.recorder.last()?.headers['x-conjoin-api-version']).toBe(DEFAULT_API_VERSION)
  })

  it('rejects route registration outside the OpenAPI contract', async () => {
    server = await startConjoinContractServer()

    expect(() =>
      server?.register({ method: 'GET', path: '/v1/not/a/real/conjoin/path', handler: () => conjoinSuccess({}) }),
    ).toThrow('Route is not declared in OpenAPI')
  })

  it('returns not stubbed for declared routes without fixtures', async () => {
    server = await startConjoinContractServer()

    const response = await postOrganization(server, { body: { name: 'Harbour Ledger' } })

    expect(response.status).toBe(501)
    await expect(response.json()).resolves.toMatchObject({ error: { code: 'contract_route_not_stubbed' } })
  })

  it('rejects missing required request bodies before handlers run', async () => {
    let wasHandlerCalled = false
    server = await startConjoinContractServer()
    registerOrganizationRoute(server, () => {
      wasHandlerCalled = true
    })

    const response = await postOrganization(server, {})

    expect(response.status).toBe(400)
    await expect(response.json()).resolves.toMatchObject({
      error: { code: 'contract_request_invalid', details: [{ path: 'body', message: 'is required' }] },
    })
    expect(wasHandlerCalled).toBe(false)
  })

  it('rejects request bodies that do not match OpenAPI schemas before handlers run', async () => {
    let wasHandlerCalled = false
    server = await startConjoinContractServer()
    registerOrganizationRoute(server, () => {
      wasHandlerCalled = true
    })

    const response = await postOrganization(server, { body: { name: 'No' } })

    expect(response.status).toBe(400)
    await expect(response.json()).resolves.toMatchObject({
      error: {
        code: 'contract_request_invalid',
        details: [{ path: 'body/name', message: 'must NOT have fewer than 3 characters' }],
      },
    })
    expect(wasHandlerCalled).toBe(false)
  })

  it('rejects declared header parameters that do not match OpenAPI schemas before handlers run', async () => {
    let wasHandlerCalled = false
    server = await startConjoinContractServer()
    registerOrganizationRoute(server, () => {
      wasHandlerCalled = true
    })

    const response = await postOrganization(server, {
      body: { name: 'Harbour Ledger' },
      headers: { 'conjoin-request-id': 'not-valid' },
    })

    expect(response.status).toBe(400)
    await expect(response.json()).resolves.toMatchObject({
      error: {
        code: 'contract_request_invalid',
        details: expect.arrayContaining([expect.objectContaining({ path: 'header.Conjoin-Request-Id' })]),
      },
    })
    expect(wasHandlerCalled).toBe(false)
  })

  it('rejects missing required query parameters before handlers run', async () => {
    let wasHandlerCalled = false
    server = await startConjoinContractServer()
    server.register({
      method: 'GET',
      path: EFFECTIVE_TAX_RATES_PATH,
      handler: () => {
        wasHandlerCalled = true
        return conjoinSuccess({})
      },
    })

    const response = await fetch(`${server.baseUrl}${EFFECTIVE_TAX_RATES_PATH}`)

    expect(response.status).toBe(400)
    await expect(response.json()).resolves.toMatchObject({
      error: { code: 'contract_request_invalid', details: [{ path: 'query.country', message: 'is required' }] },
    })
    expect(wasHandlerCalled).toBe(false)
  })

  it('validates bracketed object query parameters before handlers run', async () => {
    let wasHandlerCalled = false
    server = await startConjoinContractServer()
    server.register({
      method: 'GET',
      path: ZONES_PATH,
      handler: () => {
        wasHandlerCalled = true
        return conjoinList([])
      },
    })

    const response = await fetch(`${server.baseUrl}${ZONES_PATH}?sort%5Bdate_created%5D=sideways`)

    expect(response.status).toBe(400)
    await expect(response.json()).resolves.toMatchObject({
      error: {
        code: 'contract_request_invalid',
        details: expect.arrayContaining([expect.objectContaining({ path: 'query.sort/date_created' })]),
      },
    })
    expect(wasHandlerCalled).toBe(false)
  })

  it('rejects fixture statuses not declared by OpenAPI', async () => {
    server = await startConjoinContractServer()
    registerOrganizationRoute(server, () => undefined, 202)

    const response = await postOrganization(server, { body: { name: 'Harbour Ledger' } })

    expect(response.status).toBe(500)
    await expect(response.json()).resolves.toMatchObject({ error: { code: 'contract_server_error' } })
  })

  it('rejects fixture response bodies that do not match OpenAPI schemas', async () => {
    server = await startConjoinContractServer()
    server.register({
      method: 'POST',
      path: CREATE_ORGANIZATION_PATH,
      handler: () => conjoinSuccess({ organization_id: 'organization_harbourledger' }, { status: 201 }),
    })

    const response = await postOrganization(server, { body: { name: 'Harbour Ledger' } })

    expect(response.status).toBe(500)
    await expect(response.json()).resolves.toMatchObject({
      response: { message: expect.stringContaining('Response body does not match OpenAPI schema') },
      error: { code: 'contract_server_error' },
    })
  })
})
