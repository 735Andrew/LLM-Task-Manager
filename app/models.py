from pydantic import BaseModel, Field

from config import KEY_PATTERN


class AccessKey(BaseModel):
    key: str = Field(min_length=8, max_length=255, pattern=KEY_PATTERN)


class ChatMessage(BaseModel):
    message: str = Field(min_length=1, max_length=500)
