from pydantic import BaseModel, Field


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
