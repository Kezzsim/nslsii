import pytest
import io
import os

from ..main import sync_experiment

# Set this if there is an LDAP container running for testing.
# See continuous_integration/ldap/start_ldap.yml
TEST_LDAP = os.getenv("TILED_TEST_LDAP")


@pytest.mark.default_cassette("interactions.yaml")
@pytest.mark.vcr
def test_ipython(monkeypatch):
    # To avoid posting a fake proposal to real redis, check containers
    if not TEST_LDAP:
        pytest.skip("Run an LDAP container and set TEST_LDAP to run")
    # Pytest cannot handle stdin, so we need to read a canned response.
    monkeypatch.setattr("sys.stdin", io.StringIO("ftouden\nreddragon\n"))
    sync_experiment(proposal_number=56789, beamline="tst")
    assert True
