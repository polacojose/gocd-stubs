from pydantic import BaseModel


class PipelineStatus(BaseModel):
    paused: bool
    paused_cause: str
    paused_by: str
    locked: bool
    schedulable: bool
