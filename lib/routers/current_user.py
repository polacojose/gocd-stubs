from fastapi import APIRouter, Depends

from common import (
    Tags,
    authenticate_user,
    create_gocd_accept_class,
    verify_accept_header,
)
from routers.users import User

router = APIRouter(
    prefix="/go/api/current_user",
    tags=[Tags.CurrentUser],
    default_response_class=create_gocd_accept_class(version=1),
    dependencies=[Depends(verify_accept_header(1)), Depends(authenticate_user)],
)


@router.get("/")
async def get_current_user() -> User:
    return User()  # ty: ignore[missing-argument]
