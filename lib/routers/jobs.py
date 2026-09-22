from datetime import datetime
from enum import Enum

from fastapi import APIRouter, Depends
from pydantic import BaseModel, field_validator

from common import Tags, authenticate_user, verify_accept_header

router = APIRouter(
    prefix="/go/api/jobs",
    tags=[Tags.Jobs],
    dependencies=[Depends(authenticate_user), Depends(verify_accept_header)],
)


class JobState(str, Enum):
    Scheduled = "Scheduled"
    Assigned = "Assigned"
    Preparing = "Preparing"
    Building = "Building"
    Completing = "Completing"
    Completed = "Completed"
    Rescheduled = "Rescheduled"


class JobStateTransition(BaseModel):
    state: JobState
    state_change_time: int

    @field_validator("state_change_time")
    def dt_validate(cls, dt) -> datetime:
        return datetime.fromtimestamp(dt)  # noqa: DTZ006


class JobItem(BaseModel):
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
    job_state_transitions: list[JobStateTransition] | None

    @field_validator("scheduled_date")
    def dt_validate(cls, dt) -> datetime:
        return datetime.fromtimestamp(dt)  # noqa: DTZ006

    @field_validator("state")
    def st_validate(cls, st) -> JobState:
        return JobState(st)


class JobHistory(BaseModel):
    jobs: list[JobItem]


@router.get("/{pipeline_name}/{stage_name}/{job_name}/history")
async def pipeline_job_history(
    pipeline_name: str, stage_name: str, job_name: str
) -> JobHistory:
    _ = (pipeline_name, stage_name, job_name)
    return JobHistory()  # ty: ignore[missing-argument]


@router.get(
    "/{pipeline_name}/{pipeline_counter}/{stage_name}/{stage_counter}/{job_name}"
)
async def pipeline_job(
    pipeline_name: str,
    pipeline_counter: int,
    stage_name: str,
    stage_counter: int,
    job_name: str,
) -> JobItem:
    _ = (pipeline_name, pipeline_counter, stage_name, stage_counter, job_name)
    return JobItem()  # ty: ignore[missing-argument]
