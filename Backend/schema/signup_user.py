from pydantic import BaseModel, Field, EmailStr

class UserSignUp(BaseModel):
    username: str = Field(min_length=5, unique=True, nullable=False)
    name: str = Field(min_length=3, nullable=False)
    email: EmailStr = Field(unique=True, nullable=False)
    password: str = Field(max_length=300, nullable=False)