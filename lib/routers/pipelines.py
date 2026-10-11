from fastapi import APIRouter, Depends

from common import (
    Tags,
    authenticate_user,
    create_gocd_accept_class,
    verify_accept_header,
)
from models.pipelines import PipelineStatus

router = APIRouter(
    prefix="/go/api/pipelines",
    tags=[Tags.Pipelines],
    default_response_class=create_gocd_accept_class(version=1),
    dependencies=[Depends(verify_accept_header(1)), Depends(authenticate_user)],
)


@router.get("/{pipeline_name}/status")
async def pipeline_status(pipeline_name: str) -> PipelineStatus:
    _ = pipeline_name
    return PipelineStatus()  # ty: ignore[missing-argument]
