import { type AuthFlowResult, useConjoinClient, useSignUp, useUpdateAccount } from '@conjoin-cloud/react-core'
import * as Label from '@radix-ui/react-label'
import { type ChangeEvent, type FormEvent, useCallback, useRef, useState } from 'react'
import {
  type OAuthProvider,
  readFlowErrorMessage,
  readOAuthProviders,
  readSafeRedirectUrl,
} from '../internal/auth-flow-display'
import { BusyContent } from '../internal/busy-content'
import { OAuthButton } from '../internal/oauth-button'

type SignUpStep = 'details' | 'code' | 'confirmation'

type SignUpProps = {
  afterSignUpUrl?: string
  signInUrl?: string
  onSignUp?: () => void
}

const ERROR_ID = 'conjoin-sign-up-error'
const PASSWORD_MIN_LENGTH = 8
const PASSWORD_MAX_LENGTH = 256
const NAME_MAX_LENGTH = 100
const CODE_MAX_LENGTH = 8

export function SignUp({ afterSignUpUrl, signInUrl, onSignUp }: SignUpProps) {
  const { sdkConfig } = useConjoinClient()
  const signUp = useSignUp()
  const { update } = useUpdateAccount()
  const [step, setStep] = useState<SignUpStep>('details')
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [code, setCode] = useState('')
  const [error, setError] = useState<string | null>(null)
  const [isSubmitting, setIsSubmitting] = useState(false)
  const codeRef = useRef<HTMLInputElement>(null)

  const signUpEnabled = sdkConfig?.auth?.sign_up_enabled === true
  const oauthProviders = readOAuthProviders(sdkConfig?.auth?.sign_in_methods ?? [])
  const describedBy = error ? ERROR_ID : undefined

  const finishSignUp = useCallback(async () => {
    const trimmedName = name.trim()
    if (trimmedName) await update({ name: trimmedName }).catch(() => undefined)
    if (afterSignUpUrl) window.location.assign(afterSignUpUrl)
    onSignUp?.()
  }, [name, update, afterSignUpUrl, onSignUp])

  const followResult = useCallback(
    async (result: AuthFlowResult) => {
      if (result.status === 'complete') {
        await finishSignUp()
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

      setError('Unable to create account. Please try again.')
    },
    [finishSignUp],
  )

  const submitStep = useCallback(
    async (run: () => Promise<AuthFlowResult>, fallback: string) => {
      if (isSubmitting) return

      setIsSubmitting(true)
      setError(null)

      try {
        await followResult(await run())
      } catch (caught) {
        setError(readFlowErrorMessage(caught, fallback))
      } finally {
        setIsSubmitting(false)
      }
    },
    [isSubmitting, followResult],
  )

  const handleNameChange = useCallback((e: ChangeEvent<HTMLInputElement>) => {
    setName(e.target.value)
  }, [])

  const handleEmailChange = useCallback((e: ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value)
  }, [])

  const handlePasswordChange = useCallback((e: ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value)
  }, [])

  const handleCodeChange = useCallback((e: ChangeEvent<HTMLInputElement>) => {
    setCode(e.target.value)
  }, [])

  const handleDetailsSubmit = useCallback(
    async (e: FormEvent) => {
      e.preventDefault()
      const trimmedEmail = email.trim()

      if (!trimmedEmail) {
        setError('Enter your email address.')
        return
      }

      if (password.length < PASSWORD_MIN_LENGTH) {
        setError(`Use a password of at least ${PASSWORD_MIN_LENGTH} characters.`)
        return
      }

      await submitStep(
        () => signUp.start({ email: trimmedEmail, password }),
        'Unable to create account. Please try again.',
      )
    },
    [email, password, signUp, submitStep],
  )

  const handleCodeSubmit = useCallback(
    async (e: FormEvent) => {
      e.preventDefault()
      const pinCode = code.trim()
      if (!pinCode) return

      await submitStep(
        () => signUp.complete({ verification_result: { pin_code: pinCode } }),
        'Invalid verification code. Please try again.',
      )
    },
    [code, signUp, submitStep],
  )

  const handleOAuthSelect = useCallback(
    async (provider: string) => {
      if (isSubmitting) return

      setIsSubmitting(true)
      setError(null)

      try {
        const result = await signUp.startRedirect({
          provider_key: provider as OAuthProvider,
          verification_option: 'oauth_token',
        })
        const redirectUrl = readSafeRedirectUrl(result)

        if (redirectUrl === null) {
          setError('Unable to start sign up with this provider.')
          return
        }

        window.location.assign(redirectUrl)
      } catch (caught) {
        setError(readFlowErrorMessage(caught, 'Unable to start sign up with this provider.'))
      } finally {
        setIsSubmitting(false)
      }
    },
    [isSubmitting, signUp],
  )

  const handleBack = useCallback(() => {
    signUp.reset()
    setStep('details')
    setError(null)
    setCode('')
  }, [signUp])

  if (!signUp.isConfigured || !signUpEnabled) {
    return (
      <div data-conjoin-card="">
        <p data-conjoin-heading="" data-conjoin-center="">
          Sign up is not available
        </p>
      </div>
    )
  }

  return (
    <div data-conjoin-card="">
      <h2 data-conjoin-heading="" data-level="card">
        Create your account
      </h2>

      {oauthProviders.length > 0 && step === 'details' ? (
        <div data-conjoin-social-group="">
          {oauthProviders.map(provider => (
            <OAuthButton key={provider} provider={provider} onSelect={handleOAuthSelect} />
          ))}
          <div data-conjoin-divider-text="">or</div>
        </div>
      ) : null}

      {error ? (
        <p id={ERROR_ID} data-conjoin-field-error="" role="alert">
          {error}
        </p>
      ) : null}

      {step === 'details' ? (
        <form onSubmit={handleDetailsSubmit} noValidate>
          <div data-conjoin-field="">
            <Label.Root data-conjoin-label="" htmlFor="conjoin-sign-up-name">
              Name
            </Label.Root>
            <input
              id="conjoin-sign-up-name"
              data-conjoin-input=""
              type="text"
              autoComplete="name"
              value={name}
              onChange={handleNameChange}
              maxLength={NAME_MAX_LENGTH}
            />
          </div>

          <div data-conjoin-field="">
            <Label.Root data-conjoin-label="" htmlFor="conjoin-sign-up-email">
              Email address
            </Label.Root>
            <input
              id="conjoin-sign-up-email"
              data-conjoin-input=""
              type="email"
              autoComplete="email"
              value={email}
              onChange={handleEmailChange}
              placeholder="you@example.com"
              required
              maxLength={254}
              aria-invalid={error ? true : undefined}
              aria-describedby={describedBy}
            />
          </div>

          <div data-conjoin-field="">
            <Label.Root data-conjoin-label="" htmlFor="conjoin-sign-up-password">
              Password
            </Label.Root>
            <input
              id="conjoin-sign-up-password"
              data-conjoin-input=""
              type="password"
              autoComplete="new-password"
              value={password}
              onChange={handlePasswordChange}
              placeholder="Create a password"
              required
              minLength={PASSWORD_MIN_LENGTH}
              maxLength={PASSWORD_MAX_LENGTH}
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
            <BusyContent busy={isSubmitting} label="Create account" busyLabel="Creating account" />
          </button>
        </form>
      ) : null}

      {step === 'code' ? (
        <form onSubmit={handleCodeSubmit} noValidate>
          <div data-conjoin-field="" data-gap="wide">
            <Label.Root data-conjoin-label="" htmlFor="conjoin-sign-up-code">
              Code from your email
            </Label.Root>
            <input
              ref={codeRef}
              id="conjoin-sign-up-code"
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

      {step === 'confirmation' ? (
        <output data-conjoin-prompt="">Check your email for a link to finish creating your account.</output>
      ) : null}

      {signInUrl ? (
        <p data-conjoin-prompt="">
          Already have an account?{' '}
          <a href={signInUrl} data-conjoin-link="">
            Sign in
          </a>
        </p>
      ) : null}
    </div>
  )
}
