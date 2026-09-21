from fastapi import APIRouter, Depends

from common import Tags, bearer, verify_accept_header_v2

router = APIRouter(
    prefix="/go/api/admin/materials",
    tags=[Tags.Materials],
    dependencies=[Depends(bearer), Depends(verify_accept_header_v2)],
)


@router.post("/svn/notify")
async def materials_notify(repository_url: str) -> str:
    return "Success"
