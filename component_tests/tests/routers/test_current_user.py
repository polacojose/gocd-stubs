from gocd import PipelinesApi

from tests.routers.conftest import api_client

api_instance = PipelinesApi(api_client)
accept = "application/vnd.go.cd.v1+json"


def test_get_current_user(_gocd_test_container):
    pipeline_status = (
        api_instance.pipeline_status_go_api_pipelines_pipeline_name_status_get(
            pipeline_name="Open_Exercise_Server", accept=accept
        )
    )

    assert pipeline_status.paused == False
    assert pipeline_status.locked == False
    assert pipeline_status.schedulable == True
