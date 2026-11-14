import { ConjoinResponseError } from './errors'
import type { ConjoinResponseMeta, Cursor } from './types'

export type ConjoinListPage<T> = {
  readonly response: ConjoinResponseMeta
  readonly data: T[]
  readonly cursor: Cursor
  hasNextPage(): boolean
  nextPage(): Promise<ConjoinListPage<T> | null>
  [Symbol.asyncIterator](): AsyncIterator<T>
}

export type FetchNextListPage<T> = (nextCursor: string, seenCursors: ReadonlySet<string>) => Promise<ConjoinListPage<T>>

type ListBody = {
  response?: unknown
  data?: unknown
  cursor?: unknown
}

const readCursorToken = (value: unknown): string | null =>
  typeof value === 'string' && value.length > 0 ? value : null

function readCursor(value: unknown): Cursor {
  if (!value || typeof value !== 'object') {
    return { prev: null, next: null }
  }

  const cursor = value as Record<string, unknown>

  return { prev: readCursorToken(cursor.prev), next: readCursorToken(cursor.next) }
}

export function createListPage<T>(
  body: unknown,
  status: number,
  requestId: string | undefined,
  fetchNext: FetchNextListPage<T> | undefined,
  seenCursors: ReadonlySet<string> = new Set(),
): ConjoinListPage<T> {
  const list = (body && typeof body === 'object' ? body : {}) as ListBody

  if (!Array.isArray(list.data)) {
    throw new ConjoinResponseError('The list response did not hold a data array', { status, requestId })
  }

  const data = list.data as T[]
  const cursor = readCursor(list.cursor)
  const response = (list.response && typeof list.response === 'object' ? list.response : {}) as ConjoinResponseMeta
  const hasNextPage = () => cursor.next !== null && fetchNext !== undefined

  const nextPage = async (): Promise<ConjoinListPage<T> | null> => {
    if (cursor.next === null || fetchNext === undefined) {
      return null
    }

    if (seenCursors.has(cursor.next)) {
      throw new ConjoinResponseError('The list returned a cursor that it had returned before', { status, requestId })
    }
    return fetchNext(cursor.next, new Set([...seenCursors, cursor.next]))
  }

  async function* iterate(): AsyncGenerator<T> {
    let page: ConjoinListPage<T> | null = {
      response,
      data,
      cursor,
      hasNextPage,
      nextPage,
      [Symbol.asyncIterator]: iterate,
    }
    const seenCursors = new Set<string>()

    while (page !== null) {
      yield* page.data

      const next = page.cursor.next

      if (next === null || !page.hasNextPage()) {
        return
      }

      if (seenCursors.has(next)) {
        throw new ConjoinResponseError('The list returned a cursor that it had returned before', {
          status,
          requestId,
        })
      }

      seenCursors.add(next)
      page = await page.nextPage()
    }
  }

  return { response, data, cursor, hasNextPage, nextPage, [Symbol.asyncIterator]: iterate }
}
