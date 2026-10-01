from pydantic import BaseModel, EmailStr
from datetime import datetime
# @router.post("/signup")
class SignUpUserModel(BaseModel):
    id: int
    username: str
    name: str 
    email: EmailStr
    
class UpdatedSignUpUserModel(BaseModel):
    message: str
    user: SignUpUserModel
    

# @router.post("/login")
class LoginUserModel(BaseModel):
    access_token: str
    token_type: str
    

# @router.get("/profile")
class UserProfileData(BaseModel):
    id: int
    user_name: str
    full_name: str
    created_at: datetime
    email: EmailStr
    
class UserProfilePosts(BaseModel):
    title: str
    content: str
    
class UpdatedUserProfileModel(BaseModel):
    user_profile: UserProfileData
    posts: list[UserProfilePosts]
    

# @router.patch("/profile")
class UserProfileUpdateModel(BaseModel):
    message: str
    user: SignUpUserModel
    
# @router.delete("/profile")
class UserProfileDeleteModel(BaseModel):
    message: str