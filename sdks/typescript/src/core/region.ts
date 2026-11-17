export const CONJOIN_REGIONS = ['us', 'eu', 'gh'] as const

export type ConjoinRegion = (typeof CONJOIN_REGIONS)[number]

const REGION_OF_KEY_WITHOUT_REGION_CODE: ConjoinRegion = 'us'
const CONJOIN_API_ROOT_DOMAIN = 'conjoin.cloud'
const KEY_BASE_PREFIXES = ['cak_', 'cpk_'] as const
const KEY_MODE_SEGMENTS = new Set(['live', 'test'])
const KEY_SEGMENT_SEPARATOR = '_'

const isConjoinRegion = (value: string | undefined): value is ConjoinRegion =>
  value !== undefined && (CONJOIN_REGIONS as readonly string[]).includes(value)

export function readConjoinKeyRegion(key: string): ConjoinRegion {
  const basePrefix = KEY_BASE_PREFIXES.find(prefix => key.startsWith(prefix))

  if (basePrefix === undefined) {
    return REGION_OF_KEY_WITHOUT_REGION_CODE
  }

  const [regionSegment, modeSegment] = key.slice(basePrefix.length).split(KEY_SEGMENT_SEPARATOR, 2)

  if (isConjoinRegion(regionSegment) && modeSegment !== undefined && KEY_MODE_SEGMENTS.has(modeSegment)) {
    return regionSegment
  }

  return REGION_OF_KEY_WITHOUT_REGION_CODE
}

export function buildConjoinRegionBaseUrl(region: ConjoinRegion): string {
  return region === REGION_OF_KEY_WITHOUT_REGION_CODE
    ? `https://api.${CONJOIN_API_ROOT_DOMAIN}`
    : `https://api.${region}.${CONJOIN_API_ROOT_DOMAIN}`
}
