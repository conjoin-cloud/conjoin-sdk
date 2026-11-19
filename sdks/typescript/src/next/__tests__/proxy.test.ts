import type { NextRequest } from 'next/server'
import { describe, expect, it } from 'vitest'
import { createRouteMatcher } from '../proxy'

function createMockRequest(options: { url?: string } = {}): NextRequest {
  const url = options.url ?? 'https://myapp.com/dashboard'

  return { url } as unknown as NextRequest
}

describe('createRouteMatcher', () => {
  it('matches exact paths', () => {
    const matcher = createRouteMatcher(['/dashboard'])
    expect(matcher(createMockRequest({ url: 'https://myapp.com/dashboard' }))).toBe(true)
    expect(matcher(createMockRequest({ url: 'https://myapp.com/about' }))).toBe(false)
  })

  it('matches wildcard patterns', () => {
    const matcher = createRouteMatcher(['/dashboard(.*)'])
    expect(matcher(createMockRequest({ url: 'https://myapp.com/dashboard' }))).toBe(true)
    expect(matcher(createMockRequest({ url: 'https://myapp.com/dashboard/settings' }))).toBe(true)
    expect(matcher(createMockRequest({ url: 'https://myapp.com/dashboard/users/123' }))).toBe(true)
    expect(matcher(createMockRequest({ url: 'https://myapp.com/about' }))).toBe(false)
  })

  it('matches multiple patterns', () => {
    const matcher = createRouteMatcher(['/dashboard(.*)', '/api/protected(.*)'])
    expect(matcher(createMockRequest({ url: 'https://myapp.com/dashboard' }))).toBe(true)
    expect(matcher(createMockRequest({ url: 'https://myapp.com/api/protected/resource' }))).toBe(true)
    expect(matcher(createMockRequest({ url: 'https://myapp.com/api/public' }))).toBe(false)
  })

  it('does not match partial paths without wildcard', () => {
    const matcher = createRouteMatcher(['/dashboard'])
    expect(matcher(createMockRequest({ url: 'https://myapp.com/dashboard/settings' }))).toBe(false)
  })

  it('handles root path', () => {
    const matcher = createRouteMatcher(['/'])
    expect(matcher(createMockRequest({ url: 'https://myapp.com/' }))).toBe(true)
    expect(matcher(createMockRequest({ url: 'https://myapp.com/anything' }))).toBe(false)
  })

  it('escapes special regex characters in patterns', () => {
    const matcher = createRouteMatcher(['/api/v1.0/users'])
    expect(matcher(createMockRequest({ url: 'https://myapp.com/api/v1.0/users' }))).toBe(true)
    expect(matcher(createMockRequest({ url: 'https://myapp.com/api/v1X0/users' }))).toBe(false)
  })

  it('matches pathname only, ignoring query strings', () => {
    const matcher = createRouteMatcher(['/dashboard(.*)'])
    expect(matcher(createMockRequest({ url: 'https://myapp.com/dashboard?tab=settings' }))).toBe(true)
    expect(matcher(createMockRequest({ url: 'https://myapp.com/about?ref=dashboard' }))).toBe(false)
  })

  it('returns false for empty patterns array', () => {
    const matcher = createRouteMatcher([])
    expect(matcher(createMockRequest({ url: 'https://myapp.com/anything' }))).toBe(false)
  })

  it('handles multiple wildcards in a single pattern', () => {
    const matcher = createRouteMatcher(['/api/(.*)/users(.*)'])
    expect(matcher(createMockRequest({ url: 'https://myapp.com/api/v1/users/123' }))).toBe(true)
    expect(matcher(createMockRequest({ url: 'https://myapp.com/api/v2/users' }))).toBe(true)
  })
})
