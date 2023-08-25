from fastapi import APIRouter, status, Depends
from sqlalchemy.orm.session import Session
from repository import users
from database import get_db
from schemas import users as schema_users

router = APIRouter(
    tags=["users"],
    prefix="/users",
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(db: Session = Depends(get_db)):
    return users.show(db)


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(request: schema_users.UserIn, db: Session = Depends(get_db)):
    print("Creating user...", request)
    return users.create(request, db)