from __future__ import annotations

import pytest

from conjoin_cloud import Conjoin


@pytest.mark.parametrize(
    ("key", "base_url"),
    [
        ("cak_gh_live_harbourledger", "https://api.gh.conjoin.cloud"),
        ("cak_eu_test_harbourledger", "https://api.eu.conjoin.cloud"),
        ("cpk_gh_test_harbourledger", "https://api.gh.conjoin.cloud"),
        ("cpk_eu_live_harbourledger", "https://api.eu.conjoin.cloud"),
        ("cak_live_harbourledger", "https://api.conjoin.cloud"),
        ("cak_us_live_harbourledger", "https://api.conjoin.cloud"),
        ("cak_gh_staging_harbourledger", "https://api.conjoin.cloud"),
        ("sk_eu_live_harbourledger", "https://api.conjoin.cloud"),
    ],
)
def test_the_key_selects_the_regional_address(key: str, base_url: str) -> None:
    client = (
        Conjoin(publishable_key=key) if key.startswith("cpk_") else Conjoin(api_key=key)
    )

    with client:
        assert client.config.base_url == base_url
