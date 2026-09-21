from fastapi import APIRouter, Depends
from pydantic import BaseModel

from common import Tags, basic, verify_accept_header_v1

router = APIRouter(
    prefix="/go/api/current_user/access_tokens",
    tags=[Tags.AccessTokens],
    dependencies=[Depends(basic), Depends(verify_accept_header_v1)],
)


class AccessToken(BaseModel):
    id: int
    description: str
    username: str
    revoked: bool
    token: str


@router.post("/")
async def create_token_current_user() -> AccessToken:
    return AccessToken()  # ty: ignore[missing-argument]
