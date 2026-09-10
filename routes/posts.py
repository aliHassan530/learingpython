from database.database import get_session
from fastapi import APIRouter, Depends
from model.post import Post, PostCreate
from auth import get_current_user
from sqlmodel import Session, select


router = APIRouter()


@router.post("/posts")
def create_post(
    posts: PostCreate,
    user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    new_post = Post(
        user_id=user_id,
        content=posts.content
    )

    session.add(new_post)
    session.commit()
    session.refresh(new_post)

    return {
        "message": "Post created successfully",
        "post": new_post
    }


@router.get("/allPosts")
def get_all_posts(
    user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    posts = session.exec(
        select(Post)
    ).all()

    return posts


@router.put("/posts/{post_id}")
def update_post(
    post_id: int,
    post: PostCreate,
    user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Find the post
    existing_post = session.get(Post, post_id)

    # Check if post exists
    if not existing_post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    # Check if this post belongs to the logged-in user
    if existing_post.user_id != user_id:
        raise HTTPException(
            status_code=403,
            detail="You can only update your own post"
        )

    # Update content
    existing_post.content = post.content

    # Save changes
    session.add(existing_post)
    session.commit()
    session.refresh(existing_post)

    return {
        "message": "Post updated successfully",
        "post": existing_post
    }

# @router.get("/find/{post_id}")
# def find_post(
#     post_id: int,
#     user_id: str=Depends(get_current_user),
#     session: Session = Depends(get_session)
# ):

#     existing_post=session.get(Post,post_id)

#     if not existing_post:
#         raise HTTPException(
#         status_code=404,
#         detail="Post Not Found Data"
#     )

#     return {
#         "message": "Post updated successfully",
#         "post": existing_post
#     }  
@router.get("/find/{search}")
def find_post(
    search: str,
    user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Search by post ID
    if search.isdigit():
        post = session.get(Post, int(search))

        if not post:
            raise HTTPException(
                status_code=404,
                detail="Post not found"
            )

        return {
            "message": "Post found successfully",
            "post": post
        }

    # Search by keyword
    posts = session.exec(
        select(Post).where(|
            (Post.content.ilike(f"%{search}%"))
        )
    ).all()

    if not posts:
        raise HTTPException(
            status_code=404,
            detail="No posts found"
        )

    return {
        "message": "Posts found successfully",
        "posts": posts
    } 
    

@router.delete("/posts/{post_id}")
def delete_post(
    post_id: int,
    user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Find the post
    existing_post =  session.get(Post, post_id)

    # Check if post exists
    if not existing_post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    # Check if the post belongs to the logged-in user
    if existing_post.user_id != user_id:
        raise HTTPException(
            status_code=403,
            detail="You can only delete your own post"
        )

    # Delete the post
    session.delete(existing_post)
    session.commit()

    return {
        "message": "Post deleted successfully",
        "post_id": post_id
    }



# from database.database import get_session
# from fastapi import APIRouter, Depends
# from model.post import PostCreate
# from auth import get_current_user
# from sqlmodel import Session, select

# router = APIRouter()



# @router.post("/posts")
# def create_post(
#     posts: PostCreate,
#     user_id: str = Depends(get_current_user),
#     session: Session = Depends(get_session)
# ):
#     new_post = posts(
#         content=posts.content
#     )

#     session.add(new_post)
#     session.commit()
#     session.refresh(new_post)

#     return {
#         "message": "Post created successfully",
#         "post": new_post
#     }

# @router.get("/allPosts")
# def getAllPosts(
#     user_id: str = Depends(get_current_user),
#     session: Session = Depends(get_session)
# ):

#     posts = session.exec(
#         select(Post)
#     ).all()