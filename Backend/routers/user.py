from fastapi import APIRouter, Depends, HTTPException
from model.user import User
from model.posts import Post
from schema.signup_user import UserSignUp
from schema.login_user import LoginUser
from schema.update_user import UserUpdate
from response_schema.user_routes_schemas import UpdatedSignUpUserModel, LoginUserModel, UpdatedUserProfileModel, UserProfileUpdateModel, UserProfileDeleteModel
from sqlmodel import Session, select, or_
from db import get_session
from datetime import datetime, timedelta, timezone
from utils.security import hash_password, verify_password, create_access_token, get_user

router = APIRouter(prefix="/auth", tags=["User Authentication"])

# ! signup api endpoint
@router.post("/signup", response_model=UpdatedSignUpUserModel)
def signup(
    user: UserSignUp,
    session: Session = Depends(get_session)
):
    statement = select(User).where(
        or_(
            User.username == user.username,
            User.email == user.email
        )
    )
    
    db_user = session.exec(statement).first()
    
    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

        if db_user.email == user.email:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )
        
    hashed_password = hash_password(user.password)
    new_user = User(
        username = user.username,
        password = hashed_password,
        email = user.email,
        name = user.name
    )
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    return {
        "message": "User created successfully",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "name": new_user.name,
            "email": new_user.email
        }
    }


# ! login endpoint
@router.post("/login", response_model=LoginUserModel)
def login(
    user: LoginUser,
    session: Session = Depends(get_session)
):
    statement = select(User).where(User.email == user.email)
    db_user = session.exec(statement).first()
    
    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
        
    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code= 401,
            detail="Invalid email or password"
        )
    expire = datetime.now(timezone.utc)+timedelta(minutes=30)   
    access_token = create_access_token(
        {
            "sub": str(db_user.id),
            "exp": expire
        }
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    

# ! get current login user
@router.get("/profile", response_model=UpdatedUserProfileModel)
def profile(
    current_user: User = Depends(get_user)
):

    return {
        "user_profile": {
            "id": current_user.id,
            "user_name": current_user.username,
            "full_name": current_user.name,
            "created_at": current_user.created_at,
            "email": current_user.email
        },

        "posts": [
            {
                "title": post.title,
                "content": post.content
            }
            for post in current_user.posts
        ]
    }
    

# ! update user details
@router.patch("/profile", response_model=UserProfileUpdateModel)
def update_profile(
    data: UserUpdate,
    current_user: User = Depends(get_user),
    session: Session = Depends(get_session)
):

    data = data.model_dump(exclude_unset=True)
    # ? Check username only if user is trying to change it
    if data.get("username") is not None:

        statement = select(User).where(
            User.username == data["username"],
            User.id != current_user.id
        )

        existing_user = session.exec(statement).first()

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

        current_user.username = data["username"]


    # ? Update name
    if data.get("name") is not None:
        current_user.name = data["name"]


    # ? Check email only if user is trying to change it
    if data.get("email") is not None:

        statement = select(User).where(
            User.email == data["email"],
            User.id != current_user.id
        )

        existing_user = session.exec(statement).first()

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        current_user.email = data["email"]


    # ? Update password
    if data.get("password") is not None:
        current_user.password = hash_password(data["password"])


    session.commit()
    session.refresh(current_user)


    return {
        "message": "Profile updated successfully",
        "user": {
            "id": current_user.id,
            "username": current_user.username,
            "name": current_user.name,
            "email": current_user.email
        }
    }


# ! delete user
@router.delete("/profile", response_model=UserProfileDeleteModel)
def delete_profile(
    current_user: User = Depends(get_user),
    session: Session = Depends(get_session)
):
    statement = select(Post).where(Post.author_id==current_user.id)
    posts = session.exec(statement).all()
    for post in posts:
        session.delete(post)
        
    session.delete(current_user)
    session.commit()
    
    return {
        "message": "Account deleted successfully!"
    }
    
    