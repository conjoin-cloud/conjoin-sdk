import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type AcceptBody = NonNullable<operations['acceptOrganizationInvitation']['requestBody']>['content']['application/json']
type AcceptData = NonNullable<operations['acceptOrganizationInvitation']['responses']['200']['content']['application/json']['data']>

export function createAuthOrganizationInvitations(client: ConjoinClient) {
  return {
    accept: (data: AcceptBody, options?: ConjoinCallOptions) =>
      client.fetch<AcceptData>('auth/client/invitations/accept', { auth: { type: 'none' }, ...options, method: 'POST', body: data }),
  }
}
