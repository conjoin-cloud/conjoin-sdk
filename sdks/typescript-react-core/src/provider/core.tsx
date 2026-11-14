import { createConjoinClient } from '@conjoin-cloud/sdk'
import { QueryClient } from '@tanstack/query-core'
import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { type ConjoinAuthApi, createConjoinAuthApi } from '../auth/auth-api'
import { type AuthManager, createAuthManager } from './auth-manager'
import { fetchSdkConfig } from './config-fetcher'
import {
  type ConjoinAuthActions,
  ConjoinAuthActionsContext,
  ConjoinAuthStateContext,
  ConjoinClientContext,
} from './contexts'
import type { AuthFlowState, AuthTransport, ConjoinAuthState, ConjoinProviderProps, ConjoinSdkConfig } from './types'

type ConjoinProviderCoreProps = ConjoinProviderProps & {
  transport: AuthTransport
}

function authStateSignature(state: ConjoinAuthState): string {
  if (!state.isLoaded) return 'loading'
  if (!state.isSignedIn) return 'signed-out'
  return JSON.stringify([state.accountId, state.sessionId, state.organizationId, state.organizationRoles])
}

function mergePartialConfig(partial: Partial<ConjoinSdkConfig>, fallbackBaseUrl: string): ConjoinSdkConfig {
  return {
    project_id: partial.project_id ?? '',
    environment: partial.environment ?? 'test',
    api_url: partial.api_url ?? fallbackBaseUrl,
    branding: partial.branding ?? null,
    auth: partial.auth ?? null,
    relay: {
      url: partial.relay?.url ?? '',
    },
  }
}

function createAuthApiForDomain(publishableKey: string, authDomain: string | undefined): ConjoinAuthApi | null {
  if (!authDomain) return null

  try {
    return createConjoinAuthApi(publishableKey, authDomain)
  } catch {
    return null
  }
}

const AUTH_NOT_CONFIGURED_MESSAGE = 'Sign-in is not configured for this project'

export function ConjoinProviderCore({ publishableKey, children, config, transport }: ConjoinProviderCoreProps) {
  const [sdkConfig, setSdkConfig] = useState<ConjoinSdkConfig | null>(null)
  const [isConfigLoaded, setIsConfigLoaded] = useState(false)
  const [authState, setAuthState] = useState<ConjoinAuthState>({ isLoaded: false })

  const authManagerRef = useRef<AuthManager | null>(null)
  const authSignatureRef = useRef<string | null>(null)

  const handleAuthStateChange = useCallback((next: ConjoinAuthState) => {
    const signature = authStateSignature(next)
    if (signature === authSignatureRef.current) return
    authSignatureRef.current = signature
    setAuthState(next)
  }, [])

  const client = useMemo(() => {
    return createConjoinClient({
      publishableKey,
      baseUrl: config?.api_url,
    })
  }, [publishableKey, config?.api_url])

  const queryClient = useMemo(() => {
    return new QueryClient({
      defaultOptions: {
        queries: {
          staleTime: 30_000,
          retry: 2,
        },
      },
    })
  }, [])

  useEffect(() => {
    if (config) {
      setSdkConfig(mergePartialConfig(config, client.config.baseUrl))
      setIsConfigLoaded(true)
      return
    }

    let cancelled = false
    fetchSdkConfig(client)
      .then(fetched => {
        if (!cancelled) {
          setSdkConfig(fetched)
          setIsConfigLoaded(true)
        }
      })
      .catch(() => {
        if (!cancelled) setIsConfigLoaded(true)
      })

    return () => {
      cancelled = true
    }
  }, [client, config])

  const authDomain = sdkConfig?.auth?.domain
  const authApi = useMemo(() => createAuthApiForDomain(publishableKey, authDomain), [publishableKey, authDomain])

  useEffect(() => {
    if (!isConfigLoaded) return

    const manager = createAuthManager({ api: authApi, transport, onStateChange: handleAuthStateChange })

    authManagerRef.current = manager
    manager.initialize()

    return () => {
      manager.destroy()
      authManagerRef.current = null
    }
  }, [authApi, transport, isConfigLoaded, handleAuthStateChange])

  const getToken = useCallback(() => {
    return authManagerRef.current?.getToken() ?? null
  }, [])

  const signOut = useCallback(async () => {
    await authManagerRef.current?.signOut()
    queryClient.removeQueries({ queryKey: ['conjoin', 'auth'] })
  }, [queryClient])

  const completeFlow = useCallback(async (flow: AuthFlowState) => {
    const manager = authManagerRef.current
    if (!manager) throw new Error(AUTH_NOT_CONFIGURED_MESSAGE)
    await manager.completeFlow(flow)
  }, [])

  const switchOrganization = useCallback(
    async (organizationId: string | null) => {
      const manager = authManagerRef.current
      if (!manager) throw new Error(AUTH_NOT_CONFIGURED_MESSAGE)
      await manager.switchOrganization(organizationId)
      await queryClient.invalidateQueries({ queryKey: ['conjoin', 'auth'] })
    },
    [queryClient],
  )

  const clientContextValue = useMemo(
    () => ({ client, queryClient, sdkConfig, isConfigLoaded, authApi, transport }),
    [client, queryClient, sdkConfig, isConfigLoaded, authApi, transport],
  )

  const authActions = useMemo<ConjoinAuthActions>(
    () => ({ getToken, signOut, completeFlow, switchOrganization }),
    [getToken, signOut, completeFlow, switchOrganization],
  )

  return (
    <ConjoinClientContext.Provider value={clientContextValue}>
      <ConjoinAuthActionsContext.Provider value={authActions}>
        <ConjoinAuthStateContext.Provider value={authState}>{children}</ConjoinAuthStateContext.Provider>
      </ConjoinAuthActionsContext.Provider>
    </ConjoinClientContext.Provider>
  )
}
