from fastapi import APIRouter, Depends

from common import (
    Tags,
    authenticate_user,
)

router = APIRouter(
    prefix="/go/api/admin",
    tags=[Tags.GoCD],
    dependencies=[
        Depends(authenticate_user),
    ],
)


@router.get(
    "/config.xml",
)
async def get_config() -> str:
    return ""
