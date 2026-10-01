from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

blogs = [
    {"id": 1, "title": "Python", "content": "Learn Python"},
    {"id": 2, "title": "FastAPI", "content": "Learn FastAPI"}
]


class BlogCreate(BaseModel):
    title: str
    content: str


@app.get("/blogs")
def get_blogs():
    return blogs


@app.get("/blogs/{blog_id}")
def get_blog(blog_id: int):
    for blog in blogs:
        if blog["id"] == blog_id:
            return blog

    raise HTTPException(status_code=404, detail="Blog not found")


@app.post("/blogs", status_code=201)
def create_blog(blog: BlogCreate):
    new_blog = {
        "id": len(blogs) + 1,
        "title": blog.title,
        "content": blog.content
    }

    blogs.append(new_blog)
    return new_blog