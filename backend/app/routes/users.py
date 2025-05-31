from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate
from ..models import user as models
from ..database import SessionLocal
from passlib.context import CryptContext
from ..schemas.user import UserOut
from ..models import User
from ..dependencies import get_current_user
from fastapi import APIRouter, Depends

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "Usuario registrado con éxito"}

from ..core.security import get_current_user

@router.get("/profile")
def read_profile(user = Depends(get_current_user)):
    return {
        "message": f"Bienvenido, {user.username}",
        "email": user.email
    }

@router.get("/users/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
