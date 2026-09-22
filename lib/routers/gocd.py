from fastapi import APIRouter, Depends

from common import (
    Tags,
    authenticate_user,
    verify_accept_header,
)

router = APIRouter(
    prefix="/go/api/admin",
    tags=[Tags.GoCD],
    dependencies=[
        Depends(authenticate_user),
        Depends(verify_accept_header),
    ],
)


@router.get(
    "/config.xml",
)
async def get_config() -> str:
    return ""
