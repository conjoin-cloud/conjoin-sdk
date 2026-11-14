import { type ConjoinMembership, useAuth, useOrg } from '@conjoin-cloud/react-core'
import * as Avatar from '@radix-ui/react-avatar'
import * as Popover from '@radix-ui/react-popover'
import * as Separator from '@radix-ui/react-separator'
import { memo, useCallback, useState } from 'react'
import { Spinner } from '../internal/spinner'

type OrgSwitcherProps = {
  onOrgChange?: (organizationId: string) => void
  formatOrganization?: (membership: ConjoinMembership) => string
}

type OrgRowProps = {
  membership: ConjoinMembership
  label: string
  isActive: boolean
  isSwitching: boolean
  onSwitch: (organizationId: string) => void
}

const SWITCH_FAILED_MESSAGE = 'The organization could not be switched. Please try again.'

const defaultOrganizationLabel = (membership: ConjoinMembership): string => membership.organization_id

const OrgRow = memo(function OrgRow({ membership, label, isActive, isSwitching, onSwitch }: OrgRowProps) {
  const handleClick = useCallback(() => onSwitch(membership.organization_id), [onSwitch, membership.organization_id])

  return (
    <button
      type="button"
      data-conjoin-menu-item=""
      data-active={isActive ? 'true' : undefined}
      onClick={handleClick}
      disabled={isSwitching}
      aria-current={isActive ? 'true' : undefined}
    >
      <Avatar.Root data-conjoin-avatar="" data-size="sm">
        <Avatar.Fallback>{label[0]?.toUpperCase() ?? 'O'}</Avatar.Fallback>
      </Avatar.Root>
      <span>{label}</span>
    </button>
  )
})

export function OrgSwitcher({ onOrgChange, formatOrganization = defaultOrganizationLabel }: OrgSwitcherProps) {
  const auth = useAuth()
  const { isLoaded, membership, memberships, switchOrganization } = useOrg()

  const [isSwitching, setIsSwitching] = useState(false)
  const [isOpen, setIsOpen] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleSwitch = useCallback(
    async (organizationId: string) => {
      setIsSwitching(true)
      setError(null)
      try {
        await switchOrganization(organizationId)
        onOrgChange?.(organizationId)
        setIsOpen(false)
      } catch {
        setError(SWITCH_FAILED_MESSAGE)
      } finally {
        setIsSwitching(false)
      }
    },
    [switchOrganization, onOrgChange],
  )

  if (!auth.isLoaded || !auth.isSignedIn) return null

  const currentLabel = membership ? formatOrganization(membership) : 'Select organization'

  return (
    <Popover.Root open={isOpen} onOpenChange={setIsOpen}>
      <Popover.Trigger asChild>
        <button
          type="button"
          data-conjoin-button=""
          data-variant="outline"
          data-conjoin-org-trigger=""
          aria-label={`Current organization: ${membership ? currentLabel : 'None selected'}`}
        >
          <Avatar.Root data-conjoin-avatar="" data-size="sm">
            <Avatar.Fallback>{membership ? (currentLabel[0]?.toUpperCase() ?? 'O') : 'O'}</Avatar.Fallback>
          </Avatar.Root>
          <span>{currentLabel}</span>
        </button>
      </Popover.Trigger>

      <Popover.Portal>
        <Popover.Content data-conjoin-menu-content="" sideOffset={8} align="start">
          <div data-conjoin-menu-label="">Organizations</div>

          <Separator.Root data-conjoin-menu-separator="" />

          {error ? (
            <p data-conjoin-field-error="" role="alert">
              {error}
            </p>
          ) : null}

          {!isLoaded ? (
            <div data-conjoin-state="">
              <Spinner size="sm" label="Loading organizations" />
            </div>
          ) : null}

          {isLoaded
            ? memberships.map(entry => (
                <OrgRow
                  key={entry.organization_id}
                  membership={entry}
                  label={formatOrganization(entry)}
                  isActive={entry.organization_id === membership?.organization_id}
                  isSwitching={isSwitching}
                  onSwitch={handleSwitch}
                />
              ))
            : null}

          {isLoaded && memberships.length === 0 ? (
            <p data-conjoin-center="" data-conjoin-menu-label="">
              No organizations
            </p>
          ) : null}
        </Popover.Content>
      </Popover.Portal>
    </Popover.Root>
  )
}
