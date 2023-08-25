from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from database import Base
# from .posts import Post

class User(Base):
    """User class"""

    __tablename__ = "users"

    id = Column(String, primary_key=True, default=str(uuid4()))
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # user_posts = relationship("Post", back_populates="author")

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"<User {self.username!r}>"

    def __str__(self):
        return self.username
    
