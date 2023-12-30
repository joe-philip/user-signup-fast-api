from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models import Profile, User
from schemas import UserCreate, UserProfile

router = APIRouter()

@router.post("/register/", response_model=UserProfile)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_phone = db.query(User).filter(User.phone == user.phone).first()
    if db_phone:
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    profile_data = {
        "full_name": db_user.full_name,
        "email": db_user.email,
        "phone": db_user.phone,
        "profile_picture": None
    }
    return profile_data

@router.get("/user/{user_id}", response_model=UserProfile)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    profile_data = {
        "full_name": db_user.full_name,
        "email": db_user.email,
        "phone": db_user.phone,
        "profile_picture": profile.profile_picture if profile else None
    }
    return profile_data
