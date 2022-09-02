import random
import shutil
import string
from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, UploadFile, File

from db import db_post
from db.database import get_db
from router.schemas import PostBase

router = APIRouter(
    prefix="/post",
    tags=["Post"]
)

@router.get(
    '/',
    summary="Get all posts",
    response_description="A List of all posts")
def all_posts(db: Session = Depends(get_db)):
    """ Endpoint to get all posts"""
    return db_post.get_all_post(db)

@router.post(
    '/new',
    summary="Create a new post",
    response_description="The new post object from database")
def post_create_post(request: PostBase, db:Session = Depends(get_db)):
    """ Endpoint to create a new post"""
    return db_post.create_post(db, request)

@router.delete(
    '/{id}/delete',
    summary="Delete a post by id.",
    response_description="Return a json response as dictionary"
    )
def delete_post(id: int, db:Session = Depends(get_db)):
    """ Endpoint to delete a post by id"""
    return db_post.delete_post(id, db)


@router.post(
    '/image',
    summary="Upload an image to ./images folder.",
    response_description="Return a json response as dictionary"
)
def upload_image(image: UploadFile = File(...)):
    """ Endpoint to upload an image to ./images folder """
    # Get ascii characters
    letter = string.ascii_letters
    # Generate a 6-digit random string
    rand_str = ''.join(random.choice(letter) for i in range(6))
    # Generate a new file name
    new_image = f"_{rand_str}."
    filename = new_image.join(image.filename.rsplit('.', 1))
    path = f"images/{filename}"

    # Open the image and write to the folder
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    return {
        "message": "Upload Successfully.",
        "filename": path
    }

