import { useAccount, useAuth } from '@conjoin-cloud/react-core'
import * as Avatar from '@radix-ui/react-avatar'
import * as DropdownMenu from '@radix-ui/react-dropdown-menu'
import * as Separator from '@radix-ui/react-separator'
import { useCallback } from 'react'
import { readDisplayName, readInitials, readPrimaryEmail } from '../internal/account-display'

type AccountButtonProps = {
  onManageAccount?: () => void
  onSignOut?: () => void
}

export function AccountButton({ onManageAccount, onSignOut }: AccountButtonProps) {
  const auth = useAuth()
  const { account } = useAccount()

  const handleSignOut = useCallback(async () => {
    await auth.signOut()
    onSignOut?.()
  }, [auth, onSignOut])

  if (!auth.isLoaded || !auth.isSignedIn) return null

  const displayName = readDisplayName(account ?? null)
  const email = readPrimaryEmail(account ?? null)
  const initials = readInitials(account ?? null)
  const showEmail = email !== '' && displayName !== email

  return (
    <DropdownMenu.Root>
      <DropdownMenu.Trigger asChild>
        <button type="button" data-conjoin-trigger="" aria-label="Account menu">
          <Avatar.Root data-conjoin-avatar="" data-size="md">
            {account?.image_url ? <Avatar.Image src={account.image_url} alt={displayName} /> : null}
            <Avatar.Fallback>{initials}</Avatar.Fallback>
          </Avatar.Root>
        </button>
      </DropdownMenu.Trigger>

      <DropdownMenu.Portal>
        <DropdownMenu.Content data-conjoin-menu-content="" sideOffset={8} align="end">
          <div data-conjoin-menu-header="">
            <p data-conjoin-menu-name="">{displayName}</p>
            {showEmail ? <p data-conjoin-menu-email="">{email}</p> : null}
          </div>

          <Separator.Root data-conjoin-menu-separator="" />

          {onManageAccount ? (
            <DropdownMenu.Item data-conjoin-menu-item="" onSelect={onManageAccount}>
              Manage account
            </DropdownMenu.Item>
          ) : null}

          <DropdownMenu.Item data-conjoin-menu-item="" onSelect={handleSignOut}>
            Sign out
          </DropdownMenu.Item>
        </DropdownMenu.Content>
      </DropdownMenu.Portal>
    </DropdownMenu.Root>
  )
}
