from datetime import datetime
from enum import Enum
from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.security import (
    HTTPBearer,
)
from pydantic import BaseModel, field_validator


class Tags(str, Enum):
    Materials = "Materials"
    Pipelines = "Pipelines"
    Jobs = "Jobs"


app = FastAPI()

bearer = HTTPBearer()


# Define header dependency with default / OpenAPI documentation
def verify_accept_header_v2(
    accept: Annotated[
        str,
        Header(
            alias="Accept",
            description="API Accept Header",
            json_schema_extra={"example": "application/vnd.go.cd.v2+json"},
        ),
    ] = "application/vnd.go.cd.v2+json",
):
    if accept != "application/vnd.go.cd.v2+json":
        raise HTTPException(
            status_code=406,
            detail="Header 'Accept: application/vnd.go.cd.v2+json' is required",
        )
    return accept


def verify_accept_header_v1(
    accept: Annotated[
        str,
        Header(
            alias="Accept",
            description="API Accept Header",
            json_schema_extra={"example": "application/vnd.go.cd.v1+json"},
        ),
    ] = "application/vnd.go.cd.v1+json",
):
    if accept != "application/vnd.go.cd.v1+json":
        raise HTTPException(
            status_code=406,
            detail="Header 'Accept: application/vnd.go.cd.v1+json' is required",
        )
    return accept


########## Materials ##########


@app.post(
    "/go/api/admin/materials/svn/notify",
    tags=[Tags.Materials],
    dependencies=[Depends(bearer), Depends(verify_accept_header_v2)],
)
async def materials_notify(repository_url: str) -> str:
    return "Success"


########## Pipelines ##########


class PipelineStatusResponse(BaseModel):
    paused: bool
    paused_cause: str
    paused_by: str
    locked: bool
    schedulable: bool


@app.get(
    "/go/api/pipelines/{pipeline_name}/status",
    tags=[Tags.Pipelines],
    dependencies=[Depends(bearer), Depends(verify_accept_header_v1)],
)
async def pipeline_status(pipeline_name: str) -> PipelineStatusResponse:
    return PipelineStatusResponse()  # ty: ignore[missing-argument]


########## Jobs ##########


class JobState(str, Enum):
    Scheduled = "Scheduled"
    Assigned = "Assigned"
    Preparing = "Preparing"
    Building = "Building"
    Completing = "Completing"
    Completed = "Completed"
    Rescheduled = "Rescheduled"


class JobHistoryResponseItem(BaseModel):
    name: str
    state: JobState
    result: str
    original_job_id: int | None
    scheduled_date: datetime
    rerun: bool
    agent_uuid: str | None
    pipeline_name: str
    pipeline_counter: int
    stage_name: str
    stage_counter: str

    @field_validator("scheduled_date")
    def dt_validate(cls, dt) -> datetime:
        return datetime.fromtimestamp(dt)

    @field_validator("state")
    def st_validate(cls, st) -> JobState:
        return JobState(st)


class JobHistoryResponse(BaseModel):
    jobs: list[JobHistoryResponseItem]


@app.get(
    "/go/api/jobs/{pipeline_name}/{stage_name}/{job_name}/history",
    tags=[Tags.Jobs],
    dependencies=[Depends(bearer), Depends(verify_accept_header_v1)],
)
async def pipeline_job_history(
    pipeline_name: str, stage_name: str, job_name: str
) -> JobHistoryResponse:
    return JobHistoryResponse()  # ty: ignore[missing-argument]
