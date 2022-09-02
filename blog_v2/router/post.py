import random
import string
import shutil
from typing import List
from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_post
from auth.oauth2 import get_current_user
from schemas import PostBase, PostDisplay, UserAuth

router = APIRouter(
    prefix="/post",
    tags=["Posts"],
)

# The only value accept as url type
image_url_types = ["absolute", "relative"]

@router.post("/new")
def create_post(
    request: PostBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            details="Parameter 'image_url_type' must be 'absolute' or 'relative'.")
    return db_post.create_post(db, request)


@router.get("/", response_model=List[PostDisplay])
def posts(db: Session = Depends(get_db)):
    return db_post.get_all_posts(db)

@router.post("/image")
def upload_image(
        image: UploadFile = File(...),
        current_user: UserAuth = Depends(get_current_user)):
    rand_str = ''.join(random.choice(string.ascii_letters) for i in range(6))
    new_filename = f'_{rand_str}.'
    filename = new_filename.join(image.filename.rsplit('.', 1))
    path = f"images/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}


@router.get('/delete/{id}')
def delete_post(
    id: int,
    db:Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user)):
    return db_post.delete_post(db, id, current_user.id)
