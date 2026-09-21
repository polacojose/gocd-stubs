from fastapi import APIRouter, Depends
from pydantic import BaseModel

from common import Tags, bearer, verify_accept_header_v1

router = APIRouter(
    prefix="/go/api/pipelines",
    tags=[Tags.Pipelines],
    dependencies=[Depends(bearer), Depends(verify_accept_header_v1)],
)


class PipelineStatusResponse(BaseModel):
    paused: bool
    paused_cause: str
    paused_by: str
    locked: bool
    schedulable: bool


@router.get("/{pipeline_name}/status")
async def pipeline_status(pipeline_name: str) -> PipelineStatusResponse:
    return PipelineStatusResponse()  # ty: ignore[missing-argument]
