from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from common import ConfirmationMessage, Tags, authenticate_user, verify_accept_header

router = APIRouter(
    prefix="/go/api/users",
    tags=[Tags.Users],
    dependencies=[Depends(authenticate_user), Depends(verify_accept_header)],
)


class UserPatch(BaseModel):
    enabled: bool | None = None
    email: str | None = None
    email_me: bool | None = None


class UserCreate(UserPatch):
    login_name: str


class User(UserCreate):
    display_name: str


class UsersEmbedded(BaseModel):
    users: list[User]


class UsersResponse(BaseModel):
    embedded: UsersEmbedded = Field(alias="_embedded")


@router.get("/")
async def get_users() -> UsersResponse:
    return UsersResponse()  # ty: ignore[missing-argument]


@router.get("/{login_name}")
async def get_user(login_name: str) -> User:
    return User()  # ty: ignore[missing-argument]


@router.post("/")
async def create_user(user_base: UserCreate) -> User:
    return User()  # ty: ignore[missing-argument]


@router.patch("/{login_name}")
async def patch_user(login_name: str, user_patch: UserPatch) -> User:
    return User()  # ty: ignore[missing-argument]


@router.delete("/{login_name}")
async def delete_user(login_name: str) -> ConfirmationMessage:
    return ConfirmationMessage()  # ty: ignore[missing-argument]
