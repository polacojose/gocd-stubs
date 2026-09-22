from pydantic import BaseModel
from enum import Enum
from typing import Annotated

from fastapi import Depends, Header, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBearer


class Tags(str, Enum):
    AccessTokens = "Access Tokens"
    CurrentUser = "Current User"
    Jobs = "Jobs"
    Materials = "Materials"
    Pipelines = "Pipelines"
    Users = "Users"


class ConfirmationMessage(BaseModel):
    message: str


bearer = HTTPBearer()
basic = HTTPBasic()


async def authenticate_user(
    basic_auth=Depends(basic),  # Make sure your security schemes have auto_error=False
    bearer_auth=Depends(bearer),
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


def verify_accept_header(
    accept: Annotated[
        str,
        Header(
            alias="Accept",
            description="API Accept Header",
            json_schema_extra={"accept": "application/vnd.go.cd+json"},
        ),
    ] = "application/vnd.go.cd+json",
):
    if accept != "application/vnd.go.cd+json":
        raise HTTPException(
            status_code=406,
            detail="Header 'Accept: application/vnd.go.cd+json' is required",
        )
    return accept


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
