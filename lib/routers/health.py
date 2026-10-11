from fastapi import APIRouter, Depends, Response

from common import Tags, authenticate_user, create_gocd_accept_class
from models.health import HealthMessage, SimpleHealthMessage

router = APIRouter(
    prefix="/go/api",
    tags=[Tags.Health],
    default_response_class=create_gocd_accept_class(version=1),
    dependencies=[Depends(authenticate_user)],
)


@router.get("/v1/health")
async def check_health(response: Response) -> SimpleHealthMessage:
    response.media_type = "application/vnd.go.cd+json"
    response.status_code = 400
    return SimpleHealthMessage()  # ty: ignore[missing-argument]


@router.get("/server_health_messages")
async def health_messages() -> list[HealthMessage]:
    return []
