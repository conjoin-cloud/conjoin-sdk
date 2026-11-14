import { type AuthFlowResult, useConjoinClient, useSignIn } from '@conjoin-cloud/react-core'
import * as Label from '@radix-ui/react-label'
import * as VisuallyHidden from '@radix-ui/react-visually-hidden'
import { type ChangeEvent, type FormEvent, useCallback, useRef, useState } from 'react'
import {
  type MfaMethod,
  type OAuthProvider,
  PASSWORD_METHODS,
  readFlowErrorMessage,
  readMfaMethod,
  readOAuthProviders,
  readSafeRedirectUrl,
} from '../internal/auth-flow-display'
import { BusyContent } from '../internal/busy-content'
import { OAuthButton } from '../internal/oauth-button'

type SignInStep = 'identifier' | 'password' | 'code' | 'mfa' | 'confirmation'

type SignInProps = {
  afterSignInUrl?: string
  forgotPasswordUrl?: string
  signUpUrl?: string
  onSignIn?: () => void
}

const ERROR_ID = 'conjoin-sign-in-error'
const CODE_MAX_LENGTH = 8

export function SignIn({ afterSignInUrl, forgotPasswordUrl, signUpUrl, onSignIn }: SignInProps) {
  const { sdkConfig } = useConjoinClient()
  const signIn = useSignIn()
  const [step, setStep] = useState<SignInStep>('identifier')
  const [identifier, setIdentifier] = useState('')
  const [password, setPassword] = useState('')
  const [code, setCode] = useState('')
  const [mfaMethod, setMfaMethod] = useState<MfaMethod>('totp')
  const [error, setError] = useState<string | null>(null)
  const [isSubmitting, setIsSubmitting] = useState(false)

  const passwordRef = useRef<HTMLInputElement>(null)
  const codeRef = useRef<HTMLInputElement>(null)
  const identifierRef = useRef<HTMLInputElement>(null)

  const signInMethods = sdkConfig?.auth?.sign_in_methods ?? []
  const oauthProviders = readOAuthProviders(signInMethods)
  const usesPassword = signInMethods.some(method => PASSWORD_METHODS.has(method))
  const usesEmail = usesPassword || signInMethods.includes('email')
  const describedBy = error ? ERROR_ID : undefined

  const finishSignIn = useCallback(() => {
    if (afterSignInUrl) window.location.assign(afterSignInUrl)
    onSignIn?.()
  }, [afterSignInUrl, onSignIn])

  const followResult = useCallback(
    (result: AuthFlowResult) => {
      if (result.status === 'complete') {
        finishSignIn()
        return
      }

      if (result.status === 'mfa_required') {
        setMfaMethod(readMfaMethod(result))
        setCode('')
        setStep('mfa')
        requestAnimationFrame(() => codeRef.current?.focus())
        return
      }

      if (result.status === 'verification_required') {
        setCode('')
        setStep('code')
        requestAnimationFrame(() => codeRef.current?.focus())
        return
      }

      if (result.status === 'confirmation_required') {
        setStep('confirmation')
        return
      }

      setError('Unable to sign in. Please try again.')
    },
    [finishSignIn],
  )

  const submitStep = useCallback(
    async (run: () => Promise<AuthFlowResult>, fallback: string) => {
      if (isSubmitting) return

      setIsSubmitting(true)
      setError(null)

      try {
        followResult(await run())
      } catch (caught) {
        setError(readFlowErrorMessage(caught, fallback))
      } finally {
        setIsSubmitting(false)
      }
    },
    [isSubmitting, followResult],
  )

  const handleIdentifierChange = useCallback((e: ChangeEvent<HTMLInputElement>) => {
    setIdentifier(e.target.value)
  }, [])

  const handlePasswordChange = useCallback((e: ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value)
  }, [])

  const handleCodeChange = useCallback((e: ChangeEvent<HTMLInputElement>) => {
    setCode(e.target.value)
  }, [])

  const handleIdentifierSubmit = useCallback(
    async (e: FormEvent) => {
      e.preventDefault()
      const email = identifier.trim()
      if (!email) return

      if (usesPassword) {
        setError(null)
        setStep('password')
        requestAnimationFrame(() => passwordRef.current?.focus())
        return
      }

      await submitStep(
        () => signIn.start({ email, verification_option: 'email_verification_code' }),
        'Unable to sign in. Please check your email and try again.',
      )
    },
    [identifier, usesPassword, signIn, submitStep],
  )

  const handlePasswordSubmit = useCallback(
    async (e: FormEvent) => {
      e.preventDefault()
      if (!password) return

      await submitStep(
        () => signIn.start({ email: identifier.trim(), password }),
        'Invalid credentials. Please try again.',
      )
    },
    [identifier, password, signIn, submitStep],
  )

  const handleCodeSubmit = useCallback(
    async (e: FormEvent) => {
      e.preventDefault()
      const pinCode = code.trim()
      if (!pinCode) return

      await submitStep(
        () => signIn.complete({ verification_result: { pin_code: pinCode } }),
        'Invalid verification code. Please try again.',
      )
    },
    [code, signIn, submitStep],
  )

  const handleMfaSubmit = useCallback(
    async (e: FormEvent) => {
      e.preventDefault()
      const mfaCode = code.trim()
      if (!mfaCode) return

      const mfa =
        mfaMethod === 'phone_verification_code'
          ? { method: 'phone_verification_code' as const, phone_code: mfaCode }
          : { method: 'totp' as const, totp_code: mfaCode }

      await submitStep(
        () => signIn.complete({ verification_result: {}, mfa }),
        'Invalid verification code. Please try again.',
      )
    },
    [code, mfaMethod, signIn, submitStep],
  )

  const handleOAuthSelect = useCallback(
    async (provider: string) => {
      if (isSubmitting) return

      setIsSubmitting(true)
      setError(null)

      try {
        const result = await signIn.startRedirect({
          provider_key: provider as OAuthProvider,
          verification_option: 'oauth_token',
        })
        const redirectUrl = readSafeRedirectUrl(result)

        if (redirectUrl === null) {
          setError('Unable to start sign in with this provider.')
          return
        }

        window.location.assign(redirectUrl)
      } catch (caught) {
        setError(readFlowErrorMessage(caught, 'Unable to start sign in with this provider.'))
      } finally {
        setIsSubmitting(false)
      }
    },
    [isSubmitting, signIn],
  )

  const handleBack = useCallback(() => {
    signIn.reset()
    setStep('identifier')
    setError(null)
    setPassword('')
    setCode('')
    requestAnimationFrame(() => identifierRef.current?.focus())
  }, [signIn])

  if (!signIn.isConfigured) {
    return (
      <div data-conjoin-card="">
        <p data-conjoin-heading="" data-conjoin-center="">
          Sign in is not available
        </p>
      </div>
    )
  }

  return (
    <div data-conjoin-card="">
      <h2 data-conjoin-heading="" data-level="card">
        Sign in
      </h2>

      {oauthProviders.length > 0 && step === 'identifier' ? (
        <div data-conjoin-social-group="">
          {oauthProviders.map(provider => (
            <OAuthButton key={provider} provider={provider} onSelect={handleOAuthSelect} />
          ))}
        </div>
      ) : null}

      {oauthProviders.length > 0 && usesEmail && step === 'identifier' ? (
        <div data-conjoin-divider-text="">or</div>
      ) : null}

      {error ? (
        <p id={ERROR_ID} data-conjoin-field-error="" role="alert">
          {error}
        </p>
      ) : null}

      {step === 'identifier' && usesEmail ? (
        <form onSubmit={handleIdentifierSubmit} noValidate>
          <div data-conjoin-field="" data-gap="wide">
            <Label.Root data-conjoin-label="" htmlFor="conjoin-sign-in-identifier">
              Email address
            </Label.Root>
            <input
              ref={identifierRef}
              id="conjoin-sign-in-identifier"
              data-conjoin-input=""
              type="email"
              autoComplete="email"
              value={identifier}
              onChange={handleIdentifierChange}
              placeholder="you@example.com"
              required
              aria-invalid={error ? true : undefined}
              aria-describedby={describedBy}
              maxLength={254}
            />
          </div>

          <button
            type="submit"
            data-conjoin-button=""
            data-variant="primary"
            data-block="true"
            data-spacing="stacked"
            disabled={isSubmitting}
            aria-busy={isSubmitting}
          >
            <BusyContent busy={isSubmitting} label="Continue" busyLabel="Signing in" />
          </button>
        </form>
      ) : null}

      {step === 'password' ? (
        <form onSubmit={handlePasswordSubmit} noValidate>
          <VisuallyHidden.Root>
            <label htmlFor="conjoin-sign-in-email-hidden">Email</label>
            <input id="conjoin-sign-in-email-hidden" type="email" value={identifier} readOnly autoComplete="email" />
          </VisuallyHidden.Root>

          <div data-conjoin-field="" data-gap="wide">
            <Label.Root data-conjoin-label="" htmlFor="conjoin-sign-in-password">
              Password
            </Label.Root>
            <input
              ref={passwordRef}
              id="conjoin-sign-in-password"
              data-conjoin-input=""
              type="password"
              autoComplete="current-password"
              value={password}
              onChange={handlePasswordChange}
              placeholder="Enter your password"
              required
              maxLength={256}
              aria-invalid={error ? true : undefined}
              aria-describedby={describedBy}
            />
          </div>

          {forgotPasswordUrl ? (
            <div data-conjoin-forgot="">
              <a href={forgotPasswordUrl} data-conjoin-link="">
                Forgot password?
              </a>
            </div>
          ) : null}

          <button
            type="submit"
            data-conjoin-button=""
            data-variant="primary"
            data-block="true"
            data-spacing="stacked"
            disabled={isSubmitting}
            aria-busy={isSubmitting}
          >
            <BusyContent busy={isSubmitting} label="Sign in" busyLabel="Signing in" />
          </button>

          <button
            type="button"
            data-conjoin-button=""
            data-variant="outline"
            data-block="true"
            data-spacing="stacked"
            onClick={handleBack}
          >
            Back
          </button>
        </form>
      ) : null}

      {step === 'code' || step === 'mfa' ? (
        <form onSubmit={step === 'code' ? handleCodeSubmit : handleMfaSubmit} noValidate>
          <div data-conjoin-field="" data-gap="wide">
            <Label.Root data-conjoin-label="" htmlFor="conjoin-sign-in-code">
              {step === 'code' ? 'Code from your email' : 'Verification code'}
            </Label.Root>
            <input
              ref={codeRef}
              id="conjoin-sign-in-code"
              data-conjoin-input=""
              data-mono="true"
              type="text"
              inputMode="numeric"
              autoComplete="one-time-code"
              value={code}
              onChange={handleCodeChange}
              placeholder="Enter the code"
              required
              maxLength={CODE_MAX_LENGTH}
              aria-invalid={error ? true : undefined}
              aria-describedby={describedBy}
            />
          </div>

          <button
            type="submit"
            data-conjoin-button=""
            data-variant="primary"
            data-block="true"
            data-spacing="stacked"
            disabled={isSubmitting}
            aria-busy={isSubmitting}
          >
            <BusyContent busy={isSubmitting} label="Verify" busyLabel="Verifying" />
          </button>

          <button
            type="button"
            data-conjoin-button=""
            data-variant="outline"
            data-block="true"
            data-spacing="stacked"
            onClick={handleBack}
          >
            Back
          </button>
        </form>
      ) : null}

      {step === 'confirmation' ? <output data-conjoin-prompt="">Check your email for a sign-in link.</output> : null}

      {signUpUrl ? (
        <p data-conjoin-prompt="">
          Don't have an account?{' '}
          <a href={signUpUrl} data-conjoin-link="">
            Sign up
          </a>
        </p>
      ) : null}
    </div>
  )
}
