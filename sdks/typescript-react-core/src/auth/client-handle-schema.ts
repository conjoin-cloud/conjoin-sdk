import { CLIENT_HANDLE_IDENTIFIER_MAX_LENGTH, CLIENT_HANDLE_IDENTIFIER_PATTERN } from '@conjoin-cloud/sdk/auth'
import * as v from 'valibot'

const ClientHandleIdentifierSchema = v.pipe(
  v.string(),
  v.minLength(1),
  v.maxLength(CLIENT_HANDLE_IDENTIFIER_MAX_LENGTH),
  v.regex(CLIENT_HANDLE_IDENTIFIER_PATTERN),
)

export const ClientHandleSchema = v.object({
  client_id: ClientHandleIdentifierSchema,
  reference_id: ClientHandleIdentifierSchema,
})
