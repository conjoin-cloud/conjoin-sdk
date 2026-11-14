import type { ConjoinClient } from '@conjoin-cloud/sdk'
import type { QueryClient } from '@tanstack/query-core'
import { createContext } from 'react'
import type { ConjoinAuthApi } from '../auth/auth-api'
import type { AuthFlowState, AuthTransport, ConjoinAuthState, ConjoinSdkConfig, ConjoinThemeState } from './types'

export type ConjoinClientContextValue = {
  client: ConjoinClient
  queryClient: QueryClient
  sdkConfig: ConjoinSdkConfig | null
  isConfigLoaded: boolean
  authApi: ConjoinAuthApi | null
  transport: AuthTransport
}

export type ConjoinAuthActions = {
  getToken: () => string | null
  signOut: () => Promise<void>
  completeFlow: (flow: AuthFlowState) => Promise<void>
  switchOrganization: (organizationId: string | null) => Promise<void>
}

export const ConjoinClientContext = createContext<ConjoinClientContextValue | null>(null)
export const ConjoinAuthStateContext = createContext<ConjoinAuthState | null>(null)
export const ConjoinAuthActionsContext = createContext<ConjoinAuthActions | null>(null)
export const ConjoinThemeContext = createContext<ConjoinThemeState | null>(null)
