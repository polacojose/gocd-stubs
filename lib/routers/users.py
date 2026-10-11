from fastapi import APIRouter, Depends

from common import (
    ConfirmationMessage,
    Tags,
    authenticate_user,
    create_gocd_accept_class,
)
from models.users import User, UserCreate, UserPatch, UsersResponse

router = APIRouter(
    prefix="/go/api/users",
    tags=[Tags.Users],
    default_response_class=create_gocd_accept_class(version=3),
    dependencies=[Depends(authenticate_user)],
)


@router.get("/")
async def get_users() -> UsersResponse:
    return UsersResponse()  # ty: ignore[missing-argument]


@router.get("/{login_name}")
async def get_user(login_name: str) -> User:
    _ = login_name
    return User()  # ty: ignore[missing-argument]


@router.post("/")
async def create_user(user_base: UserCreate) -> User:
    _ = user_base
    return User()  # ty: ignore[missing-argument]


@router.patch("/{login_name}")
async def patch_user(login_name: str, user_patch: UserPatch) -> User:
    _ = (login_name, user_patch)
    return User()  # ty: ignore[missing-argument]


@router.delete("/{login_name}")
async def delete_user(login_name: str) -> ConfirmationMessage:
    _ = login_name
    return ConfirmationMessage()  # ty: ignore[missing-argument]
