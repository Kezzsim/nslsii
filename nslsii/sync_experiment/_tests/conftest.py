import pytest


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "record_mode": "none",
        # Obfuscate NSLS2API the Authorization request header
        "filter_headers": [("authorization", "NONE")],
    }
