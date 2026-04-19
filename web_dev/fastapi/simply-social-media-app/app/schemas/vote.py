from pydantic import BaseModel, Field


class VoteAction(BaseModel):
    post_id: int
    dir: int = Field(ge=0, le=1)


class Message(BaseModel):
    message: str

