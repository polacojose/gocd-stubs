from enum import Enum
from typing import Annotated

from fastapi import Depends, Header, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBearer
from pydantic import BaseModel


class Tags(str, Enum):
    AccessTokens = "Access Tokens"
    CurrentUser = "Current User"
    GoCD = "GoCD"
    Health = "Health"
    Jobs = "Jobs"
    Materials = "Materials"
    Pipelines = "Pipelines"
    Users = "Users"


class ConfirmationMessage(BaseModel):
    message: str


basic = HTTPBasic(auto_error=False)
bearer = HTTPBearer(auto_error=False)


async def authenticate_user(
    basic_auth=Depends(basic),  # noqa: B008
    bearer_auth=Depends(bearer),  # noqa: B008
):
    """
    Allows either Basic Auth OR Bearer token authentication.
    """
    if not basic_auth and not bearer_auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing authentication credentials.",
            headers={"WWW-Authenticate": "Bearer, Basic"},
        )
    return basic_auth or bearer_auth


def verify_gocd_confirm_header(
    confirm: Annotated[
        str,
        Header(
            alias="X-GoCD-Confirm",
            description="API X-GoCD-Confirm Header: Must be 'true'",
            json_schema_extra={"X-GoCD-Confirm": "true"},
        ),
    ] = "true",
):
    if confirm != "true":
        raise HTTPException(
            status_code=406,
            detail="Header 'X-GoCD-Confirm: true' is required",
        )
    return confirm


def create_gocd_accept_class(version: int | None) -> type[JSONResponse]:
    class GoCDJSONResponse(JSONResponse):
        pass

    if version != None:
        GoCDJSONResponse.media_type = f"application/vnd.go.cd.v{version}+json"
    else:
        GoCDJSONResponse.media_type = "application/vnd.go.cd+json"

    return GoCDJSONResponse
