from gocd import CurrentUserApi

from tests.routers.conftest import accept, api_client

api_instance = CurrentUserApi(api_client)


def test_get_current_user(_gocd_test_container):
    current_user = api_instance.get_current_user_go_api_current_user_get(accept=accept)
    assert current_user.login_name == "admin"
    assert current_user.display_name == "admin"
    assert current_user.enabled == True
