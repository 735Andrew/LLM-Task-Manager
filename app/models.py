from pydantic import BaseModel, Field

from config import KEY_PATTERN

class AccessKey(BaseModel):
    key: str = Field(min_length=8, max_length=255, pattern=KEY_PATTERN)
