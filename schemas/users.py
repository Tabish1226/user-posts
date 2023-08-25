from datetime import datetime
from typing import List
from pydantic import BaseModel
from schemas.posts import Post


class User(BaseModel):
    username: str
    email: str
    is_admin: bool = False

    class Config:
        from_attributes = True


class UserIn(User):
    password: str

    class Config:
        from_attributes = True


class UserOut(User):
    posts: List[Post] = []

    class Config:
        from_attributes = True

class TokenData(BaseModel):
    sub: dict  # Subject (usually user identifier)
    exp: datetime  # Expiration time

    class Config:
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True