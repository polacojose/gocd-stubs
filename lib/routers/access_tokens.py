from fastapi import APIRouter, Depends

from common import Tags, basic, create_gocd_accept_class, verify_gocd_confirm_header
from models.access_tokens import AccessToken

router = APIRouter(
    prefix="/go/api/current_user/access_tokens",
    tags=[Tags.AccessTokens],
    default_response_class=create_gocd_accept_class(version=1),
    dependencies=[
        Depends(basic),
        Depends(verify_gocd_confirm_header),
    ],
)


@router.post("/")
async def create_token_current_user() -> AccessToken:
    return AccessToken()  # ty: ignore[missing-argument]
