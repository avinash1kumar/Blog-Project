from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr

class User(SQLModel, table=True):
    # in id default=None will help in generating id automatically
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(min_length=5, unique=True, nullable=False)
    name: str = Field(min_length=3, nullable=False)
    email: EmailStr = Field(unique=True, nullable=False)
    password: str = Field(max_length=300, nullable=False)
    created_at: datetime = Field(
    default_factory=lambda: datetime.now(timezone.utc)
    )
    # ? this posts column will not get created in User table
    posts: list["Post"] = Relationship(back_populates="author")
    # here "Post" is post table