import type { ConjoinAuthApi } from '../auth/auth-api'
import type { AuthTransport } from '../provider/types'
import { collectPages } from './internal/collect-pages'
import { useAuthActions } from './internal/use-auth-actions'
import { useAuthState } from './internal/use-auth-state'
import { useSignedInQuery } from './internal/use-signed-in-query'

export type ConjoinMembership = Awaited<ReturnType<ConjoinAuthApi['selves']['listOrganizations']>>['data'][number]

const NO_MEMBERSHIPS: ConjoinMembership[] = []

const readMemberships = (authApi: ConjoinAuthApi, transport: AuthTransport): Promise<ConjoinMembership[]> =>
  collectPages(authApi.selves.listOrganizations({}, transport.readSessionToken(), transport.sessionCallOptions('GET')))

export function useOrg() {
  const authState = useAuthState()
  const { switchOrganization } = useAuthActions()
  const result = useSignedInQuery('organizations', readMemberships)
  const isSignedIn = authState.isLoaded && authState.isSignedIn
  const organizationId = isSignedIn ? authState.organizationId : null
  const organizationRoles = isSignedIn ? authState.organizationRoles : []
  const memberships = result.data ?? NO_MEMBERSHIPS

  return {
    isLoaded: result.isLoaded,
    organizationId,
    organizationRoles,
    membership: memberships.find(membership => membership.organization_id === organizationId) ?? null,
    memberships,
    error: result.error,
    switchOrganization,
  }
}
