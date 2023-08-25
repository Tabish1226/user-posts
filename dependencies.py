from decouple import config
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from schemas.users import TokenData
from utils.utils import get_user_exception, token_expired_exception

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login")

def create_access_token(data: dict, expires: timedelta):
    expiry_time = datetime.utcnow() + expires
    data["exp"] = expiry_time
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_access_token(token):
    try:
        token_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return token_data
    except JWTError:
        raise get_user_exception()
def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        token_data = verify_access_token(token)
        if token_data.get("user_id") is None:
            raise get_user_exception()
        if token_data.get("exp") < datetime.now().timestamp():
            raise token_expired_exception()
        return {"user_id": token_data.get("user_id"), "is_admin": token_data.get("is_admin")}
    except Exception as e:
        print(str(e))
        return get_user_exception()