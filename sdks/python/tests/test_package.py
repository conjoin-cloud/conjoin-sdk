from importlib.metadata import PackageNotFoundError, version

from conjoin_cloud import DEFAULT_API_VERSION, __version__
from conjoin_cloud._version import _UNKNOWN_VERSION


def test_version_matches_project_metadata() -> None:
    try:
        expected_version = version("conjoin-cloud")
    except PackageNotFoundError:
        expected_version = _UNKNOWN_VERSION

    assert __version__ == expected_version


def test_default_api_version_is_current() -> None:
    assert DEFAULT_API_VERSION == "2026-06-01"
