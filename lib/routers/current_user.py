from fastapi import APIRouter, Depends

from common import Tags, authenticate_user, verify_accept_header
from routers.users import User

router = APIRouter(
    prefix="/go/api/current_user",
    tags=[Tags.CurrentUser],
    dependencies=[Depends(authenticate_user), Depends(verify_accept_header)],
)


@router.get("/")
async def get_current_user() -> User:
    return User()  # ty: ignore[missing-argument]
