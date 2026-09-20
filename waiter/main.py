import os
from time import sleep

from devtools import pprint
from openapi_client import ApiClient, Configuration, JobHistoryResponseItem, JobState

from generated.openapi_client.api.jobs_api import JobsApi


def main():

    configuration = Configuration(
        host=os.getenv("HOST"),
        access_token=os.getenv("ACCESS_TOKEN"),
    )
    with ApiClient(configuration) as api_client:
        api_instance = JobsApi(api_client)
        pipeline_name = "certbot-server"  # str |
        stage_name = "build"  # str |
        job_name = "build"  # str |
        accept = "application/vnd.go.cd.v1+json"  # str | API Accept Header (optional) (default to 'application/vnd.go.cd.v1+json')

        started = False
        last_state = JobState.COMPLETED

        while True:
            last_job = get_state(
                api_instance,
                pipeline_name,
                stage_name,
                job_name,
                accept,
            )

            if last_job is None:
                return

            if not started and last_job.state != JobState.COMPLETED:
                started = True

            if started:
                if last_job.state != last_state:
                    pprint(last_job)
                    last_state = last_job.state

                if last_job.state == JobState.COMPLETED:
                    return

            sleep(1)


def get_state(
    api_instance,
    pipeline_name,
    stage_name,
    job_name,
    accept,
) -> JobHistoryResponseItem | None:
    try:
        # Pipeline Job History
        api_response = api_instance.pipeline_job_history_go_api_jobs_pipeline_name_stage_name_job_name_history_get(
            pipeline_name, stage_name, job_name, accept=accept
        )
        return api_response.jobs[0]
    except Exception as e:
        print(
            f"Exception when calling JobsApi->pipeline_job_history_go_api_jobs_pipeline_name_stage_name_job_name_history_get: {e}\n"
        )


if __name__ == "__main__":
    main()
