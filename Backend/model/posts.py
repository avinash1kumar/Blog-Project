from sqlmodel import Relationship, SQLModel, Field


class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str 
    content: str
    author_id: int = Field(foreign_key="user.id") # user -> User model ka table hai / user ka table hai
    # ? this author col will not get created in Post table
    author: "User" = Relationship(back_populates="posts")
    
    
# class Post(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     title: str
'''
      # ! sa_column=Column(Text) means:- 
        This tells SQLModel:

        Python: content is a str
        MySQL: store it as TEXT
        
        this will help you in storing long texts. like written in blogs.
'''
      
#     content: str = Field(sa_column=Column(Text))
#     author_id: int = Field(foreign_key="user.id")