from fastapi import APIRouter, Depends

from common import (
    Tags,
    authenticate_user,
    create_gocd_accept_class,
    verify_accept_header,
)
from models.jobs import JobHistory, JobItem

router = APIRouter(
    prefix="/go/api/jobs",
    tags=[Tags.Jobs],
    default_response_class=create_gocd_accept_class(version=1),
    dependencies=[Depends(verify_accept_header(1)), Depends(authenticate_user)],
)


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
