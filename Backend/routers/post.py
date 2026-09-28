from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session , select
from model.user import User
from model.posts import Post
from schema.post_data import PostData
from schema.update_post import UpdatePost
from db import get_session
from utils.security import get_user

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("")
def write_blog(
    post: PostData,
    current_user: User = Depends(get_user),  # current_user me user ka sara details aa jayega. get_user user return kr rah hai
    session: Session = Depends(get_session) 
):
    
    new_post = Post(
        title=post.title,
        content=post.content,
        author_id=current_user.id
    )
    
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    
    return {
        "title": new_post.title,
        "content": new_post.content
    }
    

@router.get("")
def get_all_posts(
    current_user: User = Depends(get_user),
    session: Session = Depends(get_session)
):
    statement = select(
        User.name.label("author"), 
        Post.title,
        Post.content
    ).join(
        Post,
        Post.author_id == User.id
    )
    
    result = session.exec(statement).all()
    
    return [
        {
            "author": row.author,
            "title": row.title,
            "content": row.content
        }
        for row in result
    ]
    

# ! get post by postnumber { post_id }
@router.get("/{post_id}")
def single_post(
    post_id:int,
    current_user: User = Depends(get_user),
    session: Session = Depends(get_session)
):
    statement = select(Post).where(Post.id == post_id)
    post = session.exec(statement).first()
    
    if post is None:
        raise HTTPException(
            status_code=404,
            detail="There is no post exist with this number"
        )
    
    return post


# ! update post
@router.patch("/{post_id}")
def update_post(
    post_id: int,
    data: UpdatePost,
    current_user: User = Depends(get_user),
    session: Session = Depends(get_session)
):
    statement = select(Post).where(
        Post.id == post_id, 
        Post.author_id == current_user.id
    )
    post = session.exec(statement).first()
    
    if post is None:
        raise HTTPException(
            status_code=404,
            detail= "Not Found"
        )
        
    updated_data = data.model_dump(exclude_unset=True)
    
    if updated_data.get("title") is not None:
        post.title = updated_data["title"]
    
    if updated_data.get("content") is not None:
        post.content = updated_data["content"]
        
    session.commit()
    session.refresh(post)
    
    return {
        "message": "Post Updated Successfully",
        "post": {
            "id": post.id,
            "title": post.title,
            "content": post.content
        }
    }


# ! Delete Post
@router.delete("/{post_id}")
def delete_post(
    post_id: int,
    current_user: User = Depends(get_user),
    session: Session = Depends(get_session)
):
    statement = select(Post).where(
        Post.id == post_id, 
        Post.author_id == current_user.id
    )
    
    post = session.exec(statement).first()
    
    if post is None:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
    
    session.delete(post)
    session.commit()
    
    return {
        "message": "Post deleted successfully"
    }
    