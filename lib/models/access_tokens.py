from pydantic import BaseModel


class AccessToken(BaseModel):
    id: int
    description: str
    username: str
    revoked: bool
    token: str
