from pydantic import BaseModel, Field
from pydantic_core import Url


class MaterialsGitNotifyRequest(BaseModel):
    repository_url: str


class MaterialAttributes(BaseModel):
    url: Url
    invert_filter: bool
    name: str | None
    auto_update: bool
    branch: str | None
    shallow_clone: bool


class Material(BaseModel):
    type: str
    fingerprint: str
    attributes: MaterialAttributes


class MaterialsEmbedded(BaseModel):
    materials: list[Material]


class MaterialsResponse(BaseModel):
    embedded: MaterialsEmbedded = Field(alias="_embedded")
