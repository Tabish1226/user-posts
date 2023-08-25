from pydantic import BaseModel


class Post(BaseModel):
    id: str = None
    title: str = None
    content: str = None
    author_id: str = None
    class Config:
        from_attributes = True