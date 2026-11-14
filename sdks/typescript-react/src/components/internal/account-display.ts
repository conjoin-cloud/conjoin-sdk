import type { ConjoinAccount } from '@conjoin-cloud/react-core'

export function readPrimaryEmail(account: ConjoinAccount | null): string {
  const emails = account?.emails ?? []

  return (emails.find(entry => entry.is_primary) ?? emails[0])?.email ?? ''
}

export function readDisplayName(account: ConjoinAccount | null): string {
  return account?.name?.trim() || readPrimaryEmail(account)
}

export function readInitials(account: ConjoinAccount | null): string {
  const words = readDisplayName(account).split(/\s+/).filter(Boolean)
  const initials = words.length > 1 ? `${words[0]?.[0] ?? ''}${words.at(-1)?.[0] ?? ''}` : (words[0]?.[0] ?? '')

  return initials.toUpperCase()
}
