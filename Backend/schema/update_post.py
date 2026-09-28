from pydantic import BaseModel

class UpdatePost(BaseModel):
    title: str | None = None
    content: str | None = None