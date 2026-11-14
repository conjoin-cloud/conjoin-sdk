import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type GetProjectData = NonNullable<operations['getProjectBranding']['responses']['200']['content']['application/json']['data']>
type PatchProjectBody = NonNullable<operations['patchProjectBranding']['requestBody']>['content']['application/json']
type PatchProjectData = NonNullable<operations['patchProjectBranding']['responses']['200']['content']['application/json']['data']>
type GetOrgOverrideData = NonNullable<operations['getOrgBrandingOverride']['responses']['200']['content']['application/json']['data']>
type PatchOrgOverrideBody = NonNullable<operations['patchOrgBrandingOverride']['requestBody']>['content']['application/json']
type PatchOrgOverrideData = NonNullable<operations['patchOrgBrandingOverride']['responses']['200']['content']['application/json']['data']>

export function createCloudBrandings(client: ConjoinClient) {
  return {
    getProject: (options?: ConjoinCallOptions) =>
      client.fetch<GetProjectData>('cloud/branding/', { ...options, method: 'GET' }),

    patchProject: (data: PatchProjectBody, options?: ConjoinCallOptions) =>
      client.fetch<PatchProjectData>('cloud/branding/', { ...options, method: 'PATCH', body: data }),

    getOrgOverride: (organizationId: string, options?: ConjoinCallOptions) =>
      client.fetch<GetOrgOverrideData>(`cloud/branding/organizations/${encodePathParam(organizationId)}`, { ...options, method: 'GET' }),

    patchOrgOverride: (organizationId: string, data: PatchOrgOverrideBody, options?: ConjoinCallOptions) =>
      client.fetch<PatchOrgOverrideData>(`cloud/branding/organizations/${encodePathParam(organizationId)}`, { ...options, method: 'PATCH', body: data }),
  }
}
