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


# Define header dependency with default / OpenAPI documentation
def verify_accept_header_v2(
    accept: Annotated[
        str,
        Header(
            alias="Accept",
            description="API Accept Header",
            json_schema_extra={"example": "application/vnd.go.cd.v2+json"},
        ),
    ] = "application/vnd.go.cd.v2+json",
):
    if accept != "application/vnd.go.cd.v2+json":
        raise HTTPException(
            status_code=406,
            detail="Header 'Accept: application/vnd.go.cd.v2+json' is required",
        )
    return accept


def verify_accept_header_v1(
    accept: Annotated[
        str,
        Header(
            alias="Accept",
            description="API Accept Header",
            json_schema_extra={"example": "application/vnd.go.cd.v1+json"},
        ),
    ] = "application/vnd.go.cd.v1+json",
):
    if accept != "application/vnd.go.cd.v1+json":
        raise HTTPException(
            status_code=406,
            detail="Header 'Accept: application/vnd.go.cd.v1+json' is required",
        )
    return accept
