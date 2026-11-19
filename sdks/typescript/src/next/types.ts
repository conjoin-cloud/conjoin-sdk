export type AuthObject = {
  accountId: string
  sessionId: string
  organizationId: string | null
  organizationRoles: string[]
  getToken: () => string
}

export type NextAdapterConfig = {
  secretKey?: string
  publishableKey?: string
  jwksUrl?: string
  authDomain?: string
}
