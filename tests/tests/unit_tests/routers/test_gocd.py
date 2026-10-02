import pytest
from gocd import GoCDApi

from tests.component_tests.conftest import accept


@pytest.fixture(scope="module")
def api_instance(gocd_test_container_client):
    yield GoCDApi(gocd_test_container_client)


def test_get_config(api_instance: GoCDApi):
    config = api_instance.get_config_go_api_admin_config_xml_get(
        accept=accept,
    )

    assert "811219a0-e1fb-4688-bc09-092a70ce0c34" in config
