from datetime import timedelta
from models.users import User
from fastapi import HTTPException
from utils.utils import verify_password, token_exception
from dependencies import create_access_token

async def login_controller(request, db):
    try:
        user = db.query(User).filter(User.username == request.username).first()
        if not user:
            raise token_exception()
        if not verify_password(request.password, user.password):
            raise token_exception()
        token = create_access_token({"user_id": user.id, "is_admin": user.is_admin}, expires=timedelta(minutes=60))
        return token
    except HTTPException as e:
        print(str(e))