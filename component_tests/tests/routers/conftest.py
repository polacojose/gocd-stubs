import pytest
from gocd import ApiClient, Configuration
from testcontainers.core.container import DockerContainer
from testcontainers.core.image import DockerImage
from testcontainers.core.waiting_utils import wait_for_logs

configuration = Configuration(
    username="admin",
    password="admin",
)
api_client = ApiClient(configuration)


@pytest.fixture(scope="session")
def _gocd_test_container():
    with (
        DockerImage(path="./docker/", tag="gocd-test-image:v25.3.0") as image,
        DockerContainer(image=str(image), ports=[8153]) as container,
    ):
        configuration.host = f"http://localhost:{container.get_exposed_port(8153)}"
        global api_client
        api_client = ApiClient(configuration)
        wait_for_logs(container, "GoCD server started successfully.")

        yield container
