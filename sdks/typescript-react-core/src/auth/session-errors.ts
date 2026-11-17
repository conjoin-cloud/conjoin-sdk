import { ConjoinApiError } from '@conjoin-cloud/sdk'

const SESSION_REJECTION_STATUSES: ReadonlySet<number> = new Set([400, 401, 403])

export const isSessionRejection = (error: unknown): boolean =>
  error instanceof ConjoinApiError && SESSION_REJECTION_STATUSES.has(error.status)

export async function readSessionUnlessRejected<T>(read: () => Promise<T>): Promise<T | null> {
  try {
    return await read()
  } catch (error) {
    if (isSessionRejection(error)) return null
    throw error
  }
}
