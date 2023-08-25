from passlib.context import CryptContext
from fastapi import HTTPException, status

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    '''Hash password with bcrypt'''
    return pwd_cxt.hash(password)

def verify_password(password: str, hashed_password: str):
    '''Verify password with bcrypt'''
    return pwd_cxt.verify(password, hashed_password)


#Exceptions
def get_user_exception():
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return credentials_exception


def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token_exception_response


def token_expired_exception():
    token_expired_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token expired",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token_expired_response