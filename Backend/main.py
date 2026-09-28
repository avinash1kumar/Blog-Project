from fastapi import FastAPI
from model.user import User
from model.posts import Post
from db import create_table

app = FastAPI()

create_table()

from routers.user import router as signup_route
app.include_router(signup_route)

from routers.post import router as write_blog_router
app.include_router(write_blog_router)

@app.get("/")
def home():
    return {"welcome Home"}