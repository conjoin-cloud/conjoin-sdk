import { useCallback, useMemo, useRef } from 'react'
import type { ConjoinAuthApi } from '../auth/auth-api'
import type { AuthFlowKind, AuthFlowState, AuthTransport } from '../provider/types'
import { useAuthActions } from './internal/use-auth-actions'
import { useConjoinClient } from './internal/use-conjoin-client'

type WebFlows = ConjoinAuthApi['webFlows']

export type SignInStartBody = Parameters<WebFlows['startSignin']>[0]
export type SignInCompleteBody = Parameters<WebFlows['completeSignin']>[0]
export type SignUpStartBody = Parameters<WebFlows['startSignup']>[0]
export type SignUpCompleteBody = Parameters<WebFlows['completeSignup']>[0]
export type AuthFlowResult = Awaited<ReturnType<WebFlows['startSignin']>>

type FlowBodies = {
  signin: { start: SignInStartBody; complete: SignInCompleteBody }
  signup: { start: SignUpStartBody; complete: SignUpCompleteBody }
}

export type OAuthRedirectResult = {
  code: string
  state: string
}

const AUTH_NOT_CONFIGURED_MESSAGE = 'Sign-in is not configured for this project'

type FlowStep = 'start' | 'complete'
type FlowStepBody = SignInStartBody | SignInCompleteBody | SignUpStartBody | SignUpCompleteBody

function callFlowStep(
  authApi: ConjoinAuthApi,
  transport: AuthTransport,
  flow: AuthFlowState,
  step: FlowStep,
  body: FlowStepBody,
): Promise<AuthFlowResult> {
  const calls = transport.platform === 'web' ? authApi.webFlows : authApi.nativeFlows
  const options = transport.flowCallOptions(flow)

  if (flow.kind === 'signin') {
    return step === 'start'
      ? calls.startSignin(body as SignInStartBody, options)
      : calls.completeSignin(body as SignInCompleteBody, options)
  }

  return step === 'start'
    ? calls.startSignup(body as SignUpStartBody, options)
    : calls.completeSignup(body as SignUpCompleteBody, options)
}

function readClientHandle(result: AuthFlowResult): AuthFlowState['clientHandle'] {
  if (!('client_handle' in result)) return null

  const handle = result.client_handle

  if (typeof handle !== 'object' || handle === null) return null
  if (!('client_id' in handle) || !('reference_id' in handle)) return null
  if (typeof handle.client_id !== 'string' || typeof handle.reference_id !== 'string') return null

  return { client_id: handle.client_id, reference_id: handle.reference_id }
}

function useAuthFlow<TKind extends AuthFlowKind>(kind: TKind) {
  const { authApi, transport } = useConjoinClient()
  const { completeFlow } = useAuthActions()
  const flowRef = useRef<AuthFlowState | null>(null)

  const runStep = useCallback(
    async (flow: AuthFlowState, step: FlowStep, body: FlowStepBody): Promise<AuthFlowResult> => {
      if (authApi === null) throw new Error(AUTH_NOT_CONFIGURED_MESSAGE)

      const result = await callFlowStep(authApi, transport, flow, step, body)

      if (flowRef.current !== flow) return result

      const clientHandle = readClientHandle(result)
      const nextFlow: AuthFlowState = {
        ...flow,
        proof: result.state ? { ...flow.proof, state: result.state } : flow.proof,
        clientHandle: clientHandle ?? flow.clientHandle,
      }
      flowRef.current = nextFlow

      if (result.status === 'complete') {
        await completeFlow(nextFlow)
        if (flowRef.current === nextFlow) flowRef.current = null
      }

      return result
    },
    [authApi, transport, completeFlow],
  )

  const start = useCallback(
    async (body: FlowBodies[TKind]['start']): Promise<AuthFlowResult> => {
      const flow: AuthFlowState = { kind, proof: await transport.createFlowProof(), clientHandle: null }
      flowRef.current = flow

      return runStep(flow, 'start', body)
    },
    [kind, transport, runStep],
  )

  const complete = useCallback(
    async (body: FlowBodies[TKind]['complete']): Promise<AuthFlowResult> => {
      const flow = flowRef.current
      if (flow === null) throw new Error('Start the flow before you complete it')

      return runStep(flow, 'complete', body)
    },
    [runStep],
  )

  const startRedirect = useCallback(
    async (body: FlowBodies[TKind]['start']): Promise<AuthFlowResult> => {
      const result = await start(body)
      const flow = flowRef.current

      if (flow !== null && result.redirect_url) transport.saveRedirectFlow(flow)

      return result
    },
    [start, transport],
  )

  const completeRedirect = useCallback(
    async ({ code, state }: OAuthRedirectResult): Promise<AuthFlowResult> => {
      const flow = transport.takeRedirectFlow(state)
      if (flow === null || flow.kind !== kind) {
        throw new Error('The sign-in redirect does not match a sign-in that this app started')
      }

      flowRef.current = flow

      return runStep(flow, 'complete', { verification_result: { oauth_token: code } })
    },
    [kind, transport, runStep],
  )

  const reset = useCallback(() => {
    flowRef.current = null
  }, [])

  return useMemo(
    () => ({ isConfigured: authApi !== null, start, complete, startRedirect, completeRedirect, reset }),
    [authApi, start, complete, startRedirect, completeRedirect, reset],
  )
}

export function useSignIn() {
  return useAuthFlow('signin')
}

export function useSignUp() {
  return useAuthFlow('signup')
}
