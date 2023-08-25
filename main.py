from fastapi import FastAPI
from routers import users, auth, posts
from database import Base, engine
from repository.auth import login_controller

app = FastAPI()


Base.metadata.create_all(bind=engine)


# Write DOCSTRING for the function below

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(posts.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

@app.get("/token")
async def login_for_access_token():
    return login_controller()