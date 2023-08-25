from fastapi import APIRouter, status, Depends
from sqlalchemy.orm.session import Session
from database import get_db
from repository.posts import *
from dependencies import get_current_user
from schemas.posts import Post
from typing import Any, List

router = APIRouter(
    tags=["posts"],
    prefix="/posts",
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Post])
async def get_posts(_:dict=Depends(get_current_user), db: Session = Depends(get_db)) -> Any:
    return get_posts_controller(db)

@router.get("/my", status_code=status.HTTP_200_OK, response_model=List[Post])
async def get_my_posts(request:dict=Depends(get_current_user), db: Session = Depends(get_db)) -> Any:
    return get_my_posts_controller(request, db)

@router.get("/search", status_code=status.HTTP_200_OK, response_model=List[Post])
async def search_posts(query:str, _:dict=Depends(get_current_user), db: Session = Depends(get_db)) -> Any:
    return search_posts_controller(query, db)

@router.get("/by-id/{id}", status_code=status.HTTP_200_OK, response_model=Post)
async def search_by_id_posts(id:str, _:dict=Depends(get_current_user), db: Session = Depends(get_db)) -> Any:
    return search_by_id_posts_controller(id, db)


@router.post("/create", status_code=status.HTTP_200_OK)
async def create_posts(post: Post,request:dict=Depends(get_current_user), db: Session = Depends(get_db)):
    return create_post_controller(post,request,db)

@router.delete("/delete/{id}", status_code=status.HTTP_200_OK)
async def delete_post(id: str,request:dict=Depends(get_current_user), db: Session = Depends(get_db)):
    return delete_post_controller(id,request,db)

@router.patch("/update/{id}", status_code=status.HTTP_200_OK)
async def update_post(id: str,body:Post,request:dict=Depends(get_current_user), db: Session = Depends(get_db)):
    return update_post_controller(id,body,request,db)

