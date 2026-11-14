import type { ConjoinListPage } from '@conjoin-cloud/sdk'

export const MAX_COLLECTED_ITEMS = 1_000

export async function collectPages<T>(firstPage: Promise<ConjoinListPage<T>>, stop?: (item: T) => boolean) {
  const items: T[] = []

  for await (const item of await firstPage) {
    items.push(item)
    if (stop?.(item) || items.length >= MAX_COLLECTED_ITEMS) break
  }

  return items
}
