from pydantic import BaseModel

class PostData(BaseModel):
    title: str 
    content: str
    # author_id: int
    # ? user can't send or write author_id by themself. for author_id we need to verify that is this user loged in or not. if loged in then we get the id from user table and pass that id in author_id.