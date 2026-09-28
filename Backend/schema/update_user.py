from pydantic import BaseModel, Field, EmailStr

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=5)
    name: str | None = Field(default=None, min_length=3)
    email: EmailStr | None = None
    password: str | None = Field(default=None, max_length=300)