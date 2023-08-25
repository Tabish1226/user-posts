from fastapi import APIRouter, status, Depends
from sqlalchemy.orm.session import Session
from repository.auth import login_controller
from database import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=["auth"],
    prefix="/auth",
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return await login_controller(request, db)