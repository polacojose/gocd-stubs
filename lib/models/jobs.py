from datetime import datetime
from enum import Enum

from pydantic import BaseModel, field_validator


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
