from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class SimpleHealthMessage(BaseModel):
    health: str = Field(doc="A short summary of the error or warning.")


class HealthMessage(BaseModel):
    message: str = Field(doc="A short summary of the error or warning.")
    detail: str = Field(doc="A longer message with more details about the error.")
    level: str = Field(
        doc="The intensity of the message. Can be one of WARNING, ERROR."
    )
    time: datetime = Field(doc="The UTC time when the message was gnerated.")

    @field_validator("time")
    def dt_validate(cls, dt) -> datetime:
        return datetime.fromtimestamp(dt)  # noqa: DTZ006
