from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.user import UserRead


class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    content: str = Field(min_length=1)
    published: bool = True


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserRead

    model_config = ConfigDict(from_attributes=True)


class PostOut(BaseModel):
    Post: PostRead
    votes: int

