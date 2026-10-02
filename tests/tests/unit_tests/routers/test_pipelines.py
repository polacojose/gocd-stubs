import pytest
from gocd import PipelinesApi

from tests.component_tests.conftest import accept


@pytest.fixture(scope="module")
def api_instance(gocd_test_container_client):
    yield PipelinesApi(gocd_test_container_client)


def test_get_pipeline_status(api_instance: PipelinesApi):
    status = api_instance.pipeline_status_go_api_pipelines_pipeline_name_status_get(
        pipeline_name="Example_Pipeline", accept=accept
    )
    assert status.paused == False
    assert status.locked == False
