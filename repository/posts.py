from models.posts import Post
from fastapi import HTTPException, status
from utils.utils import get_user_exception

def get_posts_controller(db):
    posts = db.query(Post).all()
    if posts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Posts not found")
    return posts

def get_my_posts_controller(request, db):
    if request.get("user_id") is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User error")
    user_id = request.get("user_id")
    filtered_posts = db.query(Post).filter(Post.author_id == user_id).all()
    if not filtered_posts:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Posts not found")
    return filtered_posts

def search_posts_controller(query, db):
    if query is None or query == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Query is not valid.")
    queried_posts = db.query(Post).filter(Post.title.contains(query) | Post.content.contains(query)).all()
    if not queried_posts:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Posts not found")
    return queried_posts

def search_by_id_posts_controller(id, db):
    if id is None or id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID is not valid.")
    queried_posts = db.query(Post).filter(Post.id == id).first()
    if not queried_posts:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post not found")
    return queried_posts

def create_post_controller(post,request,db):
    if post.title is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title is required")
    if post.content is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Content is required")
    if request.get("user_id") is None:
        raise get_user_exception()
    try:
        post = Post(
            title=post.title,
            content=post.content,
            author_id=request.get("user_id")
        )

        if post is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Post not created")
        db.add(post)
        db.commit()
        print(post)
        return {
            "Post": post.title,
            "status": status.HTTP_201_CREATED,
            "message": "Post created successfully"
            }
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong.")
    

def delete_post_controller(id, request, db):
    post_id = id
    if not post_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID is not correct")
    user_id = request.get("user_id")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User id is not valid.")
    try:
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        if post.author_id != user_id:
            return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
        db.delete(post)
        db.commit()
        return {
            "Post": post.title,
            "status": status.HTTP_204_NO_CONTENT,
            "message": "Post deleted successfully"
            }
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong.")
    
def update_post_controller(id,body,request,db):
    post_id = id
    if not post_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Post id is invalid.")
    user_id = request.get("user_id")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User id is not valid.")
    try:
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        if post.author_id != user_id:
            return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
        post.title = body.title
        post.content = body.content
        db.add(post)
        db.commit()
        return {
            "Post": post.title,
            "status": status.HTTP_204_NO_CONTENT,
            "message": "Post updated successfully"
            }
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong.")