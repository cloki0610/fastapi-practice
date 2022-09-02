from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_user
from schemas import UserBase, UserDisplay

router = APIRouter(
    prefix="/user",
    tags=["Users"],
)

@router.post('/new', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)