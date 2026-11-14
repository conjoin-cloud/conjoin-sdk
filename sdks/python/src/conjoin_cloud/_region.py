from __future__ import annotations

from typing import Literal, get_args

ConjoinRegion = Literal["us", "eu", "gh"]

CONJOIN_REGIONS: tuple[ConjoinRegion, ...] = get_args(ConjoinRegion)

_REGION_OF_KEY_WITHOUT_REGION_CODE: ConjoinRegion = "us"
_CONJOIN_API_ROOT_DOMAIN = "conjoin.cloud"
_KEY_BASE_PREFIXES = ("cak_", "cpk_")
_KEY_MODE_SEGMENTS = frozenset({"live", "test"})
_KEY_SEGMENT_SEPARATOR = "_"


def read_conjoin_key_region(key: str) -> ConjoinRegion:
    base_prefix = next((prefix for prefix in _KEY_BASE_PREFIXES if key.startswith(prefix)), None)
    if base_prefix is None:
        return _REGION_OF_KEY_WITHOUT_REGION_CODE

    segments = key[len(base_prefix) :].split(_KEY_SEGMENT_SEPARATOR, 2)
    if len(segments) < 2:
        return _REGION_OF_KEY_WITHOUT_REGION_CODE

    region_segment, mode_segment = segments[0], segments[1]
    for region in CONJOIN_REGIONS:
        if region == region_segment and mode_segment in _KEY_MODE_SEGMENTS:
            return region

    return _REGION_OF_KEY_WITHOUT_REGION_CODE


def build_conjoin_region_base_url(region: ConjoinRegion) -> str:
    if region == _REGION_OF_KEY_WITHOUT_REGION_CODE:
        return f"https://api.{_CONJOIN_API_ROOT_DOMAIN}"
    return f"https://api.{region}.{_CONJOIN_API_ROOT_DOMAIN}"
