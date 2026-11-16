import type { ValidateFunction } from 'ajv'
import Ajv2020 from 'ajv/dist/2020'
import addFormats from 'ajv-formats'

type Schema = Record<string, unknown>

const PATTERN_SAMPLES: Readonly<Record<string, string>> = {
  '^[A-Z]{2}$': 'GH',
  '^cnj_req_[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$':
    'cnj_req_0198f0f7-5d0b-7b4a-8d5a-cf5693f0b2c1',
  '^[0-9a-f]+$': 'a1b2c3',
  '^[a-z][a-z0-9:._-]*$': 'invoice.paid',
  '^[a-z0-9][a-z0-9:._-]*$': 'invoice.paid',
  '^[0-9]{6}$': '123456',
  '^[a-z]{3,8}$': 'monthly',
  '^[A-Za-z0-9_]+(?:\\[(?:0|[1-9][0-9]?)\\])?(?:\\.[A-Za-z0-9_]+(?:\\[(?:0|[1-9][0-9]?)\\])?){0,7}$': 'items[0].name',
  '^[\\w-]{1,80}$': 'harbour-ledger',
  '^[a-z.]+$': 'billing.read',
  '^[a-z]{3,10}$': 'weekly',
  '^authact_[a-zA-Z0-9_-]+$': 'authact_harbour_ledger',
  '^[a-z][a-z0-9]*(_[a-z0-9]+)*$': 'harbour_ledger',
  '^[a-zA-Z0-9\\-_:.]+$': 'harbour-ledger:2026.11',
  '^[0-9A-Za-z#!&@]+$': 'Ledger#2026',
}

const FORMAT_SAMPLES: Readonly<Record<string, string>> = {
  uri: 'https://ledger.example.com/hooks/conjoin',
  email: 'ledger.owner@example.com',
  'date-time': '2026-11-14T10:00:00.000Z',
  date: '2026-11-14',
  uuid: '0198f0f7-5d0b-4b4a-8d5a-cf5693f0b2c1',
}

const MAX_DEPTH = 12

const isRecord = (value: unknown): value is Schema =>
  Boolean(value) && typeof value === 'object' && !Array.isArray(value)

export class SchemaSampler {
  readonly #ajv = new Ajv2020({ strict: false, allErrors: false })
  readonly #validators = new WeakMap<Schema, ValidateFunction>()

  constructor(readonly document: { components?: Record<string, unknown> }) {
    addFormats(this.#ajv)
  }

  sample(schema: unknown): unknown {
    return this.#sample(schema, 0)
  }

  matches(schema: unknown, value: unknown): boolean {
    if (!isRecord(schema)) return true

    let validator = this.#validators.get(schema)

    if (validator === undefined) {
      validator = this.#ajv.compile({ ...schema, components: this.document.components })
      this.#validators.set(schema, validator)
    }

    return validator(value)
  }

  #resolve(schema: Schema): Schema {
    const ref = schema.$ref

    if (typeof ref !== 'string') return schema

    const target = ref
      .replace(/^#\//, '')
      .split('/')
      .reduce<unknown>((node, key) => (isRecord(node) ? node[key] : undefined), this.document)

    if (!isRecord(target)) throw new Error(`Unresolved schema reference ${ref}`)

    return this.#resolve(target)
  }

  #sample(raw: unknown, depth: number): unknown {
    if (!isRecord(raw) || depth > MAX_DEPTH) return null

    const schema = this.#resolve(raw)

    if ('const' in schema) return schema.const
    if (Array.isArray(schema.enum)) return schema.enum.find(value => value !== null) ?? schema.enum[0]
    if (schema.example !== undefined && this.matches(schema, schema.example) && schema.example !== 'string') {
      return schema.example
    }

    for (const key of ['oneOf', 'anyOf'] as const) {
      const branches = schema[key]

      if (Array.isArray(branches)) {
        const candidates = branches.map(branch => this.#sample(branch, depth + 1))
        const nonNull = candidates.find(candidate => candidate !== null && this.matches(schema, candidate))

        return nonNull ?? candidates.find(candidate => this.matches(schema, candidate)) ?? candidates[0]
      }
    }

    if (Array.isArray(schema.allOf)) {
      return Object.assign({}, ...schema.allOf.map(part => this.#sample(part, depth + 1)))
    }

    const type = Array.isArray(schema.type) ? schema.type.find(value => value !== 'null') : schema.type

    return this.#sampleType(schema, type, depth)
  }

  #sampleType(schema: Schema, type: unknown, depth: number): unknown {
    if (type === 'string' && schema.format === 'binary') {
      return new Blob(['harbour ledger statement'], { type: 'text/plain' })
    }
    if (type === 'string') return this.#sampleString(schema)
    if (type === 'integer' || type === 'number') return this.#sampleNumber(schema, type)
    if (type === 'boolean') return true
    if (type === 'null') return null

    if (type === 'array') {
      const count = typeof schema.minItems === 'number' && schema.minItems > 0 ? schema.minItems : 1
      return Array.from({ length: count }, () => this.#sample(schema.items, depth + 1))
    }

    if (type === 'object' || isRecord(schema.properties)) {
      const properties = isRecord(schema.properties) ? schema.properties : {}
      const required = Array.isArray(schema.required) ? schema.required.map(String) : Object.keys(properties)

      return Object.fromEntries(required.map(name => [name, this.#sample(properties[name] ?? {}, depth + 1)]))
    }

    return 'sample'
  }

  #sampleString(schema: Schema): string {
    if (typeof schema.pattern === 'string') {
      const sample = PATTERN_SAMPLES[schema.pattern]
      if (sample === undefined) throw new Error(`Add a sample for the pattern ${schema.pattern}`)
      return sample
    }

    if (typeof schema.format === 'string' && FORMAT_SAMPLES[schema.format]) return FORMAT_SAMPLES[schema.format]

    const minLength = typeof schema.minLength === 'number' ? schema.minLength : 1
    const maxLength = typeof schema.maxLength === 'number' ? schema.maxLength : Math.max(minLength, 16)
    const base = 'harbourledger'.repeat(Math.ceil(Math.max(minLength, 1) / 13))

    return base.slice(0, Math.min(Math.max(minLength, Math.min(13, maxLength)), maxLength))
  }

  #sampleNumber(schema: Schema, type: string): number {
    const minimum = typeof schema.minimum === 'number' ? schema.minimum : undefined
    const exclusiveMinimum = typeof schema.exclusiveMinimum === 'number' ? schema.exclusiveMinimum : undefined
    const maximum = typeof schema.maximum === 'number' ? schema.maximum : undefined
    let value = minimum ?? (exclusiveMinimum !== undefined ? exclusiveMinimum + 1 : 1)

    if (maximum !== undefined && value > maximum) value = maximum

    return type === 'integer' ? Math.ceil(value) : value
  }
}
