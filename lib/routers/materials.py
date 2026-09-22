from pydantic import BaseModel
from fastapi import APIRouter, Depends, status

from common import (
    ConfirmationMessage,
    Tags,
    authenticate_user,
    verify_accept_header,
    verify_gocd_confirm_header,
)

router = APIRouter(
    prefix="/go/api/admin/materials",
    tags=[Tags.Materials],
    dependencies=[
        Depends(authenticate_user),
        Depends(verify_accept_header),
        Depends(verify_gocd_confirm_header),
    ],
)


class MaterialsGitNotifyRequest(BaseModel):
    repository_url: str


@router.post(
    "/git/notify",
    status_code=status.HTTP_202_ACCEPTED,
)
async def materials_git_notify(
    request: MaterialsGitNotifyRequest,
) -> ConfirmationMessage:
    return ConfirmationMessage()  # ty: ignore[missing-argument]
