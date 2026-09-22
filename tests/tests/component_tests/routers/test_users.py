import pytest
from gocd import UserCreate, UserPatch, UsersApi

from tests.component_tests.conftest import accept


@pytest.fixture(scope="module")
def api_instance(gocd_test_container_client):
    yield UsersApi(gocd_test_container_client)


def test_get_user(api_instance):
    user = api_instance.get_user_go_api_users_login_name_get(
        login_name="admin", accept=accept
    )

    assert user.login_name == "admin"
    assert user.display_name == "admin"
    assert user.enabled == True


def test_get_users(api_instance):
    response = api_instance.get_users_go_api_users_get(accept=accept)

    for user in response.embedded.users:
        assert user.login_name == "admin"
        assert user.display_name == "admin"
        assert user.enabled == True
        return

    assert False


def test_create_user(api_instance):
    user = api_instance.create_user_go_api_users_post(
        user_create=UserCreate(login_name="NewUser"), accept=accept
    )

    assert user.login_name == "NewUser"
    assert user.display_name == "NewUser"
    assert user.enabled == True


def test_patch_user(api_instance):

    test_email = "someemail@test.com"
    user = api_instance.patch_user_go_api_users_login_name_patch(
        login_name="admin",
        user_patch=UserPatch(email=test_email, email_me=True),
        accept=accept,
    )

    assert user.login_name == "admin"
    assert user.display_name == "admin"
    assert user.email == test_email
    assert user.email_me == True
