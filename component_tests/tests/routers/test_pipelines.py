from gocd import PipelinesApi

from tests.routers.conftest import accept, api_client

api_instance = PipelinesApi(api_client)


def test_get_pipeline_status(_gocd_test_container):
    status = api_instance.pipeline_status_go_api_pipelines_pipeline_name_status_get(
        pipeline_name="Open_Exercise_Server", accept=accept
    )
    assert status.paused == False
    assert status.locked == False
