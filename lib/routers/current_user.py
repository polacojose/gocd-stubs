from fastapi import APIRouter, Depends
from pydantic import BaseModel

from common import Tags, authenticate_user, verify_accept_header_v1

router = APIRouter(
    prefix="/go/api/current_user",
    tags=[Tags.CurrentUser],
    dependencies=[Depends(authenticate_user), Depends(verify_accept_header_v1)],
)


class User(BaseModel):
    login_name: str
    display_name: str
    enabled: bool
    email: str | None
    email_me: bool


@router.get("/")
async def get_current_user() -> User:
    return User()  # ty: ignore[missing-argument]
