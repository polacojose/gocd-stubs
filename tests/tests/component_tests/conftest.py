import pytest
from gocd import ApiClient, Configuration
from testcontainers.core.container import DockerContainer
from testcontainers.core.image import DockerImage
from testcontainers.core.waiting_utils import wait_for_logs

accept = "application/vnd.go.cd+json"


@pytest.fixture(scope="package")
def gocd_test_container_client():
    with (
        DockerImage(
            path="./docker/", tag="gocd-component_tests-image:v25.3.0"
        ) as image,
        DockerContainer(image=str(image), ports=[8153]) as container,
    ):
        port = container.get_exposed_port(8153)
        wait_for_logs(container, "GoCD server started successfully.")

        client = ApiClient(
            Configuration(
                host=f"http://localhost:{port}", username="admin", password="admin"
            )
        )

        yield client
