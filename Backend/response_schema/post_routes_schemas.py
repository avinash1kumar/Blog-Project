from pydantic import BaseModel

# @router.post()
class PostDataResponse(BaseModel):
    title: str
    content: str
    
# @router.get("")
class GetMethodResponse(BaseModel):
    author: str
    title: str
    content: str
    

# @router.patch("/{post_id}")
class PostResponse(BaseModel):
    id: int
    title: str
    content: str

class UpdatePostResponse(BaseModel):
    message: str
    post: PostResponse
    
    
class DeletePostResponse(BaseModel):
    message: str