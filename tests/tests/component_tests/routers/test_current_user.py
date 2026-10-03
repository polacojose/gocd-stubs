import pytest
from gocd import CurrentUserApi

from tests.component_tests.conftest import accept


@pytest.fixture(scope="module")
def api_instance(gocd_test_container_client):
    yield CurrentUserApi(gocd_test_container_client)


def test_get_current_user(api_instance: CurrentUserApi):
    current_user = api_instance.get_current_user_go_api_current_user_get(accept=accept)
    assert current_user.login_name == "admin"
    assert current_user.display_name == "admin"
    assert current_user.enabled == True
