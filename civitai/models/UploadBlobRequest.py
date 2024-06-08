from typing import *

from pydantic import BaseModel, Field

from .TimeSpan import TimeSpan


class UploadBlobRequest(BaseModel):
    """
    None model

    """

    key: Optional[str] = Field(alias="key", default=None)

    replace: Optional[bool] = Field(alias="replace", default=None)

    duration: Optional[TimeSpan] = Field(alias="duration", default=None)
