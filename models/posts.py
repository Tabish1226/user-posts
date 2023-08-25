from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Post(Base):
    """POST TABLE"""

    __tablename__ = "posts"

    id = Column(String, primary_key=True, default=str(uuid4()))

    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id = Column(String, ForeignKey("users.id"))
    
    author = relationship("User", backref="user_posts")

    def __init__(self, title, content, author_id):
        self.title = title
        self.content = content
        self.author_id = author_id

    def __repr__(self):
        return f"<Post {self.title!r}>"

    def __str__(self):
        return self.title
