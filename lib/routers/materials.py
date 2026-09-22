from fastapi import APIRouter, Depends

from common import Tags, authenticate_user, verify_accept_header

router = APIRouter(
    prefix="/go/api/admin/materials",
    tags=[Tags.Materials],
    dependencies=[Depends(authenticate_user), Depends(verify_accept_header)],
)


@router.post("/svn/notify")
async def materials_notify(repository_url: str) -> str:
    return "Success"
