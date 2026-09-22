import pytest
from gocd import MaterialsApi, MaterialsGitNotifyRequest

from tests.component_tests.conftest import accept


@pytest.fixture(scope="module")
def api_instance(gocd_test_container_client):
    yield MaterialsApi(gocd_test_container_client)


def test_get_materials(api_instance: MaterialsApi):
    response = api_instance.get_all_materials_go_api_config_materials_get(
        accept=accept,
    )

    assert len(response.embedded.materials) > 0


def test_material_git_notify(api_instance: MaterialsApi):
    message = api_instance.notify_git_materials_go_api_admin_materials_git_notify_post(
        materials_git_notify_request=MaterialsGitNotifyRequest(
            repository_url="git@github.com:polacojose/open_exercise.git"
        ),
        accept=accept,
        x_go_cd_confirm="true",
    )

    assert (
        message.message
        == "The material is now scheduled for an update. Please check relevant pipeline(s) for status."
    )
