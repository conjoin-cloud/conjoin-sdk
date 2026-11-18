'use client'

export type { ConjoinAuthApi } from './auth/auth-api'
export {
  AUTH_CODE_CHALLENGE_HEADER,
  AUTH_CODE_VERIFIER_HEADER,
  AUTH_STATE_HEADER,
  CLIENT_HANDLE_HEADER,
  encodeClientHandle,
} from './auth/flow-headers'
export { type AuthFlowCrypto, type AuthFlowProof, createAuthFlowProof } from './auth/flow-proof'
export { createRedirectFlowRegistry, type RedirectFlowStore } from './auth/redirect-flows'
export { isSessionRejection, readSessionUnlessRejected } from './auth/session-errors'
export { useConjoinClient } from './hooks/internal/use-conjoin-client'
export { type ConjoinAccount, type ConjoinAccountUpdate, useAccount, useUpdateAccount } from './hooks/use-account'
export { useAuth } from './hooks/use-auth'
export {
  type AuthFlowResult,
  type OAuthRedirectResult,
  type SignInCompleteBody,
  type SignInStartBody,
  type SignUpCompleteBody,
  type SignUpStartBody,
  useSignIn,
  useSignUp,
} from './hooks/use-auth-flow'
export { type PriceBundleItem, useBundles } from './hooks/use-bundles'
export { useChannel } from './hooks/use-channel'
export { useCheckout } from './hooks/use-checkout'
export { useConjoinStatus } from './hooks/use-conjoin-status'
export { useEntitlements } from './hooks/use-entitlements'
export { type ConjoinMembership, useOrg } from './hooks/use-org'
export { type ConjoinSession, useSession, useSessions } from './hooks/use-session'
export { useStorageUpload } from './hooks/use-storage-upload'
export { ConjoinProviderCore } from './provider/core'
export type {
  AuthClientHandle,
  AuthFlowKind,
  AuthFlowState,
  AuthSessionGrant,
  AuthTransport,
  ColorPalette,
  ConjoinAuthState,
  ConjoinBranding,
  ConjoinProviderProps,
  ConjoinSdkAuthSettings,
  ConjoinSdkConfig,
} from './provider/types'
