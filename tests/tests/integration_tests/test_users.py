import pytest
from gocd import UserCreate, UserPatch, UsersApi

from tests.integration_tests.conftest import accept


@pytest.fixture(scope="module")
def api_instance(gocd_test_container_client):
    yield UsersApi(gocd_test_container_client)


def test_user_flow(api_instance: UsersApi):

    login_name = "test_user"
    test_email = "test_user@test_email.com"

    # Create User
    user = api_instance.create_user_go_api_users_post(
        user_create=UserCreate(login_name="test_user", email=test_email, email_me=True),
        accept=accept,
    )

    assert user.enabled == True
    assert user.login_name == login_name
    assert user.display_name == login_name
    assert user.email == test_email
    assert user.email_me == True

    # Get User
    user = api_instance.get_user_go_api_users_login_name_get(
        login_name=login_name,
        accept=accept,
    )

    assert user.enabled == True
    assert user.login_name == login_name
    assert user.display_name == login_name
    assert user.email == test_email
    assert user.email_me == True

    users = api_instance.get_users_go_api_users_get(accept=accept).embedded.users
    assert len(users) == 2

    # Update User
    test_email = "someemail2@test.com"
    user = api_instance.patch_user_go_api_users_login_name_patch(
        login_name=login_name,
        user_patch=UserPatch(email=test_email, email_me=False),
        accept=accept,
    )

    assert user.enabled == True
    assert user.login_name == login_name
    assert user.display_name == login_name
    assert user.email == test_email
    assert user.email_me == False

    # Disable User
    user = api_instance.patch_user_go_api_users_login_name_patch(
        login_name=login_name,
        user_patch=UserPatch(enabled=False),
        accept=accept,
    )

    assert user.enabled == False

    # Delete User
    message = api_instance.delete_user_go_api_users_login_name_delete(
        login_name=login_name, accept=accept
    )

    assert (
        message.message
        == f"User with login name '{login_name}' was deleted successfully!"
    )

    users = api_instance.get_users_go_api_users_get(accept=accept).embedded.users
    # Confirm deleted
    assert len(users) == 1
