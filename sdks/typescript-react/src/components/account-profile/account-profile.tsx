import {
  type ConjoinAccount,
  type ConjoinSession,
  useAccount,
  useSessions,
  useUpdateAccount,
} from '@conjoin-cloud/react-core'
import * as Avatar from '@radix-ui/react-avatar'
import * as Label from '@radix-ui/react-label'
import * as Separator from '@radix-ui/react-separator'
import * as Tabs from '@radix-ui/react-tabs'
import { type ChangeEvent, type FormEvent, useCallback, useState } from 'react'
import { readDisplayName, readInitials, readPrimaryEmail } from '../internal/account-display'
import { BusyContent } from '../internal/busy-content'
import { Spinner } from '../internal/spinner'

type TabValue = 'profile' | 'sessions'

type Feedback = { type: 'success' | 'error'; message: string }

const NAME_MAX_LENGTH = 100

function FeedbackMessage({ feedback }: { feedback: Feedback }) {
  return (
    <p data-conjoin-feedback="" data-tone={feedback.type} role={feedback.type === 'error' ? 'alert' : 'status'}>
      {feedback.message}
    </p>
  )
}

function readErrorMessage(error: unknown, fallback: string): string {
  return error instanceof Error && error.message ? error.message : fallback
}

function ProfileTab({ account }: { account: ConjoinAccount }) {
  const { update, isPending } = useUpdateAccount()
  const [name, setName] = useState(account.name ?? '')
  const [feedback, setFeedback] = useState<Feedback | null>(null)

  const handleNameChange = useCallback((e: ChangeEvent<HTMLInputElement>) => {
    setName(e.target.value)
  }, [])

  const handleSave = useCallback(
    async (e: FormEvent) => {
      e.preventDefault()
      if (isPending) return

      setFeedback(null)

      try {
        await update({ name: name.trim() })
        setFeedback({ type: 'success', message: 'Profile updated' })
      } catch (error) {
        setFeedback({ type: 'error', message: readErrorMessage(error, 'Failed to update profile') })
      }
    },
    [update, name, isPending],
  )

  const imageUrl = account.image_url

  return (
    <form onSubmit={handleSave}>
      <div data-conjoin-profile-head="">
        <Avatar.Root data-conjoin-avatar="" data-size="lg">
          {imageUrl ? <Avatar.Image src={imageUrl} alt="" /> : null}
          <Avatar.Fallback>{readInitials(account)}</Avatar.Fallback>
        </Avatar.Root>
        <div>
          <p data-conjoin-profile-name="">{readDisplayName(account)}</p>
          <p data-conjoin-profile-email="">{readPrimaryEmail(account)}</p>
        </div>
      </div>

      <Separator.Root data-conjoin-separator="" />

      <div data-conjoin-field="">
        <Label.Root data-conjoin-label="" htmlFor="conjoin-profile-name">
          Name
        </Label.Root>
        <input
          id="conjoin-profile-name"
          data-conjoin-input=""
          autoComplete="name"
          value={name}
          onChange={handleNameChange}
          maxLength={NAME_MAX_LENGTH}
        />
      </div>

      {feedback ? <FeedbackMessage feedback={feedback} /> : null}

      <button type="submit" data-conjoin-button="" data-variant="primary" disabled={isPending} aria-busy={isPending}>
        <BusyContent busy={isPending} label="Save" busyLabel="Saving" />
      </button>
    </form>
  )
}

type SessionRowProps = {
  session: ConjoinSession
  isCurrent: boolean
  isRevoking: boolean
  onRevoke: (sessionId: string) => void
}

function SessionRow({ session, isCurrent, isRevoking, onRevoke }: SessionRowProps) {
  const handleRevoke = useCallback(() => onRevoke(session.session_id), [onRevoke, session.session_id])
  const country = session.last_activity?.country_code
  const startedAt = session.last_activity?.initiated_at ?? session.date_created

  return (
    <div data-conjoin-session-row="">
      <div>
        <p data-conjoin-session-title="">{isCurrent ? 'Current session' : 'Signed-in session'}</p>
        <p data-conjoin-session-meta="">
          {new Date(startedAt).toLocaleString()}
          {country ? ` · ${country}` : ''}
        </p>
      </div>
      {isCurrent ? (
        <span data-conjoin-session-status="">Active</span>
      ) : (
        <button
          type="button"
          data-conjoin-button=""
          data-variant="outline"
          onClick={handleRevoke}
          disabled={isRevoking}
          aria-busy={isRevoking}
        >
          Sign out
        </button>
      )}
    </div>
  )
}

function SessionsTab() {
  const { isLoaded, sessions, currentSessionId, revoke, isRevoking } = useSessions()
  const [feedback, setFeedback] = useState<Feedback | null>(null)

  const handleRevoke = useCallback(
    async (sessionId: string) => {
      setFeedback(null)
      try {
        await revoke(sessionId)
        setFeedback({ type: 'success', message: 'Session signed out' })
      } catch (error) {
        setFeedback({ type: 'error', message: readErrorMessage(error, 'Failed to sign out the session') })
      }
    },
    [revoke],
  )

  return (
    <div>
      <h3 data-conjoin-heading="" data-level="section">
        Active sessions
      </h3>

      {feedback ? <FeedbackMessage feedback={feedback} /> : null}

      {isLoaded ? (
        sessions.map(session => (
          <SessionRow
            key={session.session_id}
            session={session}
            isCurrent={session.session_id === currentSessionId}
            isRevoking={isRevoking}
            onRevoke={handleRevoke}
          />
        ))
      ) : (
        <p data-conjoin-muted="">Loading session data...</p>
      )}
    </div>
  )
}

export function AccountProfile() {
  const { account } = useAccount()
  const [activeTab, setActiveTab] = useState<TabValue>('profile')

  const handleTabChange = useCallback((value: string) => {
    setActiveTab(value === 'sessions' ? 'sessions' : 'profile')
  }, [])

  if (!account) {
    return (
      <div data-conjoin-card="">
        <div data-conjoin-state="">
          <Spinner size="md" label="Loading account" />
        </div>
      </div>
    )
  }

  return (
    <div data-conjoin-card="">
      <Tabs.Root value={activeTab} onValueChange={handleTabChange}>
        <Tabs.List data-conjoin-tabs-list="" aria-label="Account settings sections">
          <Tabs.Trigger data-conjoin-tabs-trigger="" value="profile">
            Profile
          </Tabs.Trigger>
          <Tabs.Trigger data-conjoin-tabs-trigger="" value="sessions">
            Sessions
          </Tabs.Trigger>
        </Tabs.List>

        <Tabs.Content data-conjoin-tabs-content="" value="profile" forceMount hidden={activeTab !== 'profile'}>
          {activeTab === 'profile' ? <ProfileTab account={account} /> : null}
        </Tabs.Content>

        <Tabs.Content data-conjoin-tabs-content="" value="sessions" forceMount hidden={activeTab !== 'sessions'}>
          {activeTab === 'sessions' ? <SessionsTab /> : null}
        </Tabs.Content>
      </Tabs.Root>
    </div>
  )
}
