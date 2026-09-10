from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database.database import get_session
from model.models import User,LoginRequest 
from auth import create_access_token,get_current_user


router = APIRouter()


# ---------------- SIGNUP ----------------

@router.post("/signup")
def signup(
    user: User,
    session: Session = Depends(get_session)
):

    # Check username
    existing_username = session.exec(
        select(User).where(User.username == user.username)
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    # Check email
    existing_email = session.exec(
        select(User).where(User.email == user.email)
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Create user
    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    # Save user
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
      # Create JWT token
    token = create_access_token(
        data={
            "user_id": new_user.id,
            "username": new_user.username
        }
    )


    return {
        "message": "Signup successful",
        "user_id": new_user.id,
        "access_token": token,
        "token_type": "bearer"

    }


# ---------------- LOGIN ----------------

@router.post("/login")
def login(
    login_data: LoginRequest,
    session: Session = Depends(get_session)
):

    # Find user by email
    user = session.exec(
        select(User).where(User.email == login_data.email)
    ).first()

    # Check user/password
    if not user or user.password != login_data.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Create JWT token
    token = create_access_token(
        data={
            "user_id": user.id,
            "username": user.username
        }
    )

    return {
        "message": "Login successful",
        "user_id": user.id,
        "access_token": token,
        "token_type": "bearer"
    }



@router.get("/me")
def get_my_profile(
    user_id: int = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    user = session.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


