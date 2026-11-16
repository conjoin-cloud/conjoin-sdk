import type { DeclaredHeader } from './operations'
import { isRecord } from './utils'

export type AuthMode = 'default' | 'none' | 'scimBearer' | 'publishableKey' | 'session' | 'portalTicket'

type SecuritySchemeGroup = {
  mode: AuthMode
  schemes: ReadonlySet<string>
}

const SECURITY_SCHEME_GROUPS: readonly SecuritySchemeGroup[] = [
  { mode: 'default', schemes: new Set(['conjoinApiKey']) },
  { mode: 'scimBearer', schemes: new Set(['scimBearer']) },
  { mode: 'publishableKey', schemes: new Set(['conjoinPublishableKey']) },
  { mode: 'session', schemes: new Set(['conjoinSessionBearer', 'conjoinSessionCookie']) },
  { mode: 'portalTicket', schemes: new Set(['conjoinPortalTicketHeader', 'conjoinPortalTicketQuery']) },
]

const PORTAL_TICKET_HEADER_SCHEME = 'conjoinPortalTicketHeader'
const PORTAL_TICKET_ARGUMENT_NAME = 'portalTicket'

export const resolveAuthMode = (operation: Record<string, unknown>, operationId: string): AuthMode => {
  const security = operation.security

  if (!Array.isArray(security)) return 'default'

  const schemes = security.flatMap(requirement => (isRecord(requirement) ? Object.keys(requirement) : []))

  if (schemes.length === 0) return 'none'

  const group = SECURITY_SCHEME_GROUPS.find(candidate => schemes.every(scheme => candidate.schemes.has(scheme)))

  if (group === undefined) {
    throw new Error(`${operationId} declares the security schemes ${schemes.join(', ')}, which no SDK call supports`)
  }

  return group.mode
}

export const readPortalTicketHeader = (securitySchemes: Record<string, unknown> | undefined): DeclaredHeader => {
  const scheme = securitySchemes?.[PORTAL_TICKET_HEADER_SCHEME]

  if (!isRecord(scheme) || scheme.in !== 'header' || typeof scheme.name !== 'string') {
    throw new Error(`The document declares no header for ${PORTAL_TICKET_HEADER_SCHEME}`)
  }

  return { name: scheme.name, argumentName: PORTAL_TICKET_ARGUMENT_NAME, required: true }
}
