from enum import Enum
from typing import Annotated

from fastapi import Header, HTTPException
from fastapi.security import HTTPBearer


class Tags(str, Enum):
    Materials = "Materials"
    Pipelines = "Pipelines"
    Jobs = "Jobs"


bearer = HTTPBearer()


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
