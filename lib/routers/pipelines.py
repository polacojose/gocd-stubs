from fastapi import APIRouter, Depends
from pydantic import BaseModel

from common import Tags, authenticate_user, verify_accept_header

router = APIRouter(
    prefix="/go/api/pipelines",
    tags=[Tags.Pipelines],
    dependencies=[Depends(authenticate_user), Depends(verify_accept_header)],
)


class PipelineStatus(BaseModel):
    paused: bool
    paused_cause: str
    paused_by: str
    locked: bool
    schedulable: bool


@router.get("/{pipeline_name}/status")
async def pipeline_status(pipeline_name: str) -> PipelineStatus:
    _ = pipeline_name
    return PipelineStatus()  # ty: ignore[missing-argument]
