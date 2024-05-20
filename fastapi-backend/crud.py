from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
import hashlib
import os


def hash_password(password: str, salt: str = None):
    if salt is None:
        salt = os.urandom(32)

    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate):
    hashed = hash_password(user.password)
    db_user = User(username=user.username, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
