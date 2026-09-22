from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field
from pydantic_core import Url

from common import (
    ConfirmationMessage,
    Tags,
    authenticate_user,
    verify_accept_header,
    verify_gocd_confirm_header,
)

router = APIRouter(
    prefix="/go/api",
    tags=[Tags.Materials],
    dependencies=[
        Depends(authenticate_user),
        Depends(verify_accept_header),
        Depends(verify_gocd_confirm_header),
    ],
)


class MaterialsGitNotifyRequest(BaseModel):
    repository_url: str


class MaterialAttributes(BaseModel):
    url: Url
    invert_filter: bool
    name: str | None
    auto_update: bool
    branch: str | None
    shallow_clone: bool


class Material(BaseModel):
    type: str
    fingerprint: str
    attributes: MaterialAttributes


class MaterialsEmbedded(BaseModel):
    materials: list[Material]


class MaterialsResponse(BaseModel):
    embedded: MaterialsEmbedded = Field(alias="_embedded")


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
    return ConfirmationMessage()  # ty: ignore[missing-argument]
