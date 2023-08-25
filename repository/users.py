from sqlalchemy.orm import Session
import schemas.users as schema_users
import models.users as model_users
from utils import utils


def create(request: schema_users.UserIn, db: Session):
    """
    Create a new user
    """
    user = model_users.User(
        username=request.username,
        email=request.email,
        password=utils.hash_password(request.password)
    )
    
    print(user.__dict__.items())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def show(db: Session):
    """
    Show a user
    """
    return db.query(model_users.User).all()
