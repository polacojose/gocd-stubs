from fastapi import APIRouter, Depends, status

from common import (
    ConfirmationMessage,
    Tags,
    authenticate_user,
    create_gocd_accept_class,
    verify_gocd_confirm_header,
)
from models.materials import MaterialsGitNotifyRequest, MaterialsResponse

router = APIRouter(
    prefix="/go/api",
    tags=[Tags.Materials],
    default_response_class=create_gocd_accept_class(version=2),
    dependencies=[
        Depends(authenticate_user),
        Depends(verify_gocd_confirm_header),
    ],
)


@router.get(
    "/config/materials",
)
async def get_all_materials() -> MaterialsResponse:
    return MaterialsResponse()  # ty: ignore[missing-argument]


@router.post(
    "/admin/materials/git/notify",
    status_code=status.HTTP_202_ACCEPTED,
)
async def notify_git_materials(
    request: MaterialsGitNotifyRequest,
) -> ConfirmationMessage:
    _ = request
    return ConfirmationMessage()  # ty: ignore[missing-argument]
